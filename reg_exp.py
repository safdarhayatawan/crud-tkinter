import re
string = 'abcd'
pattern  = 'a'
if re.match(pattern,string):
    print('match is found')
else:
    print('not found')

string = 'bcda'
pattern  = 'a'
if re.search(pattern,string):
    print('match is found')
else:
    print('not found')

    Lecture: Writing our first regular expression
import re
 
pattern ="a"
 
string ="abc"
 
if re.match(pattern,string):
 
    print('match found')
 
else:
 
    print('no match found')
Lecture: Match & Search
import re
 
pattern ="a"
 
string ="bc"
 
if re.match(pattern,string):
 
    print('match found')
 
else:
 
    print('no match found')
Lecture: Star Metacharacter
import re
 
pattern ="ab*c"
 
string ="abbbbaaaabbbbbc"
 
if re.match(pattern,string):
 
    print('match found')
 
else:
 
    print('no match found')


Lecture: Plus Metacharacter example
import re
 
pattern ="a+bc"
 
string ="aaaaabc"
 
if re.match(pattern,string):
 
    print('match found')
 
else:
 
    print('no match found')


Lecture: Curly braces example
import re
 
pattern =r"ab{c}"
 
string ="abbbbbb"
 
if re.match(pattern,string):
 
    print('match found')
 
else:
 
    print('no match found')


Lecture: Wildcard Example
import re
 
pattern =r"a.b"
 
string ="acbb"
 
if re.match(pattern,string):
 
    print('match found')
 
else:
 
    print('no match found')
Lecture: Optional metacharacter example
import re
 
pattern =r"python-?file"
 
string ="pythonfile"
 
if re.match(pattern,string):
 
    print('match found')
 
else:
 
    print('no match found')
Lecture: Caret metacharacter
import re
 
pattern =r"^an"
 
string ="any"
 
if re.match(pattern,string):
 
    print('match found')
 
else:
 
    print('no match found')
Lecture: Character class
import re
 
pattern =r"[0-9]"
 
string ="0123"
 
if re.match(pattern,string):
 
    print('match found')
 
else:
 
    print('no match found')
Lecture: Find All
import re
 
text ="the sun is shining, the birds are singing"
pattern =r"the"
 
matches = re.findall(pattern,text)
print(matches)
Lecture: Character class & find all
import re
 
text ="The cat and the dog sat on the mat"
pattern =r"[abc]"
 
matches = re.findall(pattern,text)
print(matches)
Lecture: Finding vowels
import re
 
text ="The quick brown fox jumps over the lazy dog"
pattern =r"[aeiou]"
 
matches = re.findall(pattern,text)
print(matches)
Lecture: Shorthand for numeric characters
import re
 
text ="The meeting is scheduled at 9 AM"
pattern =r"\d"
 
matches = re.findall(pattern,text)
print(matches)
Lecture: W shorthand
import re
 
text ="The sentence includes punctuations! \n"
pattern =r"\W"
 
matches = re.findall(pattern,text)
print(matches)
Lecture: S shorthand
import re
 
text ="The sentence \t includes punctuations! \n"
pattern =r"\S+"
 
matches = re.findall(pattern,text)
print(matches)
Lecture: Combining shorthands & metacharacters
import re
 
text ="Helooooo Python is awesomeeeee!"
pattern =r"\w*o+\w*"
 
matches = re.findall(pattern,text)
print(matches)
Lecture: Matching phone numbers part 1
import re
 
text ="Please contact me at +1 (123) 456-7890 or via emial at john@example.com"
pattern =r"\+?\d{1,3}[-.\s]\(?\d{1,3}\)?]"
 
matches = re.findall(pattern,text)
print(matches)
Lecture: Matching phone numbers part 2
import re
 
text ="Please contact me at +1 (123) 456-7890 or via emial at john@example.com"
pattern =r"\+?\d{1,3}[-.\s]\(?\d{1,3}\)?[-.\s]?\d{1,3}[-.\s]?d{1,4}"
 
matches = re.findall(pattern,text)
print(matches)


Lecture: Matching emails
import re
 
text ="Please contact me at +1 (123) 456-7890 or via emial at john@example.com"
pattern =r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
 
matches = re.findall(pattern,text)
print(matches)
Lecture: Checking validity of emails
import re
 
email = input("Enter email address")
pattern =r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
 
re.match(pattern,email):
    print("Valid email")
else:
    print(Invalid Email)
# Lecture: Matching dates
# import re
 
text = "Date: 2023-06-08 1990-01-02"
pattern =r"\d{4}-\d{2}-\d{2}"
 
dates = re.findall(pattern,text)
print(dates)
