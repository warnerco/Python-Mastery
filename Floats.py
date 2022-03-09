#Floats, this program tells you how many 
#integers are in the list in main function
#I want to make a different version so that 
#a similar program can tell you how many numbers are 
#real/int or if they're positive or negative or zero
#from a CSV file #nnw

def count_int(L):
    cn = 0
    for i in L:
        if type(i) is int:
            cn = cn+1
    print("You have", cn, "real numbers")


def main():
    
    L = [2.3,2.4,4.5,5,6,5,6,7,8,7,6,5,4,5.6,7.8,8.9,4.5]
    print(count_int(L))
    
main()

