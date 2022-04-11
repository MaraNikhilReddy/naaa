import math
from queue import PriorityQueue


def shortest_path(graph, start, goal):
    
    pathQueue = PriorityQueue()
    pathQueue.put(start, 0)
    
    previous = {start: None}
    score = {start: 0}

    while True:
        if(pathQueue.empty()):
            break
        current = pathQueue.get()

        if current == goal:
            constructPath(previous, start, goal)

        for neighbor in graph.roads[current]:
            updateScore = score[current] + heuristicMeasure(graph.intersections[current], graph.intersections[neighbor])
            
            if neighbor not in score or updateScore < score[neighbor]:
                score[neighbor] = updateScore
                totalScore = updateScore + heuristicMeasure(graph.intersections[current], graph.intersections[neighbor])
                pathQueue.put(neighbor, totalScore)
                previous[neighbor] = current

    return constructPath(previous, start, goal)


def heuristicMeasure(start, goal):
    return math.sqrt(((start[0] - goal[0]) ** 2) + ((start[1] - goal[1]) ** 2))

def constructPath(previous, start, goal):
    current = goal
    path = [current]
    while current != start:
        current = previous[current]
        path.append(current)
    path.reverse()
    return path