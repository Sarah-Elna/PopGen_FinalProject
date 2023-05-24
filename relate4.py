
import os

cmd = "~/populationgenomics/software/relate/scripts/TreeView/TreeView.sh \
            --haps ../step2/all/chr3.haps \
            --sample ../step2/all/chr3.sample \
            --anc ../step2/all/all_chr3_relate.anc \
            --mut ../step2/all/all_chr3_relate.mut \
            --poplabels ../data/all_inds.txt \
            --bp_of_interest 49000000 \
            --years_per_gen 25 \
            -o ../step2/plots/all_tree_49000000"
os.system(cmd)

cmd = "~/populationgenomics/software/relate/scripts/TreeView/TreeView.sh \
            --haps ../step2/all/prep.chr3.haps \
            --sample ../step2/all/prep.chr3.sample \
            --anc ../step2/all/all_chr3_relate.anc \
            --mut ../step2/all/all_chr3_relate.mut \
            --poplabels ../data/all_inds.txt \
            --bp_of_interest 51506205 \
            --years_per_gen 25 \
            -o ../step2/plots/all_tree_51506205"
os.system(cmd)