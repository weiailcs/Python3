import os
import sys
import getopt
import time
import threading
import Checksum
import BasicSender


# msg_type = 'start', 'end', 'ack', 'data'
class Sender(BasicSender.BasicSender):
    def __init__(self, dest, port, filename, debug=False):
        super(Sender, self).__init__(dest, port, filename, debug)

        self.msg_size = 1472
        self.end = 1 << 32
        self.window_size = 5
        self.max = 0
        self.resend_time = 0.5
        self.packet = {}
        self.ack = {}

    def start(self):
        t = threading.Thread(target=self.handle_response)
        t.setDaemon(True)
        t.start()

        seqno = 0
        while seqno <= self.end + 1:
            if seqno > self.max + self.window_size:
                continue
            self.send_msg(seqno)
            seqno += 1

        t.join()

    # zhi jie fa song
    def send_msg(self, seqno):
        if seqno > self.end:
            return

        msg = self.infile.read(self.msg_size)

        if seqno == 0:
            msg_type = 'start'
        elif msg.__len__() < self.msg_size:
            msg_type = 'end'
            self.end = seqno
        else:
            msg_type = 'data'

        packet = self.make_packet(msg_type, seqno, msg)
        self.send(packet)
        self.packet[seqno] = (packet, time.time())

    # chao shi chong fa
    def handle_timeout(self, seqno):
        msg = self.packet[seqno][0]
        self.send(msg)
        self.packet[seqno] = (msg, time.time())

    # ack di yi ci jie shou
    def handle_new_ack(self, seqno):
        for key, value in self.packet.items():
            if key < seqno:
                self.resend_time = self.resend_time * 0.75 + (time.time() - value[1]) * 0.5
                self.packet.pop(key)
        self.max = max(self.max, seqno)

    # di er ci jie shou
    def handle_dup_ack(self, seqno):
        msg = self.packet[seqno][0]
        self.send(msg)
        self.packet[seqno] = (msg, time.time())

    def log(self, msg):
        if self.debug:
            print msg

    def handle_response(self):
        while True:
            response = self.receive(0.005)
            if response and Checksum.validate_checksum(response):
                msg_type, seqno, data, checksum = self.split_packet(response)
                seqno = int(seqno)

                if seqno > self.end:
                    return

                if seqno not in self.ack:
                    self.handle_new_ack(seqno)
                else:
                    self.handle_dup_ack(seqno)

            for key, value in self.packet.items():
                if time.time() - value[1] > self.resend_time:
                    self.handle_timeout(key)


if __name__ == "__main__":
    def usage():
        print "BEARS-TP Sender"
        print "-f FILE | --file=FILE The file to transfer; if empty reads from STDIN"
        print "-p PORT | --port=PORT The destination port, defaults to 33122"
        print "-a ADDRESS | --address=ADDRESS The receiver address or hostname, defaults to localhost"
        print "-d | --debug Print debug messages"
        print "-h | --help Print this usage message"


    try:
        opts, args = getopt.getopt(sys.argv[1:],
                                   "f:p:a:d", ["file=", "port=", "address=", "debug="])
    except:
        usage()
        exit()

    port = 33122
    dest = "localhost"
    filename = None
    debug = False

    for o, a in opts:
        if o in ("-f", "--file="):
            filename = a
        elif o in ("-p", "--port="):
            port = int(a)
        elif o in ("-a", "--address="):
            dest = a
        elif o in ("-d", "--debug="):
            debug = True

    s = Sender(dest, port, filename, debug)
    try:
        s.start()
    except (KeyboardInterrupt, SystemExit):
        exit()
