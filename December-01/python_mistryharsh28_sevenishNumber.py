# Sevenish Number is a power of seven or sum of unique powers of 7
# 5th : 1   0   1
#       7^2 7^1 7^0
#       -----------
#       49 + 0 + 1  = 50
# So we find the binary number of n and then use the powers of 7 as shown
# to find the number


def binary_number(n):

    if(n == 0):
        return '0'
    elif(n == 1):
        return '1'
    else: 
        return binary_number(n//2) + str(n%2)
        

def sevenishNumber(n):

    if(isinstance(n, int) and n > 0):

        binary_n = binary_number(n)

        result = 0

        for index, bit in enumerate(binary_n[::-1]): # reverse of binary_n to traverse for left
            result = (7**index) * int(bit) + result

        return result

    else:
        return "n should be a natural number"


result = sevenishNumber(1)
print(result)

result = sevenishNumber(5)
print(result)

result = sevenishNumber(10)
print(result)


