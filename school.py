import random

# Worth mentioning first is the length of the different prints. Due to the small size of my laptop,
# the horizontal width of all outputs is pretty small, and depending on resolution, sentances may appear to be cut in half.
# This was unfortunately unavoidable, but it should not affect the experience except for minor annoyance.

party_name = ""
party_survived = True

print("\nThis little game is a text-based adventure game, where you'll manage a\n"
      "handful of adventurers. These adventurers are all categorized by their\n"
      "class: Martial, Finesse, or Magic. In this adventure, your party will\n"
      "come across a number of obstacles that, for some, will be difficult -\n"
      "but to other heroes, it will be barely any challenge at all.")


def menu_start():
    print()
    print("\tWELCOME!")
    option = input("1. Game start\n2. Information regarding classes & types\n3. Quit\n")
    if not option:
        print("You need to select an option.")
        menu_start()
    elif option == "1":
        game_start()
    elif option == "2":
        menu_character_types()
    elif option == "3":
        print("Goodbye!")
    else:
        print("That's not a menu option.")
        menu_start()


def menu_character_types():
    print("\tClass Information")
    option = input("1. Martial information\n2. Finesse information\n3. Magic information\n")
    if not option:
        print("You ned to select an option.")
        menu_character_types()
    elif option == "1":
        menu_print_martial()
        menu_start()
    elif option == "2":
        menu_print_finesse()
        menu_start()
    elif option == "3":
        menu_print_magic()

        menu_start()
    else:
        print("That's not a menu option.")
        menu_character_types()


def menu_print_martial():
    print("\tBlademaster\n"
          "The Blademaster is a man of war, a master of dueling.\n"
          "His skills are no less valuable against monstrosities, however.\n"
          "Any warrior worth his salt must be adept at not only fighting,\n"
          "But be able to survive the march to far away dangerous locations.\n")
    print("\tBarbarian\n"
          "The Barbarian is a savage from tribes on the fringes of the known world.\n"
          "Do not underestimate him however -  despite the pelts and crude greatsword,\n"
          "the Barbarian is a seasoned veteran of harsh terrain and a dangerous life.\n")
    print("\tGuardian\n"
          "The Guardian is a master of fighting with sword and shield.\n"
          "The Guardian is driven to defend her allies, who stand resolute behind\n"
          "her shieldwall. Experienced and possessed of tremendous stamina,\n"
          "the Guardian will make a good addition to any long venture.\n")


def menu_print_finesse():
    print("\tRogue\n"
          "The Rogue is a scoundrel, a thief, a pickpocket, a hoodlum...\n"
          "But one who knows when to break from her past troubles, to rise\n"
          "to the occasion - and be the hero she needs to be. Experienced in\n"
          "surviving in harsh conditions and poverty, her strength, quick wit\n"
          "and intellect will be of value to any venture.\n"
          "But uh, count your coins before you leave. Just in case.\n")
    print("\tSwashbuckler\n"
          "The Swashbuckler is a daring fighter; adept with rapier and tankard alike.\n"
          "So long as he's intoxicated, he is utterly fearless. With him, he carries\n"
          "a magic heirloom of times bygone - a flask that never dries up.\n"
          "Boisterous, bold, brave and boorish, he'll be an asset to the team.\n"
          "A drunk asset.\n")
    print("\tHunter\n"
          "The Hunter is a quiet figure, a solemn man who will accept any\n"
          "task or duty, usually never without comment. While he can\n"
          "skin a wild animal in minutes, he is a master of using the bow.\n"
          "Of course, he is also an expert at tracking and survival skills.\n")


def menu_print_magic():
    print("\tOracle\n"
          "The Oracle is a mystical figure, who often speaks in riddles.\n"
          "Despite occasional allusions to other-worldly guidance and\n"
          "an annoying tendency to proclaim 'so it was foretold' and the like,\n"
          "the Oracle is a formidable magician who can use ethereal power and\n"
          "supernatural insights to incredible effect.\n")
    print("\tWizard\n"
          "Wizards are mages who have trained their power since birth.\n"
          "With decades of study, wizards become powerful arch-mages,\n"
          "able to create tempests, banish demons, create illusions...\n"
          "Unfortunately, your wizard isn't as skilled. But at least\n"
          "he succeeded (and survived) his apprentice trials!\n")
    print("\tWarlock\n"
          "Warlocks gain their magical power through questionable, often heretical,\n"
          "means. But dabbling in forbidden arts has it's benefits. Maybe not dental\n"
          "plans, but unnatural lifespans, secrets whispered by demons, cosmic\n"
          "understanding and the ability to conjure pillars of fire that burns green\n"
          "with the barely-understood potency of lower planes of existence.\n"
          "Your warlock is a little bit ways off from that, but he knows how\n"
          "to summon lesser demons to his bidding, at least.\n")


class Player:
    def __init__(self, name, player_class):
        self.name = name  # The name of every player character.
        self.player_class = player_class  # Player_class determines player_class_type.
        # Game is built around this second type, which determines if your selected player auto wins or fails
        # Whatever scene they attempt to overcome. If they're not on the auto_fail or auto_succeed list,
        # It's a 50/50 to succeed.
        if self.player_class is "Blademaster":
            print("martial:", self.player_class)
            self.player_class_type = "martial"

        elif self.player_class is "Guardian":
            print("martial:", self.player_class)
            self.player_class_type = "martial"

        elif self.player_class is "Barbarian":
            print("martial:", self.player_class)
            self.player_class_type = "martial"

        elif self.player_class is "Rogue":
            print("finesse:", self.player_class)
            self.player_class_type = "finesse"

        elif self.player_class is "Swashbuckler":
            print("finesse:", self.player_class)
            self.player_class_type = "finesse"

        elif self.player_class is "Hunter":
            print("finesse:", self.player_class)
            self.player_class_type = "finesse"

        elif self.player_class is "Oracle":
            print("magic:", self.player_class)
            self.player_class_type = "magic"

        elif self.player_class is "Wizard":
            print("magic:", self.player_class)
            self.player_class_type = "magic"

        elif self.player_class is "Warlock":
            print("magic:", self.player_class)
            self.player_class_type = "magic"


class AdventureScene:
    def __init__(self, short_desc, long_desc, auto_fail, auto_succeed,
                 auto_fail_print, fail_print, success_print, special_success):
        self.short_desc = short_desc  # Brief desc of the encounter to be used after resolution
        self.long_desc = long_desc  # Long desc that appears when first encountering the scene
        self.auto_fail = auto_fail  # Determines which class type auto fails the challenge
        self.auto_succeed = auto_succeed  # Determines which class type auto succeeds the challenge
        self.auto_fail_print = auto_fail_print  # Output for classes that auto fail
        self.fail_print = fail_print   # Output for when a player fails
        self.success_print = success_print   # Output for when a player succeeds
        self.special_success = special_success   # Output if there's a special scene for your class

    def attempt(self, active_character):  # The attempt function that checks for success.
        print(active_character.name, "the", active_character.player_class, "steps forth.\n")
        if self.auto_fail == active_character.player_class_type:  # If your class type auto fails.. well, tough luck.
            print(self.auto_fail_print)
            print(active_character.name, "has died!")
            party_roster.remove(active_character)  # Removes dead player from the party roster.
        elif self.auto_succeed == active_character.player_class_type:
            special_success = False  # Var to check if player gets a unique print based on class instead of generic
            for special_success_class in self.special_success:
                if special_success_class == active_character.player_class: 
                    # If there is a unique print for active player's class, play that instead
                    print(self.special_success[special_success_class]) 
                    special_success = True
            if special_success is False:  # If the player didn't get a unique print, print generic success
                print(self.success_print)
        elif self.auto_fail != active_character.player_class_type:  # If you can't auto win or auto fail, randomize
            if self.auto_succeed != active_character.player_class_type:
                randomized_outcome = random.randrange(0, 100)
                if randomized_outcome >= 50:  # If fortune smiles, you win!
                    special_success = False
                    for special_success_class in self.special_success:
                        if special_success_class == active_character.player_class:
                            # same unique possible print as earlier, if you succeed
                            print(self.special_success[special_success_class])
                            special_success = True
                    if special_success is False:  # If the player didn't get a unique print, print generic success
                        print(self.success_print)

                elif randomized_outcome < 50:  # Bad luck kills you.
                    print(self.fail_print)
                    print(active_character.name, "has died!")
                    party_roster.remove(active_character)  # Removes dead player from the party roster.
            else:
                print("Attempt function ended in else #1! Should not happen!")
        else:
            print("Attempt function ended in else #2! Should not happen!")


############
# Basilisk #
############
# Long desc is printed when first arriving at a scene (that is, when it is first called)
basil_long_desc = "\nIn your search for the Tomb of Sucellus, your party travels over the steep hills," \
                     "\nnarrow canyons and mountainous terrain near the foothills of Mount Arkos." \
                     "\nIt is here, overlooking a narrow ravine, that your party simply must" \
                     "\ncross through - or risk weeks of delay - that you see the beast.\n" \
                     "\nA basilisk." \
                     "\nThese deadly creatures can turn any man into stone, or so the myths tell," \
                     "\nand fearful magi whisper of how the beast supposedly favours their flesh." \
                     "\nOne amongst your party must descend into the valley and face the beast.\n"
# Auto fail print is shown when player selects a class type that auto fails in the scene.
# In this case, Magic class types auto fail the Basilisk encounter.
basil_auto_fail_print = "Your mage hesitantly descends into the valley, and moves to face the beast." \
                        "\nYour mage begins to conjure a spell to strike at the creature" \
                        "\nbut with sudden vigour it surges forth, as the echo of it's hungry" \
                        "\nbelly reverberates throughout the valley. Your mage panics," \
                        "\nruns back and throws out a weak bolt of magic, but the beast" \
                        "\nignores it completely. Your party is helpless to watch as the beast" \
                        "\nrapidly closes the distance and consumes your poor mage. At least" \
                        "\nthe hunger of the beast appears to have been satiated."
# Fail print is shown when player selects a class type that might fail the scene - and does.
# Since there are three class types, and one must always succeed & one must always fail,
# This print is actually only shown for one class type (in this case, Finesse-types.
basil_fail_print = "Your chosen member moves forth to attack the beast, and begins an" \
                   "\nintricate side-stepping pattern, avoiding the blows of the great" \
                   "\nlumbering beast. A thrust, a stab, but the hide of the beast resists." \
                   "\nYour dashing trickster leaps back a step, to find a better angle to" \
                   "\nattack the creature from. And that is when eyes lock." \
                   "\nYou can do nothing but watch in fear as limbs lock up," \
                   "\nthe weapon clatters to the ground uselessly, and the basilisk descends" \
                   "\nto partake in it's favourite meal. At least the hunger of the" \
                   "\nbeast appears to be satiated..."
# Success print is shown when player selects any of the other two class types - either
# auto succeeding, or rollin' the dice and succeeding with luck.
basil_success_print = "Your chosen member moves forth to attack the beast, and begins an" \
                      "\nintricate side-stepping pattern, avoiding the blows of the great" \
                      "\nlumbering beast. A thrust, a stab, and the beast begins to bleed." \
                      "\nYour dashing trickster leaps back a step, to find a better angle to" \
                      "\nattack the creature from. The beast begins to frenzy, surging after," \
                      "\nand in a moment of heroism you watch as the blade flies forward." \
                      "\nSteel meets flesh, and the beast rolls over gurgling blood as" \
                      "\nthe weapon pierces the flesh in it's mouth, dying slowly." \
                      "\nA harrowing victory, but a victory nonetheless."
# Special success is a dictionary that shows special unique prints instead of the regular
# success prints, Not all classes have unique success prints.
basil_special_success = {"Barbarian": "With a mighty roar your barbarian leaps off the cliff"
                                      "\nand slams into the basilisk, the blade cutting deep."
                                      "\nIt thrashes, it heaves, but the beast is undone. ",
                         "Blademaster": "With solemn steps your Blademaster descends into the valley to face down"
                                        "\nthe basilisk. The blade sings through the air, and where your Blademaster"
                                        "\nhas dexterity, the reptilian creature has raw strength."
                                        "\nBut raw strength is not enough."
                                        "\nA duck, a spin, and then the blade hits exposed neck,"
                                        "\ncutting through the monstrosity - and it dies"
                                        "\nchoking on it's own blood. Your Blademaster bows,"
                                        "\nas reverently as if it was human foe, then sheathes"
                                        "\nthe blade and continues. ",
                         "Hunter": "Your hunter scoffs. This is not the first challenge such"
                                   "\nan experienced ranger has faced. Nocking an arrow, taking aim,"
                                   "\na whistling projectile of death sails into the valley,"
                                   "\npropelled by drawing strength and gravity. It flies true,"
                                   "\nstriking the beast in the eye, blinding it utterly."
                                   "\nA few calmly aimed sister-arrows finish the beast,"
                                   "\nall without a hint of danger to the expedition."}
# Adventure scene is created w. variables above
basilisk_below = AdventureScene("the Basilisk Below", basil_long_desc, "magic", "martial", basil_auto_fail_print,
                                basil_fail_print, basil_success_print, basil_special_success)
# This repeats for each scene
##########
# Forest #
##########
forest_long_desc = "You stand upon the threshold of the Forest of Mist." \
                   "\nThe forest is said to be infinite in size, and contain a thousand paths." \
                   "\nOnly those of exceptional cleverness could hope to navigate the forest," \
                   "\nFor it is said to hold a malevolent intelligence." \
                   "\nWho dares guide the party through?\n"
forest_auto_fail_print = "Though skilled in the arts of war, your chosen leader" \
                         "\nIsn't the most reliable when it comes to navigation" \
                         "\nthrough a haunted forest. The party is lost in a mist..." \
                         "\n\nThe party at last emerges, delayed and scattered, but intact -" \
                         "\nexcept for your chosen navigator, who is never seen again."
forest_fail_print = "Though skilled in the art of subtle movement and dexterous," \
                    "\nyour chosen leader, it turns out, isn't clever enough to" \
                    "\nnavigate a haunted forest. Your party is lost in a fog..." \
                    "\nThe group at last emerges, delayed and scattered, but intact -" \
                    "\nexcept for your chosen navigator, who is never seen again."
# Only rogue lacks special print. So, rogue gets the standard print since only they can acquire it.
forest_success_print = "Few would think a rogue would be skilled at navigating through a forest." \
                       "\nFewer still would trust their lives to a street urchin in guiding them" \
                       "\nthrough a forest haunted with dark spirits. Yet, for all the misgivings," \
                       "\nyour rogue has done the seemingly impossible. Whether it was her honed" \
                       "\nperception, keen mind or an innate danger-sense is a mystery your rogue" \
                       "\nis only too happy to play up. But she did it, and by the light of dawn" \
                       "\nyour party leaves the forest - all hands accounted for."
forest_special_success = {"Swashbuckler": "Only the gods know by what madness your Swashbuckler"
                                          "\nled your group through that dark and dismal forest."
                                          "\nThe others would whisper afterwards of his drunken"
                                          "\ntirade, of challenging a stygian black creature"
                                          "\nin the heart of night - and despite the blinding"
                                          "\ndark, felling it. Insanity, they say. Madness."
                                          "\nThese are the only traits such a drunken bravo brings"
                                          "\nto the table. And yet... yet he did the impossible.",
                          "Hunter": "Your hunter scoffs. A forest."
                                    "\nThis is standard fare. Ordering a hard march,"
                                    "\nYour hunter stays ahead a few paces at all times."
                                    "\nThough not the most congenial leader,"
                                    "\nyour hunter leads the party through in record time.",
                          "Oracle": "Your Oracle leads like a drunken reveler, stumbling"
                                    "\nthrough the forest in what seems like random"
                                    "\ndirections. Your party fears for their life,"
                                    "\nbut when the fogs clear your finds themselves"
                                    "\non the other side, safe and sound.",
                          "Wizard": "Your wizard takes a disturbingly long amount"
                                    "\nof time deciding on a direction every time the"
                                    "\nwoodlands offer diverging paths or the mists"
                                    "\nclear, but slowly, methodically, your party"
                                    "\nmoves forward. It may have taken half a day"
                                    "\nlonger than it should, but you're through,"
                                    "\nat least - and with every body accounted for.",
                          "Warlock": "Your warlock, when designated leader,"
                                     "\nimmediately orders a sacrifice. A pack animal,"
                                     "\nnot a party member, he clarifies. Away from"
                                     "\nthe group, he invokes the power of his patron"
                                     "\nfrom spheres away from this earth. Darkness"
                                     "\nlankets the area, and torches are snuffed out."
                                     "\nWhen light returns, a trail of blood leads"
                                     "\ninto the forest. Your warlock confidently"
                                     "\nleads the party to follow it to the other side."}
forest_of_mist = AdventureScene("the Forest of Mists", forest_long_desc, "martial", "magic", forest_auto_fail_print,
                                forest_fail_print, forest_success_print, forest_special_success)
##########
# Bridge #
##########
bridge_long_desc = "\nYou reach the Bridge of Doom." \
                   "\nThe ancient bridgekeeper is said to possess wisdom beyond ages," \
                   "\nAnd can separate any lie from truth. Those who lie to him cannot cross." \
                   "\nWho will parley with him for passage?\n"
bridge_auto_fail_print = "Your hero steps forth. The bridgekeeper calls out:" \
                         "\n\"WHAT... is your favorite colour?\"" \
                         "\n\"Red- no wait, oran- AAIIIIiiiii.....\"" \
                         "\nWith a horrific scream, an invisible force" \
                         "\nHurls your hero over the side of the bridge to disappear" \
                         "\ninto the fog below. The bridgekeeper cackles, and with a 'puf'" \
                         "\ninto the thin air. Warily, your party crosses the bridge."
bridge_fail_print = "Your hero steps forth. The bridgekeeper calls out:" \
                    "\n\"WHAT... is your favorite colour?\"" \
                    "\n\"Red- no wait, oran- AAIIIIiiiii.....\"" \
                    "\nWith a horrific scream, an invisible force" \
                    "\nHurls your hero over the side of the bridge to disappear" \
                    "\ninto the fog below. The bridgekeeper cackles, and with a 'puf'" \
                    "\ninto the thin air. Warily, your party crosses the bridge."
bridge_success_print = "Your hero steps forth. The bridgekeeper calls out:" \
                       "\n\"WHAT... is the air speed velocity of an unladen swallow?\"" \
                       "\n\"What do you mean, 'an unladen swallow'? An african," \
                       "\n\"or a european swallow?\" Your hero retorts." \
                       "\n\"I.. i... I don't know- AAAAIIIiiiiii......" \
                       "\nWith a horrific scream, an invisible force" \
                       "\nHurls the bridgekeeper over the side of the bridge" \
                       "\ninto the fog below. Relieved, your party crosses the bridge."
bridge_special_success = {"Rogue": "Your rogue moves up to talk to the bridgekeeper,"
                                   "\nspeaking with him in low tones. They seem to argue,"
                                   "\nbefore your rogue produces a small jingling pouch"
                                   "\nfrom a pocket somewhere in her armor."
                                   "\nThe bridgekeeper weighs it in his hand, then"
                                   "\ndisappears in a puff of smoke."
                                   "\nRelieved, your party crosses, only later"
                                   "\ndiscovering that everyone is light of a few coins.",
                          "Warlock": "Your warlock rushes forward.\"Hey, Tim - Tim!\""
                                     "The two shake hands, obviously friends from some"
                                     "time past, and begin discussing the merits"
                                     "and difficulties of demonic summoning."
                                     "Waving your party to cross while he continues"
                                     "speaking to the bridgekeeper, he catches up"
                                     "to the party a few minutes later on the other side."}
bridge_of_doom = AdventureScene("the Bridge of Doom", bridge_long_desc, "martial", "magic", bridge_auto_fail_print,
                                bridge_fail_print, bridge_success_print, bridge_special_success)
########
# Gate #
########
gate_long_desc = "\nYou reach the Gate of Adamant." \
                 "\nThe gate bars the passage in a narrow valley, the only" \
                 "\npassage for miles around. The gate is a silvery sheen," \
                 "\nand the fifteen-foot tall double doors have no handles," \
                 "\nno keyhole, no features... except for a single purple" \
                 "\nrune that glows dimly in the very center." \
                 "\nWho will try to get your party through it?\n"
gate_auto_fail_print = "Cracking their knuckles, your leader steps forth to try" \
                       "\nto open the gate. With no lock to pick, no mechanism to" \
                       "\nseemingly trigger, your hero elects to simply try to push" \
                       "\nit open. That, it turns out, was a bad idea." \
                       "\nLightning discharges from the purple seal, sending a thunderbolt" \
                       "\ndown on the poor chap. The purple symbol fizzles," \
                       "\nsparks fly, and with a thunderclap it is gone." \
                       "\nThe survivors, pushing the charred body to the side," \
                       "\neasily open the gate."
gate_fail_print = "Cracking their knuckles, your leader steps forth to try" \
                  "\nto open the gate. Your hero elects to simply test it first," \
                  "\nsmacking it with the blade. That, it turns out, was a bad idea." \
                  "\nLightning discharges from the purple seal, sending a thunderbolt" \
                  "\ndown on the poor chap. The purple symbol fizzles," \
                  "\nsparks fly, and with a thunderclap it is gone." \
                  "\nThe survivors, pushing the charred body to the side," \
                  "\neasily open the gate."
gate_success_print = "Your leader steps forth, cracking knuckles to test the gate." \
                     "\nNot seeing any obvious means of entry, your clever hero decides" \
                     "\nto pick up a rock and throw it at the sigil. This, it turns out," \
                     "\nwas actually a good idea. Lightning discharges from the seal," \
                     "\ncoursing through the rock and partially melting it." \
                     "\nThe purple symbol fizzles, sparks fly, and with a thunderclap" \
                     "\nit is gone. Your leader leverages the gate open and" \
                     "\nyour party continues into the valley beyond."
gate_special_success = {"Hunter": "Your hunter shrugs, and doing what he does best,"
                                  "\nfires an arrow at the door. This, it turns out,"
                                  "\nwas actually a good idea. Lightning discharges from the seal,"
                                  "\ncoursing through the rock and partially melting it."
                                  "\nThe purple symbol fizzles, sparks fly, and with a thunderclap"
                                  "\nit is gone. Your hunter pushes the gate open,"
                                  "\nand your party continues.",
                        "Wizard": "Your wizard steps forward with unexpected glee."
                                  "\n\"Ho-hum, if this isn't a curiosity!\" He exclaims."
                                  "\n\"I believe it was.. Mmyes, Beleannar, the Scholar,"
                                  "\nwho wrote of this\", he says, stroking his beard"
                                  "\nand examining the gate. \"A simple gesture will do it\","
                                  "\nhe vows, and incants a spell. An ethereal key manifests"
                                  "\nbefore him in midair. After a moments pause, it begins to"
                                  "\nlevitate up into the air towards the seal. When it connects,"
                                  "\nthere is a clap of thunder, a discharge of lightning from"
                                  "\nthe sigil - and then both key and arcane seal is gone."
                                  "\nYour wizard dusts off his hands and, with surprising ease,"
                                  "\npushes open the gate, and your party continues."}
sealed_gate = AdventureScene("the Sealed Gate", gate_long_desc, "finesse", "magic", gate_auto_fail_print,
                             gate_fail_print, gate_success_print, gate_special_success)
###############
# Haunted Fen #
###############
fen_long_desc = "\nYou reach the Fen of Ghosts." \
                "\nThe swampy morass is said to hold ten thousand dead from a battle eons ago." \
                "\nFearful wanderers whisper of ghosts that haunt it - and that" \
                "\nany who attempts to cross draws their ire. They will surely" \
                "\nattempt to trick your party down into the boggy waters." \
                "\nWho will guide the party through the haunted mire?\n"
fen_auto_fail_print = "Your leader guides the party forward, avoiding the sinking" \
                      "\ndepths of the mire. But though fearless and skilled with" \
                      "\nblade, your leader isn't the best at.. resisting temptation." \
                      "\nIn a moment of fatigue, your leader spots something - a person," \
                      "\nstruggling in the water. A fair girl, crying out for help." \
                      "\nImmediately diving to aid her, despite the outcries from the" \
                      "\nthe rest of the party, your leader disappears beneath the waves." \
                      "\nOnly a burst of bubbles and blood surfaces." \
                      "\nStill, your party continues, and hours later, exhausted," \
                      "\nreach the far side, safe from the ghosts of the fen."
fen_fail_print = "You begin making your way through the marshy and haunted fen," \
                 "\nMagic leading the way to shield you against the horrors that may" \
                 "\nlurk beneath. Then - there! - your party spots it: a young girl," \
                 "\ncrying out for help, struggling not to sink into the depths." \
                 "\nImmediately, your leader unleashes a bolt of eldritch energy" \
                 "\nthat soars against the girl. With a flash of light, it is revealed -" \
                 "\na rotting horror, that screams and disappears beneath the waves!" \
                 "\nYour party begins moving forward again before a shout comes to your" \
                 "\nattention - in the chaos, it appears one of your pack animals is now" \
                 "\ntrapped, beginning to sink! Your leader hastes forward to aid the struggling" \
                 "\nbeast... and that is when your party discovers, it too was a ruse." \
                 "\nit was a mere illusion. With barely any time to shout in alarm, your" \
                 "\nleader is dragged beneath the waves, never to emerge." \
                 "\nFortunately, the spirits of the bog seem pleased with this offering," \
                 "\nfor the rest of the party escapes the haunted fen without further incidents."
fen_success_print = "Your chosen man begins to lead the way. In the haunted mire," \
                    "\nintellect and cold reason holds stronger sway than bravery and" \
                    "\nsheer boldness. Then, in the distance, a scream - a woman calls out." \
                    "\nA form struggling against the swampwater. With methodical calmness," \
                    "\nyour leader orders the group to ignore it. A phantom, that is all." \
                    "\nWith a horrific shrief of frustration, the woman shapeshifts into" \
                    "\nsome unnatural rotting monstrosity, glares at your party, then descends" \
                    "\ninto the dark waters. It is never seen again, and your party reaches" \
                    "\nthe far side safe and sound."
fen_special_success = {"Rogue": "An unlikely candidate, some would claim. A pickpocket"
                                "\nshould lead your party through a haunted swamp? Madness."
                                "\nYet, whether it be madness or intuitive thinking, it works."
                                "\nEars pricked and eyes constantly scanning the horizon,"
                                "\nYour rogue is the first to react when your party hears a voice cry out."
                                "\nA woman, struggling in the swamp for help..."
                                "\nBut a woman no more, once the rogue's thrown dagger finds it's mark."
                                "\nThe once-woman thrashes, screams, then casts off it's illusion"
                                "\nto reveal a horrific visage.. one that glares daggers at your rogue,"
                                "\nbefore sinking into the waves to wait for easier prey."
                                "\nNothing further troubles your party in the crossing over the Fen.",
                       "Hunter": "Your hunter confidently leads your group through"
                                 "\nthe swampy mire. Though he is only truly at home"
                                 "\nin forests, he says, this is close enough.\n"
                                 "\nThen, the alluring siren call sings out. A young girl,"
                                 "\ncrying out for help, struggling in the mire. Your"
                                 "\nparty pauses, uncertain if this is a mirage or real,"
                                 "\nbut your hunter calmly draws an arrow from his quiver,"
                                 "\ntakes aim, and fires. The cry turns to a raging howl,"
                                 "\nan eldrich scream, and the once-girl, now a rotting corpse,"
                                 "\nsinks back into the mire. The party continues, escaping"
                                 "\nthe fen without any more obstacles.",
                       "Oracle": "The oracle contemplates for several minutes, seated cross-legged"
                                 "\nin the mud and dirt in the fen. When the party begins to grow angry"
                                 "\nwith boredom, he perks up his head. Wordlessly, he begins leading"
                                 "\nthe way forward. Your party can only shrug and follow his guidance."
                                 "\nWell it is that they did, for despite misgivings, his path is a safe"
                                 "\none that seems to avoid any troubles or haunts. Once, the party hears"
                                 "\na distant scream and something in the fog-shrouded horizon, but your Oracle"
                                 "\nno attention it. Hours later, your party emerges from the fen - soaked"
                                 "\nfrom the strange path, but hearts and mind at ease from the safe passage."}
fen_of_ghosts = AdventureScene("the Fen of Ghosts", fen_long_desc, "martial", "finesse", fen_auto_fail_print,
                               fen_fail_print, fen_success_print, fen_special_success)
########
# Lake #
########
lake_long_desc = "\nYou come to the Lake of Caerbannog." \
                 "\nThe lake is placid and calm, and a gentle breeze blows from across it." \
                 "\nThe ground around the lake is soft ankle-high grass, and" \
                 "\nyou see no creatures around save for a small rabbit." \
                 "\nBy the lake's shore, there is a small boat moored." \
                 "\nIt looks placid enough... but tales tell of sea serpents beneath." \
                 "\nWho will guide the party across the lake?" \
                 "\n"
lake_auto_fail_print = "As anticipated, serpents from beneath the waves strike" \
                       "when your party least expects it, though all are high-strung." \
                       "Your group fights, staunchly opposing the foe, but it's too much." \
                       "They're too many. With a scream, your leader is pulled from the boat," \
                       "to go overboard. Only a burst of bubbles and a pool of blood emerges." \
                       "The feast appears to satiate the beasts, for the rest crosses safely."
lake_fail_print = lake_auto_fail_print  # Auto fail & normal fail are similar enough.
lake_success_print = "As expected, serpents from beneath the waves strike when your party" \
                     "\nleast anticipates it. Your group fights the enraged serpents, " \
                     "\nbut it's too much. They're too many.\n" \
                     "\nThen, your leader roars. With a heroic thrust, one of the serpents is" \
                     "\npierced, then two more lose their heads. The rest hiss and roar," \
                     "\nbut, frightened of this display, pull back. They sink back beneath the waves." \
                     "\nDark shapes continue to swim beneath the boat in the dark waters," \
                     "\nbut they do not emerge again. Your party emerges on the far side -" \
                     "\na few wounds and nicks, but all alive."
lake_special_success = {"Oracle": "As anticipated, serpents from beneath the waves strike"
                                  "\nwhen your party least expects it, though all are high-strung."
                                  "\nYour party begins a furious fight for their very lives,"
                                  "\nwhen the Oracle rises from his seat and speaks."
                                  "\nIn words no human tongue should be able to speak,"
                                  "\nwith authority and a tone beyond what he should be able"
                                  "\nto produce, the Oracle speaks to the beasts in a deep"
                                  "\nand rumbling voice. The serpents recoil, and despite"
                                  "\ntheir reptilian faces, fear is manifest. They dive"
                                  "\nbeneath the surface, and do not show themselves again."
                                  "\nYour Oracle shakes his head, as though clearing his head,"
                                  "\nand has no recollection of the event. Your party"
                                  "\ncrosses to the far side in uneasy relief.",
                        "Wizard": "As anticipated, serpents from beneath the waves strike"
                                  "\nwhen your party least expects it, though all are high-strung."
                                  "\nYour party begins to fight them off, when from a sleeve, "
                                  "\nhe produces a scroll. He begins to chant arcane words as the "
                                  "\nglyphs on the scroll disintegrate before your party's very eyes,"
                                  "\nbut it works.\n"
                                  "\nSome manner of incandescent sphere manifests around the boat,"
                                  "\nand the thrashing serpents fail to strike through it. Catiously,"
                                  "\nyour party begins to row again, under the protection of the bubble."
                                  "\nOnly a scant few feet from the shore, the bubble disperses, and your"
                                  "\nparty rushes onto the far side - just in time to avoid the wrothful"
                                  "\nserpents attack the boat, sinking it in moments."
                                  "\nYour wizard shrugs off thanks, and cautions that he has no more"
                                  "\nscrollls of such kind hidden elsewhere.",
                        "Warlock": "As anticipated, serpents from beneath the waves strike"
                                   "\nwhen your party least expects it, though all are high-strung."
                                   "\nYour warlock immediately leaps up to stand in the boat, and,"
                                   "\nbrandishing a polished skull kept somewhere in his robes,"
                                   "\nholds it up and speaks words in a language none other"
                                   "\ncomprehend - one disturbingly nonhuman, that should"
                                   "\nbe impossible for a mammalian vocal cord to replicate."
                                   "\nYet, it works. The serpents sway in the water, then,"
                                   "\nslowly, descends. Their dark shapes continue to swim"
                                   "\nbeneath the boat for the rest of the crossing, but they"
                                   "\ndo not emerge again."}
lake_of_caerbannog = AdventureScene("the Lake of Caerbannog", lake_long_desc, "finesse", "magic", lake_auto_fail_print,
                                    lake_fail_print, lake_success_print, lake_special_success)
##############
# Cockatrice #
##############
trice_long_desc = "\nYou encounter a cockatrice, feasting on the flesh of a merchant and his steed." \
                  "\nA horrible amalgamation of many different creatures," \
                  "\nonly those of incredible fortitude and willpower" \
                  "\ncould hope to not be petrified by their stare." \
                  "\nWith luck, magic may slay the beast." \
                  "\nWho will challenge the monster?"
trice_auto_fail_print = "Your dexterous fighter challenges the cockatrice...\n" \
                        "\nBut this proves to be unwise. It rears back, and your" \
                        "\nhero is caught in it's stare. Fortunately, the cockatrice" \
                        "\nnow has a new meal to preoccupy itself with, and the" \
                        "\nrest of your party stealthily slinks past it while" \
                        "\nit is busy feeding."
trice_fail_print = "Your mage fails to account for it's terrific speed, and is\n" \
                   "helpless when it stares him down, petrifying him." \
                   "Fortunately, the beast is preoccupied with now consuming\n" \
                   "it's quarry, and your party stealthily bypass it."
trice_success_print = "Your mage contemplates the obstacle before him, before deciding" \
                      "\non a swift resolution. Conjuring a bolt of ethereal energy, he" \
                      "\nsends it streaking towards the beast, which recoils in anger and pain." \
                      "\nBut it is not dead. It roars, paces forward, but glares at your mage" \
                      "\nand the rest of the party behind him. With uncanny intellect, it roars" \
                      "\nagain, and then begin to slowly back away from the challenge." \
                      "\nIt does not return to harry you again."
trice_special_success = {"Blademaster": "Your Blademaster moves in to strike it with"
                                        "\nblinding speed, and it shrieks in pain and fury"
                                        "\nwhen his blade makes contact - but it is not dead."
                                        "\nAngrily, it hisses and rears back to petrify your"
                                        "\nchampion... when he averts his gaze and brings up his"
                                        "\nshimmering blade in parry. The beast, catching sight"
                                        "\nof itself, shrieks in alarm - before it falls prey"
                                        "\nto it's own power. With contempt, your Blademaster"
                                        "\npushes over the petrified cockatrice to shatter"
                                        "\ninto a thousand pieces.",
                         "Barbarian": "With sudden alacrity and eagerness for the challenge,"
                                      "\nyour barbarian howls and rushes into the fray. The beast,"
                                      "\nalerted by his loud screaming, readies and attacks in turn."
                                      "\nThe two trade blows, each suffering minor grazing injuries,"
                                      "\nbefore your barbarian is caught in it's stare. Muscles lock up,"
                                      "\nhe grows perfectly still, and the cockatrice's bloody beak descends.\n"
                                      "\nJust as planned. He snaps out of the feigned paralyzation,"
                                      "\nand with a mighty hew sends the cockatrice's head flying ten feet.",
                         "Guardian": "\nYour Guardian advances slowly towards the beast, her"
                                     "\nheavy armor and shield making it impossible to catch it off-guard."
                                     "\nThe beast surges forward, but your Guardian brings up her shield,"
                                     "\npummeling the beast in the beak with the shield. Undaunted, it"
                                     "\nattacks again, but a thrust with her short sword into it's gully"
                                     "\nmakes it reconsider the approach. It rears back, and attempts to"
                                     "\ntransfix your guardian with it's stare... But she merely raises"
                                     "\nher shield - tricking it into gazing into it's own reflection"
                                     "\nin the polished shield. With a final shriek, it begins to lock up"
                                     "\nand slowly turn into stone."}
cockatrice = AdventureScene("the Rampaging Cockatrice", trice_long_desc, "finesse", "martial", trice_auto_fail_print,
                            trice_fail_print, trice_success_print, trice_special_success)


def choose_active_character(char_list):  # Function for user to select which character
    # That should attempt to succeed in the scene
    player_list = 0  # Iteration for list of players
    print("\t" + "Characters")
    while True:
        try:
            for char in char_list:  # Prints a list of all characters (still alive)
                print(str(player_list+1) + ".", char.name + ", the", char.player_class)
                player_list += 1  # Increment counter, so you get a neat numbering
            chosen_character = int(input("Choose your dood: ")) - 1
            if chosen_character >= len(char_list):  # If user tries to input number out of index, force a new input
                print("That character doesn't exist. Try a lower number.\n")
                continue
            if chosen_character < 0:  # Prevents user from inputting 0 or negative numbers
                print("Try selecting an actual character.")
                continue
            else:  # Only if player correctly selects a char does loop break
                break
        except ValueError or TypeError:  # Except to handle value or type errors
            print("That's not a number. Try again.\n")
            continue
    active_character = char_list[chosen_character]  # active_character becomes a
    # Player type variable - the character the player chose.
    return active_character


def check_player_number():  # Simple function called after every resolved attempt checking if the player's group dies.
    global party_survived
    if len(party_roster) < 1:
        print("Your party has succumbed to the dangers in the wilds."
              "The lands of Erebus are not for the feint of heart,"
              "or weak of will or strength. Or perhaps Fate or Lady Luck"
              "merely decreed that today was not your day, for here"
              "ends the tale of", party_name + ".")
        party_survived = False
    else:
        party_survived = True


def game_start():

    party_number = 0  # Total party number
    created_players = 0  # Variable to loop through number of player characters created
    while party_number <= 0 or party_number > 12:  # Requires between 1 and 12 members
        try:
            print("How many players do you want to have? You can have between 1 and 12.")
            print("While there is no direct downside to having as many as possible,")
            print("know that it might be hard to keep them all alive.")
            party_number = int(input("How many players do you want to have? (1-12)\n"))
            if party_number > 12:  # If too many, runs again to force user to input a lower number
                print(party_number, "people is a little too many to go on a quest.\nTry a lower number.\n")
                continue
            if party_number < 4:  # Warning that you'll probably lose some members.
                print("Only", str(party_number) + "? It will be a deadly quest. Are you sure? (N to cancel)")
                confirm = input().lower()
                if confirm == "n":
                    print("Let's select another number then.\n")
                    party_number = 0  # Resets party number so user stays in loop
                    continue
                # No elif or else since only a N/n is taken as a retry
        except ValueError or TypeError:  # Except to handle value or type errors
            print("That's not a number. Try again.\n")
            continue

    print("Very well, then.\n" + str(party_number), "members will set forth then on the quest.")
    global party_name
    party_name = input("What shall be the name of this band of fellows?\n").capitalize()  # Any good party needs a name!
    global party_roster
    party_roster = []
    # party_roster is the list of those in the party. The list will contain each instance of a Player class.

    # These are the classes the user can choose for each player character.
    # They have three different

    while created_players < party_number:  # For every created player, loops through name & class selection
        new_name = input(
            "Player " + str(created_players + 1) + ":\nWhat is your name?")  # User selects each chars' name
        if new_name is "":  # Should the user decide to not input a name, it will loop until they do so.
            print("That's not a name. Try again.")
            continue
        new_name = new_name.capitalize()  # To make it a little bit more neat.

        new_player_class = 0  # Initializing new_player_class. This is not required at all, except
        # PyCharm thought there was a chance one could get past the loop beneath without declaring it.
        # it is only declared for formality's sake.

        print("Player", new_name + ", you must also have a class.")
        selected_class = False
        while selected_class is False:
            try:
                for i in range(len(class_choices)):
                    print(i + 1, "-", class_choices[i])
                new_player_class = int(input("And what will be your class?")) - 1  # -1 because first class is index 0
                if new_player_class >= len(class_choices):  # If user tries to go out of index
                    print("That's no class. Try again.")
                    print()
                    continue
                elif new_player_class < 0:  # If user inputs number too low
                    print("Try a higher number..")
                    print()
                    continue
                else:  # If the user (finally) inputs a correct number, loop breaks (for current player) and moves on
                    print(new_name, "has become a", class_choices[new_player_class] + ".")
                    break
            except ValueError:  # if user decides to input something that isn't a number.
                print("Digits only.\nTry again.")
                continue

        party_roster.append(new_name)  # Adds the newly created character's name to the roster.
        index = created_players
        created_players += 1
        party_roster[index] = Player(new_name, class_choices[new_player_class])
        # Creates a new instance of the Player class in the party_roster list.
        # This means party_roster contains a list of all the Player class instances!
        print("Welcome", new_name + ".")
        print()

    welcome_text = "WELCOME, "
    welcome_num = 0
    for index in party_roster:
        welcome_text += index.name
        welcome_text += ", "
        welcome_num += 1
    welcome_text += "\nCompanions of the group "
    welcome_text += party_name
    welcome_text += "!"
    print(welcome_text)

    print()
    print("For centuries, the land of Erebus have known strife.\n"
          "Ever since the ice receded and civilizations began to rise up again,\n"
          "nations and civilizations have struggled against each other to come out\n"
          "on top of a world that knows only brutality, violence and barbarism.\n")
    print("In these tumultuous times, great wealth is made and lost.\n"
          "War is, after all, hugely profitable to those who do not experience it.\n"
          "Now,", party_name, "has been given a quest by one of the fledgling nations:\n"
          "Find the Tomb of Sucellus, and the priceless artifact within, so the nation\n"
          "will not perish into ruin as so many others have before the onslaught\n"
          "of the wild hordes of Orcus, the self-proclaimed King of Barbarians.\n")
    print("If you succeed, you will gain loot and rewards beyond your wildest dreams.\n")
    print("If you fail...")
    print("Chaos will know no end, and mankind may perhaps never rise beyond.")
    print("\n" * 2)

    print(party_name, "sets out from the capitol. After a journey of several days,\n"
                      "they come before their first obstacle.\n")

    random_scene1 = random.randrange(0, len(AdventureScenesList))  # A scene is randomly picked
    # from the possible scenes contained in the list of adventure scenes
    print(AdventureScenesList[random_scene1].long_desc)  # First prints the long intro text
    active_character = choose_active_character(party_roster)  # User must select active character
    AdventureScenesList[random_scene1].attempt(active_character)   # active character attempts to succeed...

    check_player_number()
    if party_survived is True:
        print("With", AdventureScenesList[random_scene1].short_desc, "behind you, your journey continues.")
        print()

        # Scene number 2. The same happens as above.
        random_scene2 = random.randrange(0, len(AdventureScenesList))
        while random_scene2 == random_scene1:  # Check to ensure you don't get the same scene again.
            random_scene2 = random.randrange(0, len(AdventureScenesList))
        print(AdventureScenesList[random_scene2].long_desc)
        active_character = choose_active_character(party_roster)
        AdventureScenesList[random_scene2].attempt(active_character)

        check_player_number()
        if party_survived is True:
            print("With", AdventureScenesList[random_scene2].short_desc, "behind you, your journey continues.")
            print()

            random_scene3 = random.randrange(0, len(AdventureScenesList))
            while random_scene3 == random_scene1 or random_scene3 == random_scene2:
                # Check extended to ensure you don't get any scenes already shown.
                random_scene3 = random.randrange(0, len(AdventureScenesList))
            print(AdventureScenesList[random_scene3].long_desc)
            active_character = choose_active_character(party_roster)
            AdventureScenesList[random_scene3].attempt(active_character)

            check_player_number()
            if party_survived is True:
                print("With", AdventureScenesList[random_scene3].short_desc, "behind you, your journey continues.")
                print()

                print("At long last, your party finally reach the Tomb of Sucellus.",
                      "\nOf the", created_players, "who set out,", len(party_roster),
                      "managed to make it to the Tomb.",
                      "\nBut now... they must enter the Tomb, and brave the dangers inside.\n"
                      "But what", party_name, "found within, is a tale for another time.")
                # Woo, you won!


# List of the scenes
AdventureScenesList = [basilisk_below, forest_of_mist, bridge_of_doom, sealed_gate,
                       fen_of_ghosts, lake_of_caerbannog, cockatrice]

# List of different classes, called whenever a new player is created
class_choices = ["Blademaster", "Guardian", "Barbarian",
                 "Rogue", "Swashbuckler", "Hunter",
                 "Oracle", "Wizard", "Warlock"]

menu_start()  # calls menu_start which starts the whole program
