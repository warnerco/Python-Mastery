#Fibonacci sequence program nnw

def F(n): 
    if n == 1:
        return 1
    if n == 2:
        return 1
    previous = 1
    onebeforeprevious = 1
    for i in range (3,n+1):     
        #range(3,8)=[3,4,5,6,7]  
        #(3,4+1) = [3,4] #i = 3 current = 1+1
        current = previous + onebeforeprevious
        onebeforeprevious = previous
        previous = current
    return current

def main():
    print(F(7))
main()

