class Timer:

    def __init__(self):
        self.time = 0
    

    def count(self):
        """timer starts timing, time plus 1"""

        self.time += 1

    
    def setTime(self, newtime:int=0):
        """set time to a certain value"""

        self.time = newtime