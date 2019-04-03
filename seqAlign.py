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

# Refactored write output to file function
def writeToFile(alignment1, alignment2):
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
    f.close()

# Returns amino acid based on sequence of three codons
def codon(seq):
        if seq == "ttt" or seq == "ttc":
                return "Phe"
        elif seq == "tta" or seq == "ttg" or seq == "ctt" or seq == "ctc" or seq == "cta" or seq == "ctg":
                return "Leu"
        elif seq == "tct" or seq == "tcc" or seq == "tca" or seq == "tcg" or seq == "agt" or seq == "agc":
                return "Ser"
        elif seq == "tat" or seq == "tac":
                return "Tyr"
        elif seq == "tgt" or seq == "tgc":
                return "Cys"
        elif seq == "tgg":
                return "Trp"
        elif seq == "cct" or seq == "ccc" or seq == "cca" or seq == "ccg":
                return "Pro"
        elif seq == "cat" or seq == "cac":
                return "His"
        elif seq == "caa" or seq == "cag":
                return "Gln"
        elif seq == "cgt" or seq == "cgc" or seq == "cga" or seq == "cgg" or seq == "aga" or seq == "agg":
                return "Arg"
        elif seq == "att" or seq == "atc" or seq == "ata":
                return "Ile"
        elif seq == "atg":
                return "Met"
        elif seq == "act" or seq == "acc" or seq == "aca" or seq == "acg":
                return "Thr"
        elif seq == "aat" or seq == "aac":
                return "Asn"
        elif seq == "aaa" or seq == "aag":
                return "Lys"
        elif seq == "gtt" or seq == "gtc" or seq == "gta" or seq == "gtg":
                return "Val"
        elif seq == "gct" or seq == "gcc" or seq == "gca" or seq == "gcg":
                return "Ala"
        elif seq == "gat" or seq == "gac":
                return "Asp"
        elif seq == "gaa" or seq == "gag":
                return "Glu"
        elif seq == "ggt" or seq == "ggc" or seq == "gga" or seq == "ggg":
                return "Gly"
        elif seq == "taa" or seq == "tag" or seq == "tga":
                return "STOP"

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
writeToFile(alignment1, alignment2)

# BLASTn results from
# https://blast.ncbi.nlm.nih.gov/Blast.cgi?PAGE=MegaBlast&PROGRAM=blastn&BLAST_PROGRAMS=megaBlast&PAGE_TYPE=BlastSearch&BLAST_SPEC=blast2seq&DATABASE=n/a&QUERY=&SUBJECTS=
# For box 1 enter "NC_026433.1" and for box 2 enter "NC_007366.1", then select "Somewhat similar sequences" below and BLAST
rangeBLAST = "954 to 1569"
scoreBLAST = "65.3"
expectBLAST = "1e-13"
identitiesBLAST = "400/629 (64%)"
gapsBLAST = "23/629 (3%)"

counter = 0
synonymous1 = 0
nonsynonymous1 = 0
while counter < (len(alignment1) - 2):
        sequence1 = alignment1[counter] + alignment1[counter + 1] + alignment1[counter + 2]
        mutation1 = alignment2[counter] + alignment1[counter + 1] + alignment1[counter + 2]
        mutation2 = alignment1[counter] + alignment2[counter + 1] + alignment1[counter + 2]
        mutation3 = alignment1[counter] + alignment1[counter + 1] + alignment2[counter + 2]
        if codon(sequence1) == codon(mutation1) and codon(sequence1) != "None" and codon(mutation1) != "None":
                if alignment1[counter] != alignment2[counter] and alignment1[counter] != "-" and alignment2[counter] != "-":
                        synonymous1 += 1
        elif alignment1[counter] != alignment2[counter] and alignment1[counter] != "-" and alignment2[counter] != "-":
                nonsynonymous1 += 1
        if codon(sequence1) == codon(mutation2) and codon(sequence1) != "None" and codon(mutation2) != "None":
                if alignment1[counter + 1] != alignment2[counter + 1] and alignment1[counter + 1] != "-" and alignment2[counter + 1] != "-":
                        synonymous1 += 1
        elif alignment1[counter + 1] != alignment2[counter + 1] and alignment1[counter + 1] != "-" and alignment2[counter + 1] != "-":
                nonsynonymous1 += 1
        if codon(sequence1) == codon(mutation3) and codon(sequence1) != "None" and codon(mutation3) != "None":
                if alignment1[counter + 2] != alignment2[counter + 2] and alignment1[counter + 2] != "-" and alignment2[counter + 2] != "-":
                        synonymous1 += 1
        elif alignment1[counter + 2] != alignment2[counter + 2] and alignment1[counter + 2] != "-" and alignment2[counter + 2] != "-":
                nonsynonymous1 += 1
        counter += 3

counter = 0
synonymous2 = 0
nonsynonymous2 = 0
while counter < (len(alignment2) - 2):
        sequence2 = alignment2[counter] + alignment2[counter + 1] + alignment2[counter + 2]
        mutation1 = alignment1[counter] + alignment2[counter + 1] + alignment2[counter + 2]
        mutation2 = alignment2[counter] + alignment1[counter + 1] + alignment2[counter + 2]
        mutation3 = alignment2[counter] + alignment2[counter + 1] + alignment1[counter + 2]
        if codon(sequence2) == codon(mutation1) and codon(sequence2) != "None" and codon(mutation1) != "None":
                if alignment1[counter] != alignment2[counter] and alignment1[counter] != "-" and alignment2[counter] != "-":
                        synonymous2 += 1
        elif alignment1[counter] != alignment2[counter] and alignment1[counter] != "-" and alignment2[counter] != "-":
                nonsynonymous2 += 1
        if codon(sequence2) == codon(mutation2) and codon(sequence2) != "None" and codon(mutation2) != "None":
                if alignment1[counter + 1] != alignment2[counter + 1] and alignment1[counter + 1] != "-" and alignment2[counter + 1] != "-":
                        synonymous1 += 1
        elif alignment1[counter + 1] != alignment2[counter + 1] and alignment1[counter + 1] != "-" and alignment2[counter + 1] != "-":
                nonsynonymous2 += 1
        if codon(sequence2) == codon(mutation3) and codon(sequence2) != "None" and codon(mutation3) != "None":
                if alignment1[counter + 2] != alignment2[counter + 2] and alignment1[counter + 2] != "-" and alignment2[counter + 2] != "-":
                        synonymous2 += 1
        elif alignment1[counter + 2] != alignment2[counter + 2] and alignment1[counter + 2] != "-" and alignment2[counter + 2] != "-":
                nonsynonymous2 += 1
        counter += 3

print(synonymous1)
print(nonsynonymous1)
print(synonymous2)
print(nonsynonymous2)

#TODO count # of mutations: indels, synonymous mutations, nonsynonymous mutations, and other stuff

#TODO display data has a table

#TODO each of us needs to write our own individual report using the data we find

#TODO make a presentation for wednesday