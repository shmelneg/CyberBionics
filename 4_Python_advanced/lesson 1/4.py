print("-=normal multiplication=-")


def normal_mult(a, b=1):
    return a * b


print(normal_mult(5))
print(normal_mult(5, 2))
print("-=curryied multiplication=-")


def curryied_mult(a):

    def do_mult(b):
        return a * b

    return do_mult

print(curryied_mult(5)(2))
double = curryied_mult(2)
print(double(5))
