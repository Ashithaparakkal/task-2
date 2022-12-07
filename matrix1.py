#python program to print the required pattern

def printPattern(m,n):      #function to print the required pattern
    
    arr = [[0 for i in range(m)]   #arr[][] will store the pattern matrix
    for j in range(n)]
    p = 1

    #store the values for the upper triangle of the pattern
    for k in range(n):
        j=k
        i=0
        
        while(j >= 0):
            arr[i][j] = p
            p += 1
            i = i+1
            j = j-1
    #store the values for the lower triangle of the pattern
    for k in range(1,n,1):
        i = k
        j = n-1
        f = k
        while(j >= f):
            arr[i][j] = p
            p += 1
            i = i+1
            j = j-1
    #print the pattern
    for i in range(0, m, 1):
        for j in range(0, n, 1):
            print(arr[i][j],end=" ")
        print("\n",end="")
#driver code
if __name__=='__main__':
    m = 3 
    n=3
    
    printPattern(m,n)



#o/p
# 1 2 4 
# 3 5 7 
# 6 8 9

            

 
