from fasta_reader import read_fasta, write_fasta

fa = read_fasta("data/ecoli.fa")
for item in fa:
    de = item.defline
    se = item.sequence

de += "(Halved)"
se = se[0:int(len(se)/2)]

with write_fasta("shortecoli.fa") as file:
    file.write_item(de, se)