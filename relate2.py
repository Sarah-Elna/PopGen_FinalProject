import os

populations = ["YRI", "LWK", "GWD", "MSL", "ESN"]

for i in range(0, 5):
    # Estimate historical population size and reestimate branch lengths of trees
    cmd = "~/populationgenomics/software/relate/scripts/EstimatePopulationSize/EstimatePopulationSize.sh -i ../step2/{pop}/{pop}_chr3_relate -m 1.25e-8 --poplabels ../data/{pop}_inds.txt -o ../step2/{pop}/{pop}_popsize --threshold 0".format(pop=populations[i])
    os.system(cmd)
