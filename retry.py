from time import sleep
import math

class MaxRetriesExceededError(Exception):
    pass

def Retry(max_attempts: int = 10):
    '''
        Created by RenatoUb
        GNU GPLv3
        Decorator that receives a function and retries it up to N times, 
        respecting the maximum number of attempts specified in the 'max_attempts' variable.
        
        The decorator calculates the number of rounds (N) based on the Gauss sum formula.

        Args:
            max_attempts (int): The maximum number of retry attempts.

        Returns:
            function: A decorated function that will be retried up to 'max_attempts' times.

        Raises:
            MaxRetriesExceededError: Raised when the maximum number of retries is exceeded.

    '''
    def decorator(function):
        # Calculate Delta
        delta = 1 - 4 * -1 * max_attempts * 2
        # Rounds is the unknown that will be used in the sum of gauss
        rounds = (-1 + math.sqrt(delta)) / 2

        def wrapper(*args, **kwargs):
            count = 1
            last_exception = None  # Inicialize last_exception como None
            while count <= rounds:
                try:
                    print(f'Retry {count} in {str(__file__)}')
                    func_response = function(*args, **kwargs)
                    break
                except Exception as e:
                    last_exception = e  # Capture a exceção aqui
                    sleep(count)
                    count += 1
                    func_response = None
            else:
                raise MaxRetriesExceededError(f"Maximum number of retries exceeded.\nLast exception: {str(last_exception)}")
            return func_response

        return wrapper

    return decorator
