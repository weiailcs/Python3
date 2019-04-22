# -*- coding: utf-8 -*-

import sim
from sim.core import CreateEntity, topoOf
from sim.basics import BasicHost
from hub import Hub
from sim import topo as topo


def create(switch_type=Hub, host_type=BasicHost):
    host_type.create('s')
    host_type.create('t')

    switch_type.create('s1')
    switch_type.create('s2')
    switch_type.create('s3')
    switch_type.create('s4')

    topo.link(s, s1)

    topo.link(t, s2)
    topo.link(t, s4)

    topo.link(s1, s2)
    topo.link(s1, s3)
    topo.link(s3, s4)


if __name__ == '__main__':
    pass
