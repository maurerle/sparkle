# SPDX-FileCopyrightText: ASSUME Developers
#
# SPDX-License-Identifier: AGPL-3.0-or-later

import json
import time
from multiprocessing import Process

from distributed_simulation.main import agent, agent_adresses, manager, tcp_host
from world_script import init

from assume import World


def run_distrib(n=1, m=1):
    # man = Process(target=manager)
    for i in range(n - 1):
        agent_adresses.append(((tcp_host, 9099 + i), "clock_agent"))
    ags = []
    for i in range(n):
        ag = Process(target=agent, args=(i, n, m))
        ags.append(ag)

    for ag in ags:
        ag.start()

    # time.sleep(2)
    manager()

    # man.join()
    for ag in ags:
        ag.join()


def run_sync(n=1):
    db_uri = "postgresql://assume:assume@localhost:5432/assume"
    db_uri = ""
    world = World(database_uri=db_uri)
    world.loop.run_until_complete(init(world, n))
    world.run()


def compare_runtime(ns=range(1, 3)):
    """This test compares the runtime between distributed and single process simulation"""
    results = []
    for n in ns:
        print("start simulation with", n)
        t = time.time()
        run_distrib(n)
        duration = time.time() - t
        results.append((n, m, "distrib", duration))

        t = time.time()
        run_sync(n)
        duration = time.time() - t
        results.append((n, m, "sync", duration))
        time.sleep(1)
    return results


def compare_speedup(exponent=3):
    total_agents = 2**exponent
    ns = [2**x for x in range(exponent + 1)]
    results = []
    for n in ns:
        m = total_agents // n
        print(f"start simulation with {n} processes with {m} agents each")
        t = time.time()
        run_distrib(n, m)
        duration = time.time() - t
        results.append((n, m, "distrib", duration))
        print(results)
    return results


if __name__ == "__main__":
    # n = 1
    # m = 16
    # print("start simulation with", n)
    # t = time.time()
    # run_distrib(n, m)
    # # run_sync(n*m)
    # duration = time.time() - t
    # print("duration", duration)

    # results = compare_runtime(range(1,4))
    results = compare_speedup(5)
    # print(results)

    with open("runtime_tests.json", "w") as f:
       json.dump(results, f, indent=4)

    # with open("runtime_tests.json", "r") as f:
    #     results = json.load(f)
