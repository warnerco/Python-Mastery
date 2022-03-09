#ratio function #nnw
#this program is to show ratios of positive, negative,
#and zero numeric data types the ratio is based on
#the length (indicies) of the array object arr


def ratiofunc(arr): #object arr is the array we will traverse thru
    
    length = (len(arr)) #using built-in function len to traverse thru arr
    pos = 0
    neg = 0
    zer = 0

    for i in range(length):
        #this is the for loop that will traverse
        #thru the arrsy and increase the increment when this for loop
        #reads a pos,neg,zer numeric data type and will divide that incrementation
        #for each pos, neg, zer with the total length of the array
        
        if (arr[i] > 0):
            pos += 1
        elif(arr[i] < 0):
            neg += 1
        elif(arr[i] == 0):
            zer += 1
          
    print("Positive ratio:",pos/length, end= ", ")
    print("Negative ratio:",neg/length, end= ", ")
    print("Zero ratio:", zer/length, end= ", ")
    print("...calculations completed...")


"""
i want to make an input function so the user can input int separated by commas but str and int conflict
array = str(input("Enter a list of numbers separated by commas (no decimals allowed): ")).split(",")
print(ratiofunc(array))
"""

def main():
    array = [-1,-4, -7,-9,-7]
    ratiofunc(array)
    
main()