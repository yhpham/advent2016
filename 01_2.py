import re

direct = "R2, L1, R2, R1, R1, L3, R3, L5, L5, L2, L1, R4, R1, R3, L5, L5, R3, L4, L4, R5, R4, R3, L1, L2, R5, R4, L2, R1, R4, R4, L2, L1, L1, R190, R3, L4, R52, R5, R3, L5, R3, R2, R1, L5, L5, L4, R2, L3, R3, L1, L3, R5, L3, L4, R3, R77, R3, L2, R189, R4, R2, L2, R2, L1, R5, R4, R4, R2, L2, L2, L5, L1, R1, R2, L3, L4, L5, R1, L1, L2, L2, R2, L3, R3, L4, L1, L5, L4, L4, R3, R5, L2, R4, R5, R3, L2, L2, L4, L2, R2, L5, L4, R3, R1, L2, R2, R4, L1, L4, L4, L2, R2, L4, L1, L1, R4, L1, L3, L2, L2, L5, R5, R2, R5, L1, L5, R2, R4, R4, L2, R5, L5, R5, R5, L4, R2, R1, R1, R3, L3, L3, L4, L3, L2, L2, L2, R2, L1, L3, R2, R5, R5, L4, R3, L3, L4, R2, L5, R5"
# direct = "R8, R4, R4, R8"

preDir = re.findall(r"[\w']+", direct)
directions = []

for group in preDir:
	directions.append(re.split('(\d+)', group))

# change directions to be NESW
if directions[0][0] == 'R':
	directions[0][0] = 'E'
elif directions[0][0] == 'L':
	directions[0][0] = 'W'

for index in range(len(directions)):
	if directions[index][0] == 'R':
		if directions[index - 1][0] == 'N':
			directions[index][0] = 'E'
		elif directions[index - 1][0] == 'E':
			directions[index][0] = 'S'
		elif directions[index - 1][0] == 'S':
			directions[index][0] = 'W'
		elif directions[index - 1][0] == 'W':
			directions[index][0] = 'N'
	elif directions[index][0] == 'L':
		if directions[index - 1][0] == 'N':
			directions[index][0] = 'W'
		elif directions[index - 1][0] == 'E':
			directions[index][0] = 'N'
		elif directions[index - 1][0] == 'S':
			directions[index][0] = 'E'
		elif directions[index - 1][0] == 'W':
			directions[index][0] = 'S'

# create map of visited locations
loc = [0, 0]
locations = {str(loc): 0}

def addToMap(loc):
	if str(loc) in locations:
		print (loc)
	else:
		locations[str(loc)] = 0

for index in range(len(directions)):
	if directions[index][0] == 'N':
		for i in range(int(directions[index][1])):
			loc[1] += 1
			addToMap(loc)
	elif directions[index][0] == 'E':
		for i in range(int(directions[index][1])):
			loc[0] += 1
			addToMap(loc)
	elif directions[index][0] == 'S':
		for i in range(int(directions[index][1])):
			loc[1] -= 1
			addToMap(loc)
	elif directions[index][0] == 'W':
		for i in range(int(directions[index][1])):
			loc[0] -= 1
			addToMap(loc)