# get the occurence of all vowels and consonent from the large given string.

def vc(string):
   vowels=[each for each in string if each in "aeiouAEIOU"]
   print("Length of the vowels from a string: ",len(vowels))
   consonent=[each for each in string if each not in "aeiouAEIOU "]
   print("length of the consonants from a string: ",len(consonent))
string=input()
vc(string)