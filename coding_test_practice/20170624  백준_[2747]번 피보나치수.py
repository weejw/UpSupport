def pi(n):
    x, y = 0, 1
    for i in range(n):
        x, y = y, x + y
    return x


def main():
    print(pi(int(input())))


main()
