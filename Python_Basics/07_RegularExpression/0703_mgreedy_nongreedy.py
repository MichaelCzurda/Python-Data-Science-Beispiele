#! python3
#0703_mgreedy_nongreedy.py - More Regex
#Since (Ha){3,5} can match three, four, or five instances of Ha in the string
#'HaHaHaHaHa', you may wonder why the Match object’s call to group() in the
#previous curly bracket example returns 'HaHaHaHaHa' instead of the shorter
#possibilities. After all, 'HaHaHa' and 'HaHaHaHa' are also valid matches of the
#regular expression (Ha){3,5}.

#Python’s regular expressions are greedy by default, which means that in
#ambiguous situations they will match the longest string possible. The nongreedy
#version of the curly brackets, which matches the shortest string possible,
#has the closing curly bracket followed by a question mark.
import re

greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
print(mo1.group())
#HaHaHaHaHa

nonGreedyRegex = re.compile(r'(Ha){3,5}?')
mo2 = nonGreedyRegex.search('HaHaHaHaHa')
print(mo2.group())
#HaHaHa
