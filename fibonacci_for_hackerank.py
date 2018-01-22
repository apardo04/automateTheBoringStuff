cube = lambda x: x**3

def fibonacci(n):
    fib_list = [0, 1]
    for x in range(2, n):
        fib_list.append(fib_list[x-1] + fib_list[x-2])
    return fib_list

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))