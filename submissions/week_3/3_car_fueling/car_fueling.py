# python3
import sys
    

def compute_min_refills(distance, mileage, stops): 
    # Inputs
    #   distance: an integer representing the distance between the start and ending positions 
    #   tank: an integer representing the mileage  
    #   stops: an array of gas stations we can re-fuel at along the way from start to end.  
    # Output
    #   The minimum number of stops you'll need to make, or -1 if the journey is impossible  
    # write your code here 
    stops.insert(0,0), stops.append(distance) 
    refills = 0
    position = 0 
    most_recent = position 
    while stops[position] != distance: 
        if stops[position+1] - stops[most_recent] <= mileage:  
            position += 1 
        elif position == most_recent: 
            return -1
        else: 
            refills += 1
            most_recent = position 
    return refills 
    
if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
