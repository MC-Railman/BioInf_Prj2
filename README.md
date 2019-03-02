# BioInf_Prj2
Project 2 for BioInformatics
CS445/545 Project2 Understanding Sequence Comparison and Influenza Virus

Flu is an infectious disease caused by an influenza virus. It has been reported that this year’s influenza vaccine is only 47% effective, yet it’s considered “effective” since the 2017-2018 flu vaccine was estimated to be only 40% effective [cdc].

[cdc] Interim Estimates of 2018–19 Seasonal Influenza Vaccine Effectiveness — United States, February 2019. Weekly / February 15, 2019 / 68(6);135–139. https://www.cdc.gov/mmwr/volumes/68/wr/mm6806a2.htm?s_cid=mm6806a2_w

For your second project, you will try to understand the virus from several different points of view. It is to be done in a project group. The effort and responsibilities of the students in a group must be clearly enough delimited and stated in a statement (attached to your project report) so that each of you can be graded fairly and separately.

The goals of this project:

·       Understanding genetic makeup of flu virus;

·       Implementing sequence alignment algorithms;

·       Understanding different types of mutations;

·       Practicing on conducting comparative scientific research.

 

For graduate students, you are required to read the following two papers for your project:

1.     Mossad SB. Influenza update 2018-2019: 100 years after the great pandemic. Cleve Clin J Med. 2018 Nov; 85(11):861-869. doi: 10.3949/ccjm.85a.18095.

https://www.ncbi.nlm.nih.gov/pubmed/30395523

2.     Nicole M. Bouvier, Peter Palese. The Biology of Influenza Viruses, Vaccine. 2008 Sep 12; 26(Suppl 4): D49–D53.

https://www.ncbi.nlm.nih.gov/pubmed/19230160/

 

Genomic data you will use for your project should be retrieved from Genbank. For example

·       ViralMultiSegProj274585

o   https://www.ncbi.nlm.nih.gov/assembly/GCF_000928555.1

·       Influenza A virus (A/Shanghai/02/2013(H7N9)) segment 6 neuraminidase

o   https://www.ncbi.nlm.nih.gov/nuccore/NC_026429.1

·       Influenza A virus (A/human/Ohio/2006(H3N2)) segment 6 neuraminidase

o   https://www.ncbi.nlm.nih.gov/nuccore/EF554797.1

(Note: GenBank Accession Numbers KF021594-KF021601 represent sequences from the 8 segments of Influenza A virus (A/Shanghai/02/2013(H7N9) and GenBank Accession Numbers EF554792-EF554799 represent sequences from the 8 segments of Influenza A virus (A/human/Ohio/2006(H3N2)).)


 

To complete the project, you need:

1)     Understand Genbank entries at NCBI and answer the following questions for “https://www.ncbi.nlm.nih.gov/assembly/GCF_000928555.1”:

i)       What’s the size/length of this flu virus genome? What is it made of? (RNA/DNA)?

ii)     How many genes does this virus genome contain; what are their names?

iii)   What does CDS mean? How many CDSs are there? How many proteins does the virus genome code? What are they?

2)     Implement pairwise alignment in python (or whatever language your group likes) (you group should figure out which alignment algorithm you need to use);

3)     Pairwise align a sequence of “NP” gene with another “NP” gene, for example NC_026429.1 vs EF554797.1;

4)     Count the number of mutations and characterize each mutation. So you should have two tables like:

NP

#indel

# synonymous mutations

# nonsynonymous mutations

Other things you find relevant /interesting

Shanghai

 

 

 

 

Ohio

 

 

 

 

5)     Run BLAST on the two genes and summarize the findings:

NP

#indel

# synonymous mutations

# nonsynonymous mutations

Other things you find relevant /interesting

Shanghai

 

 

 

 

Ohio

 

 

 

 

6)     Other things that might worth to look into.

 

What to submit – Individual Report which includes:

 Abstract - Give a brief presentation of the problem, summarize the methods, and outline your results and conclusions.

 

Introduction - Detailed problem description and background knowledge of the problem. Outline approaches you take to solve the problem and present a short literature survey on the approaches you are taking.

 

Materials and methods - Description of data acquisition, including the source. Description of the methods used, including complexity analysis of the algorithms.

 

Implementation - Give a high level description of your implementation of your approach.

 

Results and discussion - Describe and analyze the results of your computation. Use tables or graphs wherever you can.

 

Conclusion - Conclude your study. Summarize the main objectives and results, as in the introduction, but from the perspective of the readers who have read the main part of the report and need reminding what it is all about.

 

References - Give detailed references to the sources of information. References should be actually referred to in the text. For example write "see ref. 16" if you want to refer to a book/paper for an idea you present in the report.

 

Appendices - Include your source code with all the good comments and other supporting materials.

 

For graduate students, you need to include a summary of the two papers you are required to read and your perspective on flu virus.

 

Submission instructions
Paper copy and electronic copy

When you are ready to submit, obtain a printed copy of your report and your Python program. Remember to sign and attach the required Academic Integrity Pledge cover sheet. The printed report and program must be turned in by the start of class on the date the program is due.

In addition, you must submit an electronic copy of your program through Brightspace. You are required to zip your program inside an archive following these steps:

1.    Create a folder named group_# (replace # by your group number). 

Place the source file(s) inside the folder.
Right-click on the folder and choose Send To... Compressed Folder (or use some other Zip utility to archive the entire folder). The goal is to create a zip archive namedgroup_#.zip that contains the folder which contains the source files for your project. 
Upload this single zipped file to Brightspace.
 
