# SPDX-FileCopyrightText: ASSUME Developers
#
# SPDX-License-Identifier: AGPL-3.0-or-later

import pytest

from sparkle_cli.cli import cli


@pytest.mark.slow
def test_cli():
    args = "-s example_01a -c tiny -db sqlite:///./examples/local_db/test_mini.db"
    cli(args.split(" "))


@pytest.mark.slow
def test_cli_network():
    args = "-s example_01d -c base -db sqlite:///./examples/local_db/test_mini.db"
    cli(args.split(" "))
