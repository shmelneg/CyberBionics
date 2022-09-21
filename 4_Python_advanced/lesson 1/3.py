def decorator(fn):
    def decorated_fn(*args, **kwargs):
        result = fn(*args, **kwargs)
        return list(filter(lambda x: x % 2 == 0, result))

    return decorated_fn


@decorator
def fibonacci(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    fib_list = [1, 1]
    for _ in range(2, n):
        fib_list.append(fib_list[-1] + fib_list[-2])
    return fib_list

print(fibonacci(20))
