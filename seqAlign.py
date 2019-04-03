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
alignment1 = ""
alignment2 = ""

# Initialize first row with gaps
for i in range(0,1702):
        matrix[i][0] = i * gap

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

print(alignment1)
print(alignment2)

#TODO compare our sequence alignment to BLAST on the genbank website

#TODO count # of mutations: indels, synonymous mutations, nonsynonymous mutations, and other stuff

#TODO display data has a table

#TODO each of us needs to write our own individual report using the data we find

#TODO make a presentation for wednesday