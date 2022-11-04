from retry import Retry

@Retry(time=6)
def test():
    # Function that return a simple error
    raise Exception("Generic Error")

test()
