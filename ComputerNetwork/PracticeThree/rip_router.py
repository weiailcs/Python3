from sim.basics import *

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

        # self.ports[dst] = port
        self.ports = {}

        # self.routing_table[neighbor][dst] = cost
        self.routing_table = {}

        # self.shortest_path[dst] = (neighbor, cost)
        self.shortest_path = {}

        self.INF = 100

    def handle_rx(self, packet, port):

        # print packet

        def min_by_port(lst):
            lowers = []
            for index, (key, value) in enumerate(sorted(lst, key=lambda x: x[1])):
                if index == 0:
                    lowers.append((key, value))
                elif value == lowers[0][1]:
                    lowers.append((key, value))
            return min(lowers, key=lambda x: self.ports[x[0]])

        def update_shortest_path():
            '''
            should update ?
            '''

            pre = self.shortest_path.copy()
            destDict = {}
            for row in self.routing_table:  # each row is the neighbour
                for dest in self.routing_table[row]:  # the dictionary has a whole bunch of "dest, cost" values
                    cost = self.routing_table[row][dest]
                    if destDict.has_key(dest):
                        lst = destDict[dest]
                        lst.append((row, cost))
                        destDict[dest] = lst  # through row, costing cost
                    else:
                        destDict[dest] = [(row, cost)]

            for dest in destDict:  # destdict is each destination and the cost to get through it, and who its through
                self.shortest_path[dest] = min_by_port(destDict[dest])

            # print " mincosts is ", self.minCosts,  "changed  = ", preChange != self.minCosts
            return pre != self.shortest_path

            # flag = False
            # for neighbor in self.routing_table:
            #     for dst in self.routing_table[neighbor]:
            #         cost = self.routing_table[neighbor][dst]
            #         if dst in self.shortest_path:
            #             if cost < self.shortest_path[dst][1]:
            #                 flag = True
            #                 self.shortest_path[dst] = (neighbor, cost)
            #         else:
            #             flag = True
            #             self.shortest_path[dst] = (neighbor, cost)
            # return flag

        def struct_update_packet(neighbor):
            '''
            pack update message
            '''
            update_packet = RoutingUpdate()
            for dst in self.shortest_path:
                if dst != neighbor:
                    if self.shortest_path[dst][0] == neighbor:
                        update_packet.add_destination(dst, self.INF)
                    else:
                        update_packet.add_destination(dst, self.shortest_path[dst][1])
            return update_packet

        if isinstance(packet, DiscoveryPacket):
            '''
            handle initial message
            '''
            neighbor = packet.src
            self.ports[neighbor] = port
            if packet.is_link_up:
                self.routing_table[neighbor] = {neighbor: 1}
            else:
                # print self.routing_table
                print self
                del self.routing_table[packet.src]
        elif isinstance(packet, RoutingUpdate):
            '''
            handle update message
            '''
            if packet.src not in self.routing_table:
                pass
            else:
                neighbor = packet.src
                # self.ports[neighbor] = port
                for dst in packet.all_dests():
                    if packet.get_distance(dst) == self.INF:
                        self.routing_table[neighbor][dst] = self.INF
                    else:
                        self.routing_table[neighbor][dst] \
                            = 1 + packet.get_distance(dst)
        else:
            '''
            handle normal message
            '''
            if packet.dst in self.shortest_path:
                if self.shortest_path[packet.dst][1] != self.INF:
                    neighbor = self.shortest_path[packet.dst][0]
                    self.send(packet, self.ports[neighbor], flood=False)
            return None

        if update_shortest_path():
            '''
            flood, send update message
            '''
            for neighbor in self.routing_table:
                update_packet = struct_update_packet(neighbor)
                if len(update_packet.all_dests()) > 0:
                    self.send(update_packet, self.ports[neighbor], flood=False)
