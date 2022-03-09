#this program helps me understand object oriented programming within python  
#nnw
#source: https://www.geeksforgeeks.org/bound-unbound-and-static-methods-in-python/


class sample(object):
    
    ObjectNo = 0
    
    def __init__(self, name1):
        
        self.name = name1 #assigning name1 to self within init function 
        
        sample.ObjectNo = sample.ObjectNo + 1 #calling ObjectNo from class sample and 
        #making the iteration increase by 1 from the initilization of 0 which will then be assigned
        #to the self.ObjNumber below to be able to use ObjectNo within init function since it is 
        #outside of init function but within class sample
        
        self.ObjNumber = sample.ObjectNo #assigning sample.ObjectNo to new self.ObjNumber 
        #as it's unique ID for init function so it can be used within init function like I mentioned in 
        #comment above
        
    def myfunc(self): #this function shows that each time we call this function outside of def functions,
        #it will assign each new object with the next counted iterations to correspond each called object 
        #in the order of iteration that it was called 
        
        print("my name is: ",self.name,"from object: ", self.ObjNumber) #most recent 
        
    def alter(self, newname): #if we run sampl with sampl.alter('B') then this would
        #replace 'A' with 'B' but would not change the iteration, just replace the previous
        #object with new object 'B'
        self.name = newname
        
    #def myfunc2():
        #print("I am a boundless method! Hahaha")
        
samp1 = sample("B") #my new variable in which i call class 'sample' and 
#assign the letter 'A' in the object parameter
#change 'A' to any other object 

samp1.myfunc() #the new variable sampl will call class sample with object paramter A, 
#increase self.ObjNumber to 1, then be called to name1 but then its appended by our self.name = name1 
#in init func then run thru myfunc() #nnw and be called again in self.name and the 1 iteration is called 
#thru self.ObjNumber but won't change if we keep calling sampl and not create sampl2, sampl3, etc...


    