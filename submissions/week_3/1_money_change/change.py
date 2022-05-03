# Uses python3
# Problem:
#   Design and implement a greedy algorithm to find the minimum number of coins needed to change the input value 
#   (an integer) into coins with denominators 1, 5, and 10.  
import sys

def get_change(m):
    #Input: A single integer m, where m is at least greater than or equal to 1.  
    #Output: The minimum number of coins with denominations 1, 5, 10 that changes m.  
    coins = 0 
    while m != 0: 
        if m >= 10: 
            m -= 10
            coins += 1
        elif m >=5 and m < 10: 
            m -= 5 
            coins += 1
        else: 
            m -= 1 
            coins += 1
    return coins

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))


