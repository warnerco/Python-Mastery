#this script turns binary into digits 
#NNW
def bd(n):
    return int(n,2)

if __name__=='__main__':
     #print(bd('01101000'))
     #print(bd('01100101'))
     #print(bd('01100011'))
     bdUser = str(input("Enter Binary Digits (8 only):"))

print(bd(bdUser))

  


