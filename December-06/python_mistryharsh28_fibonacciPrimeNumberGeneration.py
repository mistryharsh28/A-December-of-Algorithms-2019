

def fibonacci_prime_numbers(n):

    result = []

    second_prev = 0
    prev = 1
    i = 0
    while(i<n):
        next_fibo = prev + second_prev

        # check if next_fibo is prime
        for j in range(2, next_fibo//2):
            if next_fibo % j == 0:
                break
        else:
            if(next_fibo != 1):
                result.append(next_fibo)
                i = i + 1
        
        second_prev = prev
        prev = next_fibo

    return result

result = fibonacci_prime_numbers(5)
print(result)