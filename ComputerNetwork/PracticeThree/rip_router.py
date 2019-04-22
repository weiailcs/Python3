from sim.basics import *

'''
Create your RIP router in this file.
TODO:	break ties with router ID 
		implement implicit withdrawl
		implement poision reverse and split horizon??
'''

'''
class DiscoveryPacket (Packet):
    """
    A "link latency change" packet.
    latency should be float("inf") if the link is down.
    """
    def __init__(self, src, latency):
        Packet.__init__(self, src=src)
        self.latency = latency
        self.is_link_up = (latency != None and latency != float("inf"))

    def __repr__ (self):
        return "<%s from %s->%s, %s, %s>" % (self.__class__.__name__,
                                 self.src.name if self.src else None,
                                 self.dst.name if self.dst else None,
                                 self.latency,
                                 self.is_link_up)
'''

'''
class RoutingUpdate (Packet): 
    """
    A Routing Update message to use with your RIPRouter implementation.
    """

    def __init__(self):
        Packet.__init__(self)
        self.paths = {}

    def add_destination(self, dest, distance):
        """
        Add a destination to announce, along with senders distance to that dest.
        """
        self.paths[dest] = distance

    def get_distance(self, dest):
        """
        Get the distance to the specified destination.
        """
        return self.paths[dest]

    def all_dests(self):
        """
        Get a list of all destinations with paths announced in this message.
        """
        return self.paths.keys()

    def str_routing_table(self):
        return str(self.paths) 
'''


class RIPRouter(Entity):

    def __init__(self):
        self.ports = {}

        # self.routing_table[neighbor][dst] = cost
        self.routing_table = {}

        # self.shortest_path[dst] = (neighbor, cost)
        self.shortest_path = {}

        self.INF = 100

    def handle_rx(self, packet, port):

        def update_shortest_path():
            flag = False
            for neighbor in self.routing_table:
                for dst in self.routing_table[neighbor]:
                    cost = self.routing_table[neighbor][dst]
                    if dst in self.shortest_path:
                        if cost < self.shortest_path[dst][1]:
                            flag = True
                            print cost, self.shortest_path[dst][1]
                            self.shortest_path[dst] = (neighbor, cost)
                    else:
                        flag = True
                        self.shortest_path[dst] = (neighbor, cost)
            return flag

        def struct_update_packet(src):
            update_packet = RoutingUpdate()
            for dst in self.shortest_path:
                if dst != src:
                    if self.shortest_path[dst][0] == src:
                        update_packet.add_destination(dst, self.INF)
                    else:
                        update_packet.add_destination(dst, self.shortest_path[dst][1])
            return update_packet

        if isinstance(packet, DiscoveryPacket):
            self.ports[packet.src] = port
            if packet.is_link_up:
                self.routing_table[packet.src] = {packet.src: 1}
            else:
                # del self.ports[packet.src]
                del self.routing_table[packet.src]

        elif isinstance(packet, RoutingUpdate):
            if packet.src not in self.routing_table:
                pass
            else:
                for dst in packet.all_dests():
                    if packet.get_distance(dst) == self.INF:
                        self.routing_table[packet.src][dst] = self.INF
                    else:
                        self.routing_table[packet.src][dst] \
                            = self.shortest_path[packet.src][1] + packet.get_distance(dst)
        else:
            if packet.dst in self.shortest_path:
                if self.shortest_path[packet.dst][1] != self.INF:
                    self.send(packet, self.ports[self.shortest_path[packet.dst][0]], flood=False)
            return None

        if update_shortest_path():
            for neighbor in self.routing_table:
                update_packet = struct_update_packet(neighbor)
                if len(update_packet.all_dests()) > 0:
                    self.send(update_packet, self.ports[neighbor], flood=False)
