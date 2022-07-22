from turtle import *
import random
from Points import *

t = Turtle()
t.color("red")
t.speed()

class buildingHouse:
    def drawingHouse(self):
        for i in range(2):
            t.forward(600)
            t.right(90)
            t.forward(500)
            t.right(90)
            
    def drawingWindows(self):
        counter = 0
        pastTL = []
        pastBR = []
            
        while(counter != 50):
            topLeftX = random.randint(0, 601)
            topLeftY = random.randint(-501, 0)
            
            bottomRightX = random.randint(0,601)
            bottomRightY = random.randint(-501, 0)
            
            if(topLeftX > bottomRightX or topLeftY < bottomRightY):
                continue
            
            flag = None
            
            if(20 <= bottomRightX - topLeftX <= 50 and 15 <= topLeftY - bottomRightY <= 40):
                if not(self.checkOverlap(PointT(topLeftX, topLeftY), PointB(bottomRightX, bottomRightY), pastTL, pastBR)):
                    counter += 1
                    flag = True
                    pastTL.append(PointTL(topLeftX, topLeftY))
                    pastBR.append(PointBR(bottomRightX, bottomRightY))
                    
            if(flag == True):
                t.color("green")
                t.penup()
                t.goto(topLeftX, topLeftY)
                t.pendown()
                t.goto(bottomRightX, topLeftY)
                t.goto(bottomRightX, bottomRightY)
                t.goto(topLeftX, bottomRightY)
                t.goto(topLeftX, topLeftY)  
                
    def checkOverlap(self, TL, BR, TLList, BRList):
        isOverlap = False
        for i in range(len(TLList)): 
            isOverlap = True
            if(TL.x > BRList[i].x or BR.x < TLList[i].x):
                isOverlap = False
                
            if(TL.y < BRList[i].y or TLList[i].y < BR.y):
                isOverlap = False
                
            if(isOverlap):
                break
            
        return isOverlap
