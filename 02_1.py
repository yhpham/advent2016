from enum import Enum

key1 = "LRRLLLRDRURUDLRDDURULRULLDLRRLRLDULUDDDDLLRRLDUUDULDRURRLDULRRULDLRDUDLRLLLULDUURRRRURURULURRULRURDLULURDRDURDRLRRUUDRULLLLLDRULDDLLRDLURRLDUURDLRLUDLDUDLURLRLDRLUDUULRRRUUULLRDURUDRUDRDRLLDLDDDLDLRRULDUUDULRUDDRLLURDDRLDDUDLLLLULRDDUDDUUULRULUULRLLDULUDLLLLURRLDLUDLDDLDRLRRDRDUDDDLLLLLRRLLRLUDLULLDLDDRRUDDRLRDDURRDULLLURLRDLRRLRDLDURLDDULLLDRRURDULUDUDLLLDDDLLRLDDDLLRRLLURUULULDDDUDULUUURRUUDLDULULDRDDLURURDLDLULDUDUDDDDD"
key2 = "RUURUDRDUULRDDLRLLLULLDDUDRDURDLRUULLLLUDUDRRUDUULRRUUDDURDDDLLLLRRUURULULLUDDLRDUDULRURRDRDLDLDUULUULUDDLUDRLULRUDRDDDLRRUUDRRLULUULDULDDLRLURDRLURRRRULDDRLDLLLRULLDURRLUDULDRDUDRLRLULRURDDRLUDLRURDDRDULUDLDLLLDRLRUDLLLLLDUDRDUURUDDUDLDLDUDLLDLRRDLULLURLDDUDDRDUDLDDUULDRLURRDLDLLUUDLDLURRLDRDDLLDLRLULUDRDLLLDRLRLLLDRUULUDLLURDLLUURUDURDDRDRDDUDDRRLLUULRRDRULRURRULLDDDUDULDDRULRLDURLUDULDLDDDLRULLULULUDLDDRDLRDRDLDULRRLRLRLLLLLDDDRDDULRDULRRLDLUDDDDLUDRLLDLURDLRDLDRDRDURRDUDULLLDLUDLDRLRRDDDRRLRLLULDRLRLLLLDUUURDLLULLUDDRLULRDLDLDURRRUURDUDRDLLLLLLDDDURLDULDRLLDUDRULRRDLDUDRLLUUUDULURRUR"
key3 = "URRRLRLLDDDRRLDLDLUDRDRDLDUDDDLDRRDRLDULRRDRRDUDRRUUDUUUDLLUURLRDRRURRRRUDRLLLLRRDULRDDRUDLRLUDURRLRLDDRRLUULURLURURUDRULDUUDLULUURRRDDLRDLUDRDLDDDLRUDURRLLRDDRDRLRLLRLRUUDRRLDLUDRURUULDUURDRUULDLLDRDLRDUUDLRLRRLUDRRUULRDDRDLDDULRRRURLRDDRLLLRDRLURDLDRUULDRRRLURURUUUULULRURULRLDDDDLULRLRULDUDDULRUULRRRRRLRLRUDDURLDRRDDULLUULLDLUDDDUURLRRLDULUUDDULDDUULLLRUDLLLRDDDLUUURLDUDRLLLDRRLDDLUDLLDLRRRLDDRUULULUURDDLUR"
key4 = "UULDRLUULURDRLDULURLUDULDRRDULULUDLLDURRRURDRLRLLRLDDLURRDLUUDLULRDULDRDLULULULDDLURULLULUDDRRULULULRDULRUURRRUDLRLURDRURDRRUDLDDUURDUUDLULDUDDLUUURURLRRDLULURDURRRURURDUURDRRURRDDULRULRRDRRDRUUUUULRLUUUDUUULLRRDRDULRDDULDRRULRLDLLULUUULUUDRDUUUDLLULDDRRDULUURRDUULLUUDRLLDUDLLLURURLUDDLRURRDRLDDURLDLLUURLDUURULLLRURURLULLLUURUUULLDLRDLUDDRRDDUUDLRURDDDRURUURURRRDLUDRLUULDUDLRUUDRLDRRDLDLDLRUDDDDRRDLDDDLLDLULLRUDDUDDDLDDUURLDUDLRDRURULDULULUDRRDLLRURDULDDRRDLUURUUULULRURDUUDLULLURUDDRLDDUDURRDURRUURLDLLDDUUDLLUURDRULLRRUUURRLLDRRDLURRURDULDDDDRDD"
key5 = "LLRUDRUUDUDLRDRDRRLRDRRUDRDURURRLDDDDLRDURDLRRUDRLLRDDUULRULURRRLRULDUURLRURLRLDUDLLDULULDUUURLRURUDDDDRDDLLURDLDRRUDRLDULLRULULLRURRLLURDLLLRRRRDRULRUDUDUDULUURUUURDDLDRDRUUURLDRULDUDULRLRLULLDURRRRURRRDRULULUDLULDDRLRRULLDURUDDUULRUUURDRRLULRRDLDUDURUUUUUURRUUULURDUUDLLUURDLULUDDLUUULLDURLDRRDDLRRRDRLLDRRLUDRLLLDRUULDUDRDDRDRRRLUDUDRRRLDRLRURDLRULRDUUDRRLLRLUUUUURRURLURDRRUURDRRLULUDULRLLURDLLULDDDLRDULLLUDRLURDDLRURLLRDRDULULDDRDDLDDRUUURDUUUDURRLRDUDLRRLRRRDUULDRDUDRLDLRULDL"

numpad = [	[1, 2, 3], 
			[4, 5, 6], 
			[7, 8, 9]]

row = 1
col = 1
pos = numpad[row][col]

for move in key5:
	if move == 'U':
		if pos != 1 and pos != 2 and pos != 3:
			row -= 1
			pos = numpad[row][col]
	elif move == 'R':
		if pos != 3 and pos != 6 and pos != 9:
			col += 1
			pos = numpad[row][col]
	elif move == 'D':
		if pos != 7 and pos != 8 and pos != 9:
			row += 1
			pos = numpad[row][col]
	elif move == 'L':
		if pos != 1 and pos != 4 and pos != 7:
			col -= 1
			pos = numpad[row][col]

print (pos)
