import models.sumoprotkin as sumo
import models.pipelines as pipelines
import os

def sumo_stages(IDs=None):
    if IDs:
        if len(IDs)==1:
            pass
        elif len(IDs)>1:
            pass
        else:
            pass
    else:
        return sumo.stages(debug=False)




if __name__=="__main__":
    import argparse

    parser = argparse.ArgumentParser(description="SumoProtKin tool cli")
    parser.add_argument("--reset_cache", help="Reset cache file")
    args = parser.parse_args()

    if args.reset_cache == "on":
        clear = True
    else:
        clear = False
    stages = sumo.stages(debug=False)
    pipelines.Pipeline(stages, clear_cache=clear)