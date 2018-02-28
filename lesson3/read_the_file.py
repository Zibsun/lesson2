import re

word_count = 0

def get_word_count(str):
	# splitting using regexp
    words = re.split("[ .,;@#$%^&*(){}|?~\n]", str)	
    # getting rid of empty strings
    a = list(filter(len, words))
    print (a)
    return len(a)

with open('referat.txt', 'r', encoding='utf-8') as f:
    for line in f:
    	word_count += get_word_count(line)

print (word_count)