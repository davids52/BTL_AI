from Cells import Cell
import pygame
import time

clock = pygame.time.Clock()
WIDTH = 1200
HEIGHT = 600
class Maze_duplicate:
    def __init__(self,tile) -> None:
        self.grid_cells = [Cell(col,row,tile) for row in range(HEIGHT//tile) for col in range(WIDTH//tile)]

    def maze_map(self):
        path_cell = {}
        for cell in self.grid_cells:
            path_cell[(cell.x,cell.y)] = cell.walls
        return path_cell
    def generate_maze(self,sc):
        generated_maze = True
        oke = True
        current_cell = self.grid_cells[0]
        stack = []
        breakcount = 1
        while len(stack) != 0 or oke :
            oke = False
            sc.fill(pygame.Color('black'))
            
            
            for cell in self.grid_cells:
                # print(cell.x,cell.y)
                cell.draw(sc)
                # cell.draw_inside()
                # for react in cell.get_rects():
                #     pygame.draw.rect(sc,pygame.Color('blue'),react)
            current_cell.visited = True
            for rect in current_cell.get_rects():
                # print(rect)   
                pygame.draw.rect(sc,pygame.Color('blue'),rect)
            
            next_cell = current_cell.check_neighbors(self.grid_cells)
            if next_cell:
                next_cell.visited = True
                breakcount+=1
                stack.append(current_cell)
                remove_walls(current_cell,next_cell)
                current_cell = next_cell
            elif stack:
                current_cell = stack.pop()    
            pygame.display.flip()
            clock.tick(20)
        
        return
    def tracePath(self,start,end,maze_map,grid_cells,sc):
        path = DFS(start,end,maze_map)
        if path is not None:
            for cell in path:
                time.sleep(.2)
                # print("oke")
                for i in grid_cells:
                    if i.x == cell[0] and i.y == cell[1]:
                        i.draw_inside(sc)
                pygame.display.update()
        return
            
def DFS(start,end,maze,visited= None,path= None):
    if visited is None:
        visited = set()
    if path is None:
        path = []
    path = path + [(start)]
    visited.add(start)
    if start == end:
        return path 
    
    navigation = maze[(start)]
    
    for direction in Corresponding_Position(start,end):
        if navigation[direction] == False:
            new_position = ChangPosition(start,direction)
            if new_position not in visited:
                new_path = DFS(new_position,end,maze,visited,path)
                if new_path:
                    return new_path
    visited.remove(start)
    return None
def Corresponding_Position(cur_posi,end):
    #TH1
    if cur_posi[0] >= end[0] and cur_posi[1] > end[1]:
        return ['left','top','bottom','right']
    #TH2
    elif cur_posi[0] >= end[0] and cur_posi[1] < end[1]:
        return ['right','top','bottom','left']
    elif cur_posi[0] > end[0] and cur_posi[1] == end[1]:
        return ['top','left','right','bottom']
    #Th3
    elif cur_posi[0] <= end[0] and cur_posi[1] > end[1]:
        return ['left','bottom','top','right']
    #TH4
    elif cur_posi[0] <= end[0] and cur_posi[1] < end[1]:
        return ['right','bottom','top','left']
    else:
        return ['bottom','left','right','top']
def ChangPosition(cur_posi,navi):
    if navi == 'left':
        return (cur_posi[0] - 1,cur_posi[1])
    elif navi == 'right':
        return (cur_posi[0] + 1,cur_posi[1])
    elif navi == 'bottom':
        return (cur_posi[0],cur_posi[1] +1)
    else:
        return (cur_posi[0],cur_posi[1] - 1)
def remove_walls(current, next):
    dx = current.x - next.x
    if dx == 1:
        current.walls['left'] = False
        next.walls['right'] = False
    elif dx == -1:
        current.walls['right'] = False
        next.walls['left'] = False
    dy = current.y - next.y
    if dy == 1:
        current.walls['top'] = False
        next.walls['bottom'] = False
    elif dy == -1:
        current.walls['bottom'] = False
        next.walls['top'] = False