# SPDX-FileCopyrightText: ASSUME Developers
#
# SPDX-License-Identifier: AGPL-3.0-or-later

import time
from subprocess import Popen

ps = []
n = 4

p_man = Popen("python -m distributed_simulation.world_manager".split(" "))


time.sleep(1)
for i in range(n):
    p = Popen(
        f"python -m distributed_simulation.world_agent {i} {n} {9098+i}".split(" ")
    )
    ps.append(p)

p_man.wait()
print("now killing")
for p in ps:
    p.wait(timeout=1)
