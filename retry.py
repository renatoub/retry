from time import sleep
import math

def Retry(time:int=10):
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
    def decorator(function):
        # Calculate Delta
        delta = 1-4*-1*time*2
        # Rounds is the unknown that will be used in the sum of gauss
        rounds = (-1+math.sqrt(delta))/2
        def wrapper(*args,**kwargs):
            count=1
            while count<=rounds:
                try:
                    print(f'Retry {count} in {str(__file__)}')
                    func_response = function(*args,**kwargs)
                    break
                except:
                    sleep(count)
                    count+=1
                    func_response=None
            return func_response
        return wrapper
    return decorator
