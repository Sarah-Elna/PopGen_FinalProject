import os

populations = ["all", "YRI", "LWK", "GWD", "MSL", "ESN"]

for i in range(0, 6):
    # Build tree along the genome
    cmd = "~/populationgenomics/software/relate/bin/Relate --mode All -m 1.25e-8 -N 30000 --haps ../step2/{pop}/prep.{pop}_chr3.haps.gz --sample ../step2/{pop}/prep.{pop}_chr3.sample.gz --map ../data/genetic_map_chr3_combined_b37.txt -o {pop}_chr3_relate".format(pop=populations[i])
    os.system(cmd)
