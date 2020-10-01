import sys

args = sys.argv
text = args[1]
text = list(text)
for i in range(len(text)):
	print(hex(ord(text[i])))
for i in range(len(text)):
	if ord(text[i]) > 0xdc00:
		text[i] = chr(ord(text[i]) - 0xdc00) #so weeeeeeeird, fucking utf-8 and shitty encoding
	print(chr(ord(text[i]) - i), end="")
