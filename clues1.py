# Sampling branch lengths (coalescent time) with Relate

import os

populations = ["all", "YRI", "LWK", "GWD", "MSL", "ESN"]

for i in range(0, 6):
    # Detecting selection
    cmd = "~/populationgenomics/software/relate/scripts/SampleBranchLengths/SampleBranchLengths.sh \
        -i ../step2/{pop}/{pop}_chr3_relate \
        -o ../step3/{pop}/{pop}_relate_sub \
        -m 1.25e-8 \
        --coal ../step2/{pop}/{pop}_popsize.coal \
        --format b \
        --num_samples 100 \
        --first_bp 51000000 --last_bp 52000000".format(pop=populations[i])
    os.system(cmd)
