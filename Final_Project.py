# -*- coding: utf-8 -*-
# As I worked on this code between school and home I had to change between raw_input() and input()
from __future__ import print_function
import random
room = random.randint(1,100) #this is going to act as a percentile role for each room to determine where the player goes
enemies_defeated = 0 #Number of enemies the player has defeated. Will need to fight 5 to get to the boss
hit_points = 30 #total hit points of the character that will be affected when they get hit by the enemy
win_lose_status = "lose" 
werewolf_status = "NOT A WEREWOLF"
restrictions = "null" #added January 27 2018 to make battle restrictions in fights like the mermaid and the snake
user_input = "" #This will regularly be using input to see what the player wants to do 
attack = ["smack","punch", "kick", "stab", "assault", "brutalize", "attack", "verbally abuse", "strike", "bash", "shank", "throw a rock at"] #added on January 19th to give your attack some variety
dodge = ["swoop", "duck", "dodge", "hop", "stumble", "skirt", "sidestep", "shuffle"] #added on January 23nd to give dodging some variety
defeated = ["defeated", "destroyed", "killed", "eaten", "conquered", "crushed", "overcome"]
monster_attack = 1 #added on January 23nd to help switch between monster attacks
damage = 1 #added June 7th - I would like to start incorporating a damge system where you can do more damage with better equipment
modifier = 0 #added June 7th for items
player_damage = damage + modifier
#Instead of giving each creature its own set of variables, each creature has a dictionary with its image, attack, hp, attack messages, and death message. 
piccolo = {"name":" Piccolo","description": "This is the first room! You see seven orange orbs lining the wall that have a different number of pulsing stars on each one. As you enter, an aggressive green being with antenna and foreign clothing approaches you. It throws a rock at you and screams, “DODGE!” I guess now is a better time than any to learn how to dodge. And attack of course.",
"image": """
                       _.-=/^---._
                      /^_.-^  _  --^=_
                   ./'-^__    _>=\^^==^-.   
                   |'/^^_/  /^    \ \.^\/ 
                  ,|/| '  /'  _____\ `\|.^.|
                  |'/   /_--^^ .   ^^-./ /||
                  |/,--^  ,     |     / /||'
                ._|/   \ /  __,-/    / /-,||
                \ '/    ;  /O  / _    |) )|,
                 i \./^O\./_,-^/^    ,;-^,'      
                  \ |`--/ ..-^^      |_-^       
                   `|  \^-_,/^Y\      | ^^\    
                   _i.   ".--V_/     /| \. ^\._____...--.>^^^^^^-------...._
                  /  i   ^--^^     /'|' |\. |./'        |                  ;
___...----/^^^^---|.  `._\  /^   /' |'_/' \ `|         |'               ,/'
         |'        \   _|^-.__./'__.^^\     .|        ,|            _.-^
         `\       ,|`_./^^-----^^._    ` ./ /        /^        _.-^^/
                  |'  ^                  /-^                ./^    /
\                 `\_     __.-<       _,/                 ./'     |'
 `\.        `i       ^^--/._____...--^            .      ./       |.
   `|        |                                   /       /        `|
""",
"atk":1,
"hp":4,
"attack_1": "Piccolo throws a rock at you and screams,'DODGE!'",
"attack_2": "'Good, you're learning.'",
"death": "'Now, go on your quest and win...'",
}
            #added names on January 19th
skeleton = {"name":" the skeleton","description": "You enter a cave-like room and the strong smell of dirt wafts to your nose. It seems spacious enough yet somehow claustrophobic in a way. Bones are spread across the floor and some seem to be gathering. The bones click and clank as they form a single human skeleton that seems to have a bone to pick with you. Its jaw chatters as if laughing at you. Now is time to fight!",
"image": """
    _.--""--._        
   ."          ".     
  | .   `      ` |    
  \(            )/   
   \)__.    _._(/  
   //   >..<   \\  
   |__.' vv '.__/ 
      l'''"''l    
      \_    _/  
 _      )--(     _  
| '--.__)--(_.--' |  
 \ |`----''----'| / 
  ||  `-'  '--' || 
  || `--'  '--' || 
  |l `--'--'--' |l  
 |__|`--'  `--'|__| 
 |  |    )-(   |  | 
  ||     )-(    \|| 
  || __  )_(  __ \\  
  ||'  `-   -'  \ \\ 
  ||\_   `-'   _/ |_\ 
 /_\ _)J-._.-L(   /`-\ 
|`- I_)O /\ O( `--l\\\| 
||||( `-'  `-') .-' ||| 
 \\\ \       / /   /// 
    \ \     / / 
     \ \   / / 
     /  \ /  \ 
     |_()I()._| 
     \   /\   / 
      | /  \ | 
      | |   \ \ 
      | |    \ \ 
      | |     \ \ 
      | |      \ \_ 
      | |      /-._\ 
     |.-.\    //.-._) 
      \\\\   /// 
       \\\\-'''
""",
"atk":1,
"hp":5,
"attack_1": "The skeleton mauls you with a bone. It is humerous.",
"attack_2": "This time it throws you a bone. You take no damage.",
"death": "As you hit it one more time, all of the bones poof into dust. It seems you have won.",
"loot_1": "femur", #Loot added 11 June 2018 in order to change how much damage the player can do
"loot_2": "bone claws"
}

mermaid = {"name":" the mermaid","description": "You enter a beautiful cave lined with glittering ores that have yet to be gathered. Taking up about half of the room is a pool of murky water. There is movement and then a body slowly rises above the water and rests on the shore. At first it looks human, but the bottom half of it looks like a fish of some sort. Unfortunately, it licks its sharp teeth and looks at you hungrily. I guess you need to fight for your flesh.",
"image": """
               .---.
              (_,/\ \ 
             (`- -(  )
             ) \=  ) (
       |\_   (.-' '--.)
        \(   /(_)-(_) \ 
         \ \/ /\   /`\ \ 
          \_/  / . \  //
              /'---'\`/_
           _ / ^   ^ ;--;
        .--`| ^  ^ /`    `),
       /`  . \  ^ /`  ) .   ').
  ~^~`/  (    \^ / (       '  \^-~`-~
 -  ^ ~^-    . )/   .    )  '-.;~^-~^~-
    ~^~-      / `\ - .  ~^~ ,-.`~~^~^~^
  ~- `^_~-~^-| \^ \~_~^ -~^~- ~^`~^ ^~
   ~_~^- .-./__/\__`\-. ~^_-~^- ~^- 
      ^~ `-^~=~-`=~-~=-'    ~
""",
"atk":2,
"hp":3,
"attack_1": "The mermaid bites at your ankles",           #Some creatures have more attacks than others that may have extra affects
"attack_2": "She sits and observes your actions.",
"attack_3": "She sings a song and appears to be a very beautiful maiden that you wouldn't want to hurt.",
"death": "Her song ends and her eyes roll back as she sinks to the bottom of the pool. You succeeded this time."
}

killer_rabbit = {"name":" the killer rabbit","description": "You enter an area that looks like a barnyard. A single, dirty rabbit hops around peacefully. Another rabbit approaches the first one is instantly torn to pieces. Blood stains its fur as the rabbit notices your presence. It stares into your eyes with red, demonic eyes. You must kill the killer or be killed.",
"image": """
            /|      __
           / |   ,-~ /
          Y :|  //  /
          | jj /( .^
          >-"~"-v"
         /       Y
        jo  o    |
       ( ~T~     j
        >._-' _./
       /   "~"  |
      Y     _,  |
     /| ;-"~ _  l
    / l/ ,-"~    |
    \//\/      .- |
     Y        /    Y   
     l       I     !
     ]\      _\    /"|
    (" ~----( ~   Y.  )
~~~~~~~~~~~~~~~~~~~~~~~~~~
""",
"atk":1,
"hp":2,
"attack_1": "The rabbit knaws on your leg.",
"attack_2": "It tries to jump on your face and fails.",
"death": "The rabbit wasn't as tough as you thought. Time to move on.",
"loot_1":"rabbit's foot",
"loot_2":"pitchfork"
}

#Completed on January 12 by 8:40 AM
lesser_dog = {"name":" lesser dog","description": "You enter a puzzling room that looks like it could have been part of a video game with low graphics. A dog wearing armor and standing on two legs is standing around and turns at the sound of footsteps. It looks very friendly and happy. It bark at you with content, but it wields a sword so you must get ready to fight just in case it attacks.",
"image": """
MMMMMMMMMMMMMMMMMMMMMMMMMMMM. MMMMMMMMMM .?MMMMMMMMM..M..MMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMM...MMMMMMMM ..?MMMMMMMMM..M..MMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMM....M ....M ..?MMMMMMMMM..M..MMM
MMMMMMMMMMMMMMMMMMMMMMMMMMM..... .......... MMMMMMMM..M..MMM
MMMMMMMMMMMMMMMM?.....MMMMM..................MMMMMMM..M..MMM
MMMMMMMMMMMM...    ....MMMM.............  ...MMMMMMM..M..MMM
MMMMMM......MMMMMMMMM...MM......MMM....MM.?MM.MMMMMM..M..MMM
MMMM.    MMMMMMMMM.MM ..MM...MM.MMM......  ....MMMMM..M..MMM
MM .MMMMMMMMMMM.. . MM..MMM..........MMM..IM...MMMMM..M..MMM
MM MMMMMMMMMMMM ... MM..MM......M ...MMM..?M....MMMM..M..MMM
MM MM MMMMMMMMMM?....M..MM.......MM...M .M$....MMMMM..M..MMM
MM.....MMMMMMMMM?....M..MMM.....M .MMMMMM....MMMMMMM..M..MMM
MM ...MMMMMMMMMMMM..MM..MM.M  ...MM M..M....  MMMMMM..M..MMM
MM ...MMMMMMMMMMMM.MMM..MM..M  ....MM..M....MM.MMMMM..M..MMM
MM M..MMMMMMMMMMMM.MMM..MM..MM.......MM ....M...MMMM..M..MMM
MM.M..MMMMMMMMMMMM. MMM.. M..M.M.MM....M..?M.....MMM..M..MMM
MM.MM MMMMMMMMMMMM....M.. M... . MM..M.M   ......MMM..M..MMM
MM M  MMMMMMMMMMMM....M.. M........M.MM .........MMM..M..MMM
MM M..MMMMMMMMMMMM..  M.. M.........MM.   ?M.M....8M..M..MMM
MMM.M MMMMMMMMMMMM. MMM.. M......MMMMMM ......M...8MM...MMMM
MMM.M .MMMMMMMMM?..MMMM.. M.MMMMM ....M ......M..MMMM...MMMM
MMM.M .NMMMMMMMM?..MMMM.. M...........M ......M.MM=  MMM, MM
MMM.MM....MMMMMM?...MMM.. M...........M ...... MMM~       MM
MMM.MM... MM.MMM?.. MMM.. M...........M .......MMMMMM.M.MMMM
MMM.MMM . MM..MMMMM MMM.. M...........M ......MMM . MM..MMMM
MMM.MM...MMM..MMMMMMMMM.. M...........M ......MMM . M....MMM
MMMM.M   MMM..MMMMMMMMM.. M...........M ... .M.MM . M... MMM
MMMM.MMMMMMMMMMMMMMMMMM.. M.M.......M MMMMMMM MMMMMMM MMMMMM
MMMM.MMMMMMMMMMMMMMMMMM.. M..MMMMMMMMMMMMMMMM.MMMMMMM.M.MMMM
MMMMM MMMMMMMMMMMMMMMMMM...MMMMMMMMMMMMMMMMM..MMMMMMM.M.MMMM
M  MM MMMMMMMMMMMMM MMMM...MMMMMMMMM      ..M MMMMMMM.M.MMMM
MM...M.MMMMMMMMMMMM MMMM...M............MMMM.M.MMMMMM...MMMM
M....M.MMM. M  .$MM. MMM. .M             .?M .M.MMMMMMMMMMMM
M.M .MM  M  MM  $MM  MMM.  M           MMM$  M  MMMMMMMMMMMM
MM .  M  MM.MM .$MMMMMMM. .MMMMMMMMMMMM    .M. . MMMMMMMMMMM
M.M   M  MM MM  $MMMMMMM. .MMMMMMMMMMMMM .   . .  8MMMMMMMMM
MM   ..MM MMMMM $MMMMMMM. .M....  .. ...M  . . .  8MMMMMMMMM
MM NM  MM MMMMM $MMMMMMM. .M   .         M7  . .  8MMMMMMMMM
MMMMM   MM MMMM $MMMMMMM. .M....  .. ..  .?MMM .    MMMMMMMM
MMMMM   MM MMMMMMMMMMMMM. .M   .  .      MMMMMMM .  MMMMMMMM
MMMMMMM .MM MMMMMMMMMMMM. .MMMMMMMM MMM.   . . .MM~ MMMMMMMM
MMMMMMMM MM MMMMMMMMMMMM.  M      .MMMM         MMMMMMMMMMMM
MMMMMMMMMMMM MMMMMMMMMM.  MM      .MMMMM        MMMMMMMMMMMM
MMMMMMMMMMMM MMMMMMMMMM.  M.   . MMMMMMM   . . MMMMMMMMMMMMM
MMMMMMMMMMMMM MMMMMMMMM.  M.   . MMMMMMMM.     MMMMMMMMMMMMM
MMMMMMMMMMMMM MMMMMMMMM   M.    MMMMMMMMM... .MMMMMMMMMMMMMM
MMMMMMMMMMMMMM MMMMMMM..MMMM...MMMMMMMMMMM$. .MMMMMMMMMMMMMM
MMMMMMMMMMMMMMM $MMMMM  MMMM   MMMMMMMMMMMMM .MMMMMMMMMMMMMM
MMMMMMMMMMMMMMMM? MMMM..MMMM..MMMMMMMMMMMMMM .MMMMMMMMMMMMMM
MMMMMMMMMMMMMMMM?  MMM .MMMM  MMMMMMMMMMMMMM .MMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMM  M...MMM.. MMMMMMMMMMMMMM . MMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMM. .  MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMM ..MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
""",
"atk":1,
"hp":7,
"attack_1": "It pokes you playfully. Maybe a little too hard on accident.",
"attack_2": "It whines at you and wants to play.",
"death": "There may have been another way around this battle, but what you did works.",
"loot_1":"sword"
}
psuedodragon = {"name":" the psuedodragon","description": "You enter a room filled with glittering gold, trinkets, and baubles. You move closer to get a better look at the treasure and one pile shifts and rumbles. A little dragon head pokes up about the loot and tries to breath fire on you, but just spits out some smoke. This little guy looks like it wants to fight, so fight you will.",
"image": """
                /           /
                /' .,,,,  ./         
               /';'     ,/    
              / /   ,,//,`'`      
             ( ,, '_,  ,,,' ``   
             |    /@  ,,, ;" `  
            /    .   ,''/' `,``   
           /   .     ./, `,, ` ; 
        ,./  .   ,-,',` ,,/''\,'   
       |   /; ./,,'`,,'' |   |     
       |     /   ','    /    |  
        \___/'   '     |     |  
          `,,'  |      /     `\  
               /      |        ~\  
              '       (
             :
            ; .         \-- 
          :   \         ;  
""",
"atk":2,
"hp":4,
"attack_1": "The little draon flies up and scratches at you with its claws.",
"attack_2": "It tries to breath fire again, but fails.",
"death": "It is unfortunate that you had to kill such a little dragon, but it is better to take care of dragons early on.",
"loot_1": "dagger",
"loot_2":"potion"
}

werewolf = {"name":" the werewolf","description": "You enter a place that is heavily forested. From behind a tree pops out a being that look like a wolf that was once human. Standing on two legs, it snarls at you and snaps its teeth. It may have lost its humanity from being in that form for too long. Hopefully, in the coming battle you won’t become just like it.",
"image": """
                                 /\ 
                                ( ;`~v/~~~ ;._
                             ,/'"/^) ' < o\  '".~'--\--,
                           ,/",/W  u '`. ~  >,._..,   )'
                          ,/'  w  ,U^v  ;//^)/')/^\;~)'
                       ,/"'/   W` ^v  W |;         )/'
                     ;''  |  v' v`" W }  \ 
                    "    .'\    v  `v/^W,) '\)\.)\/)
                             `\   ,/,)'   ''')/^"-;'
                                  \ 
                                   '". _
                                        \ 
""",
"atk":4,
"hp":8,
"attack_1": "The werewolf bites at your arm.",  #This bite will affect the players werewolf status. If they go into the full moon room, it will change the result
"attack_2": "Two claws catch you as you make your next move.",
"attack_3": "It sits still and scratches at some fleas.",
"death": "The werewolf howls one last time. Death seems to be the only way to cure a lycanthropic life."
}

spooder = {"name":" the spider","description": "You enter an area covered in cobwebs and bugs wrapped in spider silk. You see tea cups filled with little spiders and a sort of spider pastry with a sign that says 'Made by spiders, for spiders, of spiders.'",
"description2": "You continue forward and encounter a giant spider that wants to eat your face. This is no spooder friend, you’ve got to spar with it.",
"image": """
           ____                      ,
          /---.'.__             ____//
               '--.\           /.---'
          _______   \          //
        /.------.\  \|      .'/  ______
       //  ___  \ \ ||/|\  //  _/_----.\__
      |/  /.-.\  \ \:|< >|// _/.'..\   '--'
         //   \ . | \ '.|.'/ /_/ / \ 
        //     \ \_\/" ' ~\-'.-'    \ 
       //       '-._| :H: |'-.__     \ 
      //           (/'==='\)'-._\     ||
      ||                        \     \|
      ||                         \     '
      |/                          \ 
                                   ||
                                   ||
                                   \ 
                                    '
""",
"atk":2,
"hp":8,
"attack_1": "It craws around and bites you with its strange gnashing fangs", #If the player uses the spider pastry the fight will end and the enemy will be considered defeated. This is a reference to Miss Muffet in Undertale
"attack_2": "It spins you into a web. You can't dodge next time.",
"attack_3": "The spider plots against you.",
"death": "Now that is how you deal with a spider.",
"loot_1":"venom"
}

snek = {"name":" the snake","description": "You now enter an area with tall grass and wildly growing weeds. Some of the plants start to shift and you hear a low hissing sounds. A large venomous snake rises above the plants in a mesmerizing dance. It bares it fangs, dripping with toxic fluids and looks as if it will strike you. Let’s get this show on the road.",
"image": """
      _,..,,,_ 
                     '``````^~"-,_`"-,_
       .-~c~-.                    `~:. ^-.     
   `~~~-.c    ;                      `:.  `-,     _.-~~^^~:.
         `.   ;      _,--~~~~-._       `:.   ~. .~          `.
          .` ;'   .:`           `:       `:.   `    _.:-,.    `.
        .' .:   :'    _.-~^~-.    `.       `..'   .:      `.    '
       :  .' _:'   .-'        `.    :.     .:   .'`.        :    ;
       :  `-'   .:'             `.    `^~~^`   .:.  `.      ;    ;
        `-.__,-~                  ~-.        ,' ':    '.__.`    :'
                                     ~--..--'     ':.         .:'
                                                     ':..___.:'
""",
"atk":1,
"hp":4,
"attack_1": "The snake slithers up and tries to sink its fangs into you.",
"attack_2": "It sways back and forth threateningly.",
"attack_3": "It slithers around you and tries to constrict your body.",
"death": "You slice the snake in half and blood splatters its beautiful scales. What a horrible way to go.",
"loot_1":"venom"
}

#Completed January 12th by 10:30 AM

rock = {"name":"the rock","description": "You enter an empty room with a single rock in the center. Did it just move towards you? Nope. It’s just a rock. Fight?",
"image": """
It's just a rock
""",
"atk":1,
"hp":20,
"attack_1": "Punching a rock hurts.",
"attack_2": "The rock doesn't do anything.",
"death": "That's really weird that you just defeated a rock, but okay.", #In this fight, the player just has to run away in order to defeat the rock, but they can punch it to death if they want
"loot_1": "really big rock"
}

wizard = {"name":"the wizard","description": "You enter a space that looks like it is part of a castle. The stone walls are lined with torches and in front of you an enemy approaches. This man has a long gray beard, a purple hat, a long robe, and a wand in his hand. This seems to be a stereotypical wizard. He prepares a spell as you prepare and attack.",
"image": """
                   ____ 
                  .'* *.'
               __/_*_*(_
              / _______ \ 
             _\_)/___\(_/_ 
            / _((\- -/))_ \ 
            \ \())(-)(()/ /
             ' \(((()))/ '
            / ' \)).))/ ' \ 
           / _ \ - | - /_  \ 
          (   ( .;''';. .'  )
          _\ __ /    )\ __"/_
            \/  \   ' /  \/
             .'  '...' ' )
              / /  |  \ \ 
             / .   .   . \ 
            /   .     .   \ 
           /   /   |   \   \ 
         .'   /    b    '.  '.
     _.-'    /     Bb     '-. '-._ 
 _.-'       |      BBb       '-.  '-. 
(________mrf\____.dBBBb.________)____)
""",
"atk":4,
"hp":6,
"attack_1": "The wizard sends a fireball your way.", 
"attack_2": "He has to prepare a spell before casting.",
"death": "Congratulations, you have defeated the wizard!",
"loot_1": "staff",
"loot_2": "dagger"
}

alien = {"description": "Suddenly, you are immersed in a strange light from above. You start floating off the ground and see a grey alien, eating toast, staring at you. It doesn’t seem too aggressive and walks away. You have officially been abducted by aliens.",
"image": """
             ,-"     "-.
            /           \ 
           /             \ 
          /     )-"-(     \ 
         /     ( 6 6 )     \ 
        /       \ " /       \ 
       /         )=(         \ 
      /   o   .--"-"--.   o   \ 
     /    I  /  -   -  \  I    \ 
 .--(    (_}y/\       /\y{_)    )--.
(    ".___l\/__\_____/__\/l___,"    )
 \                                 /
  "-._      o O o O o O o      _,-"
      `--Y--.___________.--Y--'
         |==.___________.==| hjw
         `==.___________.==' `97


""", #Image changed on January 17th because the previoius image kept throwing errors
     #Image2 removed on January 19th. I found it unneccesary as the description will suffice
"win": "Well then congratulations, you won!", #This is a random event that can lead to the player winning or losing, it is their choice
"loss": "Well then I guess you lost. Sorry."
}

moon = {"description": "You enter a large field lit by the light of a full moon.You might be able to rest in the grass and stare at the stars in order to regain some energy.",
#description occurs normally, description 2 occurs if the player is a werewolf
"description2": "You feel an urge to howl at the full moon and do so. In a painful series of events your body morphs into a canine. From there, you lose control of yourself and your memories too. You wake up in human form towards the edge of a field. The moon is still full so you rush out of the area in order to escape another transformation.",
"image": """
        _..._  .
   .  .'     `.    .      .  *
     :         :           .
*    :         :   .     *
     `.       .'  .            .
.      `-...-'         *
"""
}

#Completed by January 12 11:35 AM

boss = {"name":"Bowser", 
"image":"""

───────▄█──────────█─────────█▄───────
─────▐██──────▄█──███──█▄─────██▌─────
────▐██▀─────█████████████────▀██▌────
───▐██▌─────██████████████─────▐██▌───
───████────████████████████────████───
──▐█████──██████████████████──█████▌──
───████████████████████████████████───
────███████▀▀████████████▀▀███████────
─────█████▌──▄▄─▀████▀─▄▄──▐█████─────
───▄▄██████▄─▀▀──████──▀▀─▄██████▄▄───
──██████████████████████████████████──
─████████████████████████████████████─
▐██████──███████▀▄██▄▀███████──██████▌
▐█████────██████████████████────█████▌
▐█████─────██████▀──▀██████─────█████▌
─█████▄─────███────────███─────▄█████─
──██████─────█──────────█─────██████──
────█████────────────────────█████────
─────█████──────────────────█████─────
──────█████────────────────█████──────
───────████───▄────────▄───████───────
────────████─██────────██─████────────
────────████████─▄██▄─████████────────
───────████████████████████████───────
───────████████████████████████───────
────────▀█████████▀▀█████████▀────────
──────────▀███▀────────▀███▀──────────
""",
"atk":8,
"hp":60,
"attack_1": "Bowser leaps immensly into the air. You can't hit him while he is in the air. ",
"attack_2": "'MWHAHAHAHAHA YOU WILL NEVER WIN!' ",
"attack_3": "He attempts to hit you with his massive arms. ",
"attack_4": "Bowser takes a deep in breath and release a huge wave of flames at you. ",
"death":"You have finally beaten him. He tumbles and falls into the lava. Bowser screams in anger as he sinks to the bottom."
} 


def fight(monster):        #function added January 19
    global hit_points   #This function should work for the monsters that don't have special attacks or events like piccolo, skeleton, killer_rabbit, psuedodragon, and wizard
    global user_input
    global attack   #stating "global" makes sure the function sees the variable as global, not local. VERY IMPORTANT
    global enemies_defeated
    global monster_attack
    global player_damage
    global modifier
    global damage
    hp = monster["hp"]
    print(monster["image"])
    print(monster["description"])
    while hp>0 and hit_points>0:
        user_input = input("Would you like to attack or dodge? ")
        if user_input.lower() == "attack" or user_input.lower() == "a":
            print("You",attack[random.randint(0,len(attack)-1)], monster["name"], " for", player_damage, "point(s) of damage") #dodging and monster attack added by January 23nd 8:20 AM
            hp -= player_damage #changed combat order January 27th 2018 so that you attack before the enemy
            if monster_attack == 1:
                print (monster["attack_1"])
                hit_points -= monster["atk"]
                print("You are now at", hit_points, "hit points")
            elif monster_attack == 2:
                print (monster["attack_2"])
        elif user_input.lower() == "dodge" or user_input.lower() == "d":
            if monster_attack == 1:
                print (monster["attack_1"])
            elif monster_attack == 2:
                print (monster["attack_2"])
            print("But you", dodge[random.randint(0,len(dodge)-1)], "out of the way.")
        elif monster == piccolo and user_input.lower() == "skip":                   #added this so that I can skip the Piccolo fight and test other parts of the code
            print("Well, I guess you already know how to proceed. Goodbye Piccolo.")
            hp=0
        elif user_input.lower() == "check" or user_input.lower() == "c":
            check()
        else:
            print("You can't do that")
        monster_attack = random.randint(1,2)
    if hit_points>0:
        print(monster["death"])
        print("Congrats! You have defeated", monster["name"])
        enemies_defeated += 1 #This part of the function finished by January 19th 8:35
        if not monster == piccolo: #fixes the piccolo not having anything for loot issue - June 13th
            loot = random.randint(1,5)
            if (loot == 1 or loot == 2 or loot == 3) and not monster == "piccolo" :
                if loot ==1 or loot == 2:
                    loot = monster["loot_1"]
                elif loot == 3:
                    loot = monster["loot_2"]
                print("You found a %s!" %loot)
                if loot == "femur" or loot == "pitchfork" or loot == "dagger" or loot == "staff":
                    print("Would you like to equip the %s? Note that this will replace your previous item" %loot) #figured out the %s solution on June 13th. Before there was an unneccessary space between the loot and the ? or !
                    user_input = input(" ")
                    if user_input.lower() == "yes" or user_input.lower() == "y":
                        if loot == "pitchfork":
                            modifier = 2
                            print("You equip the pitchfork!") #added this line to confirm your action was recieved on June 13th
                        elif loot == "dagger":
                            modifier =3
                            print("You equip the dagger!")
                        elif loot == "staff":
                            modifier = 4
                            print("You equip the staff!")
                        elif loot == "femur":
                            modifier = 4
                            print("You equip the femur!")
                elif loot == "bone claws":
                    print("You have obtained bone claws!")
                    damage +=2
                elif loot == "rabbit's foot":
                    print("You have obtained a rabbit's foot, how lucky.")
                    damage +=1
                elif loot == "potion":
                    print("You have found a potion. Let's hope this is a good one")
                    healing = random.randint(5,10)
                    print("You have gained", healing, "hit points!")
                    hit_points += healing
    else:
        print("It appears that", monster["name"], "has", defeated[random.randint(0,len(defeated)-1)], "you.")
        
def moon_room():
    global user_input
    global hit_points
    global werewolf_status
    global moon
    if werewolf_status == "NOT A WEREWOLF":
        print("This place seems very peaceful.")
        user_input = input("Would you like to check anything before you rest? ")
        if user_input.lower() == "yes" or user_input.lower() == "y":
            check()
        print("Sleeping can regenerate some hit points, but some rests are better than others. Hopefully, you sleep well...")
        sleep = random.randint(5,15) #With the addition of weapons, the game started to become too easy. These numbers were reduced on 11 June 2018
        hit_points += sleep
        user_input = input("")
        print("You regained", sleep, "hit points!")
    else: #This part added January 27th for the werewolf status
        print(moon["description2"])
        sleep = random.randint(1,10)
        hit_points += sleep
        user_input = input("")
        print("It seems you have regained", sleep, "hit points!")
    
def check(): #added January 27th 2018 so that players can check some of their stats during battle. Further stats may be added later
    global user_input
    global hit_points
    global enemies_defeated
    global werewolf_status
    global player_damage
    user_input = input("Would you like to check your hit points, number of enemies defeated, or player damage? ")
    if user_input.lower() == "hit points" or user_input.lower() == "hp":
        print("HIT POINTS:", hit_points)
    elif user_input.lower() == "number of enemies defeated" or user_input.lower() == "number of enemies" or user_input.lower() == "enemies" or user_input.lower() == "enemies defeated" or user_input.lower() == "e":
        print("ENEMIES DEFEATED:", enemies_defeated)
    elif user_input.lower() == "werewolf status" or user_input.lower() == "werewolf" or user_input.lower() == "w":
        print("WEREWOLF STATUS:", werewolf_status)
    elif user_input.lower() == "player damage" or user_input.lower() == "d" or user_input.lower() == "p": #added June 7th to accompany the new stat
        print("PLAYER DAMAGE:", player_damage)
    else:
        print("You can't do that")
        
def mermaid_fight(): #Completed by January 27th 2018 8:30 PM
    global hit_points   #this fight was copied from the fight() function and adapted for the mermaid
    global user_input
    global attack
    global enemies_defeated
    global monster_attack
    global mermaid
    global restrictions
    global player_damage
    hp = mermaid["hp"]
    print(mermaid["image"])
    print(mermaid["description"])
    while hp>0 and hit_points>0:
        user_input = input("Would you like to attack or dodge? ")
        if user_input.lower() == "attack" or user_input.lower() == "a" and restrictions == "null":
            if not restrictions == "null":
                restrictions = "null"
            print("You",attack[random.randint(0,len(attack)-1)], "the mermaid for", player_damage,  "point(s) of damage")
            hp -= player_damage
            if monster_attack == 1:
                print (mermaid["attack_1"])
                hit_points -= mermaid["atk"]
                print("You are now at", hit_points, "hit points")
            elif monster_attack == 2:
                print (mermaid["attack_2"])
            elif monster_attack == 3:
                print (mermaid["attack_3"])
                print("You cannot attack next turn.")
                restrictions = "mermaid song"
        elif user_input.lower() == "dodge" or user_input.lower() == "d":
            if not restrictions == "null":
                restrictions = "null"
            if monster_attack == 1:
                print (mermaid["attack_1"])
                print("But you", dodge[random.randint(0,len(dodge)-1)], "out of the way.")
            elif monster_attack == 2:
                print (mermaid["attack_2"])
                print("But you", dodge[random.randint(0,len(dodge)-1)], "out of the way.")
            elif monster_attack == 3:
                print (mermaid["attack_3"])
                print("But you shake off the effects of the song")            
        elif user_input.lower() == "check" or user_input.lower() == "c":
            check()
        else:
            print("You can't do that")
        monster_attack = random.randint(1,3)
    if hit_points>0:
        print(mermaid["death"])
        print("Congrats! You have defeated the mermaid")
        enemies_defeated += 1
        restrictions = "null"
    else:
        print("It appears that the mermaid has", defeated[random.randint(0,len(defeated)-1)], "you.")
        
def snek_fight(): #Completed by January 27th 2018 8:40 PM
    global hit_points   #this fight was copied from the mermaid_fight() function and adapted for the snek
    global user_input
    global attack
    global enemies_defeated
    global monster_attack
    global snek
    global restrictions
    global player_damage
    hp = snek["hp"]
    print(snek["image"])
    print(snek["description"])
    while hp>0 and hit_points>0:
        user_input = input("Would you like to attack or dodge? ")
        if user_input.lower() == "attack" or user_input.lower() == "a":
            if not restrictions == "null":
                restrictions = "null"
            print("You",attack[random.randint(0,len(attack)-1)], "the snek for", player_damage, "point(s) of damage")
            hp -= player_damage
            if monster_attack == 1:
                print (snek["attack_1"])
                hit_points -= snek["atk"]
                print("You are now at", hit_points, "hit points")
            elif monster_attack == 2:
                print (snek["attack_2"])
            elif monster_attack == 3:
                print (snek["attack_3"])
                print("You cannot dodge next turn.")
                restrictions = "snek"
        elif user_input.lower() == "dodge" or user_input.lower() == "d" and restrictions == "null":
            if not restrictions == "null":
                restrictions = "null"
            if monster_attack == 1:
                print (snek["attack_1"])
                print("But you", dodge[random.randint(0,len(dodge)-1)], "out of the way.")
            elif monster_attack == 2:
                print (snek["attack_2"])
                print("But you", dodge[random.randint(0,len(dodge)-1)], "out of the way.")
            elif monster_attack == 3:
                print (snek["attack_3"])
                print("But you slip out of the snek's grasp")            
        elif user_input.lower() == "check" or user_input.lower() == "c":
            check()
        else:
            print("You can't do that")
        monster_attack = random.randint(1,3)
    if hit_points>0:
        print(snek["death"])
        print("Congrats! You have defeated the snek")
        enemies_defeated += 1
        restrictions = "null"
    else:
        print("It appears that the snek has", defeated[random.randint(0,len(defeated)-1)], "you.")
    
def werewolf_fight(): #Completed by January 29th 8:00 AM
    global hit_points   #this fight was copied from the mermaid_fight() function and adapted for the werewolf
    global user_input
    global attack
    global enemies_defeated
    global monster_attack
    global werewolf
    global restrictions
    global werewolf_status
    global player_damage
    global damage
    hp = werewolf["hp"]
    print(werewolf["image"])
    print(werewolf["description"])
    while hp>0 and hit_points>0:
        user_input = input("Would you like to attack or dodge? ")
        if user_input.lower() == "attack" or user_input.lower() == "a":
            print("You",attack[random.randint(0,len(attack)-1)], "the werewolf for", player_damage, "point(s) of damage")
            hp -= player_damage
            if monster_attack == 1:
                print (werewolf["attack_1"])
                hit_points -= int(werewolf["atk"]/2)
                print("You are now at", hit_points, "hit points")
                werewolf_chance = random.randint(1,4)
                if werewolf_chance == 1:
                    print("The bite leaves a mark that won't heal for quite some time.")
                    werewolf_status = "YOU ARE A WEREWOLF"
                    damage += 1 #Added June 7th - You become stronger because you can't heal as much now -changed from 2 to 1, it was far too powerful
            elif monster_attack == 2:
                print (werewolf["attack_2"])
                hit_points -= werewolf["atk"]
                print("You are now at", hit_points, "hit points")
            elif monster_attack == 3:
                print (werewolf["attack_3"])
        elif user_input.lower() == "dodge" or user_input.lower() == "d":

            if monster_attack == 1:
                print (werewolf["attack_1"])
                print("But you", dodge[random.randint(0,len(dodge)-1)], "out of the way.")
            elif monster_attack == 2:
                print (werewolf["attack_2"])
                print("But you", dodge[random.randint(0,len(dodge)-1)], "out of the way.")
            elif monster_attack == 3:
                print (werewolf["attack_3"])
                print("But you", dodge[random.randint(0,len(dodge)-1)], "out of the way.")            
        elif user_input.lower() == "check" or user_input.lower() == "c":
            check()
        else:
            print("You can't do that")
        monster_attack = random.randint(1,3)
    if hit_points>0:
        print(werewolf["death"])
        print("Congrats! You have defeated the werewolf")
        enemies_defeated += 1
    else:
        print("It appears that the werewolf has", defeated[random.randint(0,len(defeated)-1)], "you.")
        
def rock_fight(monster):    #function copied from fight() function and adapted for the rock
    global hit_points  
    global user_input
    global attack   
    global enemies_defeated
    global monster_attack
    global player_damage
    global modifier
    hp = monster["hp"]
    print(monster["image"])
    print(monster["description"])
    while hp>0 and hit_points>0:
        user_input = input("Would you like to attack,dodge, or honestly just leave? ")
        if user_input.lower() == "attack" or user_input.lower() == "a":
            print("You",attack[random.randint(0,len(attack)-1)], monster["name"], " for",player_damage, "point(s) of damage") 
            hp -= player_damage
            if monster_attack == 1:
                print (monster["attack_1"])
                hit_points -= monster["atk"]
                print("You are now at", hit_points, "hit points")
            elif monster_attack == 2:
                print (monster["attack_2"])
        elif user_input.lower() == "dodge" or user_input.lower() == "d":
            print (monster["attack_2"])
            print("But you", dodge[random.randint(0,len(dodge)-1)], "out of the way.")
        elif user_input.lower() == "check" or user_input.lower() == "c":
            check()
        elif user_input.lower() == "just leave" or user_input.lower() == "leave" or user_input.lower() == "l":
            print("That was probably the best decision you have made.")
            hp = 0
        else:
            print("You can't do that")
        monster_attack = random.randint(1,2)
    if hit_points>0:
        print(monster["death"])
        print("Congrats! You have defeated", monster["name"])
        enemies_defeated += 1 
        if hp<1:
            loot = random.randint(1,5)
            if loot == 1:
                print("You obtained a really big rock. This replaces your current weapon.")
                modifier = 6
    else:
        print("It appears that", monster["name"], "has", defeated[random.randint(0,len(defeated)-1)], "you.")
        
def spooder_fight(monster):        #function added January 29th by 8:45 AM
    global hit_points   #This function was adjusted from the fight() and snek_fight() function
    global user_input
    global attack  
    global monster_attack
    global enemies_defeated
    global restrictions
    global player_damage
    cake = 'n'
    hp = monster["hp"]
    print(monster["description"])
    user_input = input("Would you like to take one and leave the suggested amount of money? ")
    if user_input.lower() == "yes" or user_input.lower() == "y":
        print("You now have a spider cake.")
        cake = "y"
    print(monster["image"])
    print(monster["description2"])
    while hp>0 and hit_points>0:
        if cake == "y":
            user_input = input("Would you like to attack, dodge, or eat the cake? ")
        else:
            user_input = input("Would you like to attack or dodge? ")
        if user_input.lower() == "attack" or user_input.lower() == "a":
            if not restrictions == "null":
                restrictions = "null"
            print("You",attack[random.randint(0,len(attack)-1)], monster["name"], " for", player_damage,"point(s) of damage")
            hp -= player_damage
            if monster_attack == 1:
                print (monster["attack_1"])
                hit_points -= monster["atk"]
                print("You are now at", hit_points, "hit points")
            elif monster_attack == 2:
                print (monster["attack_2"])
                restrictions = "spooder"
            elif monster_attack == 3:
                print (werewolf["attack_3"])
        elif user_input.lower() == "dodge" or user_input.lower() == "d" and restrictions == "null":
            if not restrictions == "null":
                restrictions = "null"
            if monster_attack == 1:
                print (monster["attack_1"])
                print("But you", dodge[random.randint(0,len(dodge)-1)], "out of the way.")
            elif monster_attack == 2:
                print (monster["attack_2"])
                print("But you", dodge[random.randint(0,len(dodge)-1)], "out of the way.")
            elif monster_attack == 3:
                print (werewolf["attack_3"])
                print("But you shake off the webs")
        elif user_input.lower() == "check" or user_input.lower() == "c":
            check()
        elif user_input.lower() == "eat cake" or user_input.lower() == "e" or user_input.lower() == "eat the cake" or user_input.lower() == "eat":
            hit_points += 5
            print("You regain 5 hp!")
            print("Another spider in a dress crawls out from behind some webs. 'Oh! You support us spiders. Then there is no need to fight.'")
            print("The spiders back down and you can leave")
            hp = 0
        else:
            print("You can't do that")
        monster_attack = random.randint(1,3)
    if hit_points>0:
        restrictions = "null"
        print(monster["death"])
        print("Congrats! You have defeated", monster["name"])
        enemies_defeated += 1
    else:
        print("It appears that", monster["name"], "has", defeated[random.randint(0,len(defeated)-1)], "you.")
        
def alien_abduction():
    global alien
    global user_input
    global hit_points
    print(alien["image"])
    print(alien["description"]) 
    user_input = input("Is this a win or a loss to you? ")
    while True:
        if user_input.lower() == "win" or user_input.lower() == "w":
            print(alien["win"])
            break
        elif user_input.lower() == "loss" or user_input.lower() == "l":
            print(alien["loss"])
            hit_points = 0
            break
        else:
            print("You cannot do that")
    
def lesser_dog_fight(monster): #added January 30th 2018 by 7:05 PM
    global hit_points   #This function was adjusted from the spooder_fight() function
    global user_input
    global attack  
    global monster_attack
    global enemies_defeated
    global restrictions
    global player_damage
    global modifier
    hp = monster["hp"]
    print(monster["image"])
    print(monster["description"])
    pet = 0
    while hp>0 and hit_points>0:
        if pet >0:
            print("Now that you have made it happy, you can probably just leave.")
        user_input = input("Would you like to attack,dodge, or pet? ")
        if user_input.lower() == "attack" or user_input.lower() == "a":
            print("You",attack[random.randint(0,len(attack)-1)], monster["name"], " for", player_damage, "point(s) of damage")
            hp -= player_damage 
            if monster_attack == 1:
                print (monster["attack_1"])
                hit_points -= monster["atk"]
                print("You are now at", hit_points, "hit points")
            elif monster_attack == 2:
                print (monster["attack_2"])
        elif user_input.lower() == "dodge" or user_input.lower() == "d" and restrictions == "null":
            if monster_attack == 1:
                print (monster["attack_1"])
                print("But you", dodge[random.randint(0,len(dodge)-1)], "out of the way.")
            elif monster_attack == 2:
                print (monster["attack_2"])
                print("But you", dodge[random.randint(0,len(dodge)-1)], "out of the way.")
        elif user_input.lower() == "check" or user_input.lower() == "c":
            check()
        elif user_input.lower() == "pet" or user_input.lower() == "p":
            pet += 1  
            print(pet)
            print("Lesser dog yips in excitement and licks your face.")
            print("He seems ")
            for i in range(pet):
                print("very")
            print("happy.")
        elif user_input.lower() == "leave" or user_input.lower() == "l" and pet > 0:
            print("Lesser dog is sad to see you go, and hopes you will come back soon.")
            enemies_defeated += 1
            break
        else:
            print("You can't do that")
        monster_attack = random.randint(1,2)
    if hit_points>0 and hp<1:
        print(monster["death"])
        print("Congrats! You have defeated", monster["name"])
        enemies_defeated += 1
        loot = random.randint(1,6)
        if loot == 1:
            print("You have obtained lesser dog's sword. This replaces your current weapon")
            modifier = 5
    elif hp < 1:
        print("It appears that", monster["name"], "has", defeated[random.randint(0,len(defeated)-1)], "you.")
        

print("WELCOME to the DUNGEON!")  #Little intro added January 30th to givce the player a little info before just jumping into the game
print("Your goal is to defeat 10 enemies in order to survive. Your quest starts with a battle with Piccolo.")
print("                                              GOOD LUCK!")
user_input = input("")
fight(piccolo)                             #game officially starts here with the Piccolo fight to teach you how to play
user_input = input("")

print("Now that you know how to play, anytime during combat you can type in 'check' to see what some of your stats are. Good luck!")
user_input = input("")

while hit_points>0 or enemies_defeated<10:#second boolean added on January 23rd. I may have the player move on to harder enemies with a chance of facing the boss or just face the boss.
    player_damage = damage + modifier
    if hit_points<1:
        break
    elif enemies_defeated>9:
        break
    elif room >=1 and room <= 10: #The room variable is a random number between one a one hundred. Each room has its own percent of occuring from that random number. The skeleton has a 10% chance of occuring
        fight(skeleton)
        user_input = input("")
        room = random.randint(1,100) #This will make a new room number so that when the while statement goes through again, there will be a new room
    elif room >=11 and room <= 15: #The mermaid has a 5% chance of occuring
        mermaid_fight()
        user_input = input("")
        room = random.randint(1,100)
    elif room >=16 and room <= 25: #The killer_rabbit has a 10% chance of occuring
        fight(killer_rabbit)
        user_input = input("")
        room = random.randint(1,100)
    elif room >=26 and room <= 34: #The lesser dog has a 9% chance of occuring
        lesser_dog_fight(lesser_dog)
        user_input = input("")
        room = random.randint(1,100)
    elif room >=35 and room <= 39: #The psuedodragon has a 5% chance of occuring
        fight(psuedodragon)
        user_input = input("")
        room = random.randint(1,100)
    elif room >=40 and room <= 49: #The werewolf has a 10% chance of occuring
        werewolf_fight()
        user_input = input("")
        room = random.randint(1,100)
    elif room >=50 and room <= 59: #The spooder has a 10% chance of occuring
        spooder_fight(spooder)
        user_input = input("")
        room = random.randint(1,100)
    elif room >=60 and room <= 69: #The snek has a 10% chance of occuring
        snek_fight()
        user_input = input("")
        room = random.randint(1,100)
    elif room >=70 and room <= 79: #The rock has a 10% chance of occuring
        rock_fight(rock)
        user_input = input("")
        room = random.randint(1,100)
    elif room >=80 and room <= 84: #The wizard has a 5% chance of occuring
        fight(wizard)
        user_input = input("")
        room = random.randint(1,100)
    elif room == 85: #The alien abduction has 1% chance to occur
        alien_abduction()
        user_input = input("")
        break
        room = random.randint(1,100)
    elif room >=86 and room <= 100: #The full moon room has a 15% chance of occuring
        print(moon["image"])
        print(moon["description"])
        moon_room()
        user_input = input("")
        room = random.randint(1,100)

#Completed by January 17th 8:15 AM

if hit_points <= 0:
    print("GAME OVER")
else:
    print("CONGRATULATIONS!")
    if enemies_defeated < 10:
        print ("YOU WON BY BEING ABDUCTED BY ALIENS")
    else:
        print("YOU WON BY DEFEATING THE ENEMIES")
print("ENEMIES DEFEATED:", enemies_defeated) #Some final stats for the player. May be added on to later
print("WEREWOLF STATUS:", werewolf_status)
print("PLAYER DAMAGE:", player_damage)
print("MAYBE YOU CAN DO BETTER NEXT TIME.")

#Completed by January 23rd 8:30 AM
if hit_points>0:
    user_input = input("Would you like to move on to a harder level? ")
    if user_input.lower() == "yes" or user_input.lower() == "y":
            print("WELCOME TO THE DUNGEON 2")
            print("YOUR ENEMIES HAVE GOTTEN MORE DIFFICULT, AND YOU CAN CONTINUE TO GATHER ITEMS ON YOUR QUEST")
            if modifier == 0:
                print("HERE IS A ROCK TO GET YOU STARTED")
                modifier = 1
            print("YOU HAVE ALREADY FOUGHT 10 ENEMIES. IF YOU DEFEAT 10 MORE YOU CAN GET TO THE BOSS")
            print ("GOOD LUCK")
            
            if hit_points<30:
                hit_points = 30
                print("Your hit points have returned to normal")
            else:
                print("You have enough health. Looks like there is no healing for you right now")
            
            skeleton["atk"] += 2 #this adds to the attack of all of the monsters in order to add some difficulty to the game
            mermaid["atk"] += 2
            killer_rabbit["atk"] += 2
            lesser_dog["atk"] += 2
            psuedodragon["atk"] += 2
            werewolf["atk"] += 2
            spooder["atk"] += 2
            snek["atk"] += 2
            rock["atk"] += 2
            wizard["atk"] += 2
            
            user_input = input("")
            while hit_points>0 or enemies_defeated<20:#this is all just copy and pasted from the first dungeon
                player_damage = damage + modifier
                if hit_points<1:
                    break
                elif enemies_defeated>19:
                    break
                elif room >=1 and room <= 10: #The room variable is a random number between one a one hundred. Each room has its own percent of occuring from that random number. The skeleton has a 10% chance of occuring
                    fight(skeleton)
                    user_input = input("")
                    room = random.randint(1,100) #This will make a new room number so that when the while statement goes through again, there will be a new room
                elif room >=11 and room <= 15: #The mermaid has a 5% chance of occuring
                    mermaid_fight()
                    user_input = input("")
                    room = random.randint(1,100)
                elif room >=16 and room <= 25: #The killer_rabbit has a 10% chance of occuring
                    fight(killer_rabbit)
                    user_input = input("")
                    room = random.randint(1,100)
                elif room >=26 and room <= 34: #The lesser dog has a 9% chance of occuring
                    lesser_dog_fight(lesser_dog)
                    user_input = input("")
                    room = random.randint(1,100)
                elif room >=35 and room <= 39: #The psuedodragon has a 5% chance of occuring
                    fight(psuedodragon)
                    user_input = input("")
                    room = random.randint(1,100)
                elif room >=40 and room <= 49: #The werewolf has a 10% chance of occuring
                    werewolf_fight()
                    user_input = input("")
                    room = random.randint(1,100)
                elif room >=50 and room <= 59: #The spooder has a 10% chance of occuring
                    spooder_fight(spooder)
                    user_input = input("")
                    room = random.randint(1,100)
                elif room >=60 and room <= 69: #The snek has a 10% chance of occuring
                    snek_fight()
                    user_input = input("")
                    room = random.randint(1,100)
                elif room >=70 and room <= 79: #The rock has a 10% chance of occuring
                    rock_fight(rock)
                    user_input = input("")
                    room = random.randint(1,100)
                elif room >=80 and room <= 84: #The wizard has a 5% chance of occuring
                    fight(wizard)
                    user_input = input("")
                    room = random.randint(1,100)
                elif room == 85: #The alien abduction has 1% chance to occur
                    alien_abduction()
                    user_input = input("")
                    break
                    room = random.randint(1,100)
                elif room >=86 and room <= 100: #The full moon room has a 15% chance of occuring
                    print(moon["image"])
                    print(moon["description"])
                    moon_room()
                    user_input = input("")
                    room = random.randint(1,100)
                    
                    
            if hit_points <= 0:
                print("GAME OVER")
            else:
                print("CONGRATULATIONS!")
                if enemies_defeated < 20:
                    print ("YOU WON BY BEING ABDUCTED BY ALIENS")
                else:
                    print("YOU WON BY DEFEATING THE ENEMIES")
            print("ENEMIES DEFEATED:", enemies_defeated) #Some final stats for the player. May be added on to later
            print("WEREWOLF STATUS:", werewolf_status)
            print("PLAYER_DAMAGE:", player_damage)
            print("MAYBE YOU CAN DO BETTER NEXT TIME.")
            
#added by June 7th at 8:30 AM -lots of bugs to fix
#Most of the bugs are fixed by now. Need to fix the piccolo bug for looting -June 13th
if hit_points> 0 and enemies_defeated > 19:
    user_input = input("Are you ready for the boss? ")
    if user_input.lower() == "y" or user_input.lower() == "yes":
        print("Good luck...")
    else:
        print("TOO BAD")
        
    print("You enter a chamber with metal blocks for a floor and lava bubbling to the sides of the path. In front of you rests an alter with three potions.")
    print("The first potion is blood red, the second is sapphire blue, and the last is emerald green")
    user_input = input("Which do you choose? ")
    if user_input.lower() == "b" or user_input.lower() == "blue" or user_input.lower() == "s" or user_input.lower() == "sapphire"or user_input.lower() == "sapphire blue": #started to work forward from here on June 13th
        print("This potion fills you with power and invigorates your arms.") #I added a lot of options above since you get penalized for choosing nothing 
        print("               You gain 5 damage!")
        damage +=5
    elif user_input.lower() == "r" or user_input.lower() == "red" or user_input.lower() == "b" or user_input.lower() == "blood" or user_input.lower() == "blood red":
        print("This potion fills you with energy and heals some of your wounds.")
        print("               You gain 20 hit points!")
        hit_points += 20
    elif user_input.lower() == "g" or user_input.lower() == "green" or user_input.lower() == "emerald" or user_input.lower() == "e" or user_input.lower() == "emerald green":
        print("You hear an echo of someone's deep laughter and the voice turns to say 'EQUALITY'")
        temporary = hit_points + boss["hp"]
        temporary = temporary/2 #the player won't be certain as to what heppens here, but it hint at equality just like with coins in Mario Party
        hit_points = temporary #Basically the average of the boss hp and your hp is taken and given to both of you. Sometimes it helps sometimes it hurts
        boss["hp"] = temporary
        print("You aren't completley certain as to what just happened, but you now have %d hit points." %hit_points)
    else:
        print("Your indecision aggravates the alter. The red potion is flung at your head and red fluid oozes down your body")
        print("This still helps heal your wounds, but probably not as much as if you had drank it")
        print("              You gain 10 hit points!")
        hit_points += 10
    user_input = input("Would you like to check any last stats?")
    if user_input.lower() == "y" or user_input.lower == "yes":
        check()
    print("WELCOME TO THE FINAL BATTLE")
    print("IF YOU WIN THIS, YOU TRULY ARE THE CHAMPION OF THE DUNGEON")
    player_damage = damage + modifier
    hp = boss["hp"]
    print(boss["image"])
    while hp>0 and hit_points>0:
        monster_attack = random.randint(1,10)
        user_input = input("Would you like to attack or dodge? ")
        if user_input.lower() == "attack" or user_input.lower() == "a":
            if monster_attack == 6 or monster_attack == 7: #20%chance
                print(boss["attack_1"])
            elif monster_attack == 1 or monster_attack == 2 or monster_attack == 3 or monster_attack == 4 or monster_attack == 5: #50% chance of ocurring
                print("You",attack[random.randint(0,len(attack)-1)], "Bowser for", player_damage, "point(s) of damage") 
                hp -= player_damage 
                print (boss["attack_3"])
                hit_points -= boss["atk"]
                print("You are now at", hit_points, "hit points")
            elif monster_attack == 8 or monster_attack == 9: #20% chance
                print("You",attack[random.randint(0,len(attack)-1)], "Bowser for", player_damage, "point(s) of damage") 
                hp -= player_damage 
                print (boss["attack_2"])
            elif monster_attack == 10: #10% chance
                print("You",attack[random.randint(0,len(attack)-1)], "Bowser for", player_damage, "point(s) of damage") 
                hp -= player_damage 
                print(boss["attack_4"])
                hit_points -= int(boss["atk"]*2)
                print("You are now at", hit_points, "hit points")
        elif user_input.lower() == "dodge" or user_input.lower() == "d":
            if monster_attack == 1 or monster_attack == 2 or monster_attack == 3 or monster_attack == 4 or monster_attack == 5: 
                print (boss["attack_3"])
                print("But you", dodge[random.randint(0,len(dodge)-1)], "out of the way.")
            elif monster_attack == 6 or monster_attack == 7:
                print(boss["attack_1"])
            elif monster_attack == 8 or monster_attack == 9:
                print (boss["attack_2"])
            elif monster_attack == 10:
                print("You", dodge[random.randint(0,len(dodge)-1)], "out of the way of most of the flames, but the lingering heat still overtakes you.")
                hit_points -= int(boss["atk"]/4)
                print("You are now at", hit_points, "hit points")
        elif user_input.lower() == "check" or user_input.lower() == "c":
            check()
        else:
            print("You can't do that")
    if hit_points>0:
        print(boss["death"])
        print("Congratulations! You have vanquished the beast and completed THE DUNGEON")
        print("ENEMIES DEFEATED:", enemies_defeated)
        print("WEREWOLF STATUS:", werewolf_status)
        print("PLAYER_DAMAGE:", player_damage)  
    else:
        print("It appears that", boss["name"], "has", defeated[random.randint(0,len(defeated)-1)], "you.")