def series(n, x):
    sum = 0
    for i in range(1, n * 2, 2):
        sum += (-1) ** (i // 2) * x ** i
    print("sum of series = ", sum)
            







if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n=int(input())
        x=int(input())
        series(n,x)