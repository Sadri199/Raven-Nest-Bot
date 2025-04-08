import random

#################Data#################
act_char = ['Raven Test','Stop "x"','Remove "x"','Rescue "x"','Pursuit "x"','Guard "x"','Destroy "x"','Arena Battle!','Attack "x"','Eliminate "x"','Disrupt "x"','Protect "x"','Capture "x"','Intercept "x"','Assist "x"','Spy "x"','Training!','Ridge Racing!','Dance Battle!','Twerk Off','Hear "x"','Conversation Needed','Group Chat!','Fishing Competition!','Cooking Tournament!','Drink Competition','Pool Match','Reading Time','Date "x"','Bakery Time!','"x" is High','Rehab "x"','Deliver Drugs!']

act_org = ['Mop Up "x"','Nullify "x"','Chase "x"','Obstruct "x"','Secure "x"','Help "x"','Survey "x"']

act_loc = ['Recon "x"','Hinder "x"','Preserve "x"','Regain "x" ','Infiltrate "x"','Search "x"','Defend "x"','Retake "x"','Observe "x"','Assault "x"','Enter "x"','Hack Database']

objective_list = ["Goku (Mid)", "Shadow the Hedgehog", "Dorothy (Nikke)", "Hustler-1", "Nemo (AC)", "Gohan Calvo", "Rena Hirose (AC)", "Asterix", "Obelix", "Leos Klein", "Stinger", "Phoenix (AC)", "Malcolm (UT)", "Abyssal Dision", "Mobius-1", "Blaze (AC)", "Blaze the Cat", "Ezio Auditore", "Kapura", "Tom Nook", "SpongeBob", "JC Denton", "Adam Jensen", "Albert Wesker", "Colgate", "Krolik", "Nemesis (GF2)", "Red Shoes (Nikke)", "Prof. Hojo", "Yoshimitsu", "SHODAN"] #Can't be longer than 20 characters!

organization_list = ["Raven's Nest", "Emeraude", "Chrome", "Murakumo Millenium", "PROGTECH", "Neucom", "Liandri", "Twitch Staff", "Global Cortex", "Chemical-Dyne", "Struggle", "UPEO", "General Resource", "Zio Matrix", "Crest", "Mirage", "Kisaragi", "ISAF"] #Can't be longer than 20 characters!

requester_list = ["Vargskelethor", "Miles 'Tails' Prower", "Sugar (Nikke)", "Neromatsu", "Billy Kid (ZZZ)", "Big the Cat", "Froggy", "Doro", "Snoop Dogg", "Obama", "Air Bud", "Pom-Pom", "Anne (Nikke)", "Yuffie Kisaragi", "Hello Kitty"] #Can't be longer than 20 characters!
requester_list.extend(objective_list)
requester_list.extend(organization_list)
#print(requester_list)

extra_enemies = ["MT", "Stinger", "Nine Ball", "Rapture (Nikke)", "Gun Hunter (Sonic)", "Frieza Soldier", "Saibaman", "R-101", "Su-37", "Disorder Unit", "Goomba", "Chuckya", "Arkbird (AC)"]

locations = ["Montevideo", "Kame House", "Space Colony ARK", "The Ark (Nikke)", "Zam City", "Isaac City", "Usea", "Megafloat (AC)", "Vihul Spaceport", "Zio Matrix's HQ", "Murakumo Dome", "PROGTECH Factory", "Amber Crown", "Trene City", "Arena", "Ruglen Lab", "Stonehenge (AC)", "Megalith (AC)", "Facing Worlds", "Area 51", "Chemical Plant", "Midgar", "Moonlit Wilderness", "Hell, MI", "Island (AC)", "Astral Express", "The Elmo (GF2)", ] #Can't be longer than 16 characters!

titles = ["CEO", "President", "Super Saiyan", "Pokemon Trainer", "Nine Breaker", "Stripper", "Paladin", "Fisherman", "Scammer", "Priest", "A Demon of Razgriz"]

songs = ["Rednex - Cotton Eye Joe", "Chocolate - Mayonesa", "Mariya Takeuchi - Plastic Love", "Carlos Gardel - Por Una Cabeza", "daniwell - Nyan Cat", "The Hampsterdance Song", "Michael Sembello - Maniac", "Eilert Pilarm - Jailhouse Rock"]

drinks = ["Beer", "Soda", "Cow Milk", "Pigeon Milk", "Soy Sauce", "Vodka", "Fabuloso", "John's Daphne", "Pepto-Bismol", "Gasoline", "WD-40"]

drugs = ["Cocainum", "Marihuaninum", "Grass", "Gajanma Bajanmaia", "Tobacco", "Benadryl", "Fentanylum", "Laxatives", "Viagra", "Vitamin D"]

addiction = []
addiction.extend(drinks)
addiction.extend(drugs)
#################Data#################

#################Reward#################
class Reward:
    
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
            image = "char"
            return merge, chosen_act, chosen_obj, chosen_req, chosen_loc, image
        
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
            image = "org"
            return merge, chosen_act_org, chosen_org, chosen_req, chosen_loc, image
        
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
            image = "loc"
            return merge, chosen_act_loc, chosen_item, chosen_req, chosen_loc, image 
        
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
        self.main_char = instance_rand[2] 
        self.main_req = instance_rand[3]
        self.main_loc = instance_rand[4]
        self.main_image = instance_rand[5]
        
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
                total_ext = chosen_ext +" "+"x" +quantity
                return f"{total_ext}", chosen_ext
            else:
                chosen_ext = "Unknown"
                return "Unknown", chosen_ext
        
        def otherSelector():
            get_title = random.randrange (0, len(titles))
            chosen_title = titles[get_title]
            
            get_song = random.randrange (0, len(songs))
            chosen_song = songs[get_song]
            
            get_drink = random.randrange (0, len(drinks))
            chosen_drink = drinks[get_drink]
            
            get_drug = random.randrange (0, len(drugs))
            chosen_drug = drugs[get_drug]
            
            get_addict = random.randrange (0, len(addiction))
            chosen_addict = addiction[get_addict]
            
            return chosen_title, chosen_song, chosen_drink, chosen_drug, chosen_addict
          
        instance_ext = extras()
        instance_other = otherSelector()
        
        self.extra_enemies = instance_ext[0]
        self.this_extra = instance_ext[1]
        
        self.title = instance_other[0]
        self.song = instance_other[1]
        self.drink = instance_other[2]
        self.drug = instance_other[3]
        self.addict = instance_other[4]
        
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
            if text_definer == 'Raven Test':
                brief = f"This is the only test we give to people who want to become a Raven. You must battle against {self.main_char} and survive. If you survive, you will be considered a Raven. That's all. Good luck."
                condition = f"Win the battle."
                return brief, condition
            elif text_definer == 'Stop "x"':
                brief = f"We have managed to obtain vital information about {self.main_char}. They plan to hide inside {self.main_loc}'s sewers and build their headquarters there. We will never let them do it."
                condition = f"Destroy their HQ."
                return brief, condition
            elif text_definer == 'Remove "x"':
                brief = f"I need help with a job I have taken. It's at an abandoned base in {self.main_loc}. I was supposed to kill {self.main_char} but i couldn't. I'll pay you {self.reward} for this job."
                condition = f"Kill the target."
                return brief, condition
            elif text_definer == 'Rescue "x"':
                brief = f"We lost communications with one of our transport trucks heading towards {self.main_loc}. We strongly believe that this was an act of a terrorist group targeting {self.main_char}. Eliminate all attackers."
                condition = f"Rescue the target."
                return brief, condition
            elif text_definer == 'Pursuit "x"':
                brief = f"Just now, {self.main_char}, thought to be part of a terrorist group, appeared in {self.main_loc}. They are cornered in a nearby parking garage. Go to the scene ASAP and take care of them."
                condition = f"Apprehend the target."
                return brief, condition
            elif text_definer == 'Guard "x"':
                brief = f"We have been informed of a plan to attack {self.main_char}. They are in {self.main_loc} and it has very little cover. Arrive ASAP there. Give highest priority to ensuring their safety."
                condition = f"Protect the target."
                return brief, condition
            elif text_definer == 'Destroy "x"':
                brief = f'Terrible news just came in. {self.main_char} has gotten hold of the Giant Space Cannon! The weapon is certain to seal the fate of the world if it is fired at {self.main_loc}. Go to Space and stop them!'
                condition = f"Eliminate the target."
                return brief, condition
            elif text_definer == 'Arena Battle!':
                brief = f"Come participate in an AC battle that {self.main_req} will be holding over the next few days. This event pits {self.main_char} in an AC-to-AC battle where the winner takes it all."
                condition = f"Beat the Opponent."
                return brief, condition
            elif text_definer == 'Attack "x"':
                brief = f"I've sent out a mission request to {self.main_char}. The request I sent out, was for the removal of MTs attacking the Construction Site in {self.main_loc}. Your objective is to eliminate {self.main_char}."
                condition = f"Kill the target."
                return brief, condition
            elif text_definer == 'Eliminate "x"':
                brief = f"We've relocated our Chief Scientist to our Corporate HQ in {self.main_loc}, but the building is now under attack. The intruder is {self.main_char}. We have no time to waste. Take them out."
                condition = f"Finish the target."
                return brief, condition
            elif text_definer == 'Disrupt "x"':
                brief = f"We would like you to disrupt the military exercises of {self.main_char}'s forces. We have been informed that their organization has been collecting data for Project Phantasma. Destroy all enemies."
                condition = f"Stop their actions."
                return brief, condition
            elif text_definer == 'Protect "x"':
                brief = f"We have decided to transfer {self.main_char} to an abandoned factory located in the slums of {self.main_loc}. Their intel is valuable, protect them at all costs."
                condition = f"Guard the target."
                return brief, condition
            elif text_definer == 'Capture "x"':
                brief = f"We have been informed that a high ranking official will be visiting {self.main_char}'s facility in {self.main_loc}. Arrive there and capture them."
                condition = f"Detain the target."
                return brief, condition
            elif text_definer == 'Intercept "x"':
                brief = f"THIS IS AN URGENT MESSAGE. {(self.main_char).upper()} HAS DISCOVERED THE LOCATION OF OUR BASE IN {(self.main_loc).upper()}. THEY WILL BE ARRIVING QUICKLY. YOU MUST ASSIST US."
                condition = f"Halt their actions."
                return brief, condition
            elif text_definer == 'Assist "x"':
                brief = f"We're requesting you to assist {self.main_char}'s transportation team. They are now moving from the base in {self.main_loc} to our HQ, but they are under attack. Help them reach their destination."
                condition = f"Team arrives safely."
                return brief, condition
            elif text_definer == 'Spy "x"':
                brief = f"There is some intel regarding {self.main_char} that we need to corroborate.We know they are at a hotel in {self.main_loc} for the next 24 hours. Don't alert them."
                condition = f"Gather useful information."
                return brief, condition
            elif text_definer == 'Training!':
                brief = f"{self.main_char} is training to become {self.title} and I can't help with that. You will be rewarded for your assistance."
                condition = f"Help in their training."
                return brief, condition 
            elif text_definer == 'Ridge Racing!':
                brief = f"A new race will start soon in {self.main_loc} and the current champion is {self.main_char}. I pay you a hefty sum to win this race, if you can't win, at least end in a higher position than {self.main_char}."
                condition = f"Win the race."
                return brief, condition
            elif text_definer == 'Dance Battle!':
                brief = f"{self.main_char} challenges you to a Dance Battle to {self.song} in {self.main_loc} dance hall! Do you accept?"
                condition = f"Move those feets." 
                return brief, condition 
            elif text_definer == 'Twerk Off':
                brief = f'{self.main_char} have been talking bad about you in your back. They say you have "No ass", and that they can "Shake them better than you". You will be rewarded.'
                condition = f"Shake that ass."
                return brief, condition 
            elif text_definer == 'Hear "x"':
                brief = f"I'm concerned about {self.main_char} and their lack of friends. They need someone to vent but i have no time for that because of the current project (excuses). Please give them a call."
                condition = f"Withstand the monologue."
                return brief, condition 
            elif text_definer == 'Conversation Needed':
                brief = f"{self.main_char} is very talkative and I run out of things to talk with them. Go to {self.main_loc} and talk with them, even small talk will help."
                condition = f"Ask them about something."
                return brief, condition 
            elif text_definer == 'Group Chat!':
                brief = f"{self.main_char}'s secret group chat has been discovered. They are planning to bombard the vicinity of {self.main_loc}. Get in there and take screenshots."
                condition = f"This will never happen in real life."
                return brief, condition 
            elif text_definer == 'Fishing Competition!':
                brief = f'I am making a Fishing Competition, because you know my motto: "Woman want me, Fish fear me". It is all about that bass life and no one knows it more than {self.main_char}. Are you ready to bass it up at {self.main_loc}?'
                condition = f"Come here fishy fishy."
                return brief, condition 
            elif text_definer == 'Cooking Tournament!':
                brief = f"{self.main_char} is the current Cooking Champion and they are hosting a tournament. I can't stand this anymore but I can't even cook rice. You will have to do."
                condition = f"Make that spaghetti."
                return brief, condition
            elif text_definer == 'Drink Competition':
                brief = f"{self.main_char} is having a bad day and to cheer them up they are taking shots of {self.drink}. I cannot accompany them but we can't leave a person drinking alone. You should do it, c'mon, I'll even pay you a bit."
                condition = f"Don't drive after drinking."
                return brief, condition
            elif text_definer == 'Pool Match':
                brief = f"{self.main_char} is at a local pub in {self.main_loc} and they are playing Pool. Go there and play, this is a distraction for another plan, keep them busy there."
                condition = f"Hit the balls with the stick."
                return brief, condition
            elif text_definer == 'Reading Time':
                brief = f"{self.main_char} has sleeping problems and they need someone to read them a book. {self.reward} will be enough for you to do it?"
                condition = f"Make them sleep."
                return brief, condition
            elif text_definer == 'Date "x"':
                brief = f"{self.main_char} has social problems and will never get a date. I am feeling worried about this so just, go and do it yourself. Nothing crazy, just have a dinner and talk about the weather or something."
                condition = f"Pretend you like them."
                return brief, condition
            elif text_definer == 'Bakery Time!':
                brief = f"{self.main_char} is making Croissants and they really need help. I'm not good at cooking so please, help them out."
                condition = f"Don't burn the Croissants."
                return brief, condition
            elif text_definer == '"x" is High': 
                brief = f"{self.main_char} is smonking a lot of {self.drug}, they are really high. They are so high. They are challenging you to a drug battle, do you accept to get high?"
                condition = f"Get high???"
                return brief, condition
            elif text_definer == 'Rehab "x"':
                brief = f"{self.main_char} has taken to many {self.addict}, they need help. You accept any type of job right? Help them get detoxified."
                condition = f"Stop their addiction."
                return brief, condition
            elif text_definer == 'Deliver Drugs!':
                brief = f"{self.main_char} and I are in party and need some of that, you know, {self.addict}. Can you help us?"
                condition = f"Deliver that stuff."
                return brief, condition
            elif text_definer == 'Mop Up "x"':
                brief = f"We have heard a rumor that a former {self.main_char}'s facility in {self.main_loc} has recently been visited by an unknown group. Eliminate them ASAP."
                condition = f"Destroy the group."
                return brief, condition
            elif text_definer == 'Nullify "x"':
                brief = f"{self.main_char}'s group broke into our property at {self.main_loc}. They stole several tanks and fled. We cannot leave them be. Go and defeat them as soon as possible."
                condition = f"Take out the thieves."
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
                brief = f"Emergency. We'll are sending a mission request directly. The {self.main_char}'s Marine Laboratory is under attack. We've sent another Raven, but they were unable to complete the mission."
                condition = f"Repel the assault."
                return brief, condition
            elif text_definer == 'Survey "x"':
                brief = f"We have some clues about a secret base of operations in the area of {self.main_loc}. See if you can find it, but be careful, {self.main_char} is patroling nearby."
                condition = f"Collect information."
                return brief, condition
            elif text_definer == 'Recon "x"':
                brief = f"Our intelligence has determined that {self.main_char} has an underground factory in the snowy region of {self.main_loc}.Your mission is to find the point of entry and destroy the door lock system."
                condition = f"Find the entry point."
                return brief, condition
            elif text_definer == 'Hinder "x"':
                brief = f"We have decided to carry out an operation intended to occupy {self.main_char}'s base of activities in {self.main_loc}. Our First Division has already begun fighting. Your mission is to support our troops."
                condition = f"Assault the base."
                return brief, condition
            elif text_definer =='Preserve "x"':
                brief = f"We want you to guard a new type of radar for ACs that we have developed. A prototype model is stored in a warehouse at {self.main_loc}. There is a good chance that {self.main_char} agents sabotaged the system."
                condition = f"Protect the AC part."
                return brief, condition
            elif text_definer == 'Regain "x" ':
                brief = f"We just got a terrifying message from {self.main_char}. They said that they are occupying {self.main_loc}'s base. Their demands are for the immediate dismantling of {self.main_req} base. Eliminate them quickly."
                condition = f"Remove the invaders."
                return brief, condition
            elif text_definer == 'Infiltrate "x"':
                brief = f"Raid the base in {self.main_loc}. In order to bypass the security, you must destroy the four energy generators located outside. Good luck."
                condition = f"Assault the base."
                return brief, condition
            elif text_definer == 'Search "x"':
                brief = f"Information has been gathered on the whereabouts of Project Phantasma. It can be located in the subway area of {self.main_loc}. I assume {self.main_char} is planning on finding it before us, so be quick."
                condition = f"Find the intel first."
                return brief, condition
            elif text_definer == 'Defend "x"': 
                brief = f"An emergency situation has arisen in our Laboratory at the center of {self.main_loc}. It is currently under attack by unknown forces. The invaders have divided and are attacking via different routes."
                condition = f"Protect the lab."
                return brief, condition
            elif text_definer == 'Retake "x"':
                brief = f"Raven, we'd like your assistance in reestablishing {self.main_req}'s control over {self.main_loc}. You'll accompany our tanks and work with them to eliminate {self.main_char}'s forces."
                condition = f"Reclaim the sector."
                return brief, condition
            elif text_definer == 'Observe "x"':
                brief = f"We now know how to take control of {self.main_char}'s massive weapon, but before we even consider doing so, a thorough search of {self.main_loc} must be conducted. We're sending you in to scout the area."
                condition = f"Recon the location."
                return brief, condition
            elif text_definer == 'Assault "x"':
                brief = f"Preparations are underway for a full-scale assault on {self.main_loc}'s data center. You must destroy the generators that power the security system and eliminate all {self.main_char}'s patrols you find."
                condition = f"Invade the data center."
                return brief, condition
            elif text_definer == 'Enter "x"':
                brief = f"The {self.main_loc} Waste-Treatment Plant has been commandeered by {self.main_char}'s group of armed terrorists. Remove the forces occupying the facility."
                condition = f"Repulse the intruders."
                return brief, condition
            elif text_definer == 'Hack Database':
                brief = f"We have found the location to a secret database in {self.main_loc} belonging to {self.main_char}. It can only be breached in person, that's your part in this operation."
                condition = f"Find the Computer Room."
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