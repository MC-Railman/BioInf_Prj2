#!/usr/bin/python
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

# Variables for scoring
gap = -2
mismatch = -1
match = 1

# Uses numpy to create an empty 1702x1763 matrix to represent our sequence scoring matrix
matrix = numpy.empty([1702,1763])
alignment1 = ""
alignment2 = ""

print("Creating matrix...")
# Initialize first row with gaps
for i in range(0,1702):
        matrix[i][0] = i * gap

print("Processing matrix scores...")
y = 0
# Fill in the scoring matrix for global alignment
for g2 in gene2:
        y += 1                  # increment row
        x = 0                   # reset to first column column
        matrix[x][y] = y * gap  # put gap in first column
        for g1 in gene1:
                x += 1          # increment column
                if g1 == g2:                                            # if match add match
                        matrix[x][y] = matrix[x - 1][y - 1] + match
                else:                                                   # else choose the largest of a gap or a mismatch
                        gap1 = matrix[x][y - 1] + gap
                        gap2 = matrix[x - 1][y] + gap
                        mis = matrix[x - 1][y - 1] + mismatch
                        if (gap1 > gap2) and (gap1 > mis):
                                matrix[x][y] = gap1
                        elif (gap2 > gap1) and (gap2 > mis):
                                matrix[x][y] = gap2
                        else:
                                matrix[x][y] = mis

print("Aligning sequences...")
# Find the optimal alignment of the two sequences
while x != 0 or y != 0:
        if gene1[x - 1] == gene2[y - 1] or (matrix[x][y] - mismatch) == matrix[x - 1][y - 1]:
                alignment1 = gene1[x - 1] + alignment1          # add base to alignmnent
                alignment2 = gene2[y - 1] + alignment2          # add base to alignment
                x -= 1                                          # move left in matrix
                y -= 1                                          # move up in matrix
        elif (matrix[x][y] - gap) == matrix[x][y - 1]:
                alignment1 = "-" + alignment1                   # add gap to alignment
                alignment2 = gene2[y - 1] + alignment2          # add base to alignment
                y -= 1                                          # move up in matrix
        elif (matrix[x][y] - gap) == matrix[x - 1][y]:
                alignment1 = gene1[x - 1] + alignment1          # add base to alignment
                alignment2 = "-" + alignment2                   # add gap to alignment
                x -= 1                                          # move left in matrix

print("Done!")
print(alignment1)
print(alignment2)

# Write alignments to file for easy comparing
f = open("Aligned_Sequences.txt", "w")
counter = 0
counter2 = 0
c = 0
for r in range(0, len(alignment1)):
    f.write(alignment1[r])
    counter += 1
    if counter == 10:
        f.write(" ")
    if counter == 20:
        f.write("\n")
        while c < r or c == r:
            f.write(alignment2[c])
            c += 1
            counter2 += 1
            if counter2 == 10:
                f.write(" ")
            if counter2 == 20:
                f.write("\n")
        counter = 0
        counter2 = 0
        f.write("\n")
#f.write(alignment1)
#f.write("\n\n")
#f.write(alignment2)
f.close()

# BLASTn results from
# https://blast.ncbi.nlm.nih.gov/Blast.cgi?PAGE=MegaBlast&PROGRAM=blastn&BLAST_PROGRAMS=megaBlast&PAGE_TYPE=BlastSearch&BLAST_SPEC=blast2seq&DATABASE=n/a&QUERY=&SUBJECTS=
# For box 1 enter "NC_026433.1" and for box 2 enter "NC_007366.1", then select "Somewhat similar sequences" below and BLAST
rangeBLAST = "954 to 1569"
scoreBLAST = "65.3"
expectBLAST = "1e-13"
identitiesBLAST = "400/629 (64%)"
gapsBLAST = "23/629 (3%)"

#TODO count # of mutations: indels, synonymous mutations, nonsynonymous mutations, and other stuff

#TODO display data has a table

#TODO each of us needs to write our own individual report using the data we find

#TODO make a presentation for wednesday
