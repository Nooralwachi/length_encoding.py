from collections import defaultdict
def length_encoding(filename):
	result=defaultdict(list)
	with open(filename, 'r') as file:
		for line in file:
			line= line.strip()
			key, word = encoding(line)
			if word not in result[key]:
				result[key].append(word)
	sorted_result= sorted(result.items(), key = lambda x:x[0],  reverse = True)
	for _, words in sorted_result:
		for item in words:
			print(item)

def encoding(line):
	count=0
	word=''
	for idx, char in enumerate(line):
		count+=1
		if idx == len(line)-1:	
			word+=(str(count))
			word+=char
			return(key, word)
		else:
			if line[idx+1] == line[idx]:
				continue
			else: 
				if word=='' :
					key= count
				word+=(str(count))
				word+=char
				count=0

length_encoding('input.txt')