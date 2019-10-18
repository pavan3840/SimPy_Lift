# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 09:33:04 2019

@author: iAmGamrr
"""
import simpy
import random

curr = 0
curr2 = 0
stat1 = True
stat2 = True
tran1 = False
tran2 = False
floors = 10

class Lift_Simulation(object):
    
    def liftFloorTrigger(env,Ftrigger):
        print('Floor Call')
        global curr,curr2,stat1,tran1,floors,move_time
        
        '''
        This if condition will make sure the given floor is present in the building.
        '''
        if Ftrigger>=0 and Ftrigger<=floors:
            '''
            This if condition will confirm if the lift is present at the same floor
            as the requested floor.
            '''
            if(curr!=Ftrigger):
                '''
                Here we have got that requested floor is not same as current 
                floor of lift. So it will move from that place to requested place.
                '''
                print('Moving from ' + str(curr) + ' to ' + str(Ftrigger))
                tran1 = True
                stat1 = False
                diff = abs(curr-Ftrigger)
                curr = Ftrigger
                move_time = diff*3
                yield env.timeout(move_time)
                '''
                Here, The lift took 3 unit time for 1 floor and reached the floor.
                The door open time is 2 for people to get in and close time is 1 too.
                '''
                print('Reached ' + str(curr) + ' at ' + str(env.now) + ' second. ' + str(diff) + ' floors')
                
                #Opening Door
                door_open_time = 2;
                yield env.timeout(door_open_time)
                stat1 = True
                tran1 = False
                print('Doors opened at ' + str(env.now) + ' second. 2 units')
                
                #Closing Door
                door_close_time = 1;
                yield env.timeout(door_close_time)
                print('Doors closed at ' + str(env.now) + ' second. 1 unit')
                print()
            else:
                '''
                Here, The lift is on the requested floor, so the doors will open and wait
                for a second and close back.
                '''
                print('Reached ' + str(curr) + ' at ' + str(env.now) + ' second. ' + str(move_time) + ' units - same floor')
                
                #Opening Door
                door_open_time = 2;
                yield env.timeout(door_open_time)
                print('Doors opened at ' + str(env.now) + ' second. 2 units')
                
                #CLosing Door
                door_close_time = 1;
                yield env.timeout(door_close_time)
                print('Doors closed at ' + str(env.now) + ' second. 1 unit')
                print()
        else:
            print('Only 10 floors are present')
                
    def liftInsideTrigger(env,Ltrigger):
        print('Lift Call')
        global curr,stat1,tran1,floors,move_time
        if Ltrigger>=0 and Ltrigger<=floors:
            if curr!=Ltrigger:
                print ('Moving from ' + str(curr) + ' to ' + str(Ltrigger))
                tran1 = True
                stat1 = False
                diff = abs(curr-Ltrigger)
                curr = Ltrigger
                move_time = abs(diff)*3
                yield env.timeout(move_time)
                print('Reached ' + str(curr) + ' at ' + str(env.now) + ' second. ' + str(diff) + ' floors')
                stat1 = True
                tran1 = False
                print()
            else:
                #Opening Door
                door_open_time = 2;
                yield env.timeout(door_open_time)
                print('Doors opened at ' + str(env.now) + ' second. 2 units')
                print('You are on the requested floor')
                print()
        else:
            print('Only 10 floors are present')

for i in range(2):
    env = simpy.Environment()    
    env.process(Lift_Simulation.liftFloorTrigger(env,random.randint(0,10)))
    env.run()
    env.process(Lift_Simulation.liftInsideTrigger(env,random.randint(0,10)))
    env.run()
