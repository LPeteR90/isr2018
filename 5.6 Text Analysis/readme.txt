Input: Taking the address of the txt file as argument. If no argument is given, the program takes the default file "austin.txt" within the folder.
Output: 
(1) Total number of words within the given txt file.
(2) Number of distinct words within the given txt file.
(3) Word frequencies for the ten highest ranked words.
(4) Word frequency distribution: r*pr for the ten highest ranked words.
(5) How many words only appear 1..10 times.

Outputs 3 to 5 are printed as dictionaries. The output is written into a txt file named 'output.txt'.

Output for given test input:

No file given - reading from default file.
Filename: austin.txt
Number of words: 124921
Number of distinct words: 7993
Word Frequencies: [('the', 4221), ('to', 4150), ('of', 3714), ('and', 3443), ('her', 2103), ('I', 1996), ('a', 1931), ('was', 1841), ('in', 1838), ('that', 1502)]
r*pr: {'the': 0.03378935487227928, 'to': 0.033220995669262975, 'of': 0.029730789859191007, 'and': 0.02756141881669215, 'her': 0.016834639492159045, 'I': 0.01597809815803588, 'a': 0.01545776931020405, 'was': 0.0147373139824369, 'in': 0.014713298804844661, 'that': 0.012023598914513973}
Words only appearing x times: [(1, 3576), (2, 1082), (3, 698), (4, 402), (5, 275), (6, 214), (7, 186), (8, 153), (9, 108), (10, 90)]
