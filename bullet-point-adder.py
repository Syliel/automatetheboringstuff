#!/usr/bin/env python3
# bullet point adder - Adds Wikipedia bullet points to the start
# of each line of text to the clipboard

import pyperclip
text = pyperclip.paste()

#separate lines and add stars

lines = text.split('\n')
for i in range(len(lines)): #loop through all indexes in 'lines' list
    lines[i] = '* ' + lines[i] #add star to each string in 'lines' list
text = '\n'.join(lines)
pyperclip.copy(text)
