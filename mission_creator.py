import random

#################Data#################
act_char = ['Raven Test: "x"','Stop "x"','Remove "x"','Rescue "x"','Pursuit "x"','Guard "x"','Destroy "x"','Raven Battle: "x"','Attack "x"','Eliminate "x"','Disrupt "x"','Protect "x"','Capture "x"','Intercept "x"','Assist "x"']

act_org = ['Mop Up "x"','Nullify "x"','Chase "x"','Obstruct "x"','Secure "x"','Help "x"']

act_loc = ['Recon "x"','Detain "x"','Preserve "x"','Regain "x" ','Infiltrate "x"','Search in "x"','Defend "x"','Retake "x"','Observe "x"','Assault "x"','Enter "x"']

objective_list = ["Goku (Mid)", "Shadow the Hedgehog", "Dorothy (Nikke)", "Hustler-1", "Nemo (AC)", "Gohan Calvo", "Rena Hirose"] #Can't be longer than 14 characters!

organization_list = ["Raven's Nest", "Emeraude", "Chrome", "Murakumo Millenium", "PROGTECH", "Neucom", "Liandri", "Twitch Staff", "Global Cortex", "Chemical-Dyne", "Struggle", "UPEO"] #Can't be longer than 14 characters!

requester_list = ["Goku (Mid)", "Vargskelethor", "Miles 'Tails' Prower", "Dorothy (Nikke)", "Hustler-1", "Raven's Nest", "Emeraude", "Chrome", "Murakumo Millenium", "PROGTECH", "Neucom", "Liandri", "Sugar (Nikke)", "Twitch Staff", "Global Cortex", "Chemical-Dyne", "Struggle", "Neromatsu"]

extra_enemies = ["MT", "Stinger", "Nine Ball", "Rapture (Nikke)", "Gun Hunter (Sonic)", "Frieza Soldier", "Saibaman", "R-101"]

locations = ["Montevideo", "Kame House", "Space Colony ARK", "The Ark (Nikke)", "Zam City", "Isaac City"] #Can't be longer than 14 characters!

#################Data#################

#################Reward#################
class Reward: #So far, working!
    
    def __init__(self):
        rand_reward = random.randrange(10000, 50000, 500)
        
        def advanceCalc():
            choice_adv = random.randrange(1, 3, 1)
            if choice_adv == 1:
                advance = 0
                return advance
            elif choice_adv == 2:
                divider = [1, 2, 4, 5]
                percentage = random.choice(divider)
                advance = int(rand_reward // percentage)
                return advance
        
        instance_adv = advanceCalc()
        
        def successCalc():
            choice_su = random.randrange(1, 2)
            if choice_su == 1:
                success = int (rand_reward - instance_adv)
                return success
            else:
                success = rand_reward
                return success
        
        instance_su = successCalc()
            
        self.reward = str(rand_reward)+"C"
        self.advance = str(instance_adv)+" "+"C"
        self.success = str(instance_su)+" "+"C"

    def __str__(self):
        return f"Reward: {self.reward} C\nAdvance: {self.advance} C\nUpon success: {self.success} C"

#################Reward#################

#################Action#################
class Action (Reward): #I need a list of actions, then i have to append this to the Characters.
    def __init__(self):
        super().__init__()
        
        def randomActionChar():
            rand_Act = random.randrange (0,len(act_char))
            chosen_act = act_char[rand_Act]
            objective = random.randrange (0, len(objective_list))
            chosen_obj = objective_list[objective]
            merge = chosen_act.replace("x",chosen_obj)
            requester = random.randrange (0, len(requester_list))
            chosen_req = requester_list[requester]
            location = random.randrange (0, len(locations))
            chosen_loc = locations[location]
            return merge, chosen_act, chosen_obj, chosen_req, chosen_loc
        
        def randomActionOrg():
            rand_Act = random.randrange (0, len(act_org))
            chosen_act_org = act_org[rand_Act]
            organization = random.randrange (0, len(organization_list))
            chosen_org = organization_list[organization]
            merge = chosen_act_org.replace("x",chosen_org)
            requester = random.randrange (0, len(requester_list))
            chosen_req = requester_list[requester]
            location = random.randrange (0, len(locations))
            chosen_loc = locations[location]
            return merge, chosen_act_org, chosen_org, chosen_req, chosen_loc
        
        def randomActionLoc():
            rand_Act = random.randrange (0, len(act_loc))
            chosen_act_loc = act_loc[rand_Act]
            location = random.randrange (0, len(locations))
            chosen_loc = locations[location]
            merge = chosen_act_loc.replace("x",chosen_loc)
            requester = random.randrange (0, len(requester_list))
            chosen_req = requester_list[requester]
            extra_item = random.randrange (0, len(objective_list))
            chosen_item = objective_list[extra_item]
            return merge, chosen_act_loc, chosen_item, chosen_req, chosen_loc 
        
        def randomAction():
            rand_Act = random.randrange (0, 3)
            if rand_Act == 0:
                act_taken = instance_act_char
                return act_taken
            elif rand_Act == 1:
                act_taken = instance_act_org
                return act_taken
            else:
                act_taken = instance_act_loc
                return act_taken
                
    
        instance_act_char = randomActionChar()
        instance_act_org = randomActionOrg()
        instance_act_loc = randomActionLoc()
        instance_rand = randomAction()
        
        self.main_action = instance_rand
        self.main_merge = instance_rand[0]
        self.main_title = instance_rand[1]
        self.main_char = instance_rand[2] ##This also applies to Items for Action Locations
        self.main_req = instance_rand[3]
        self.main_loc = instance_rand[4] 
        
    def __str__(self):
        return f"Objective: {self.main_action}Merged Title: {self.main_merge}Title: {self.main_title}Character: {self.main_char}Requester: {self.main_req}Location: {self.main_loc}"
                
#################Action#################

#################Details#################

class Details (Action): #This is working, now i need to figure out how to execute all at the same time.
    def __init__(self):
        super().__init__()
        
        def extras():
            add_extras = random.randrange(0,3)
            if add_extras == 1:
                extra_enemy = random.randrange (0, len(extra_enemies))
                chosen_ext = extra_enemies[extra_enemy]
                quantity = str(random.randrange(1, 25))
                total_ext = chosen_ext +" "+"x" +" "+quantity
                return f"{total_ext}"
            else:
                return "Unknown"
            
        instance_ext = extras()
        
        self.extra_enemies = instance_ext
        
    def __str__(self):
        super().__str__()
        return f"Objective: {self.main_action}Enemy forces: {self.extra_enemies}"    
    

#################Details#################

#################Mission Brief#################

class Mission (Details):
    def __init__(self):
        super().__init__()
        
        def missionMaker():
            text_definer = self.main_title
            if text_definer == 'Raven Test: "x"':
                brief = f"This is the only test we give to people who want to become a Raven. You must battle against the opponent {self.main_char} and survive. If you survive, you will be considered a Raven. That's all. Good luck."
                condition = f"Win the battle."
                return brief, condition
            elif text_definer == 'Stop "x"':
                brief = f"We have managed to obtain vital information of {self.main_char}. They plan to hide inside the {self.main_loc} sewers and build their headquarters there. We will never let them build their headquarters."
                condition = f"Destroy their HQ."
                return brief, condition
            elif text_definer == 'Remove "x"':
                brief = f"I need help with a job I have taken. It's at an abandoned base in {self.main_loc}. I was supposed to kill {self.main_char} but i couldn't. I'll pay you {self.reward} for this job."
                condition = f"Kill the target."
                return brief, condition
            elif text_definer == 'Rescue "x"':
                brief = f"We lost communications with one of our transport trucks heading for {self.main_loc}. We strongly believe that this was an act of a terrorist group targeting {self.main_char}. Eliminate all attackers."
                condition = f"Rescue the target."
                return brief, condition
            elif text_definer == 'Pursuit "x"':
                brief = f"Just now, {self.main_char}, thought to be part of a terrorists group, appeared in {self.main_loc}. {self.main_char} is cornered in a nearby parking garage. Go to the scene ASAP and take care of them."
                condition = f"Apprehend the target."
                return brief, condition
            elif text_definer == 'Guard "x"':
                brief = f"We have been informed of a plan to attack {self.main_char}. The location {self.main_loc}, has very little cover. Arrive ASAP there. Give highest priority to ensuring their safety."
                condition = f"Protect the target."
                return brief, condition
            elif text_definer == 'Destroy "x"':
                brief = f"Terrible news just came in. {self.main_char} has gotten hold of the giant space cannon! The weapon is certain to seal the fate of the world if it is fired at {self.main_loc} now. Go to space and stop them!"
                condition = f"Eliminate the target."
                return brief, condition
            elif text_definer == 'Raven Battle: "x"':
                brief = f"Come participate in an AC battle that {self.main_req} will be holding over the next few days. This event pits {self.main_char} in an AC-to-AC battle where the winner takes it all."
                condition = f"Beat the Opponent."
                return brief, condition
            elif text_definer == 'Attack "x"':
                brief = f"I've sent out a mission request to {self.main_char}. The request I sent out, was for the removal of MTs attacking the Construction Site in {self.main_loc}. Your objective is to take them out."
                condition = f"Kill the target."
                return brief, condition
            elif text_definer == 'Eliminate "x"':
                brief = f"We've relocated our Chief Scientist, to our Corporate HQ in {self.main_loc}. But the building is now under attack. The ID of the intruder is {self.main_char}. We have no time to waste. Take them out."
                condition = f"Finish the target."
                return brief, condition
            elif text_definer == 'Disrupt "x"':
                brief = f"We would like you to disrupt {self.main_char} military exercises. We have been informed that their organization has been using these exercises to collect data for Project Phantasma. Destroy all opposing forces."
                condition = f"Stop their actions."
                return brief, condition
            elif text_definer == 'Protect "x"':
                brief = f"We have decided to transfer {self.main_char} to an abandoned factory located in the slums of {self.main_loc}. Their intel is valuable, protect them at all costs."
                condition = f"Guard the target."
                return brief, condition
            elif text_definer == 'Capture "x"':
                brief = f"We have been informed that a high ranking official will be visiting {self.main_char}'s weapon test facility in {self.main_loc}. Arrive there and capture them."
                condition = f"Detain the target."
                return brief, condition
            elif text_definer == 'Intercept "x"':
                brief = f"THIS IS AN URGENT MESSAGE. {(self.main_char).upper()} HAS DISCOVERED THE LOCATION OF OUR BASE IN {(self.main_loc).upper()}. THEY WILL BE ARRIVING QUICKLY. YOU MUST ASSIST US."
                condition = f"Halt their actions."
                return brief, condition
            elif text_definer == 'Assist "x"':
                brief = f"We're requesting you to assist {self.main_char}'s transportation team. They are now moving from the {self.main_loc} to our HQ, but they have come under attack. Help them reach their destination."
                condition = f"Team arrives safely."
                return brief, condition
            elif text_definer == 'Mop Up "x"':
                brief = f"We have heard a rumor that a former {self.main_char} military facility in {self.main_loc} has recently been visited by an unknown group. Eliminate them ASAP."
                condition = f"Destroy the group."
                return brief, condition
            elif text_definer == 'Nullify "x"':
                brief = f"The group {self.main_char} broke into our property at {self.main_loc}, stole several tanks and fled. Since they stole tanks, we cannot leave them be. Go and defeat them as soon as possible."
                condition = f"Erase the thieves."
                return brief, condition
            elif text_definer == 'Chase "x"':
                brief = f"A sample of a new material was stolen from one of our labs in {self.main_loc}. Please track down {self.main_char} and eliminate them. There's no need to recover the sample. Good luck."
                condition = f"Eliminate all targets."
                return brief, condition
            elif text_definer == 'Obstruct "x"':
                brief = f"We want you to disrupt {self.main_char}'s Project Phantasma related shipping lines in the zone of {self.main_loc}.The targets are the {self.main_char}'s transport vehicles. Good Luck."
                condition = f"Capture the vehicles."
                return brief, condition
            elif text_definer == 'Secure "x"':
                brief = f"The enemy forces have launched a full assault on {self.main_char}'s main intelligence hub in {self.main_loc}. You must defend the facility at all costs."
                condition = f"Stop the invation."
                return brief, condition
            elif text_definer == 'Help "x"':
                brief = f"An emergency situation has come up. We'll be sending a mission request directly. The {self.main_char} Marine Laboratory is under attack. We've already sent in another Raven, but he was unable to complete the mission."
                condition = f"Repel the assault."
                return brief, condition
            elif text_definer == 'Recon "x"':
                brief = f"Our intelligence has determined that {self.main_char} has an underground factory in the snowy region of {self.main_loc}.Your mission is to find the point of entry and destroy the door lock system."
                condition = f"Find the entry point."
                return brief, condition
            elif text_definer == 'Detain "x"':
                brief = f"We have decided to carry out an operation intended to occupy {self.main_char}'s base of activities in {self.main_loc}. Our First Division has already begun fighting. Your mission is to support the our troops."
                condition = f"Assault the base."
                return brief, condition
            elif text_definer =='Preserve "x"':
                brief = f"We want you to guard a new type of radar for ACs that we have developed. A prototype model is new stored in a warehouse at {self.main_loc}. There is a good chance that {self.main_char} agents sabotaged the system."
                condition = f"Protect the AC part."
                return brief, condition
            elif text_definer == 'Regain "x" ':
                brief = f"We just got a terrifying message from {self.main_char}. They said that they are occupying {self.main_loc}'s base. Their demands are for the immediate dismantling of {self.main_req}. Eliminate them quickly."
                condition = f"Remove the invaders."
                return brief, condition
            elif text_definer == 'Infiltrate "x"':
                brief = f"Raid the base in {self.main_loc}. In order to bypass the security, simply destroy the four energy generators located outside. Good luck."
                condition = f"Assault the base."
                return brief, condition
            elif text_definer == 'Search in "x"':
                brief = f"Information has been gathered on the whereabouts of Project Phantasma. It can be located in the subway area of {self.main_loc}. I assume {self.main_char} is planning on finding it before us, so be quick."
                condition = f"Find the intel first."
                return brief, condition
            elif text_definer == 'Defend "x"': 
                brief = f"An emergency situation has arisen in our Laboratory at the center of {self.main_loc} is under attack by unknown forces. The invaders have divided and are attacking via different routes."
                condition = f"Protect the lab."
                return brief, condition
            elif text_definer == 'Retake "x"':
                brief = f"Raven, we'd like your assistance in reestablishing {self.main_req}'s control over sector {self.main_loc}. You'll accompany a contingent of our tanks and work with them to eliminate any {self.main_char} forces."
                condition = f"Reclaim the sector."
                return brief, condition
            elif text_definer == 'Observe "x"':
                brief = f"We now know how to take control of {self.main_char} massive weapon. But before we even consider doing so, a thorough search of {self.main_loc} must be conducted. We're sending you in to fulfill this objective."
                condition = f"Recon the location."
                return brief, condition
            elif text_definer == 'Assault "x"':
                brief = f"Preparations are underway for a full-scale assault on {self.main_loc}'s data center. You must destroy the generators that power the security system and eliminate all {self.main_char} patrols you find."
                condition = f"Invade the data center."
                return brief, condition
            elif text_definer == 'Enter "x"':
                brief = f"The {self.main_loc} Waste-Treatment Plant has been commandeered by {self.main_char} group of armed terrorists. Remove the forces occupying the facility."
                condition = f"Repulse the intruders."
                return brief, condition
            else:
                return "Oops, we couldn't generate a mission briefing. Sorry :("
                    
        briefing = missionMaker()
        self.mission_text = briefing[0]
        self.condition = briefing[1]
            
    def __str__(self):
        super().__str__()  
        return f"Objective: {self.main_merge}           Reward: {self.reward}CRequester: {self.main_req}Advance: {self.advance}CUpon success: {self.success}C{self.mission_text}Theatre of Operation: {self.main_loc}Enemy forces: {self.extra_enemies} Condition of Success: {self.condition}"
        #return self.main_merge, self.reward, self.main_req, self.advance, self.success, self.mission_text, self.main_loc, self.extra_enemies
#################Mission Brief#################

#decide what to do with "Condition of Success"

#################Test#################

#test_reward=Reward()
#test_action=Action()
#test_details=Details()
#test_mission=Mission()

#print(test_reward)
#print(test_action)
#print(test_details)
#print(test_mission.main_merge) #Print certain variables
#print(test_mission)
#################Test#################