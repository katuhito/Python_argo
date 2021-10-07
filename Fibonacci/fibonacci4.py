#再帰処理を使わずに、ループで求める方法

def fibonacci(n):
    fib = [1, 1]
    for i in range(2, n):
        fib.append(fib[i - 2] + fib[i -1])
    return fib[n -1]

print(fibonacci(30))
