# SPDX-FileCopyrightText: ASSUME Developers
#
# SPDX-License-Identifier: AGPL-3.0-or-later

import json
import logging

import matplotlib.pyplot as plt
import pandas as pd
from create_runtime import compare_runtime_per_process

logging.getLogger("mango.container.tcp").setLevel(logging.FATAL)



if __name__ == '__main__':
    n = 2
    m = 1
    # print("start simulation with", n)
    # t = time.time()
    #run_distrib(n, m)

    process_counts = [1, 2, 4, 8]
    agent_total_counts = [8,16,32,64]
    results = compare_runtime_per_process(process_counts, agent_total_counts)

    print(results)

    with open("runtime_tests.json", "w") as f:
        json.dump(results, f, indent=4)

    df = pd.read_json("runtime_tests.json")
    df.columns = ["n", "m", "type", "time"]

    plt.figure(figsize=(10, 6))

    for n, group in df.groupby("n"):
        plt.plot(group["m"], group["time"], label=f"{n} processes")
    plt.legend()
    plt.plot(df["n"], df["time"], label="wall time")
    plt.xlabel("n Cores")
    plt.ylabel("wall time in seconds")