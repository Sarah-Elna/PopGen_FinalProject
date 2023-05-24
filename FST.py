# This program runs a comandline prompt using vcftools to estimate FST for all 10 combinations of the 5 african populations in the populations list for each individual position.


import os

populations = ["YRI", "LWK", "GWD", "MSL", "ESN"]
full = "chr3_460_540_phased.vcf.gz"
done = []

for pop1 in populations:
    for pop2 in populations:
        if pop1 != pop2 and "{pop1}{pop2}".format(pop1=pop1, pop2=pop2) not in done and "{pop2}{pop1}".format(pop1=pop1, pop2=pop2) not in done:
            done.append("{pop1}{pop2}".format(pop1=pop1, pop2=pop2))
            done.append("{pop2}{pop1}".format(pop1=pop1, pop2=pop2))
            cmd = 'vcftools --gzvcf ../data/{full} --weir-fst-pop ../data/{pop1}_inds.txt --weir-fst-pop ../data/{pop2}_inds.txt --out ../step1/FST_{pop1}_{pop2}'.format(full=full, pop1=pop1, pop2=pop2)
            os.system(cmd.format(pop1=pop1, pop2=pop2, full=full))
