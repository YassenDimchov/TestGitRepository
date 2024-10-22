def power(number,power):
    sum = 1
    for i in range(power):
        sum *= number
    return sum

print(power(2, 10))