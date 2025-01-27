def pattern(n):
    for i in range(n):
        
        for _ in range(n - i - 1):
            print(" ", end="")
        
        
        num = 1
        for j in range(i + 1):
            print(num, end=" ")
            num = num * (i - j) // (j + 1)
        
        
        print()
        
        



if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n=int(input())
        pattern(n)
        print()