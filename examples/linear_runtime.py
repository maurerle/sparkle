# SPDX-FileCopyrightText: ASSUME Developers
#
# SPDX-License-Identifier: AGPL-3.0-or-later

import time

import matplotlib.pyplot as plt
from world_script import init

from assume import World
from multiprocessing import Process
from distributed_simulation.main import agent, agent_addresses, manager, tcp_host


plt.style.use('seaborn-v0_8')


if __name__ == '__main__':
    durations_n = []
    #xs= [1,2,3,4,5,6,7,8,16,32, 64]
    xs = list(range(1,10)) + list(range(10,32,4)) + list(range(32,128,8)) + [128]


    for i in xs:
        t = time.time()
        db_uri = "postgresql://assume:assume@localhost:5432/assume"
        world = World(database_uri=db_uri)
        init(world, n=i)
        world.run()
        dur = time.time() -t
        durations_n.append(dur)
    print(durations_n)

    # durations_n = list(map(lambda x: round(x, 4), durations_n))
    # durations_n = [0.4027,  0.3975,  0.4465,  0.5077,  0.58,  0.6784,  0.7116,  0.7079,  0.9698,  0.7892,  1.0919,  1.2917,  1.5135,  1.9654,  1.9366,  2.0432,  2.6952,  2.8881,  3.4903,  3.9164,  4.2887,  4.9917,  5.1412,  5.7752,  6.9813,  7.3731,  7.0563,  8.4565]
    plt.figure(figsize=(10,5))
    plt.xlabel("Agent Count of simulation")
    plt.ylabel("Simulation Runtime in s")
    plt.plot(xs, durations_n)
    plt.legend(["market simulation"])
    plt.savefig("agent-count.svg")


    # durations_n = 

    durations_months = []
    for i in xs:
        t = time.time()
        db_uri = "postgresql://assume:assume@localhost:5432/assume"
        world = World(database_uri=db_uri)
        init(world, months=i)
        world.run()
        dur = time.time() -t
        durations_months.append(dur)
    print(durations_months)


    # durations_months = [0.9769134521484375, 0.4847285747528076, 3.1939425468444824, 13.009318590164185, 26.49550771713257, 55.729703187942505]

    plt.loglog(xs[:-1], durations_months)


    def run_distrib(n=1, m=1):
        # man = Process(target=manager)
        for i in range(1, n):
            agent_addresses.append(((tcp_host, 9098 + i), "clock_agent"))
        ags = []
        for i in range(n):
            ag = Process(target=agent, args=(i, n, m))
            ags.append(ag)

        for ag in ags:
            ag.start()

        time.sleep(1.5)
        manager()

        # man.join()
        for ag in ags:
            ag.join()

    durations_m = []
    m = 1
    processes = 2

    n = 1
    m = 1

    for i in xs[4:6]:
        print("simulationg", i)
        t = time.time()
        m = i // processes
        run_distrib(n=processes, m=m)
        duration = time.time() - t
        durations_m.append(duration)
        # wait before next run
        time.sleep(0.2)
    print(durations_m)


    plt.figure(figsize=(10,5))
    plt.xlabel("Agent Count of simulation")
    plt.ylabel("Simulation Runtime in s")
    plt.plot(xs, durations_n)
    plt.legend(["market simulation"])
    plt.savefig("agent-count.svg")

    plt.plot(xs, durations_m)