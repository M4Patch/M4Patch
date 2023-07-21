import random

chp = int(10)
cxp = int(0)
cac = int(10)
item = int(0)
atkm = int(4)
gold = 0
inv = []

ghp = int(30)
gatk = range(1,10)
gac = int(10)
htpn = 10
ginv = [htpn]

gft = ["The goblin rushes forward and delivers a lunging blow with its club. You stumble back a few feet as it returns to its position.", "It reaches down with an awkwardly large hand and finds a sharp rock on the ground. The goblin whips it towards you with a hunter's precision. You feel a sharp sting and you may be bleeding.", "The goblin sideswipes you with its claws as you try to close distance, you're thrown off balance as it moves further away."]

d20 = list(range(1, 20))

##Items and Flavor Text##

Tome = int(0)
ti = ("You reach into your knapsack and withdraw your tome. It seems to hum with a silent energy as you attach it to your leather belt.")
tec = ("The battle begins. You grab your tome and hold it before you. The hum from before is now exponentially higher as you begin to gather up energy.")
ta = ["With one hand, you gesture at the enemy and hiss out a latin curse. Serpentine energy snakes forth and strikes the enemy in a fiery green lash. Tiny puncture wounds appear on the enemy's skin. They fade overtime.", "Arcane light crackles forth from the book and strikes the enemy with electrifying force. You can see smoke rise from the enemy's ears as it regains its footing.", "With a whisper, the pages of your tome begin to frantically turn as an unseen wind swells. It rushes forth and strikes the enemy, knocking the air out of its lungs.", "Dark energy coils out from your fingertips and slices at the enemy, causing necrotic cuts wherever it strikes.", "Tendrils of fire erupt from the pages of the tome and shoot towards the enemy. For a moment the creature is engulfed in flames and the air reeks of singed hair."]

Staff = int(0)
si = ("You take up your staff. It's a mid-height length of wood, made from a petrified elm. The entirety of it is decorated with carvings of sigils. It glows faintly as you nestle it into a loop on your belt.")
sa = ("You cast shillelagh on your staff as you bring it down onto the enemy. Ethereal green vines sprout out of every rune on the staff and they solidify as you land the blow. The enemy yowls in pain and pushes you back.", "You flourish the staff and a radiant beam of light shoots forth, knocking the enemy onto its back. The enemy lands with a wheeze. As the beam disipates, the enemy regains its footing.", "You whirl the staff over your head twice before swinging it down towards the earth. As you do a whirlwind forms overhead and then crashes into the ground with a thunderous snap. The shockwave crashes into the enemy's chest. You can see blood begin drip from its nose and ears. It shakes its head, dazed." )
sec = ("The battle begins. You take hold of your staff and it begins to glow a crisp blue light. As you swing it into position before you, white lighting crackles gently from the surface of the wood.")

Whip = int(0)
wi = ("You take up your whip and begin to coil the length of it around itself. It is made of a finely braided leather and extends about 15 feet long. As you reach the end, you carefully handle its barbed tail while nimbly securing it to your hip.")
wa = ["You snap the whip low to the ground and successfully snag the ankle of your enemy. With a tug, you're able to yank the creature off balance and they crash to the ground with a howl of pain.", "You twirl the whip above your head, the long leather tail hissing menacingly through the air as you do. With a calculated flick, you unleash the tail and it lashes out at the enemy's hand - forcing the creature to drop its weapon. It scrambles to retrieve the weapon and scurry back a few feet", "You build some momentum and unleash a flurry of strikes. Each one finds its mark on the enemy with a resounding crack. Some of its armor breaks off", "The enemy begins to advance. You draw in your focus and unleash the whip with full momentum. The tail wraps around the enemy's arm and you yank it forward - using its own momentum to send it flying past you. The creature crashes to the earth and it yowls furiously."]
wec = ("The battle begins. You unhook the whip from your side and drop its tail to the ground. The barbed leather lands with a thud.")

Dagger = int(0)
di = ("You can never go wrong with a deft dagger. You give it a few tosses up into the air - its metal catches the sun in dangerous glints along the blade. Its hilt lands in your palm comfortable and you stow it in its sheathe for later.")
da = ["You circle the enemy, waiting for an opening. As it shifts its weapon to attack, you find it. In a blur of motion, you lunge forward and pierce through the enemy's defenses. The enemy howls in pain and jumps back from you", "The enemy advances on you with a determined fury, you sidestep the oncoming attack and catch its arm with the blade. The surprise of pain forces the enemy to drop its weapon. It shoves you away and quickly takes up its weapon again.", "You pull back a few feet and poise your dagger to throw. As soon as the enemy shifts in line with your aim, you flick the dagger at it and begin to charge forward. The blade lands hilt deep. Before the enemy has time to react, you tackle it and retrieve your blade then roll back to take distance"]
dec = ("The battle begins. You brandish your dagger with a flouri and toss it a few times - determining whether to throw the blade or move in for a strike.")

Sword = int(0)
swi = ("You adjust the sheathed sword along your back - ensuring that the hilt sits high enough above your shoulder for you to reach. It has a familiar weight and you feel more sure footed because of it. There's no need to show off such a fine sword without enemies around to strike down. ")
swa = ["With a resolute stride, you close the distance between you and the enemy, eyes locked on your target. In a powerful sweeping arc, you unleash a devestating strike. The enemy staggers back, stunned.", "You raise the blade high above your head as the enemy advances on you. As it comes within distance, you strike down at an angle and collide with its armor. The creature flies off balance with a cry of fury.", "You draw the blade in an uppercut and catch the enemy across the torso, some of its armor falls away and you see a streak of blood alond your blade.", "You plunge forward, blade first, and slam the blade into your enemy. It reels backward with the momentum of your attack and yowls in pain as you drive the blade against it." ]
swec = ("The battle begins. You draw your sword from its sheathe, the metal rings as you do. Taking up a defensive stance, you eye the enemy and search for its weakest points.")

Health_Potion = int(0)
hpi = ("You draw out a medium sized flask of golden liquid. It shimmers in the light, it looks almost like sun-rays cascading through a canopy. You pop the cork and drink it down. Immediately you feel the aches and pains of battle begin to wane. You feel rejuvinated and ready to fight again.")


##Game Start##
print("Start Game? Yes/No")
prgm = input().lower()



while "yes" in prgm:
    input("Welcome to the goblin encounter test... (When you see '...' press ENTER to continue)")
    print("What is your name, adventurer?")
    cn = input()
    story1 = "Well met {}! Tell me, what is your class? (Wizard, Rogue, Fighter)"
    print(story1.format(cn))
    cc = input().upper()


    if "WIZARD" in cc:
        print("A wizard! The mastery of magic is no small feat.")
        Tome = range(1,12)
        Staff = range(1,8)
        Health_Potion = int(15)
        chp = chp + 10
        cac = cac + 3
        inv.extend(["Tome - d12", "Staff - d8", "Health Potion - 15hp"])
    elif "ROGUE" in cc:
        print("A rogue! Whether daring or devious, you certainly lead an adventurous life.")
        Whip = range(1,12)
        Dagger = range(1,8)
        Health_Potion = int(15)
        chp = chp + 10
        cac = cac + 4
        inv.extend(["Whip - d12", "Dagger - d8", "Health Potion - 15hp"])
    elif "FIGHTER" in cc:
        print("A figher eh? You should visit the inn and talk to Durden.")
        Sword = range(1,12)
        Dagger = range(1,8)
        Health_Potion = int(15)
        chp = chp + 15
        cac = cac + 6
        inv.extend(["Sword - d12", "Dagger - d8", "Health Potion - 15hp"])

    input("...")
    input("Before we begin, here is your Character Sheet...")
    character_sheet = "Name: {} - Class: {} - HP: {} - AC: {} - Inventory: {} - Gold: {}"
    print(character_sheet.format(cn, cc, chp, cac, inv, gold))

    input("...")
    
    print("Would you like to visit the shop before we begin? (yes/no)")
    shopchoice = input().lower()
    
    while "yes" in shopchoice:
        print("Welcome to the shop!")
        hptn = 15
        greatsword = range(5,15)
        grtswd = 20
        
        print("Shop again?")
        shopchoice = input().lower()
    

    print("Which weapon will you equip as your main weapon? (You will not be able to swap weapons later...cause I don't know how to do that yet...)")
    cmw = input().lower()

    if "tome" in cmw:
        print(ti)
        atktxt = ta
        eatck = tec
        cmw = Tome
    elif "staff" in cmw:
        print(si)
        atktxt = sa
        eatck = sec
        cmw = Staff
    elif "whip" in cmw:
        print(wi)
        atktxt = wa
        eatck = wec
        cmw = Whip
    elif "dagger" in cmw:
        print(di)
        atktxt = da
        eatck = dec
        cmw = Dagger
    elif "sword" in cmw:
        print(swi)
        atktxt = swa
        eatck = swec
        cmw = Sword

    input("...")

    input("Let's fight some goblins!...")

    input("...")

    input("Alone amidst the ancient trees of a sprawling forest, you cautiously make your way through the dappled shadows...")
    input("A rustling in the underbrush ahead betrays the presence of an unseen foe...")
    input("Suddenly, a small figure darts out from behind a gnarled tree - a goblin, with wild eyes and a wicked grin...")
    input("It brandishes its crude weapon and howls out a battle cry, its intentions are clear and you steel yourself for battle...")

    input("...")

    input("Quick combat test. The encounter is over when one of you reachs 0 HP...")


    cchp = "Hero: {} - HP: {}"
    print(cchp.format(cn, chp))
    gchp = "Enemy: Goblin - HP: {}"
    print(gchp.format(ghp))
    input()

    print(eatck)

    input("The goblin lunges at you first...")

    while ghp > 0 and chp > 0:

        attack = random.choice(d20) + 2
        if attack == 20:
            atkmulti = 2
            print("Critical Hit!")
        else:
            atkmulti = 1

        print(attack)

        if attack >= cac:
            damage = random.choice(gatk) * atkmulti
            print(random.choice(gft))
            atk = "You take {} damage"
            print(atk.format(damage))
            chp = chp - damage
        
        else:
            print("The goblin misses")

        input("Roll to attack!...")

        cattack = random.choice(d20) + atkm
        if cattack == 20:
            atkmulti = 2
            print("Critical Hit!")
        else:
            atkmulti = 1

        print(cattack)

        if cattack >= gac:
            print(random.choice(atktxt))
            damage = random.choice(cmw) * atkmulti
            atk = "You deal {} damage"
            print(atk.format(damage))
            ghp = ghp - damage
            
        else: 
            print("You miss!")

        input("End of Attack Phase...")    

        if chp > 0 and ghp > 0:

            if attack >= cac:
              
                if "Health Potion - 15hp" in inv:
                  print("Would you like to heal (yes/no)")
                  opt = input().lower()
  
                  if "yes" in opt:      
                      print(hpi)
                      chp = chp + Health_Potion
                      inv.remove("Health Potion - 15hp")
                    
  
            
            if ghp < 15:
                if htpn in ginv:
                    ghp = ghp + htpn
                    ginv.remove(htpn)
                    print("The goblin pulls a health potion from a pouch hanging around its neck. It wastes no time trying to open it and instead shoves the bottle between sharp teeth then chews it down - glass and all. The goblin heals for 10.")
            
   
            if attack > cac or cattack > gac:
                print(cchp.format(cn, chp))
                print(gchp.format(ghp))

            input("Begin Next Round...")

    inv = []
    
    if chp > 0:
        print("Congratulations! You defeated the goblin!")
        goldran = range(5,25)
        goldgen = random.choice(goldran)
        gold = gold + goldgen
        goldwon = "You won {} gold!"
        print(goldwon.format(gold))
    elif ghp > 0:
        print("You were defeated. Better luck next time.")
        goldloot = range(4,10)
        goldstolen = random.choice(goldloot)
        looted = "The goblin loots your corpse and takes {} gold."
        print(looted.format(goldstolen))
        gold = gold - goldstolen
        


    chp = int(10)
    cxp = int(0)
    cac = int(10)
    item = int(0)
    atkm = int(4)
    inv = [gold]

    ghp = int(30)
    gatk = range(1,10)
    gac = int(10)
    htpn = 10
    ginv = [htpn]
    print("Would you like to play again? Yes/No")
    prgm = input().lower()
        
    
input("Press ENTER to exit program.")




