from __future__ import print_function
import json
import os

with open('rpi.json') as json_file:
    data = json.load(json_file)
    revision = os.popen("cat /proc/cpuinfo | grep 'Revision' | awk '{print $3}' | sed 's/^1000//'").read().strip()
    
    for rpi in data["rpi"]:
        if revision == rpi["revision"]:
            print("version : {}".format(rpi["version"]))
            print("   date : {}".format(rpi["release_date"]))
