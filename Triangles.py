#NNW MY VERY OWN program that uses OOP to make a scatter plot of triangular geometric shapes 

import random
import matplotlib.pyplot as plt 


class Dice(object):

    def roll(self):
        r = random.choice([1,2,3,4,5,6])
        return r 

class Sierpinski(Dice):

    
    def __init__(self, L, number_of_iterations, current_pos_x, current_pos_y):
        self.ni = number_of_iterations
        self.cpy = current_pos_y
        self.cpx = current_pos_x
        self.x1 = L[0][0]
        self.y1 = L[0][1]
        self.x2 = L[1][0]
        self.y2 = L[1][1]
        self.x3 = L[2][0]
        self.y3 = L[2][1]
        Dice.__init__(self)
        
    
        
    def generate_data(self): #does not take an argument, use for loops to generate motion in python
        self.X = []
        self.Y = []
   
        for i in range(1, self.ni):
            r = self.roll()
            if r == 1 or r == 2:
                self.cpx = (self.x1 + self.cpx)/2
                self.cpy = (self.y1 + self.cpy)/2
                self.X.append(self.cpx)
                self.Y.append(self.cpy)
                
            elif r == 3 or r == 4:
                self.cpx = (self.x2 + self.cpx)/2
                self.cpy = (self.y2 + self.cpy)/2
                self.X.append(self.cpx)
                self.Y.append(self.cpy)
            
            else:
                self.cpx = (self.x3 + self.cpx)/2
                self.cpy = (self.y3 + self.cpy)/2
                self.X.append(self.cpx)
                self.Y.append(self.cpy)            
        
        

    def plot_data(self):
        plt.scatter(self.X, self.Y)
        plt.xlabel("y values")
        plt.ylabel("x values")
        plt.grid()
        plt.show()



def main():
    #S = Sierpinski([[P1x,P1y],[P2x,P2y],[P3x,P3y]], number_of_iterations, current_pos_x, current_pos_y)
    S = Sierpinski([[0,0],[20,20],[40,0]], 1000, 1, 1)
    S.generate_data()
    S.plot_data()



main()



#use terminal to execute #nnw
