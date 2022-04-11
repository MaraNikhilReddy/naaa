import math
from queue import PriorityQueue
# import PriorityQueue;

def inits(start):
    x=PriorityQueue()
    x.put(start,0)
    y={start:0}
    z={start:None}
    # print("init done and returning")
    return (x,y,z)

def Distance_btw_pionts(p1,p2):
    x=(p1[0]-p2[0])**2
    y=(p1[1]-p2[1])**2
    d=math.sqrt(x+y)
    return d


def shortest_path(input_graph,start,target):

    # print("param=",input_graph,start,target)
    prior_path_queue,cur_dist,past=inits(start)

    while prior_path_queue:
        # if(prior_path_queue.empty()):
        #     break
        temp=prior_path_queue.get()
        if(temp==target):
            # print("temp = target calling fun path")
            function_path(past,start,target)
        for i in input_graph.roads[temp]:
            a=input_graph.intersections[temp]
            b=input_graph.intersections[i]
            new_dist=cur_dist[temp]+Distance_btw_pionts(a,b)
            # print("new dist=",new_dist)

            if(i not in cur_dist or new_dist<cur_dist[i]):
                cur_dist[i]=new_dist
                a=input_graph.intersections[temp]
                b=input_graph.intersections[i]
                sum_dist=new_dist+Distance_btw_pionts(a,b)
                prior_path_queue.put(i,sum_dist)
                past[i]=temp
                
    return function_path(past,start,target)




def function_path(past,start,target):
    path=[target]

    while(target!=start):
        target=past[target]
        path.append(target)
    path.reverse()
    return path
