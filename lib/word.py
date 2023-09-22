class Word:
    def __init__(self,wpm,minutes):
        self.wpm = wpm
        self.minutes = minutes 

    def able_to(self):
        return self.wpm * self.minutes
