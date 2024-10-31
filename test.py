# SPDX-FileCopyrightText: ASSUME Developers
#
# SPDX-License-Identifier: AGPL-3.0-or-later

import yaml

from assume import World
from assume.scenario.loader_csv import load_scenario_folder

inputs_path = "examples/inputs"


# make sure that you have a database server up and running - preferabely in docker
# DB_URI = "postgresql://assume:assume@localhost:5432/assume"
# but you can use a file-based sqlite database too:
DB_URI = "sqlite:///local_db/assume_db_tutorial_05.db"


# lets look at the scenarios we have:
config_file = f"{inputs_path}/example_01f/config.yaml"
with open(str(config_file)) as f:
    config = yaml.safe_load(f)

# we have two scenarios available
list(config.keys())

world = World(database_uri=DB_URI, distributed_role=True, addr=("localhost", 9100))
load_scenario_folder(
    world,
    inputs_path=inputs_path,
    scenario="example_01f",
    study_case="ltm_case",
)
world.run()
