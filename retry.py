from time import sleep
import math

def Retry(time:int=60):
    '''
        Created by RenatoUb
        GNU GPLv3
        Decorator that receives a function and tries N times 
        according to the maximum time specified in the 'time' variable.
        The time is incremental 1 for each round respecting the maximum 
        time stipulated in the variable time, for this the function 
        calculates the number of rounds(N) based on the inverse of the 
        Gauss sum.
    '''
    # Calculate Delta
    delta = 1-4*-1*time*2
    # Rounds is the unknown that will be used in the sum of gauss
    rounds = (-1+math.sqrt(delta))/2

    def wrapper():
        count = 1
        while True:
            try:
                function()
                break
            except:
                print(f'Sleep {count} second(s)')
                sleep(count)
            if count >= rounds:
                raise Exception(f'The function took longer than the defined time({time} seconds)')
            count += 1 
    
    return wrapper()
