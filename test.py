import timeit
import time

def timer(fxn):
    def timed_fxn(self, *arg, **kw):
        start = timeit.default_timer()
        fxn(self, *arg, **kw)
        elapsed = timeit.default_timer() - start
        self.t  = self.t + elapsed
    
    return timed_fxn

class Test():
    def __init__(self):
        self.t = 0

    @timer
    def run(self, n):
        time.sleep(n)
            

if __name__ == '__main__':
    t = Test()

    t.run(5)
    t.run(3)

    print(t.t)
