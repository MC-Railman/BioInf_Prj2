# A sequence aligning program for Dr. Duan's Bioinformatics class
# Written by Tristan Hess, Scott Owens, and Ryan Weston

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
print(gene2)


#TODO implement pairwise alignment between the two sequences

#TODO count # of mutations: indels, synonymous mutations, nonsynonymous mutations, and other stuff

#TODO display data has a table

#TODO each of us needs to write our own individual report using the data we find

#TODO make a presentation for wednesday