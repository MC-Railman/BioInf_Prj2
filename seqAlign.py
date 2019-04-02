# A sequence aligning program for Dr. Duan's Bioinformatics class
# Written by Tristan Hess, Scott Owens, and Ryan Weston

import numpy

# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# OH YEAH I SHOULD PROBABLY MENTION IM USING PYTHON 3
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

# Sequence 4 from California- https://www.ncbi.nlm.nih.gov/nuccore/NC_026433.1
gene1 = "atgaaggcaatactagtagttctgctatatacatttgcaaccgcaaatgcagacacatta" \
        "tgtataggttatcatgcgaacaattcaacagacactgtagacacagtactagaaaagaat" \
        "gtaacagtaacacactctgttaaccttctagaagacaagcataacgggaaactatgcaaa" \
        "ctaagaggggtagccccattgcatttgggtaaatgtaacattgctggctggatcctggga" \
        "aatccagagtgtgaatcactctccacagcaagctcatggtcctacattgtggaaacacct" \
        "agttcagacaatggaacgtgttacccaggagatttcatcgattatgaggagctaagagag" \
        "caattgagctcagtgtcatcatttgaaaggtttgagatattccccaagacaagttcatgg" \
        "cccaatcatgactcgaacaaaggtgtaacggcagcatgtcctcatgctggagcaaaaagc" \
        "ttctacaaaaatttaatatggctagttaaaaaaggaaattcatacccaaagctcagcaaa" \
        "tcctacattaatgataaagggaaagaagtcctcgtgctatggggcattcaccatccatct" \
        "actagtgctgaccaacaaagtctctatcagaatgcagatgcatatgtttttgtggggtca" \
        "tcaagatacagcaagaagttcaagccggaaatagcaataagacccaaagtgagggrtcra" \
        "gaagggagaatgaactattactggacactagtagagccgggagacaaaataacattcgaa" \
        "gcaactggaaatctagtggtaccgagatatgcattcgcaatggaaagaaatgctggatct" \
        "ggtattatcatttcagatacaccagtccacgattgcaatacaacttgtcaaacacccaag" \
        "ggtgctataaacaccagcctcccatttcagaatatacatccgatcacaattggaaaatgt" \
        "ccaaaatatgtaaaaagcacaaaattgagactggccacaggattgaggaatatcccgtct" \
        "attcaatctagaggcctatttggggccattgccggtttcattgaaggggggtggacaggg" \
        "atggtagatggatggtacggttatcaccatcaaaatgagcaggggtcaggatatgcagcc" \
        "gacctgaagagcacacagaatgccattgacgagattactaacaaagtaaattctgttatt" \
        "gaaaagatgaatacacagttcacagcagtaggtaaagagttcaaccacctggaaaaaaga" \
        "atagagaatttaaataaaaaagttgatgatggtttcctggacatttggacttacaatgcc" \
        "gaactgttggttctattggaaaatgaaagaactttggactaccacgattcaaatgtgaag" \
        "aacttatatgaaaaggtaagaagccagctaaaaaacaatgccaaggaaattggaaacggc" \
        "tgctttgaattttaccacaaatgcgataacacgtgcatggaaagtgtcaaaaatgggact" \
        "tatgactacccaaaatactcagaggaagcaaaattaaacagagaagaaatagatggggta" \
        "aagctggaatcaacaaggatttaccagattttggcgatctattcaactgtcgccagttca" \
        "ttggtactggtagtctccctgggggcaatcagtttctggatgtgctctaatgggtctcta" \
        "cagtgtagaatatgtatttaa"

# Sequence 4 from New York- https://www.ncbi.nlm.nih.gov/nuccore/NC_007366.1
gene2 = "agcaaaagcaggggataattctattaaccatgaagactatcattgctttgagctacattc" \
        "tatgtctggttttcgctcaaaaacttcccggaaatgacaacagcacggcaacgctgtgcc" \
        "ttgggcaccatgcagtaccaaacggaacgatagtgaaaacaatcacgaatgaccaaattg" \
        "aagtcactaatgctactgaactggttcagagttcctcaacaggtggaatatgcgacagtc" \
        "ctcatcagatccttgatggagaaaactgcacactaatagatgctctattgggagaccctc" \
        "agtgtgatggcttccaaaataagaaatgggacctttttgttgaacgcagcaaagcctaca" \
        "gcaactgttacccttatgatgtgccggattatgcctcccttaggtcactagttgcctcat" \
        "ccggcacactggagtttaacaatgaaagcttcaattggactggagtcactcaaaatggaa" \
        "caagctctgcttgcaaaaggagatctaataacagtttctttagtagattgaattggttga" \
        "cccacttaaaattcaaatacccagcattgaacgtgactatgccaaacaatgaaaaatttg" \
        "acaaactgtacatttggggggttcaccacccgggtacggacaatgaccaaatcagcctat" \
        "atgctcaagcatcaggaagaatcacagtctctaccaaaagaagccaacaaaccgtaatcc" \
        "cgagtatcggatctagacccaggataagggatgtccccagcagaataagcatctattgga" \
        "caatagtaaaaccgggagacatacttttgattaacagcacagggaatctaattgctcctc" \
        "ggggttacttcaaaatacgaagtgggaaaagctcaataatgagatcagatgcacccattg" \
        "gcaaatgcaattctgaatgcatcactccaaatggaagcattcccaatgacaaaccatttc" \
        "aaaatgtaaacaggatcacatatggggcctgtcccagatatgttaagcaaaacactctga" \
        "aattggcaacagggatgcgaaatgtaccagagaaacaaactagaggcatatttggcgcaa" \
        "tcgcgggtttcatagaaaatggttgggagggaatggtagacggttggtacggtttcaggc" \
        "atcaaaattctgagggaacaggacaagcagcagatctcaaaagcactcaagcagcaatca" \
        "accaaatcaatgggaagctgaataggttgatcgggaaaacaaacgagaaattccatcaga" \
        "ttgaaaaagaattctcagaagtagaagggagaattcaggacctcgagaaatatgttgagg" \
        "acactaaaatagatctctggtcatacaacgcggagcttcttgtggccctggagaaccaac" \
        "atacaattgatctaactgactcagaaatgaacaaactgtttgaaagaacaaagaagcaac" \
        "tgagggaaaatgctgaggatatgggcaatggttgtttcaaaatataccacaaatgtgaca" \
        "atgcctgcatagggtcaatcagaaatggaacttatgaccatgatgtatacagagatgaag" \
        "cattaaacaaccggttccagatcaaaggtgttgagttgaagtcaggatacaaagattgga" \
        "tcctatggatttcctttgccatatcatgttttttgctttgtgttgctttgttggggttca" \
        "tcatgtgggcctgccaaaaaggcaacattaggtgcaacatttgcatttgagtgcattaat" \
        "taaaaacacccttgtttctact"

print(gene1)
print(len(gene1))
print(gene2)
print(len(gene2))


#TODO implement global/semi-global/local alignment between the two sequences
# Global alignment might be better with such a large gene sequence. It starts at the end instead of the highest
# score in the matrix. We wouldn't need to make pointers or anything, just compare the values around the current one
# to select a match and go. Only limitation i see if the processing power and memory in our computers to do a
# 1701 x 1762 matrix of numbers.. lol
# Going to start with a global alignment and see if I regret my decisions later.. - Tristan

# Variables for scoring
gap = -2
mismatch = -1
match = 1

# Global alignment matrix. Had to use numpy for this.
# Creates an EMPTY 1702 x 1763 matrix for scoring (one extra than the length for the first row comparing the sequences to nothing
# Use this like matrix[0][0] for the first entry, matrix[0][1] for the one below it, and matrix[1][0] for the one beside
matrix = numpy.empty([1702,1763])
alignment = ""

#TODO fill the alignment using the scoring values. We can use a nester for-loop for this, and fill it like we did with the ones in class
# If this is a terrible idea and there's an easier way to do this, feel free to dump my stuff I have here xD - Tristan


#TODO compare our sequence alignment to BLAST on the genbank website

#TODO count # of mutations: indels, synonymous mutations, nonsynonymous mutations, and other stuff

#TODO display data has a table

#TODO each of us needs to write our own individual report using the data we find

#TODO make a presentation for wednesday