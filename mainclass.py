import random

#################Reward#################
class Reward: #So far, working!
    
    def __init__(self):
        randReward = random.randrange(10000, 50000, 500)
        
        def advanceCalc():
            choiceAd = random.randrange(1, 3, 1)
            if choiceAd == 1:
                advance = 0
                return advance
            elif choiceAd == 2:
                advance = int(randReward / 2)
                return advance
            else:
                advance == randReward
                return advance
        
        instanceAd = advanceCalc()
        
        def successCalc():
            choiceSu = random.randrange(1, 2)
            if choiceSu == 1:
                success = int (randReward - instanceAd)
                return success
            else:
                success = randReward
                return success
        
        instanceSu = successCalc()
            
        self.reward = randReward
        self.advance = instanceAd
        self.success = instanceSu

    def __str__(self):
        return f"Reward: {self.reward} C \nAdvance: {self.advance} C\nUpon success: {self.success} C"

#################Reward#################

#################Action#################
class Action: #I need a list of actions, then i have to append this to the Characters.
    def __init__(self):
        
        actChar = ['Raven Test: "x"','Stop "x"','Remove "x"','Rescue "x"','Pursuit "x"','Guard "x"','Destroy "x"','Raven Battle: "x"','Attack "x"','Eliminate "x"','Disrupt "x"','Protect "x"','Capture "x"','Intercept "x"','Assist "x"']
        actOrg = ['Mop Up Organization "x"','Stop Organization "x"','Pursuit Organization "x"','Disrupt Organization "x"','Protect Organization "x"','Assist Organization "x"']
        actLoc = ['Recon "x" City','Capture "x" City','Guard "x" City','Retake "x" City','Infiltrate "x"','Search in "x"','Defend "x" City','Recapture "x" City','Invade "x" City','Assault "x" City','Enter "x"']

        def randomAction():
            randAct = random.randrange (0, 3)
            if randAct == 0:
                randAct = random.randrange (0,len(actChar))
                chosen = actChar[randAct]
                return f"{chosen}"
            elif randAct == 1:
                randAct = random.randrange (0, len(actOrg))
                chosen = actOrg[randAct]
                return f"{chosen}"
            else:
                randAct = random.randrange (0, len(actLoc))
                chosen = actLoc[randAct]
                return f"{chosen}"
    
        instanceAct = randomAction()
        
        self.mainAction = instanceAct
        
    def __str__(self):
        return f"{self.mainAction}"
                
#################Action#################

#################Character/Location#################

class Details (Action):
    def __init__(self):
        super().__init__()
        objectiveList = ["Goku", "Shadow the Hedgehog","Dorothy (Nikke)", "Nine Ball"]
        requester = ["Goku", "Obama", "Shadow the Hedgehog","Dorothy (Nikke)", "Hustler-1"]
        location = ["Montevideo, Uruguay", "Kame House", "Space Colony ARK (Sonic)", "The Ark (Nikke)", "Zam City (Armored Core)"]
        extra_enemies = ["MT (Armored Core)","Stinger (Armored Core)", "Rapture (Nikke)", "Gun Hunter (Sonic)", "Frieza Soldier"]
        
        def randomObj():
            objective = random.randrange (0, len(objectiveList))
            chosenObj = objectiveList[objective]
            return f"{chosenObj}"        
        
        instanceObje = randomObj()
        
        self.objective = instanceObje
        self.requester = requester
        self.location = location
        self.extra_enemies = extra_enemies
        
    def __str__(self):
        super().__str__()
        return f"{self.objective}"    
    

#################Character/Location#################
    
#################Test#################

a=Reward()
b=Action()
c=Details()

#print(a)
#print(b)
print(c)
#################Test#################