#Sets up a condition class
class Condition:
    #Sets up the conditions of cannibals and missionaries
    def __init__(self, cannibalStart, missionaryStart, boat, cannibalDest, missionaryDest):
        self.cannibalStart = cannibalStart
        self.missionaryStart = missionaryStart
        self.boat = boat
        self.cannibalDest = cannibalDest
        self.missionaryDest = missionaryDest
    
    #If the game is finished, return tru
    def finish(self):
        if self.cannibalStart ==0 and self.missionaryStart ==0:
            return True
        else:
            False
            
    def validateMove(self):
        if self.missionaryStart > =0 and self.missionaryDest >=0 \
                and self.cannibalStart >=0 and self.cannibalDest >=0\
                and 
    