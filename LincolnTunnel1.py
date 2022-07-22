import math
import random


class Car :
    
    def __init__(self, id, enterTime, speed) :
        self._id = id;
        self._enterTime = enterTime
        self._v = speed
        
        self._x = 0
        self._a = 0
        
        self._moving = False
        
        self._xNew = 0
        self._vNew = 0
        self._aNew = 0
    
    def __str__(self) :
        return 'ID = ' + str(self._id) + '  X = '+ str(self._x) + '  V = ' + str(self._v) + '  A = ' + str(self._a) + '  Start Time = ' + str(self._enterTime)
                                                                                                                            
    
    # getters
    def getID(self) -> int :
        return self._id
    
    def getX(self) -> float :
        return self._x;
    
    def isMoving(self) :
        return self._moving
    
    # main simulation functions
    
    def step(self, curTime, tau) :

        if curTime >= self._enterTime :
            self._moving = True 
            self._vNew = self._v + self._a*tau
            self._xNew = self._x + self._v*tau + self._a*tau*tau/2
        
    def update(self) :
        if self._moving :
            self._a = self._aNew
            self._v = self._vNew
            self._x = self._xNew
        
    # aditional simulation functions TBD
    
    
    
if __name__ == '__main__' :
    
    def isCollision(car, prevCar) :
        carSize = 3
        return prevCar != None and car.isMoving() and prevCar.isMoving() and abs(car.getX()-prevCar.getX()) < carSize
        
        
    # system initialization
    random.seed(10) 
    
    MAX_CAR = 5
    TUNNEL_LEN = 2250
    TAU = 1   # simulation step 1 sec
    
    # create car group
    cars = []
    
    for iCar in range(0, MAX_CAR) :
        nextCar = Car(iCar, iCar*3, 12) # random.randint(12, 20))
        #print(nextCar)
        cars.append(nextCar) # car speed is a random number between 12 and 19 m/sec
                    
    # simulate car group strolling through the tunnel
    
    simTime = 0
    carCollision = False
    
    while True :
        
        print('\n*** time =', simTime)
        
        # car animation sequence
        prevCar = None
        for curCar in cars :
            print(curCar)
            curCar.step(simTime, TAU)
            
            # check traffic conditions
            # 1. Car left tunnel :)
            if curCar.getX() > TUNNEL_LEN :
                cars.remove(curCar)
            # 2. Car collision check  
            if isCollision(curCar, prevCar) :
                carCollision = True
                print('!!! Car collision between', curCar.getID(), prevCar.getID())
                break
            
            prevCar = curCar
            
        if carCollision :
            break;
        if len(cars) == 0 : # all car left tunnel
            break
    
        # car parameters update: current <- new
        for curCar in cars :
            curCar.update()
        
        simTime += TAU    #increment simulation time
        
    print('\n****  Simulation is over  ****')
