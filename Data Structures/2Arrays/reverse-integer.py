''' Reverse integer, without convert to other data type like string
    Example: 1234 > 4321, 9876 > 6789
'''

def reverseInteger(number):
    reversed_num = 0
  
    while number != 0:
        digit = number % 10
        reversed_num = (reversed_num * 10) + digit
        number //= 10

    return reversed_num
    
if __name__ == "__main__":
    reversed_num = revertInteger(1234)
    print(reversed_num)
