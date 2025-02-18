def rotate(str1,str2):
    rhs=str1;count_rhs=0
    lhs=str1;count_lhs=0
    for i in range(0,len(str1)):
        q=rhs+rhs[0]
        rhs=q[1:]
        count_rhs=count_rhs+1
        if rhs==str2:
            break
        
    for i in range(len(str1)-1,-1,-1):
        q=lhs[len(str1)-1]+lhs
        lhs=q[:-1]
        count_lhs=count_lhs+1
        if lhs==str2:
            break
    return count_rhs,count_lhs
    
    






if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        str1=input()
        str2=input()
        t = rotate(str1,str2)
        
        print("count of the right side rotation is:",t[0])
        print("count of the left side rotation is:",t[1] )
        