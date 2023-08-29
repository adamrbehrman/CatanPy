from game.node import Point

class DisplayGrid():

    def __init__(self, length, width, scale = 1, empty_icon = '.'):
        self.grid = []
        self.scale = scale
        self.empty_icon = empty_icon
        for _ in range(length):
            self.grid.append([self.empty_icon] * width)

    def update_grid(self, icon:str, p:Point):
        self.grid[p.x][p.y] = icon

    def __str__(self):
        s = ''

        for i in range(len(self.grid)):
            if i > 9:
                s += str(i) + ' |'
            else:
                s += str(i) + '  |'
            
            s += ' ' * self.scale

            for j in range(len(self.grid[i])):
                curr_icon = str(self.grid[i][j])
                match len(curr_icon):
                    case 1:
                        s += curr_icon + '  '*self.scale
                    case 2:
                        s += curr_icon + ' '*self.scale
                    case 3:
                        s = s[:-1] + curr_icon + ' '*self.scale
                    case 4:
                        s = s[:-1] + curr_icon
                    case 5:
                        s = s[:-2] + curr_icon
                    case 6:
                        s = s[:-3] + curr_icon
            
            s += '\n'*self.scale

        s += '   +'
        for i in range(len(self.grid[0])):
            s += '-+-'*self.scale

        s += '\n     '
        for i in range(65, 65 + len(self.grid[0])):
            c = chr(i+6) if i > 65 + 25 else chr(i)
            s += c + '  '*self.scale
            
        return s