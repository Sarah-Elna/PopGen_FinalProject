import os

populations = ["YRI", "LWK", "GWD", "MSL", "ESN"]

for i in range(0, 5):
    # Detecting selection
    cmd = "~/populationgenomics/software/relate/scripts/DetectSelection/DetectSelection.sh \
                -i ../step2/{pop}/{pop}_chr3_relate \
                -o ../step2/{pop}/{pop}_chr3_relate_selection \
                -m 1.25e-8 \
                --years_per_gen 25".format(pop=populations[i])
    os.system(cmd)
