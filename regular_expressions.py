import re

pattern1= re.compile("hamza")

string1="this is a toy."
string2="hamza"

print(pattern1.search(string1))
print(pattern1.fullmatch(string2))






