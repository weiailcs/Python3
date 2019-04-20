from sim.api import *
from sim.basics import *

'''
Create your RIP router in this file.
'''

'''
packet = "<%s from %s->%s, %s, %s>" % (self.__class__.__name__,
                                 self.src.name if self.src else None,
                                 self.dst.name if self.dst else None,
                                 self.latency,
                                 self.is_link_up)
'''


class LearningSwitch(Entity):
    def __init__(self):
        '''
        self.routing_table[ packet.src / .dst ] = port
        '''
        self.routing_table = {}

    def handle_rx(self, packet, port):
        if packet.src not in self.routing_table:
            self.routing_table[packet.src] = port

        if packet.dst in self.routing_table:
            if packet.src == packet.dst:
                pass
            else:
                self.send(packet=packet, port=self.routing_table[packet.dst], flood=False)
        else:
            self.send(packet=packet, port=port, flood=True)
