"""def shortestToChar(string, char):
	listOfDistances = []
	for i in range(len(string)):
		if string[i] == char:
			listOfDistances.append(0)
		else:
			distF = len(string)
			distB = len(string)
			for j in range(len(string)-i):
				if string[i+j]== char:
					distF = j
					break
			steps = 0
			for k in range(i-1,-1, -1):
				steps += 1
				if string[k]== char:
					distB = steps
					print('char:',  string[k], 'after steping backward: ', steps)
					break

			if distF <= distB:
				listOfDistances.append(distF)
			else:
				listOfDistances.append(distB)

	return listOfDistances
#[0,1,2,3]
print(shortestToChar('baaa', 'b'))

print(shortestToChar('loveleetcode', 'e'))
"""

def shortestToChar(string, char):
	listOfDists = []
	for i in range(len(string)):
		if string[i] ==  char:
			listOfDists.append(0)
		else:
			distForward =  string[i+1:].find(char)
			distBackward = string[0 if i-1 < 0 else i-1 ::-1].find(char)
			
			if  distForward == -1:
				listOfDists.append(distBackward + 1)
			elif distBackward == -1:
				listOfDists.append(distForward + 1)
			elif distForward <= distBackward:
				listOfDists.append(distForward + 1)
			else:
				listOfDists.append(distBackward + 1)

	return listOfDists

print(shortestToChar('baaa', 'b'))
print(shortestToChar('loveleetcode', 'e'))
