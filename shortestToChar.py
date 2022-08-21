def shortestToChar(string, char):
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
