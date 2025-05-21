def fun(M,N,cost):
    
    for i in range(0,len(cost)):
        for j in range(i+1,len(cost)):
            if i+j == M:
                print(cost.index(i),cost.index(j))
                break
        else:
            print("not found")
    
    
    


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        M = int(input())
        N = int(input())
        cost = []
        for j in range(N):
            k=int(input())
            cost.append(k)
        fun(M,N,cost)