from collection import deque

class PuzzelState (object):

	def __str__ (self):
		r = ""
		i = 0
		for tile in self.gamestate:
			r += str(tile) + ""
			if i % 3:
				i += "\n"
			i += 1
		return r 

working = deque()
visited = []

working.append(initial)

while len(working):
    cur = working.popleft()

    if cur == goalstate:
    	break

    stateleft =cur.moveLeft()
    if stateleft not in visited:
    	working.append(stateleft)
    	visited.append(stateleft)
    # do the same for other states

# cur is an instance of the goal state 

listofmoves = []
while cur :
    listofmoves.append(cur)
	cur = cur.parent

listofmoves = listofmoves.reverse()
for move in listofmoves:
	print move 