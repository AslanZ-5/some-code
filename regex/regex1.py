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
# 12 Matching One Or More Repetitions
Regex_Pattern12 = r'^\d+[A-Z]+[a-z]+$'
# 13 Matching Ending Items
Regex_Pattern13 = r'^[A-Za-z]*s$'
# 14 Capturing & Non-Capturing Groups ( S should have 3 or more consecutive repetitions of ok)
Regex_Pattern14 = r'(ok){3,}'
# 15 Alternative Matching
Regex_Pattern15 = r'^(Mr\.|Mrs\.|Ms\.|Dr\.|Er\.)[A-Za-z]+$'
# 16 Matching Same Text Again & Again by "/group_number"
Regex_Pattern16 = r'([a-z]\w\s\W\d\D[A-Z][A-Za-z][aeiouAEIOU]\S)\1'
# 17 Backreferences To Failed Groups
Regex_Pattern17 = r"^(\d{8})$|^(\d\d-\d\d-\d\d-\d\d)$"
#18 Positive Lookahead
Regex_Pattern18 = r'o(?=oo)'
#19 Negative Lookahead
Regex_Pattern19 = r"(.)(?!\1)"
# Positive Lookbehind
Regex_Pattern20 = r"(?<=[13579])\d"
