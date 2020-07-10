def fibonacci(num):
    if num == 0 or num == 1:
        return num
    else:
        return(fibonacci(num-1) + fibonacci(num-2))

values = int(input("Please input a natural number: "))
for i in range(values+1):
    print(fibonacci(i))
