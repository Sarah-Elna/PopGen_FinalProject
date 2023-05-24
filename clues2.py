# Sampling branch lengths (coalescent time) with Relate

import os

populations = ["all", "YRI", "LWK", "GWD", "MSL", "ESN"]

for i in range(0, 6):
    # Detecting selection
    cmd = "python3 ../clues/inference.py --times ../step3/{pop}/{pop}_relate_sub --out ../step3/{pop}/out".format(pop=populations[i])
    os.system(cmd)
