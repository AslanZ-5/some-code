import re

# 1 DIGIT AND NONE DIGIT
Regex_Pattern = r"\d\d\D\d\d\D\d\d\d\d"
print(str(bool(re.search(Regex_Pattern, input()))).lower())
# 2 SPACE  AND NONE SPACE
Regex_Pattern = r"\S\S\s\S\S\s\S\S"
print(str(bool(re.search(Regex_Pattern, input()))).lower())
# 3 any word character and  any non-word character
Regex_Pattern = r"[\w]{3}\W[\w]{10}\W[\w]{3}"
print(str(bool(re.search(Regex_Pattern, input()))).lower())
# 4 Matching Start & End
Regex_Pattern = r"^\d[\w]{4}\.$"
print(str(bool(re.search(Regex_Pattern, input()))).lower())
# 5 Matching Word Boundaries
Regex_Pattern = r'\b[aeiouAEIOU]?[A-Za-z]+\b'
print(str(bool(re.search(Regex_Pattern, input()))).lower())
# 6 Matching Specific Characters
Regex_Pattern = r'^[1-3][120][xs0][30Aa][xsu][\.|,]$'
print(str(bool(re.search(Regex_Pattern, input()))).lower())
# 7 Excluding Specific Characters
Regex_Pattern = r'^[^0-9][^aeiou][^bcdDF][^\s][^AEIOU][^/.|,]$'
print(str(bool(re.search(Regex_Pattern, input()))).lower())
# 8 Matching Character Ranges
Regex_Pattern = r'^[a-z][1-9][^a-z][^A-Z][A-Z]+'
print(str(bool(re.search(Regex_Pattern, input()))).lower())