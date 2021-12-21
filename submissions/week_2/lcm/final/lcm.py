import sys

def gcd(a, b): 
    if b == 0: 
        return a 
    a_mod = a % b 
    return gcd(b, a_mod) 
    
def lcm_fast(a, b): 
    return int((a * b) / gcd(a, b))

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_fast(a, b))