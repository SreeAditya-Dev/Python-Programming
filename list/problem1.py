def fun(lst):
    for i in range(1,len(lst)):
        if sum(lst[0:i]) == sum(lst[i+1:]):
            print(sum(lst[0:i]))
            break
    else:
        print(0)
    








if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        lst=eval(input())
        fun(lst)