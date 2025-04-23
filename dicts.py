import random

char_dict = {
    "Goku (Mid)": ["img/chars/goku_mid.png","img/chars/alt/goku_mid_2.png"],
    "Shadow the Hedgehog": "img/chars/shadow_the_hedgehog.png",
    "Dorothy (Nikke)": "img/chars/dorothy.png",
    "Hustler-1": "img/chars/hustler1.png",
    "Nemo (AC)": "img/chars/nemo.png",
    "Gohan Calvo": "img/chars/gohan_calvo.png",
    "Rena Hirose (AC)": "img/chars/rena.png",
    "Asterix": "img/chars/asterix.png",
    "Obelix": "img/chars/obelix.png",
    "Leos Klein": "img/chars/leos_klein.png",
    "Stinger": "img/chars/stinger.png",
    "Phoenix (AC)": "img/chars/phoenix.png",
    "Malcolm (UT)": "img/chars/malcolm.png",
    "Abyssal Dision": "img/chars/abyssal.png",
    "Mobius-1": "img/chars/mobius.png",
    "Blaze (AC)": "img/chars/blaze.png",
    "Blaze the Cat": "img/chars/blaze_cat.png",
    "Ezio Auditore": "img/chars/ezio.png",
    "Kapura": "img/chars/kapura.png",
    "Tom Nook": "img/chars/tom_nook.png",
    "SpongeBob": "img/chars/spongebob.png",
    "JC Denton": "img/chars/jc_denton.png",
    "Adam Jensen": "img/chars/adam_jensen.png",
    "Albert Wesker": "img/chars/albert_wesker.png",
    "Colgate": "img/chars/colgate.png",
    "Krolik": "img/chars/krolik.png",
    "Nemesis (GF2)": "img/chars/nemesis_gf2.png",
    "Red Shoes (Nikke)": "img/chars/red_shoes.png",
    "Prof. Hojo": "img/chars/hojo.png",
    "Yoshimitsu": "img/chars/yoshimitsu.png",
    "SHODAN": "img/chars/shodan.png",
}

org_dict = {
    "Raven's Nest": "img/orgs/raven_nest.png",
    "Emeraude": "img/orgs/emeraude.png",
    "Chrome": "img/orgs/chrome.png",
    "Murakumo Millenium": "img/orgs/murakumo.png",
    "PROGTECH": "", #No picture found
    "Neucom": "img/orgs/neucom.png",
    "Liandri": "img/orgs/liandri.png",
    "Twitch Staff": "img/orgs/twitch.png",
    "Global Cortex": "img/orgs/global_cortex.png",
    "Chemical-Dyne": "img/orgs/chemical_dyne.png",
    "Struggle": "img/orgs/struggle.png",
    "UPEO": "img/orgs/upeo.png",
    "General Resource": "img/orgs/general_resource.png",
    "Zio Matrix": "img/orgs/zio.png",
    "Crest": "img/orgs/crest.png",
    "Mirage": "img/orgs/mirage.png",
    "Kisaragi": "img/orgs/kisaragi.png",
    "ISAF": "img/orgs/isaf.png",
}

req_dict = {
    "Vargskelethor": "img/reqs/varg.png",
    "Miles 'Tails' Prower": "img/reqs/tails.png",
    "Sugar (Nikke)": ["img/reqs/sugar.png", "img/reqs/alt/sugar_2.png"],
    "Neromatsu": "", #No picture for now, idk what to put
    "Billy Kid (ZZZ)": "img/reqs/billy_kid.png",
    "Big the Cat": "img/reqs/big.png",
    "Froggy": "img/reqs/froggy.png",
    "Doro": "img/reqs/doro.png",
    "Snoop Dogg": "img/reqs/snoop_dogg.png",
    "Obama": "img/reqs/obama.png",
    "Air Bud": "img/reqs/air_bud.png",
    "Pom-Pom": "img/reqs/pom_pom.png",
    "Anne (Nikke)": "img/reqs/anne_nikke.png",
    "Yuffie Kisaragi": "img/reqs/yuffie.png",
    "Hello Kitty": "img/reqs/hello_kitty.png",
    }

extra_dict = {
    "MT": "img/extra/mt.png",
    "Stinger": "img/extra/stinger.png",
    "Nine Ball": "img/extra/nineball.png",
    "Rapture (Nikke)": "img/extra/rapture.png",
    "Gun Hunter (Sonic)": "img/extra/gun_hunter.png",
    "Frieza Soldier": "img/extra/frieza_soldier.png",
    "Saibaman": "img/extra/saibaman.png",
    "R-101": "img/extra/r_101.png",
    "Su-37": "img/extra/su_37.png",
    "Disorder Unit": "img/extra/disorder.png",
    "Goomba": "img/extra/goomba.png",
    "Chuckya": "img/extra/chuckya.png",
    "Arkbird (AC)": "img/extra/arkbird.png",
}

loc_dict = {
    "Montevideo": "img/locs/montevideo.png",
    "Kame House": "img/locs/kame_house.png",
    "Space Colony ARK": "img/locs/colony_ark.png",
    "The Ark (Nikke)": "img/locs/the_ark.png",
    "Zam City": "img/locs/zam_city.png",
    "Isaac City": "img/locs/isaac_city.png",
    "Usea": "img/locs/usea.png",
    "Megafloat (AC)": "img/locs/megafloat.png",
    "Vilhul Spaceport": "img/locs/vilhul_spaceport.png", 
    "Zio Matrix's HQ": "img/locs/ziomatrix_hq.png", 
    "Murakumo Dome": "img/locs/murakumo_dome.png", 
    "PROGTECH Factory": "img/locs/progtech_factory.png", 
    "Amber Crown": "img/locs/amber_crown.png", 
    "Trene City": "img/locs/trene.png",
    "Arena": "img/locs/arena_pp.png", 
    "Ruglen Lab": "img/locs/ruglen.png",
    "Stonehenge (AC)": "img/locs/stonehenge.png",
    "Megalith (AC)": "img/locs/megalith.png",
    "Facing Worlds": "img/locs/facing.png",
    "Area 51": "img/locs/area_51.png",
    "Chemical Plant": "img/locs/chemical.png",
    "Midgar": "img/locs/midgar.png",
    "Moonlit Wilderness": "img/locs/moonlit.png",
    "Hell, MI": "img/locs/hell_mi.png",
    "Island (AC)": "img/locs/island_ac.png",
    "Astral Express": "img/locs/astral_express.png",
    "The Elmo (GF2)": "img/locs/elmo.png",
}



def imageChooser(picture):
    random_index = random.randrange(0,2)
    if picture in char_dict:
        correct_path = char_dict.get(picture)
        if isinstance(correct_path, list) == True:
           correct_path = char_dict.get(picture)[random_index]
           print(f"Yes, {picture} has a picture!")
           print(correct_path)
           return correct_path
        elif isinstance(correct_path, list) == False:
            correct_path = char_dict.get(picture)
            print(f"Yes, {picture} has a picture!")
            print(correct_path)
            return correct_path
        elif correct_path == "":
            correct_path = "img/unknown.png"    
        print(f"Yes, {picture} has a picture!")
        print(correct_path)
        return correct_path
    elif picture in org_dict:
        correct_path = org_dict.get(picture)
        if correct_path == "":
            correct_path = "img/unknown.png"    
        print(f"Yes, {picture} has a picture!")
        print(correct_path)
        return correct_path
    elif picture in req_dict:
        correct_path = req_dict.get(picture)
        if isinstance(correct_path, list) == True:
           correct_path = req_dict.get(picture)[random_index]
           print(f"Yes, {picture} has a picture!")
           print(correct_path)           
           return correct_path
        elif isinstance(correct_path, list) == False:
            correct_path = req_dict.get(picture)
            print(f"Yes, {picture} has a picture!")
            print(correct_path)
            return correct_path
        elif correct_path == "":
            correct_path = "img/unknown.png"      
        print(f"Yes, {picture} has a picture!")
        print(correct_path)
        return correct_path
    elif picture in extra_dict:
        correct_path = extra_dict.get(picture)
        if correct_path == "":
            correct_path = "img/unknown.png"    
        print(f"Yes, {picture} has a picture!")
        print(correct_path)
        return correct_path
    elif picture in loc_dict:
        correct_path = loc_dict.get(picture)
        if correct_path == "":
            correct_path = "img/unknown.png"    
        print(f"Yes, {picture} has a picture!")
        print(correct_path)
        return correct_path
    else:
        print(f"No, {picture} doesn't have a picture.")
        correct_path = "img/unknown.png"
        print(correct_path)
        return correct_path

#instance = imageChooser("Goku (Mid)")
#instance2 = imageChooser("Sugar (Nikke)")
