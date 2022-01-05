from functools import wraps
import time

def execution_time(method_name):
    def actual_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            res = func(*args, **kwargs)
            print(method_name + " took --- %s seconds ---" % (time.time() - start_time))
            return res
        return wrapper
    return actual_decorator

@execution_time(method_name="__test_the_decorater")
def __test_the_decorater():
    time.sleep(2)
    print("__test_the_decorater is executed")