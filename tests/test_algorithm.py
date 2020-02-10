import os

from rpi_version import Matcher


def test_simple():
    matcher = Matcher("Beta", os.path.dirname(__file__) + "/rpi.json")
    result = matcher.match()
    assert result.version == "B (Beta)"
    assert result.date == "Q1 2012"
