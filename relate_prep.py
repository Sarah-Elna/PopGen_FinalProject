
import os

populations = ["all", "YRI", "LWK", "GWD", "MSL", "ESN"]

for i in range(0, 6):
    cmd = '~/populationgenomics/software/relate/bin/RelateFileFormats --mode ConvertFromVcf --haps ../step2/{pop}/chr3.haps --sample ../step2/{pop}/chr3.sample -i ../data/filtered/{pop}_filtered_inds.recode'.format(pop=populations[i])
    os.system(cmd)
    cmd = "~/populationgenomics/software/relate/scripts/PrepareInputFiles/PrepareInputFiles.sh --haps ../step2/{pop}/chr3.haps --sample ../step2/{pop}/chr3.sample --ancestor ../data/human_ancestor_3.fa --mask ../data/20140520.chr3.strict_mask.fasta.gz -o ../step2/{pop}/prep.{pop}_chr3".format(pop=populations[i])
    os.system(cmd)
    print("vcf prep run for {pop}".format(pop = populations[i]))