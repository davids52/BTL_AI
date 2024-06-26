import random
import time
from pyamaze import maze
from pyamaze import agent

def Corresponding_Position(cur_posi,end):
    #TH1
    if cur_posi[0] >= end[0] and cur_posi[1] > end[1]:
        return ['W','N','S','E']
    #TH2
    elif cur_posi[0] >= end[0] and cur_posi[1] < end[1]:
        return ['E','N','S','W']
    elif cur_posi[0] > end[0] and cur_posi[1] == end[1]:
        return ['N','W','E','S']
    #Th3
    elif cur_posi[0] <= end[0] and cur_posi[1] > end[1]:
        return ['W','S','N','E']
    #TH4
    elif cur_posi[0] <= end[0] and cur_posi[1] < end[1]:
        return ['E','S','N','W']
    else:
        return ['S','W','E','N']
    
def ChangPosition(cur_posi,navi):
    if navi == 'W':
        return (cur_posi[0],cur_posi[1] -1)
    elif navi == 'E':
        return (cur_posi[0],cur_posi[1] + 1)
    elif navi == 'S':
        return (cur_posi[0] + 1,cur_posi[1])
    else:
        return (cur_posi[0] - 1,cur_posi[1])
    
def DFS(start,end,maze,visited= None,path= None):
    if visited is None:
        visited = set()
    if path is None:
        path = []
    path = path + [start]
    visited.add(start)
    if start == end:
        return path 
    
    navigation = maze.maze_map[(start)]
    
    for direction in Corresponding_Position(start,end):
        if navigation[direction] == 1:
            new_position = ChangPosition(start,direction)
            if new_position not in visited:
                new_path = DFS(new_position,end,maze,visited,path)
                if new_path:
                    return new_path
    visited.remove(start)
    return None

x,y = map(int,input("Type start point x,y:").split())
i,j = map(int,input("Type end point i,j:").split())

#size cua ma tran owr day
m = maze(30, 30)
m.CreateMaze(x=i,y=j,loopPercent=100)

start = time.perf_counter()
path = DFS((x,y),(i,j),m)
end = time.perf_counter()
print("Execution_time = ",end-start)
if path is not None:
    a = agent(m,x=x,y=y,footprints=True,shape='arrow',color='yellow')
    m.tracePath({a:path})
else:
    print("No route")
print(len(path))
m.run()
