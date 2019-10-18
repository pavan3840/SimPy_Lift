# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 09:33:04 2019

@author: BA20090925
"""
import simpy
import random
curr = 0
stat = True
tran = False
floors = 10
class Lift(object):
    def liftFloorTrigger(env,Ftrigger):
        global curr,stat,tran,floors
        if Ftrigger>=0 and Ftrigger<=floors:
            if(curr!=Ftrigger):
                '''
                Here we have got that requested floor is not same as current 
                floor of lift. So it will move from that place to requested place.
                '''
                print('Moving from ' + str(curr) + ' to ' + str(Ftrigger))
                tran = True
                stat = False
                curr = Ftrigger
                move_time = Ftrigger*3
                yield env.timeout(move_time)
                '''
                Here, The lift took 3 unit time for 1 floor and reached the floor.
                The door open time is 2 for people to get in and close time is 1 too.
                '''
                print('Reached ' + str(curr) + ' at ' + str(env.now) + ' second.')
                
                #Opening Door
                door_open_time = 2;
                yield env.timeout(door_open_time)
                stat = True
                tran = False
                print('Doors opened at ' + str(env.now) + ' second. 2 units')
                
                #Closing Door
                door_close_time = 1;
                yield env.timeout(door_close_time)
                print('Doors closed at ' + str(env.now) + ' second. 1 unit')
            else:
                '''
                Here, The lift is on the requested floor, so the doors will open and wait
                for a second and close back.
                '''
                print('Reached ' + str(curr) + ' at ' + str(env.now) + ' second.')
                
                #Opening Door
                door_open_time = 2;
                yield env.timeout(door_open_time)
                print('Doors opened at ' + str(env.now) + ' second. 2 units')
                
                #CLosing Door
                door_close_time = 1;
                yield env.timeout(door_close_time)
                print('Doors closed at ' + str(env.now) + ' second. 1 unit')
        else:
            print('Only 10 floors are present')
            
    def liftInsideTrigger(env,Ltrigger):
        global curr,stat,tran,floors
        if Ltrigger>=0 and Ltrigger<=floors:
            if curr!=Ltrigger:
                print ('Moving from' + str(curr))
                tran = True
                stat = False
                curr = Ltrigger
                move_time = Ltrigger*3
                yield env.timeout(move_time)
                print('Reached ' + str(curr) + ' at ' + str(env.now) + ' second.')
                stat = True
                tran = False
            else:
                
                #Opening Door
                door_open_time = 2;
                yield env.timeout(door_open_time)
                print('Doors opened at ' + str(env.now) + ' second. 2 units')
                print('You are on the requested floor')
        else:
            print('Only 10 floors are present')



for i in range(4):
    env = simpy.Environment()
    env.process(Lift.liftFloorTrigger(env,random.randint(0,11)))
    env.run(until=60)
