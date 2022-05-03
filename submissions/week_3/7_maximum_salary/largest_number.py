#Uses python3

import sys

def largest_number(digits):
    #write your code here
    answer = ""
    digits.sort() 
    answer_len = 0
    for digit in digits:
        if answer_len == 0: 
            answer += str(digit)
            answer_len += 1
        else: 
            orthodox = int(answer + str(digit))
            unorthodox = int(str(digit) + answer)
            if orthodox >= unorthodox: 
                answer = str(orthodox) 
            else: 
                answer = str(unorthodox)
    return answer

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
