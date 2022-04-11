from queue import PriorityQueue
import math

def MeasureDist(x, y):
    #Measure distance
    a = (x[0] - y[0]) ** 2
    b = (x[1] - y[1]) ** 2
    distance = math.sqrt(a + b)
    return distance
    pass

def shortest_path(gr,start,goal):
    #previous dict()
    prev = {start:None}
    #initialize dict dis_start from start
    dis_start = {start:0}
    #priority queue
    qu = PriorityQueue()
    qu.put(start,0)
    #while qu is not empty
    
    while not qu.empty():
        cur = qu.get()
        if cur == goal:
            pthConstructed(prev, start, goal)
        for vertex in gr.roads[cur]:
            # x- cord
            x = gr.intersections[cur]
            # y- cord
            y = gr.intersections[vertex]
            upScore = dis_start[cur]+  MeasureDist(x,y)
            
            if vertex not in dis_start or upScore < dis_start[vertex]:
                dis_start[vertex]=upScore
                #x- cord
                x = gr.intersections[cur]
                #y- cord
                y = gr.intersections[vertex]
                total = upScore + MeasureDist(x,y)
                qu.put(vertex,total)
                prev[vertex]=cur
    #final path            
    path = pthConstructed(prev, start, goal)
    path.reverse()
    return path
    pass
    
def pthConstructed(prev, start, goal):
    #current is equal i am putting with goal afterthat updating
    curr = goal
    #initialize array pth
    pth = [curr]
    # looping upto cur not equal to start and updating path
    while curr != start:
        curr = prev[curr]
        #update with prev[curr]
        pth.append(curr)
    return pth
    pass