from queue import PriorityQueue


def inits(start):
    prior_path_queue=PriorityQueue()
    prior_path_queue.put(start,0)
    cur_dist={start:0}
    past={start:None}
    return (prior_path_queue,cur_dist,past)

x,y,z=inits(5)