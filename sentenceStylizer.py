#!/usr/bin/python3
# This Python file uses the following encoding: utf-8

import os, sys, getopt, pyperclip

if len(sys.argv) == 1 :  
	print ('sentenceStylizer.py "string" -s "spaceChar" -c (optional, to copy into the clipboard)')
	sys.exit(2)
else:
	phrase = sys.argv[1];

copie = False
espace = "    "
phrase = phrase.lower()
phrase = phrase.replace("ê", "e")
phrase = phrase.replace("é", "e")
phrase = phrase.replace("è", "e")
phrase = phrase.replace("ë", "e")
phrase = phrase.replace("ç", "c")
phrase = phrase.replace("'", " ")
phraseStylee = ""

try:
  opts, args = getopt.getopt(sys.argv[2:],"hs:c")
except getopt.GetoptError:
  print ('sentenceBadassator.py "string" -s "spaceChar" -c (optional, to copy into the clipboard)')
  sys.exit(2)
for opt, arg in opts:
  if opt == '-h':
     print ('sentenceBadassator.py "string" -s "spaceChar" -c (optional, to copy into the clipboard)')
     sys.exit()
  elif opt in ('-s'):
     espace = arg
  elif opt in ('-c'):
     copie = True


for i in range(0,len(phrase)) :
    if phrase[i] == ' ':
    	phraseStylee += espace
    elif phrase[i] == '0':
    	phraseStylee += ":zero:"
    elif phrase[i] == '1':
    	phraseStylee += ":one:"
    elif phrase[i] == '2':
    	phraseStylee += ":two:"
    elif phrase[i] == '3':
    	phraseStylee += ":three:"
    elif phrase[i] == '4':
    	phraseStylee += ":four:"
    elif phrase[i] == '5':
    	phraseStylee += ":five:"
    elif phrase[i] == '6':
    	phraseStylee += ":six:"
    elif phrase[i] == '7':
    	phraseStylee += ":seven:"
    elif phrase[i] == '8':
    	phraseStylee += ":eight:"
    elif phrase[i] == '9':
    	phraseStylee += ":nine:"
    elif phrase[i] == '!':
    	phraseStylee += ":exclamation:"
    elif phrase[i] == '?':
    	phraseStylee += ":question:"
    elif phrase[i] == '.':
    	phraseStylee += ":large_blue_circle:"
    else:
        phraseStylee += ":regional_indicator_" + phrase[i] + ": "
        
print(phraseStylee)
if copie :
	print("\nCopié dans le presse papier.")
	pyperclip.copy(phraseStylee)
