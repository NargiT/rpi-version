from __future__ import print_function

import json
import os
from collections import namedtuple
from typing import Optional

RPI = namedtuple('RPI', 'version date')


class Matcher:

    def __init__(self, revision, path_to_file="rpi.json"):
        self._revision = revision
        with open(path_to_file) as json_file:
            self._data = json.load(json_file)

    def match(self):
        # type: () -> RPI

        if self._revision in self._data:
            return RPI(self._data[self._revision]["version"], self._data[self._revision]["release_date"])
        return RPI(None, None)


def main():
    def revision():
        # type: () ->  Optional[str]
        return os.popen("cat /proc/cpuinfo | grep 'Revision' | awk '{print $3}' | sed 's/^1000//'").read().strip()

    result = Matcher(revision()).match()

    if result.version and result.date:
        print("version : {}".format(result.version))
        print("   date : {}".format(result.date))
    else:
        print("Unknown version")


if __name__ == '__main__':
    main()
