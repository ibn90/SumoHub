import models.sumoprotkin as sumo
import models.pipelines as pipelines
import os
import argparse

parser = argparse.ArgumentParser(description="SumoProtKin tool cli")
parser.add_argument('--reset_cache',help='Reset cache file')
args =parser.parse_args()
print(args)

stages=sumo.stages
pipelines.Pipeline(stages)
