def pattern(n):
    for i in range(n):
        print(" " * (n - i - 1) + "*" * (2 * i + 1))
    
        










if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n=int(input())
        pattern(n)