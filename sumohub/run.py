import models.sumoprotkin as sumo
import models.pipelines as pipelines
import os
import argparse
import time

parser = argparse.ArgumentParser(description="SumoProtKin tool cli")
parser.add_argument("--reset_cache", help="Reset cache file")
args = parser.parse_args()
print(args)

if args.reset_cache == "on":
    clear = True
else:
    clear = False

print("Starting Pipeline")
start = time.perf_counter()
stages = sumo.stages(debug=False)
pipelines.Pipeline(stages, clear_cache=clear)
stop = time.perf_counter() - start
print("Time: " + str(stop) + "s")
