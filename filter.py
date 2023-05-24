
import os

populations1 = ["", "YRI_", "LWK_", "GWD_", "MSL_", "ESN_"]
populations2 = ["all", "YRI", "LWK", "GWD", "MSL", "ESN"]

for i in range(0, 6):
    pop1 = populations1[i]
    pop2 = populations2[i]
    cmd = 'vcftools --gzvcf ../data/chr3_{pop1}460_540_phased.vcf.gz --keep ../data/{pop2}_inds.txt --recode --out ../data/filtered/{pop2}_filtered_inds'.format(pop1=pop1, pop2=pop2)
    print("vcf filtering was run for {pop2} was run".format(pop2 = pop2))
    os.system(cmd)
