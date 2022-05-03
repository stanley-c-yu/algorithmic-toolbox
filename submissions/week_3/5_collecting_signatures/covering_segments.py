# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    #write your code here
    segments.sort() # sort segments
    points.append(segments[0][1]) # append the end point of the first segment to the points array. 
    for segment in segments: 
        current_point = points[-1] # the last point we decided was part of the solution 
        if segment[0] >= current_point and segment[0] != current_point: # only consider segments that are not already covered.  
            points.append(segment[1])
        elif segment[0] <= current_point and segment[1] <= current_point: 
            points[-1] = segment[1]
            
    return points


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
