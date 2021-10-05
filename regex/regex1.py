import re

# 1 DIGIT AND NONE DIGIT
Regex_Pattern1 = r"\d\d\D\d\d\D\d\d\d\d"
# 2 SPACE  AND NONE SPACE
Regex_Pattern2 = r"\S\S\s\S\S\s\S\S"
# 3 any word character and  any non-word character
Regex_Pattern3 = r"[\w]{3}\W[\w]{10}\W[\w]{3}"
# 4 Matching Start & End
Regex_Pattern4 = r"^\d[\w]{4}\.$"
# 5 Matching Word Boundaries
Regex_Pattern5 = r'\b[aeiouAEIOU]?[A-Za-z]+\b'
# 6 Matching Specific Characters
Regex_Pattern6 = r'^[1-3][120][xs0][30Aa][xsu][\.|,]$'
# 7 Excluding Specific Characters
Regex_Pattern7 = r'^[^0-9][^aeiou][^bcdDF][^\s][^AEIOU][^/.|,]$'
# 8 Matching Character Ranges
Regex_Pattern8 = r'^[a-z][1-9][^a-z][^A-Z][A-Z]+'
# 9 Matching {x} Repetitions
Regex_Pattern9 = r'[A-Za-z24680]{40}[13579|\s]{5}$'
# 10 Matching {x, y} Repetitions
Regex_Pattern10 = r'^[\d]{1,2}[A-Za-z]{3,}[/.]{0,3}$'
# 11 Matching Zero Or More Repetitions
Regex_Pattern11 = r'^[\d]{2,}[a-z]*[A-Z]*$'
