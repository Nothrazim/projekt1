import random

print("This little game is a text-based adventure game, where you'll manage a\n"
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
          "Do not understimate him however -  despite the pelts and crude greatsword,\n"
          "the Barbarian is a seasoned veteran of harsh terrain and a dangerous life.\n")
    print("\tGuardian\n"
          "The Guardian is a master of fighting with sword and shield.\n"
          "The Guardian is driven to defend her allies, who stand resolute behind"
          "her shieldwall. Experienced and possessed of tremendous stamina,"
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
          "Despite occasional allusions to other-worldly guidance and \n"
          "an annoying tendency to proclaim 'so it was foretold' and the like,\n"
          "the Oracle is a formidable magician who can use ethereal power and\n"
          "supernatural insights to devastating effect.\n")
    print("\tWizard\n"
          "Wizards are mages who have trained their power since birth,\n")
    print("\tWarlock\n"
          "Warlocks gain their magical power through questionable, often heretical,\n"
          "pacts.\n")


class Player:
    def __init__(self, name, player_class):
        self.name = name
        self.player_class = player_class  # Player_class determines player_class_type.
        # Game is built around this second type, which determines if your selected player auto wins or fails
        # Whatever scene they attempt to overcome. IF they're not on the auto_fail or auto_succeed list,
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

    def attempt(self, active_character):
        print(active_character.name, "the", active_character.player_class, "steps forth.")
        if self.auto_fail == active_character.player_class_type:  # If your class type auto fails.. well, tough luck.
            print(self.auto_fail_print)
            print(active_character.name, "has died!")
            party_roster.remove(active_character)  # Removes dead player from the party roster.
        elif self.auto_succeed == active_character.player_class_type:
            special_success = False  # Var to check if player gets a unique print based on class instead of generic
            for special_success_class in self.special_success:
                if special_success_class == active_character.player_class:  # If there is a unique print for active
                    print(self.special_success[special_success_class])  # player's class, play that instead
                    special_success = True
            if special_success is False:  # If the player didn't get a unique print, print generic success
                print(self.success_print)
        elif self.auto_fail != active_character.player_class_type:  # If you can't auto win or auto fail, randomize
            if self.auto_succeed != active_character.player_class_type:
                randomized_outcome = random.randrange(0, 100)
                if randomized_outcome >= 50:  # If fortune smiles, you win!
                    special_success = False
                    for special_success_class in self.special_success:
                        if special_success_class == active_character.player_class:  # same unique possible print as
                            print(self.special_success[special_success_class])  # earlier, if you succeed
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


basil_long_desc = "\nIn your search for the Tomb of Sucellus, your party travels over the steep hills," \
                     "\nnarrow canyons and mountainous terrain near the foothills of Mount Arkos." \
                     "\nIt is here, overlooking a narrow ravine, that your party simply must" \
                     "\ncross through - or risk weeks of delay - that you see the beast." \
                     "\n" \
                     "\nA basilisk." \
                     "\nThese deadly creatures can turn any man into stone, or so the myths tell," \
                     "\nand fearful magi whisper of how the beast supposedly favours their flesh." \
                     "\nOne amongst your party must descend into the valley and face the beast." \
                     "\n"
basil_auto_fail_print = "Your mage hesitantly descends into the valley, and moves to face the beast." \
                        "\nYour mage begins to conjure a spell to strike at the creature" \
                        "\nbut with sudden vigour it surges forth, as the echo of it's hungry" \
                        "\nbelly reverberates throughout the valley. Your mage panics," \
                        "\nruns back and throws out a weak bolt of magic, but the beast" \
                        "\nignores it completely. Your party is helpless to watch as the beast" \
                        "\nrapidly closes the distance and consumes your poor mage. At least" \
                        "\nthe hunger of the beast appears to have been satiated."
basil_fail_print = "Your chosen member moves forth to attack the beast, and begins an" \
                   "\nintricate side-stepping pattern, avoiding the blows of the great" \
                   "\nlumbering beast. A thrust, a stab, but the hide of the beast resists." \
                   "\nYour dashing trickster leaps back a step, to find a better angle to" \
                   "\nattack the creature from. And that is when eyes lock." \
                   "\nYou can do nothing but watch in fear as limbs lock up," \
                   "\nthe weapon clatters to the ground uselessly, and the basilisk descends" \
                   "\nto partake in it's favourite meal. At least the hunger of the" \
                   "\nbeast appears to be satiated..."
basil_success_print = "Your chosen member moves forth to attack the beast, and begins an" \
                      "\nintricate side-stepping pattern, avoiding the blows of the great" \
                      "\nlumbering beast. A thrust, a stab, and the beast begins to bleed." \
                      "\nYour dashing trickster leaps back a step, to find a better angle to" \
                      "\nattack the creature from. The beast begins to frenzy, surging after," \
                      "\nand in a moment of heroism you watch as the blade flies forward." \
                      "\nSteel meets flesh, and the beast rolls over gurgling blood as" \
                      "\nthe weapon pierces the flesh in it's mouth, dying slowly." \
                      "\nA harrowing victory, but a victory nonetheless."
basil_special_success = {"Barbarian": "With a mighty roar your barbarian leaps off the cliff"
                                      "\nand slams into the basilisk, the blade cutting deep."
                                      "\nIt thrashes, it heaves, but the beast is undone. ",
                         "Blademaster": "With solemn steps your Blademaster descends into the valley to face down"
                                        "\nthe basilisk. The blade sings through the air, and where your Blademaster"
                                        "\nhas dexterity, the reptilian creature has raw strength."
                                        "\nBut strength is not enough."
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
basilisk_below = AdventureScene("the Basilisk Below", basil_long_desc, "magic", "martial", basil_auto_fail_print,
                                basil_fail_print, basil_success_print, basil_special_success)


forest_long_desc = "\nYou stand upon the threshold of the Forest of Mist." \
                   "\nThe forest is said to be infinite in size, and contain a thousand paths." \
                   "\nOnly those of exceptional cleverness could hope to navigate the forest," \
                   "\nFor it is said to hold a malevolent intelligence." \
                   "\nWho dares guide the party through?" \
                   "\n"
forest_auto_fail_print = "Your martial dude sucks at navigation."
forest_fail_print = "You get through the forest, but you lose the leader."
forest_success_print = "You navigate through the forest."
forest_special_success = {"Hunter": "Yeah, i know woods.",
                          "Oracle": "Trust the senses, the oracle says. Okay.",
                          "Wizard": "Yes, just like my books said.",
                          "Warlock": "KLAATU, BAATU, FOREST DEMON INVOCATION"}
forest_of_mist = AdventureScene("the Forest of Mists", forest_long_desc, "martial", "magic", forest_auto_fail_print,
                                forest_fail_print, forest_success_print, forest_special_success)


bridge_long_desc = "\nYou reach the Bridge of Doom." \
                   "\nThe ancient bridgekeeper is said to possess wisdom beyond ages," \
                   "\nAnd can separate any lie from truth. Those who lie to him cannot cross." \
                   "\nWho will parley with him for passage?" \
                   "\n"
bridge_auto_fail_print = "'What is your favorite colour?'\n'Red, no blue, no- AAAIIGGHH'."
bridge_fail_print = "What is the air speed velocity of a laden swallow? Don't know? Eat yo soul."
bridge_success_print = "The bridgekeeper lets you pass for a bribe."
bridge_special_success = {"Rogue": "I bribe the bridgkeeper.",
                          "Wizard": "Your wizard knows how to riddle diddle.",
                          "Warlock": "Is that Tim? Tim, from college? Hey buddy!"
                                     "Guys, go on ahead, i know Tim, we go way back!\n"}
bridge_of_doom = AdventureScene("the Bridge of Doom", bridge_long_desc, "martial", "magic", bridge_auto_fail_print,
                                bridge_fail_print, bridge_success_print, bridge_special_success)


gate_long_desc = "" \
                 "\nYou reach the Gate of Adamant." \
                 "\nIt is a gate. It looks strong." \
                 "\nWho will try to get through it?" \
                 "\n"
gate_auto_fail_print = "Your finesse guy is zapped by the gate."
gate_fail_print = "The gate zaps your martial man, but hey, it burnt out and opened."
gate_success_print = "Your martial or magic man opened the gate."
gate_special_success = {"Hunter": "Yeah, i know woods.",
                        "Oracle": "Trust the senses, the oracle says. Okay.",
                        "Wizard": "Yes, just like my books said.",
                        "Warlock": "KLAATU, BAATU, FOREST DEMON INVOCATION"}
gate_of_adamant = AdventureScene("the Gate of Adamant", gate_long_desc, "finesse", "magic", gate_auto_fail_print,
                                 gate_fail_print, gate_success_print, gate_special_success)

fen_long_desc = "" \
                "\nYou reach the Fen of Ghosts." \
                "\nThe swampy morass is said to hold ten thousand dead from a battle eons ago." \
                "\nWho will guide the party through the haunted mire?" \
                "\n"
fen_auto_fail_print = "Your martial guy does not know how to cross a fen."
fen_fail_print = "You lost your mage. But hey, you got through."
fen_success_print = "Your dextrous or magical man got you through."
fen_special_success = {"Hunter": "Yeah, i know bogs.",
                       "Oracle": "Trust the senses, the oracle says. Okay.",
                       "Wizard": "Yes, just like my books said.",
                       "Warlock": "KLAATU, BAATU, FOREST DEMON INVOCATION"}
fen_of_ghosts = AdventureScene("the Fen of Ghosts", fen_long_desc, "martial", "finesse", fen_auto_fail_print,
                               fen_fail_print, fen_success_print, fen_special_success)

lake_long_desc = "\nYou come to the Lake of Caerbannog." \
                 "\nThe lake is placid and calm, and a gentle breeze blows from across it." \
                 "\nThe ground around the lake is soft ankle-high grass, and" \
                 "\nyou see no creatures around save for a small rabbit." \
                 "\nBy the lake's shore, there is a small boat moored." \
                 "\nWho will guide the party across the lake?" \
                 "\n"
lake_auto_fail_print = "Your fighter is wholly unprepared to fight the seamonsters."
lake_fail_print = "Your lead man is eaten by a sea monster, but hey - at least you got over the lake!"
lake_success_print = "Your guy kills the lake monster."
lake_special_success = {"Hunter": "Using almost effortless skill, your hunter\n"
                                  "bullseyes the sea monster. Eel for supper tonight!",
                        "Oracle": "Trust the senses, the oracle says. Okay.",
                        "Wizard": "Yes, just like my books said.",
                        "Warlock": "KLAATU, BAATU, FOREST DEMON INVOCATION"}
lake_of_caerbannog = AdventureScene("the Lake of Caerbannog", lake_long_desc, "martial", "magic", lake_auto_fail_print,
                                    lake_fail_print, lake_success_print, lake_special_success)

trice_long_desc = "\nYou encounter a cockatrice, feasting on the flesh of a merchant and his steed." \
                   "\nOnly those of incredible fortitude and willpower" \
                   "\ncould hope to not be petrified by their stare." \
                   "\nWith luck, magic may slay the beast." \
                   "\nWho will challenge the monster?"
trice_auto_fail_print = "Your dextrous fighter is eaten by the cockatrice.\n" \
                        "Fortunately, the beast is preoccupied with now consuming\n" \
                        "it's quarry, and your party stealthily bypass it."
trice_fail_print = "Your mage fails to account for it's terrific speed, and is\n" \
                   "helpless when it stares him down, petrifying him." \
                   "Fortunately, the beast is preoccupied with now consuming\n" \
                   "it's quarry, and your party stealthily bypass it."
trice_success_print = "Your champion, unafraid of the beast, steps forth to destroy the beast."
trice_special_success = {"Hunter": "Your Hunter shoots it from afar. Why risk close proximity?",
                         "Oracle": "Your Oracle asks for divine inspiration and succeeds",
                         "Wizard": "\"Yes, a fireball will do just fine here\",\n"
                                   "proclaims your wizard. A fireball he creates, and the beast is dead.",
                         "Warlock": "Your warlock conjures ethereal entities, which attack\n"
                                    "and consume the surprised cockatrice."}
cockatrice = AdventureScene("the Rampaging Cockatrice", trice_long_desc, "finesse", "martial", trice_auto_fail_print,
                            trice_fail_print, trice_success_print, trice_special_success)


def choose_active_character(char_list):
    player_list = 0
    print("\n" + "characters")
    while True:
        try:
            for char in char_list:
                print(str(player_list+1) + ".", char.name + ", the", char.player_class)
                player_list += 1
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
    active_character = char_list[chosen_character]
    return active_character


def game_start():
    print("bla bla bla, intro text")

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
                    print("Below 0. Try again.")
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
          "will not perish into ruin as so many others have before the onslaught"
          "of the wild hordes of Orcus, the self-proclaimed King of Barbarians.\n")
    print("If you succeed, you will gain loot and rewards beyond your wildest dreams.\n")
    print("If you fail...")
    print("chaos will know no end, and mankind may perhaps never rise beyond.")

    print("\n" * 3)

    print(party_name, "set out from the capitol. After a journey of several days,"
                      "they come before their first obstacle.")

    print(forest_long_desc)
    active_character = choose_active_character(party_roster)
    forest_of_mist.attempt(active_character)
    print("With", forest_of_mist.short_desc, "behind you, your journey continues.")
    print()

    random_scene1 = random.randrange(0, len(AdventureScenesList))
    print(AdventureScenesList[random_scene1].long_desc)
    active_character = choose_active_character(party_roster)
    AdventureScenesList[random_scene1].attempt(active_character)
    print("With", AdventureScenesList[random_scene1].short_desc, "behind you, your journey continues.")
    print()

    """
    random_scene2 = random.randrange(0, len(AdventureScenesList))
    while random_scene2 == random_scene1:
        random_scene2 = random.randrange(0, len(AdventureScenesList))
    print(AdventureScenesList[random_scene2].long_desc)
    active_character = choose_active_character(party_roster)
    AdventureScenesList[random_scene2].attempt(active_character)
    print("With", AdventureScenesList[random_scene2].short_desc, "behind you, your journey continues.")
    print()

    random_scene3 = random.randrange(0, len(AdventureScenesList))
    while random_scene3 == random_scene1 or random_scene3 == random_scene2:
        random_scene3 = random.randrange(0, len(AdventureScenesList))
    print(AdventureScenesList[random_scene3].long_desc)
    active_character = choose_active_character(party_roster)
    AdventureScenesList[random_scene3].attempt(active_character)
    print("With", AdventureScenesList[random_scene3].short_desc, "behind you, your journey continues.")
    print()
    """
    print("You reach the Tomb of Sucellus.")
    print(len(party_roster), "of the original", created_players, "have succeeded in reaching the Tomb.")


AdventureScenesList = [basilisk_below, forest_of_mist, bridge_of_doom]
# AdventureScenesList += [gate_of_adamant, fen_of_ghosts, lake_of_caerbannog, cockatrice]

class_choices = ["Blademaster", "Guardian", "Barbarian"]
class_choices += ["Rogue", "Swashbuckler", "Hunter"]  # Split up only because the list is so long
class_choices += ["Oracle", "Wizard", "Warlock"]

menu_start()

"""
"""