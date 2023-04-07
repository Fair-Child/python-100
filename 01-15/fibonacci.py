def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

num = int(input("Which number in the fibonacci sequence you want to know? "))
print(fibonacci(num))