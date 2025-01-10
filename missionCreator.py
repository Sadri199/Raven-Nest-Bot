import random

#################Data#################
actChar = ['Raven Test: "x"','Stop "x"','Remove "x"','Rescue "x"','Pursuit "x"','Guard "x"','Destroy "x"','Raven Battle: "x"','Attack "x"','Eliminate "x"','Disrupt "x"','Protect "x"','Capture "x"','Intercept "x"','Assist "x"']
actOrg = ['Mop Up Org "x"','Stop Org "x"','Pursuit Org "x"','Disrupt Org "x"','Protect Org "x"','Assist Org "x"']
actLoc = ['Recon "x" Base','Capture "x" Base','Guard "x" Base','Retake "x" Base','Infiltrate "x"','Search in "x"','Defend "x" Base','Recapture "x" Base','Observe "x" Base','Assault "x" Base','Enter "x"']

objectiveList = ["Goku (Mid)", "Shadow the Hedgehog","Dorothy (Nikke)", "Hustler-1", "Nemo (AC)", "Gohan Calvo", "Rena Hirose"] #Can't be longer than 14 characters!
organizationList = ["Raven's Nest", "Akatsuki", "Chrome", "Murakumo Millenium", "PROGTECH", "Neucom", "Liandri", "Twitch Staff", "Global Cortex", "Chemical-Dyne", "Struggle", "UPEO"] #Can't be longer than 14 characters!

requestersList = ["Goku", "Obama", "Miles 'Tails' Prower", "Dorothy (Nikke)", "Hustler-1","Raven's Nest", "Akatsuki", "Chrome", "Murakumo Millenium", "PROGTECH", "Neucom", "Liandri", "Sugar (Nikke)", "Twitch Staff", "Global Cortex", "Chemical-Dyne", "Struggle"]
extra_enemies = ["MT", "Stinger", "Nine Ball", "Rapture (Nikke)", "Gun Hunter (Sonic)", "Frieza Soldier", "Saibaman", "R-101"]

locations = ["Montevideo", "Kame House", "Space Colony ARK (Sonic)", "The Ark (Nikke)", "Zam City", "Isaac City"] #Can't be longer than 14 characters!

#################Data#################

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
                percentage = random.randrange (1, 11, 1)
                advance = int(randReward / percentage)
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
            
        self.reward = str(randReward)+"C"
        self.advance = str(instanceAd)+"C"
        self.success = str(instanceSu)+"C"

    def __str__(self):
        return f"Reward: {self.reward} C \nAdvance: {self.advance} C\nUpon success: {self.success} C"

#################Reward#################

#################Action#################
class Action (Reward): #I need a list of actions, then i have to append this to the Characters.
    def __init__(self):
        super().__init__()
        
        def randomActionChar():
            randAct = random.randrange (0,len(actChar))
            chosenAct = actChar[randAct]
            objective = random.randrange (0, len(objectiveList))
            chosenObj = objectiveList[objective]
            merge = chosenAct.replace("x",chosenObj)
            requester = random.randrange (0, len(requestersList))
            chosenReq = requestersList[requester]
            location = random.randrange (0, len(locations))
            chosenLoc = locations[location]
            return merge, chosenAct, chosenObj, chosenReq, chosenLoc
        
        def randomActionOrg():
            randAct = random.randrange (0, len(actOrg))
            chosenActOrg = actOrg[randAct]
            organization = random.randrange (0, len(organizationList))
            chosenOrg = organizationList[organization]
            merge = chosenActOrg.replace("x",chosenOrg)
            requester = random.randrange (0, len(requestersList))
            chosenReq = requestersList[requester]
            location = random.randrange (0, len(locations))
            chosenLoc = locations[location]
            return merge, chosenActOrg, chosenOrg, chosenReq, chosenLoc
        
        def randomActionLoc():
            randAct = random.randrange (0, len(actLoc))
            chosenActLoc = actLoc[randAct]
            location = random.randrange (0, len(locations))
            chosenLoc = locations[location]
            merge = chosenActLoc.replace("x",chosenLoc)
            requester = random.randrange (0, len(requestersList))
            chosenReq = requestersList[requester]
            extraItem = random.randrange (0, len(objectiveList))
            chosenItem = objectiveList[extraItem]
            return merge, chosenActLoc, chosenItem, chosenReq, chosenLoc 
        
        def randomAction():
            randAct = random.randrange (0, 3)
            if randAct == 0:
                actTaken = instanceActChar
                return actTaken
            elif randAct == 1:
                actTaken = instanceActOrg
                return actTaken
            else:
                actTaken = instanceActLoc
                return actTaken
                
    
        instanceActChar = randomActionChar()
        instanceActOrg = randomActionOrg()
        instanceActLoc = randomActionLoc()
        instanceRand = randomAction()
        
        self.mainAction = instanceRand
        self.mainMerge = instanceRand[0]
        self.mainTitle = instanceRand[1]
        self.mainChar = instanceRand[2] ##This also applies to Items for Action Locations
        self.mainReq = instanceRand[3]
        self.mainLoc = instanceRand[4] 
        
    def __str__(self):
        return f"Objective: {self.mainAction}\nMerged Title: {self.mainMerge}\nTitle: {self.mainTitle}\nCharacter: {self.mainChar}\nRequester: {self.mainReq}\nLocation: {self.mainLoc}"
                
#################Action#################

#################Details#################

class Details (Action): #This is working, now i need to figure out how to execute all at the same time.
    def __init__(self):
        super().__init__()
        
        def extras():
            addExtras = random.randrange(0,3)
            if addExtras == 1:
                extra_enemy = random.randrange (0, len(extra_enemies))
                chosenExt = extra_enemies[extra_enemy]
                quantity = str(random.randrange(1, 25))
                totalExt = chosenExt +" "+"x" +" "+quantity
                return f"{totalExt}"
            else:
                return "Unknown"
            
        instanceExt = extras()
        
        self.extra_enemies = instanceExt
        
    def __str__(self):
        super().__str__()
        return f"Objective: {self.mainAction}\nEnemy forces: {self.extra_enemies}"    
    

#################Details#################

#################Mission Brief#################

class Mission (Details):
    def __init__(self):
        super().__init__()
        
        def missionMaker ():
            textDefiner = self.mainTitle
            if textDefiner == 'Raven Test: "x"':
                brief = f"This is the only test we give to people who want to become a Raven. You must battle against the opponent {self.mainChar} and survive. If you survive, you will be considered a Raven. That's all. Good luck."
                return brief
            elif textDefiner == 'Stop "x"':
                brief = f"We have managed to obtain vital information on the terrorist {self.mainChar}. The scum plan to hide inside the {self.mainLoc} sewers and build their headquarters there. {self.mainChar} has perpetrated many terrorist acts on {self.mainLoc} in the past, and the {self.mainReq} has suffered bitter defeats. We will never let them build their headquarters."
                return brief
            elif textDefiner == 'Remove "x"':
                brief = f"Someone said you can help me out with a job I have taken.\nYou see, it's at an abandoned base in {self.mainLoc}. I was supposed to rid of {self.mainChar} but i couldn't. It was an easy job they say, but {self.mainChar} is weird.\nI'll pay you {self.reward} for this job. Can't tell you who I'm really working for. Look, I'm giving you all I should have been paid."
                return brief
            elif textDefiner == 'Rescue "x"':
                brief = f"We lost communications with one of our transport trucks heading for {self.mainLoc}.\nWe strongly believe that this was an act of a terrorist group targeting {self.mainChar}.\nGo to the site ASAP and search for {self.mainChar}.\nEliminate anyone who interferes.\nThe safety of the vehicle is of utmost priority. Do not forget this."
                return brief
            elif textDefiner == 'Pursuit "x"':
                brief = f"Just now, {self.mainChar}, thought to be part of a terrorists group, appeared in {self.mainLoc}. Indiscriminately, the group attacked the surrounding buildings and fled.\nGuards rushing to the scene cornered {self.mainChar} in a nearby parking garage, but the garage has only one large entrance, so it is not easy to get him.\nThe rest of the gang is still fleeting and we cannot spare any more men. Go to the scene ASAP and cooperate in destroying {self.mainChar}."
                return brief
            elif textDefiner == 'Guard "x"':
                brief = f"We have an emergency! We have been informed of a plan to attack {self.mainChar}.\nWe are unsure of the enemy's exact motives, but it is likely that they are after some intel {self.mainChar} have.\nThe location {self.mainLoc}, has very little cover. We feel that this would be an opportune location for the enemy to attack.\nArrive ASAP there. Give highest priority to ensuring the safety of {self.mainChar}."
                return brief
            elif textDefiner == 'Destroy "x"':
                brief = f"Terrible news just came in. {self.mainChar} has gotten hold of the most horrible fruit of mankind's madness still in space.The giant space cannon is now under the control of {self.mainChar}.\nThe weapon which drove all of humanity underground at the time of the Great Destruction, is certain to seal the fate of the world if it is fired at {self.mainLoc} now.\nThis is no longer between {self.mainReq} and {self.mainChar}.\nThe weapon's only weakness is the enormous amount of time and energy it takes to charge up. We may still be in time.\nThe best space shuttle is ready and waiting. Go into space ASAP, we are counting on you."
                return brief
            elif textDefiner == 'Raven Battle: "x"':
                brief = f"Come participate in an AC battle that {self.mainReq} will be holding over the next few days. This invitational event pits {self.mainChar} in an AC-to-AC battle where the winner takes it all.\nNaturally, there are benefits to entering. The winner of this battle will be presented with the prize of {self.reward} which is the equivalent to the pay of a special mission."
                return brief
            elif textDefiner == 'Attack "x"':
                brief = f"I've sent out a mission request to all Ravens on the NEST network.\nThe request I sent out, was for the removal of MTs attacking the Construction Site East of {self.mainLoc}. The real objective is for you to crush anyone that takes the bait.\n{self.mainChar}, from the Sub-Arena, has already accepted the mission. MTs are easy targets for Ravens, so they probably won't be ready for you. Take them when they least expects it."
                return brief
            elif textDefiner == 'Eliminate "x"':
                brief = f"We've relocated our Chief Scientist, to our Corporate HQ in {self.mainLoc}. Unfortunately our timing couldn't have been worse, as the building is now under attack.\nThe ID of the intruders is {self.mainChar} and all attempts to stop their progress have failed. They're making headway towards our building's core.\nWe have no time to waste. A top-class Raven such as yourself is needed immediately. Take out {self.mainChar}."
                return brief
            elif textDefiner == 'Disrupt "x"':
                brief = f"We would like you to disrupt {self.mainChar} military exercises.\nWe have been informed that their organization has been using these exercises to collect data for an unknown project. Destroy all opposing forces."
                return brief
            elif textDefiner == 'Protect "x"':
                brief = f"We have decided to transfer {self.mainChar} to an abandoned factory located in the slums of {self.mainLoc}.\nA rival organization is also seriously investigating this matter, so we would like you to guard the prisoner on the way to the factory."
                return brief
            elif textDefiner == 'Capture "x"':
                brief = f"We have been informed that a high ranking official will be visiting {self.mainChar}'s weapon test facility in {self.mainLoc}. Run interference and capture them.\nThe weapon testing area is secured with both anti-aerial, radar and anti-tank land mines. Beware of these deterrents - they can prematurely end the mission."
                return brief
            elif textDefiner == 'Intercept "x"':
                brief = f"THIS IS AM URGENT MESSAGE. {(self.mainChar).upper()} HAS DISCOVERED THE LOCATION OR OUR BASE IN {(self.mainLoc).upper()}. THEY WILL BE ARRIVING QUICKLY. YOU MUST ASSIST US. DESTROY ALL REMNANTS OF THEIR FORCES."
                return brief
            elif textDefiner == 'Assist "x"':
                brief = f"We're requesting you to assist {self.mainChar}'s transportation team. They are now moving from the {self.mainLoc} to our HQ, but they have come under attack.\nTheir transportation team is being guarded by our Escort Team, but they are being overwhelmed by the enemy's forces."
                return brief
            elif textDefiner == 'Mop Up Org "x"':
                brief = f"We have heard a rumor that a former {self.mainChar} military facility has recently been visited by an unknown group. The true situation is unclear but we have eye-witness reports of presumed weapons.\nAlthough supposedly already dismantled, the military superiority of {self.mainChar} was awesome in scope. It is not surprising that some may still be loyal to {self.mainChar}."
                return brief
            elif textDefiner == 'Stop Org "x"':
                brief = f"The group {self.mainChar} broke into our property at {self.mainLoc}, stole several tanks and fled. \nSince they stole tanks, we cannot leave them alone. Go and defeat them as soon as possible."
                return brief
            elif textDefiner == 'Pursuit Org "x"':
                brief = f"A sample of a new material we are developing was stolen from one of our labs. Please track down {self.mainChar} and eliminate them.\nThe group that stole the material also took out our security team. The latest reports indicate that they've entered {self.mainLoc} residential district and are poised to attack.\nPlease eliminate the thieves. There's no need to recover the sample. Good luck."
                return brief
            elif textDefiner == 'Disrupt Org "x"':
                brief = f"We want you to disrupt {self.mainChar}'s secret project related shipping lines. Although we do not have many details on this project, we should not ignore it's existence.\nThe targets are the {self.mainChar}'s transport vehicles. Good Luck."
                return brief
            elif textDefiner == 'Protect Org "x"':
                brief = f"The enemy forces have launched a full blown assault on {self.mainChar}'s main intelligence hub. The facility serves as a vital resource pool and archive for our most closely guarded secrets.\nDue to the attack, all facility resources are being relocated until the situation can be brought under control. You must defend the facility at all costs."
                return brief
            elif textDefiner == 'Assist Org "x"':
                brief = f"An emergency situation has come up. We'll be sending a mission request directly. The {self.mainChar} Marine Laboratory is under attack by an unknown MT. The attacker's objective is still unclear.\nWe've already sent in another Raven, but he was unable to complete the mission. The best he could do was stall the enemy's invasion of the facility."
                return brief
            elif textDefiner == 'Recon "x" Base':
                brief = f"Our intelligence has determined that {self.mainChar} has an underground factory in the snowy region of {self.mainLoc}. We plan to send our Special Forces to destroy the factory.\nWe are looking for someone to scout out the entrance to the factory in advance of the attack. Your mission is to find the point of entry and destroy the door lock system."
                return brief
            elif textDefiner == 'Capture "x" Base':
                brief = f"We have decided to carry out an operation intended to occupy {self.mainChar}'s base of activities in {self.mainLoc}.\nLarge amounts of material have been carried and their base is rapidly becoming a fortress. If we leave this as is, it will only become more difficult to act later.\nOur First Division has already begun fighting. Your mission is to support the invasion troops. Bring material to the supply vehicles engaged in combat.\nWe must stop them before it is too late."
                return brief
            elif textDefiner =='Guard "x" Base':
                brief = f"We want you to guard a new type of radar for ACs that we have developed.\nA prototype model is new stored in a warehouse at {self.mainLoc}, but for some reason the security system does not function at all.\nThere is a good chance that someone intentionally sabotaged the system. It is probably the work of {self.mainChar} agents."
                return brief
            elif textDefiner == 'Retake "x" Base':
                brief = f"We just got a terrifying message from {self.mainChar}. They said that they are occupying the air cleaner above {self.mainLoc}.\nThis unit takes air from above-ground, cleans it, and sends it down to the underground city. It is literally the City's lifeline.\nTheir demands are for the immediate dismantling of {self.mainReq} who they say has become the ringleader of social decay. Their false accusations are brash.\nTheir recent activities have been a string of failures thanks to you Ravens. This is a desperate act of desperate people willing to die with honor. Eliminate them quickly."
                return brief
            elif textDefiner == 'Infiltrate "x"':
                brief = f"Raid the base in {self.mainLoc}. It should be easy to pass the entrance, although take note there is a security system.\nIn order to bypass the entrance security, simply destroy the four energy generators located outside.\nThe entrance gate to access the city is secured by a computer. Destroy the underground condensers then go inside.\nOnce we confirm a successful raid, we will provide further instructions. Good luck."
                return brief
            elif textDefiner == 'Search in "x"':
                brief = f"Information has been gathered on the whereabouts of the Secret Project. It can be located in the subway area of {self.mainLoc}.\nI assume {self.mainChar} is planning on seizing the operation as well, so be on the lookout.\nLocate your target immediately and destroy it before {self.mainChar} arrives."
                return brief
            elif textDefiner == 'Defend "x" Base':
                brief = f"An emergency situation has arisen. Our Laboratory at the center of the city is under attack by unknown forces.\nThe invaders have divided into several small groups and are attacking via different routes. We assume their target is {self.mainLoc} Lab.\nThere may be some connection between these units and the ones that attacked out Marine Lab, but we aren't sure."
                return brief
            elif textDefiner == 'Recapture "x" Base':
                brief = f"Raven, we'd like your assistance in reestablishing {self.mainReq}'s control over sector {self.mainLoc}. You'll accompany a contingent of our tanks and work with them to eliminate any {self.mainChar} forces encountered.\n{self.mainChar} is the dominant corporate power in the sector at the moment, but only because they seized control while our attention was focused on other matters."
                return brief
            elif textDefiner == 'Observe "x" Base':
                brief = f"Exhaustive study of the satellite blueprints captured by one of our operatives has finally paid off. We now know how to take control of {self.mainChar} massive weapon.\nBut before we even consider doing so, a thorough hands-on search of the premises in {self.mainLoc} must be conducted.\nWe're sending you in to fulfill this objective. Explore as much of {self.mainLoc} as you can, sixty percent should be sufficient for our needs. Work quickly and exercise with caution."
                return brief
            elif textDefiner == 'Assault "x" Base':
                brief = f"Preparations are underway for a full-scale assault on {self.mainLoc}'s data storage facility.\nThe facility is well guarded against intruders and we expect to encounter heavy resistance in the form of both fixed and mobile security measures.\nOur goal is to neutralize both and safeguard the facility for a follow-up investigation.\nYour object is twofold: Destroy the generators that power the security system, and eliminate all {self.mainChar} patrols you find."
                return brief
            elif textDefiner == 'Enter "x"':
                brief = f"The {self.mainLoc} Waste-Treatment Plant has been commandeered by {self.mainChar} group of armed terrorists.\nThey claim to have taken these steps in an effort to prevent further damage to the environment, but this is just a ruse. Remove the forces occupying the facility."
                return brief
            else:
                return "Oops, we couldn't generate a mission briefing. Sorry :("
        
        briefing = missionMaker()
        self.mission_text = briefing
            
    def __str__(self):
        super().__str__()  
        return f"Objective: {self.mainMerge}           Reward: {self.reward}C\nRequester: {self.mainReq}\nAdvance: {self.advance}C\nUpon success: {self.success}C\n{self.mission_text}\nTheatre of Operation: {self.mainLoc}\nEnemy forces: {self.extra_enemies}"
        #return self.mainMerge, self.reward, self.mainReq, self.advance, self.success, self.mission_text, self.mainLoc, self.extra_enemies
#################Mission Brief#################

#################Test#################

#testReward=Reward()
#testAction=Action()
#testDetails=Details()
testMission=Mission()

#print(testReward)
#print(testAction)
#print(testDetails)
#print(testMission.mainMerge) #Print certain variables
#print(testMission)
#################Test#################