import re

pattern = re.compile("ca.e")

def print_match(m):
	if m:
		print("m.group():", m.group())
		print("m.string():", m.string)
		print("m.start():", m.start())
		print("m.end():", m.end())
		print("m.span():", m.span())
	else:
		print("No match :(")

# m = pattern.match("ce")
# print_match(m)

# m = pattern.search("bro be careful")
list = pattern.findall("dutch cafe") # findall return as a list. 
print(list)