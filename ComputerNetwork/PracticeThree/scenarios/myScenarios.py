# -*- coding: utf-8 -*-

import sim
from sim.core import CreateEntity, topoOf
from sim.basics import BasicHost
from hub import Hub
from sim import topo as topo


def create(switch_type=Hub, host_type=BasicHost):
    switch_type.create('s1')
    switch_type.create('s2')
    switch_type.create('s3')
    switch_type.create('s4')

    host_type.create('h2a')
    host_type.create('h2b')
    host_type.create('h3a')
    host_type.create('h3b')
    host_type.create('h4a')
    host_type.create('h4b')

    topo.link(s1, s2)
    topo.link(s1, s3)
    topo.link(s1, s4)

    topo.link(s2, h2a)
    topo.link(s2, h2b)
    topo.link(s3, h3a)
    topo.link(s3, h3b)
    topo.link(s4, h4a)
    topo.link(s4, h4b)


if __name__ == '__main__':
    pass
