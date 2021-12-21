import sys

def gcd_fast(a, b): 
    if b == 0: 
        return a 
    a_remainder = a % b 
    return gcd_fast(b, a_remainder)
    
if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd_fast(a, b))