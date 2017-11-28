# Psycholinguistic Analysis of Code Mixing
Speech and Natural Language Processing Term Project: CS60057. 
Department of Computer science and Engineering, Indian Institute of Technology Kharagpur.


##### Team members:
1. Avirup Saha
2. Indrasekhar Sengupta
3. Soumi Das
4. Ayan Chandra


The following files are to be executed in the chronological order as mentioned:

1. **Concat_files.py**: This file is used to extract the files of all valid users ( users who have completed all the 3 surveys ) and write the contents from all users’ files to a file named as “result.txt”
2. **Keywordnet.py**: This file is used to extract the distinct set of words used for transliteration and translation with the output being stored in “output_file.txt”
3. **Partc_resp_time_v2.py**: This file is the core of entire project. It computes the 4 metrics defined of all distinct words and stores it in “avgreaction_dict.txt” and also keeps the translation and transliteration time of each word and each participant in “reaction_time_count1.txt”.
4. **sortrankList.py**: This file sorts the words on the basis of the 4 metrics and stores them in 4 different files named as “sortedRankedWordByMetric(1/2/3/4).txt”.
5. **Find_spcorr.py**: This file finds the Spearman Correlation Coefficient between the ranks provided by the baseline paper[1] and the ranks we obtained in the last file above. So we get 4 correlation coefficients for the 4 metrics.
6. **Word2vec_cm.py**: This file represents each word ( both transliterated and translated ) in the form of a vector depending on a particular trend [ Number of people terming it (transliterated / translated) as valid in the particular bucket / total number of people terming it as valid in all buckets ]. We find out the L2 norm between the 2 versions of the words.


The metrics and the format of the files are provided below for clear understandability:

**Metric 1**: Transliterated valid/Translated valid

**Metric 2**: Transliterated valid/(Translated valid+Transliterated Valid)

**Metric 3**: (Transliterated valid/Average reaction time of transliterated valid)/(Translated valid/Average reaction time of translated valid)

**Metric 4**:  (Transliterated valid/Average reaction time of transliterated valid)/((Translated valid/Average reaction time of translated valid) + (Transliterated invalid/Average reaction time of transliterated invalid))

FILE: result.txt
1. Col1: Word
2. Col2: Translated/Transliterated
3. Col3: Valid/Invalid/TimeOut
4. Col4: Response Time

FILE: output_file.txt
1. Distinct word sets (57)

FILE: reaction_time_count1.txt
1. Col1: word (for all words)
2. Col2: participant
3. Col3: transliterated time
4. Col4: translated time

FILE: avgreaction_dict1.txt
1. Col1: Word
2. Col2: Metric1
3. Col3: Metric 2
4. Col4: Metric 3
5. Col5: Metric 4

FILE: sortedRankedWordByMetric1.txt : Rank list on the basis of Metric1
1. Col1: Word
2. Col2: Rank

FILE: sortedRankedWordByMetric2.txt : Rank list on the basis of Metric2
1. Col1: Word
2. Col2: Rank

FILE: sortedRankedWordByMetric3.txt : Rank list on the basis of Metric3
1. Col1: Word
2. Col2: Rank

FILE: sortedRankedWordByMetric4.txt : Rank list on the basis of Metric4
1. Col1: Word
2. Col2: Rank

FILE: vectorword.txt
1. Col1 : Word
2. Col2: Interval
3. Col3: Transliterated Index ( dimension)
4. Col4: Translated Index (dimension)

FILE: interval.txt
1. Col1: Word
2. Col2: Interval start
3. Col3: Number of participants terming it as transliterated in the interval
4. Col4: Number of participants terming it as translated in the interval

FILE: total.txt
1. Col1: Word
2. Col2: Total Transliterated Count
3. Col3: Total Translated Count
4. Col3: Euclidean Distance (calculated on the basis of the Transliterated and Translated Index we calculated in vectorword.txt )

##### Survey: http://www.psytoolkit.org/cgi-bin/psy2.4.0/survey?s=VCA3r

##### Reference: 
1. Jasabanta Patro, Bidisha Samanta, Saurabh Singh, Abhipsa Basu, Prithwish Mukherjee, Monojit Choudhury, Animesh Mukherjee, "All that is English may be Hindi: Enhancing language identification through automatic ranking of likeliness of word borrowing in social media", EMNLP 2017
2. Psytoolkit: www.psytoolkit.org
3. K. Bali, J. Sharma, M. Choudhury, and Y. Vyas. 2014. “i am borrowing ya mixing?” an analysis of english-hindi code mixing in facebook. In First workshop on Computational approaches to code-switching, EMNLP, page 116.
Survey: http://www.psytoolkit.org/cgi-bin/psy2.4.0/survey?s=VCA3r

