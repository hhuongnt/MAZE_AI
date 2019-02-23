a =     ["####################",
         "#                  #",
         "#                  #",
         "#                  #",
         "#       o    o     #",
         "#              o   #",
         "#                  #",
         "#                  #",
         "#           o     A#",
         "####################"]


resources = ['o', '!']
# find player_coordinate
def player_coordinate():
    player = [0,0]
    for row in range(len(a)):
        for char in range(len(a[row])):
            if a[row][char] == 'A':
                player[0] += row
                player[1] += char
    return player


player = player_coordinate()


def is_it_resources(row,char):
    if a[row][char] == 'o' or a[row][char] == '!':
        return 'resources'
    else:
        return 'not_resources'


def get_resources_pos():
    list_resc = []
    for row in range(len(a)):
        for char in range(len(a[row])):
            pos = [row,char]
            if is_it_resources(row, char) == 'resources':
                list_resc.append(pos)
    return list_resc
print(get_resources_pos())


class Cell():
    def _init_(self,row,char,reachable):
        self.reachable = reachable
        self.row = row
        self.char = char
        self.parent = None
        self.g = 0
        self.h = 0
        self.f = 0


class AStar():
    def _init_(self):
        self.opened = []
        heapg.heapify(self.opened)
        self.closed = []
        self.cells = []
        self.grid_height = len(a)
        self.grid_width = len(a[0])


def list_reachable_cells(self):
    for row in range(len(a)):
        for char in range(len(a[row])):
            if a[row][char] != '#':
                reachable = True
            else:
                reachable = False
            self.cells.append(Cell(row,char,reachable))


def get_adj_cells(self,cell):
    cells = []
    if cell.char < self.grid_width-1:
	        cells.append(self.get_cell(cell.char+1, cell.row))
	    if cell.row > 0:
	        cells.append(self.get_cell(cell.char, cell.row-1))
	    if cell.char > 0:
	        cells.append(self.get_cell(cell.char-1, cell.row))
	    if cell.row < self.grid_height-1:
	        cells.append(self.get_cell(cell.char, cell.row+1))
	    return cells


def update_cell(self,adj,cell):
