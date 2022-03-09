#this python program is to find the ratio of positive numbers, 
#negative numbers and zeros in the array up to four decimal places
#the raatio would be out of 6 if the array has 6 indices, if the array
#had 8 indices then the ratio would be out of 8 ; ratio = total of indices  

def PosNegZer(arr):
    #initialize count by setting a count parameter 
    
    posnum: 0;
    negnum: 0;
    zeronum: 0;
    
    #traverse the array and coynt the positive, 
    ##negative a zero elements -nnw
    for i in range(length): 
        if (arr[i] > 0 ):
            posnum += 1;
        elif (arr[i] <0):
            negnum += 1;
        elif (arr[i] == 0]):
            zeronum += 1;
            
    #print the raio of positivel negative. and zero elements
            