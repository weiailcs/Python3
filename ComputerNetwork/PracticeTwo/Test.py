# -*- coding: utf-8 -*-
import random

from BasicTest import *

"""
This tests random packet drops. We randomly decide to drop about half of the
packets that go through the forwarder in either direction.

Note that to implement this we just needed to override the handle_packet()
method -- this gives you an example of how to extend the basic test case to
create your own.
"""



for p in in_queue:
    if random.choice([True, False]):
        out_queue.append(p)
    print in_queue

# empty out the in_queue
in_queue = []


if __name__ == '__main__':
    r = RandomDropTest()
    r.handle_packet()
