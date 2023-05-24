# Sampling branch lengths (coalescent time) with Relate

import os

populations = ["all", "YRI", "LWK", "GWD", "MSL", "ESN"]

for i in range(0, 6):
    # Detecting selection
    cmd = "python3 ../clues/plot_traj.py ../step3/{pop}/out ../step3/plots/{pop}_fig".format(pop=populations[i])
    os.system(cmd)
