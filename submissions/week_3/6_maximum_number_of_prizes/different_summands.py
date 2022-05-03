# Uses python3
import sys

def optimal_summands(n):
    summands = []
    #write your code here        
    if n > 2: 
        prize_value = 1
        while prize_value <= 2: 
            summands.append(prize_value) 
            prize_value += 1
        summands.append(n - prize_value)
    else: 
        summands.append(n)
            
    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
