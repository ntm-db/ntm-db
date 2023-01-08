import sys
import re
from copy import copy
for l in sys.stdin:
    #Locus=ML1891c
    row = l.strip().split("\t")
    oldrow = copy(row)
    lt = re.search("Locus=([^;]*)",l).group(1)
    row[2] = "gene"
    row[8] = f"ID=gene:{lt};"+oldrow[8]
    sys.stdout.write("\t".join(row)+"\n")
    row[2] = "CDS"
    row[8] = f"Parent=gene:{lt};ID={lt};"+oldrow[8]
    sys.stdout.write("\t".join(row)+"\n")

