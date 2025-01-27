def prime(n):
    num = 2
    while num <= n:
        
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        
        if is_prime:
            print(num, end=" ")
        
        num += 1
                





if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n=int(input())
        prime(n)