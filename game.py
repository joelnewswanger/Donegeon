from random import randint


class Weapon(object):
    def __init__(self, iname, high, low):
        self.name = iname
        self.high = high
        self.low = low


class Armor(object):
    def __init__(self, iname, defence):
        self.name = iname
        self.defence = defence


class Sheild(object):
    def __init__(self, iname, defence):
        self.name = iname
        self.defence = defence


class Food(object):
    def __init__(self, iname, nourish):
        self.name = iname
        self.nourish = nourish


adjective_list = (
    "modern", "truthful", "chunky", "best", "breezy", "guarded", "abusive", "idiotic", "wretched", "abject", "ugly",
    "spiritual", "kindhearted", "iron", "joyous", "ruthless", "scared", "lamentable", "closed", "well-to-do",
    "knowing", "rampant", "legal", "coherent", "scintillating", "righteous", "toothsome", "spotted", "delirious",
    "bashful", "happy", "curved", "wiggly", "stereotyped", "festive", "wistful", "rich", "didactic", "proud", "cold",
    "perpetual", "doubtful", "homeless", "feeble", "absent", "kind", "trite", "salty", "jazzy", "unable", "naive",
    "ignorant", "slippery", "electric", "utopian", "elastic", "fixed", "measly", "noisy", "eager", "frequent",
    "actually", "omniscient", "knotty",
    "eight", "expensive", "luxuriant", "tremendous", "afraid", "wet", "crowded", "slimy", "private", "glib", "shiny",
    "flippant", "icky", "complete", "flashy", "scary", "grey", "hurt", "yielding", "gaping", "boiling", "useful",
    "statuesque", "ajar", "brief", "giddy", "foolish", "receptive", "shaky", "moaning", "whole", "four", "wooden",
    "worthless", "spiffy", "sad", "rhetorical", "robust", "automatic", "willing", "guttural", "glorious", "ordinary",
    "wakeful", "crazy", "valuable", "cagey", "ten", "obedient", "high", "accurate", "humdrum", "bright", "hushed",
    "ceaseless", "marked", "full", "industrious", "dazzling", "demonic", "wry", "scandalous", "sour", "faulty",
    "relieved",
    "coordinated", "elite", "clever", "aloof", "gabby", "slim", "mean", "misty", "jagged", "soggy", "substantial",
    "macabre", "towering", "combative", "alert", "gray", "aberrant", "assorted", "sore", "famous", "shrill", "tasteful",
    "tasty", "stupid", "waggish", "squeamish", "interesting", "nosy", "venomous", "malicious", "old", "magenta",
    "voiceless", "rough", "whimsical", "melted", "hapless", "abandoned", "royal", "internal", "woozy", "barbarous",
    "sneaky", "repulsive", "rambunctious", "successful", "ill-fated", "unwieldy", "overrated", "productive",
    "painstaking", "milky", "clammy", "vague", "frantic", "extra-small", "small", "imperfect", "accessible",
    "highfalutin", "adaptable", "hellish", "concerned", "annoyed", "nostalgic", "quickest", "axiomatic", "calculating",
    "sleepy", "ultra", "second-hand", "steep", "wasteful", "labored", "fresh", "hideous", "grandiose", "tricky",
    "nutritious", "obtainable",
    "vacuous", "far", "possessive", "husky", "silent", "parsimonious", "smoggy", "paltry", "broken", "futuristic",
    "dashing", "flat", "aback", "garrulous", "equable", "wandering", "purring", "abashed", "disastrous", "recondite",
    "exultant", "quixotic", "uppity", "bizarre", "uncovered", "painful", "loutish", "aggressive", "womanly", "eatable",
    "knowledgeable", "elfin", "addictive", "capable", "tested", "disillusioned", "lumpy", "wealthy", "educated",
    "stale", "tacit", "dreary", "ethereal", "heavy", "needy", "solid", "descriptive", "periodic", "onerous", "somber",
    "sedate", "zippy", "sincere", "grubby", "majestic", "callous", "wacky", "standing", "abhorrent", "right",
    "invincible", "earsplitting", "brainy", "round", "white", "acoustic", "hysterical", "reflective", "workable",
    "imported", "gifted",
    "icy", "dark", "tedious", "tame", "flawless", "magical", "overjoyed", "fuzzy", "rabid", "maddening", "obese",
    "abstracted", "wonderful", "greedy", "late", "special", "better", "even", "serious", "energetic", "unsightly",
    "nimble",
    "shocking", "shallow", "embarrassed", "wild", "brash", "unbecoming", "staking", "nonchalant", "bored", "impossible",
    "sordid", "level", "bad", "victorious", "dry", "parched", "goofy", "dynamic", "inconclusive", "steadfast", "rigid",
    "fast", "quaint", "zesty", "absorbed", "false", "burly", "threatening", "perfect", "limping", "profuse", "lush",
    "fragile", "deadpan", "tan", "healthy", "quizzical", "damaging", "lively", "puzzling", "lying", "meek", "cruel",
    "silky", "new", "therapeutic", "aboard", "plucky", "old-fashioned", "cute", "sparkling", "ambitious", "tender",
    "nine",
    "parallel", "tall", "secretive", "outstanding", "wholesale", "polite", "amuck", "near", "clean", "aware", "sloppy",
    "squealing", "adjoining", "romantic", "busy", "warm", "bouncy", "hulking", "adamant", "plastic", "warlike",
    "grieving",
    "humorous", "efficient", "ludicrous", "discreet", "stimulating", "sick", "fertile", "unwritten", "angry", "smiling",
    "lacking", "abundant", "momentous", "careful", "red", "married", "materialistic", "tough", "illustrious", "untidy",
    "obeisant", "habitual", "abiding", "faithful", "narrow", "frightening", "lackadaisical", "rural", "two",
    "panoramic",
    "silly", "verdant", "tawdry", "dispensable", "lopsided", "flowery", "thankful", "youthful", "simple", "little",
    "tacky",
    "boring", "gigantic", "sudden", "ratty", "giant", "general", "economic", "soft", "satisfying", "tranquil", "easy",
    "sticky", "available", "female", "irate", "rotten", "functional", "abounding", "breakable", "well-made", "deeply",
    "jolly", "tangy", "marvelous", "mere", "free", "jumbled", "immense", "vagabond", "caring", "reminiscent", "thick",
    "foregoing", "optimal", "mellow", "lavish", "brave", "fallacious", "half", "snotty", "dependent", "fancy",
    "precious",
    "strange", "opposite", "flimsy", "selfish", "ruddy", "curly", "yummy", "mammoth", "used", "hot", "sassy",
    "synonymous",
    "broad", "cautious", "unequal", "abnormal", "impolite", "tidy", "foamy", "pricey", "sore", "classy", "unbiased",
    "disgusting", "moldy", "absurd", "agreeable", "fretful", "dapper", "skillful", "bent", "fluttering", "obsequious",
    "fluffy", "ill", "motionless", "voracious", "exotic", "illegal", "infamous", "faded", "gaudy", "accidental",
    "gorgeous",
    "elegant", "awesome", "tearful", "agonizing", "placid", "overwrought", "confused", "sweltering", "gullible",
    "unknown",
    "penitent", "dizzy", "young", "damaged", "vivacious", "exuberant", "square", "greasy", "flagrant", "unsuitable",
    "upbeat", "enormous", "piquant", "typical", "wary", "frail", "direful", "petite", "mixed", "subsequent", "maniacal",
    "large", "grumpy", "ablaze", "keen", "gentle", "jittery", "permissible", "first", "numerous", "nonstop",
    "high-pitched",
    "abrasive", "psychotic", "cloudy", "lonely", "weak", "juvenile", "macho", "homely", "rare", "erect", "elated",
    "gruesome", "puzzled", "smart", "political", "evasive", "arrogant", "witty", "purple", "understood", "cooing",
    "endurable", "public", "helpless", "common", "belligerent", "innate", "certain", "miscreant", "raspy", "heavenly",
    "innocent", "vengeful", "swift", "worried", "furtive", "ready", "incompetent", "bumpy", "nondescript", "thirsty",
    "mute", "spotty", "zonked", "muddled", "alive", "aquatic", "skinny", "past", "pale", "cumbersome", "disturbed",
    "three",
    "uninterested", "pleasant", "enchanting", "real", "violet", "depressed", "instinctive", "mature", "utter",
    "delicate",
    "rustic", "teeny-tiny", "thinkable", "good", "mindless", "juicy", "befitting", "light", "pushy", "glistening",
    "stingy",
    "fierce", "awful", "awake", "weary", "frightened", "petite", "medical", "curious", "hurried", "boorish", "longing",
    "funny", "big", "quarrelsome", "harsh", "picayune", "curvy", "judicious", "stormy", "versed", "grouchy", "debonair",
    "faint", "straight", "superb", "magnificent", "crooked", "swanky", "scientific", "learned", "supreme", "one",
    "spurious", "unusual", "lucky", "bite-sized", "colossal", "huge", "massive", "capricious", "mountainous",
    "gleaming",
    "kindly", "amused", "lame", "quiet", "unnatural", "feigned", "thirsty", "fearful", "blue-eyed", "remarkable",
    "heartbreaking", "wide-eyed", "second", "spotless", "nifty", "nauseating", "aspiring", "fine", "fat", "savory",
    "fascinated", "hard", "vulgar", "envious", "crabby", "decisive", "cool", "smelly", "deserted", "dusty", "detailed",
    "safe", "thin", "glamorous", "imminent", "aboriginal", "cowardly", "male", "silent", "sable", "scattered",
    "aromatic",
    "bustling", "future", "lovely", "chief", "hanging", "different", "prickly", "loud", "probable", "rebel", "true",
    "unkempt", "black-and-white", "splendid", "lazy", "gratis", "upset", "damp", "clear", "conscious", "numberless",
    "bewildered", "careless", "naughty", "tangible", "tired", "chivalrous", "spiky", "gainful", "likeable", "few",
    "vast",
    "loose", "horrible", "lively", "lethal", "enthusiastic", "defective", "acrid", "bloody", "helpful", "shy", "earthy",
    "truculent", "boundless", "languid", "itchy", "tasteless", "short", "clumsy", "forgetful", "shut", "great",
    "nervous",
    "changeable", "well-groomed", "lyrical", "rainy", "adventurous", "separate", "observant", "snobbish", "sulky",
    "fanatical", "living", "graceful", "alluring", "delightful", "questionable", "abortive", "roasted", "abaft",
    "green",
    "cultured", "average", "mushy", "amusing", "makeshift", "symptomatic", "gusty", "quick", "tense", "stupendous",
    "poised", "dead", "tart", "watery", "hesitant", "whispering", "attractive", "ill-informed", "annoying",
    "superficial",
    "unaccountable", "neighborly", "long-term", "noiseless", "loving", "defiant", "phobic", "talented", "unequaled",
    "glossy", "pretty", "fabulous", "draconian", "hard-to-find", "guiltless", "cut", "dramatic", "ossified", "orange",
    "cuddly", "dear", "powerful", "testy", "dangerous", "wicked", "sophisticated", "odd", "encouraging", "windy",
    "delicious", "ambiguous", "ad", "hoc", "nappy", "next", "black", "drunk", "brawny", "offbeat", "dusty",
    "protective",
    "abrupt", "gamy", "melodic", "subdued", "daily", "deep", "cloistered", "extra-large", "super", "noxious", "quirky",
    "military", "hollow", "wanting", "historical", "teeny", "zealous", "hypnotic", "beneficial", "stiff", "yellow",
    "useless", "adorable", "regular", "furry", "kaput", "honorable", "ragged", "acceptable", "shaggy", "freezing",
    "handsomely", "minor", "six", "alleged", "acid", "neat", "obscene", "peaceful", "hallowed", "meaty", "halting",
    "screeching", "murky", "torpid", "decorous", "handsome", "oval", "distinct", "intelligent", "like", "familiar",
    "uptight", "null", "nebulous", "grateful", "sturdy", "nippy", "pointless", "domineering", "woebegone", "nutty",
    "equal",
    "plausible", "jealous", "rapid", "necessary", "dull", "groovy", "unarmed", "left", "thoughtless", "handy", "godly",
    "insidious", "far-flung", "irritating", "hissing", "outgoing", "exclusive", "grotesque", "creepy", "berserk",
    "puny",
    "deafening", "terrible", "psychedelic", "mighty", "miniature", "elderly", "jumpy", "quack", "third", "important",
    "organic", "tense", "divergent", "laughable", "resonant", "defeated", "poor", "plant", "enchanted", "slow",
    "trashy",
    "cute", "obsolete", "troubled", "bright", "tight", "bitter", "pumped", "shivering", "anxious", "normal",
    "determined",
    "tiresome", "heady", "friendly", "tenuous", "puffy", "open", "brown", "long", "excited", "responsible", "devilish",
    "colorful", "spectacular", "volatile", "blue", "fair", "lewd", "overt", "astonishing", "bawdy", "waiting",
    "disagreeable", "secret", "imaginary", "material", "obnoxious", "alike", "pink", "alcoholic", "wiry", "taboo",
    "pathetic", "mundane", "rude", "spooky", "apathetic", "craven", "unruly", "plain", "thoughtful", "squalid",
    "eminent",
    "literate", "present", "hateful"
)
item_type_list = {0: 'weapon', 1: 'armor', 2: 'sheild', 3: 'food', 4: 'monster', 5: 'monster'}
weapon = {'name': 'basic sword', 'high': 50, 'low': 10}
armor = {'name': 'shirt', 'defence': 10}
shield = {'name': 'no shield', 'defence': 0}
amulet = 'natural'
health = 200
dead = False
fame = 0
weapons = {'basic sword': [10, 50]}
armors = {}
shields = {}
foods = {}
inventory = [weapons, armors, shields, foods]
name = input("What is your name?: ") + " the " + adjective_list[randint(0, 999)]
print("Welcome to Donegeon, " + name + "!")
print("It's dangerous to go alone! Take this basic sword (50-10).")
print("Entering the Donegeon!")


def chkinv():
    print('weapons: ', weapons)
    print('armors: ', armors)
    print('shields: ', shields)
    print('foods: ', foods)


def status():
    print('You have', 'hitpoints', health, '.')
    print('The name ', name, 'has approximately ', fame, ' fame on the Bendrojh-Fimblston scale.')  # add inflection
    print('You are wielding a', weapon['name'], weapon['high'], weapon['low'])
    print('You are wearing a', armor['name'], armor['defence'], ' and ', shield['name'], shield['defence'])


def death():
    totfood = 0
    for key in foods:
        totfood += foods[key]
    if 0 - totfood < health:
        print('You will survive if you eat something.')
        home()
    else:
        global dead
        dead = True
        print('You died weilding', weapon['name'], ', wearing ', armor['name'], ', and ', shield['name'], '. ')
        print('The name of ', name, ' had ', fame, ' fame on the Bendrojh-Fimblston scale.')
        print('Game Over.')


def home():
    global health
    global amulet
    print('Options (shortcuts):')
    action = input('status (s), inventory (i), equip (eq), eat, or continue (c)? : ')
    if action == 'status' or action == 's':
        status()
        home()
    if action == 'inventory' or action == 'i':
        chkinv()
        home()
    if action == 'equip' or action == 'eq':
        what = input('What do you want to equip?: ')
        if what in weapons:
            weapon['name'] = what
            weapon['high'] = weapons[what][1]
            weapon['low'] = weapons[what][0]
            print('You have equiped the ', weapon['name'], ' ', weapon['high'], '-', weapon['low'])  # as a weapon
        elif what in armors:
            armor['name'] = what
            armor['defence'] = armors[what]
            print('You have equiped the ', armor['name'], armor['defence'])
        elif what in shields:
            shield['name'] = what
            shield['defence'] = shields[what]
            print('You have equiped the ', shield['name'], shield['defence'])
        else:
            print('Can not find ', what)
        home()
    if action == 'eat':
        what = input('What do you want to eat?: ')
        if what in foods:
            health = health + foods[what]
            print('You eat the ', what, 'and regain ', foods[what], 'health.')
            foods.pop(what)
        else:
            print('Can not find ', what)
        home()
    if action == 'continue' or action == 'c':
        inside(event())
    if action == 'amulet':
        desired = input()
        amulet = desired
        home()
    else:
        if not dead:
            print('Invalid entry.')
            home()


def event():
    what = randint(0, 6)
    open_it = 'n'
    if what == 0 or what == 4:
        open_it = input('Here is a chest! Open it? y/n: ')
    elif what == 1 or what == 5:
        open_it = input("There's a door in the corner. Open it? y/n: ")
    elif what == 2 or what == 6:
        open_it = 'y'
        print("Some rocks fall down behind you, you're trapped!")
    elif what == 3:
        op = input("An " + adjective_list[randint(0, 999)] +
                   ' human is sitting in the middle of the room. Greet him? y/n: ')
        if op == 'y':
            open_it = randint(3056516, 3056518)
    return [what, open_it]


def fight(monname, monpower, mondefense, monhealth, defence, level):
    global health
    global fame
    cont = input('Are you prepared to fight the ' + monname + '? y/n: ')
    if cont == 'status' or cont == 's':
        status()
        if fight(monname, monpower, mondefense, monhealth, defence, level):
            return True
    elif cont != 'n':
        while health > 0 and monhealth > 0:
            damage = randint(weapon['low'], weapon['high'])
            mondamage = randint(monpower[0], monpower[1])
            if damage > mondefense:
                dam = damage - mondefense
            else:
                dam = 0
            if mondamage > defence:
                mondam = mondamage - defence
            else:
                mondam = 0
            health = health - mondam
            monhealth -= dam
            print(name, ' does ', dam, ' damage, ', monname, ' has ', monhealth, ' left.')
            print(monname, ' does ', mondam, ' damage, ', name, ' has ', health, ' health left.')
        else:
            if health <= 0:
                print('The ', monname, ' has defeated you.')
                return False
            elif monhealth <= 0:
                fame = fame + level
                print('You have slain the ', monname, ' with your ', weapon['name'], ', while wearing ', armor['name'],
                      ' and ', shield['name'], '.')
                print('Your heroic deed gained you ', level, ' fame! The name ', name, ' is now at ', fame,
                      ' on the Bendrojh-Fimblston scale!')
                return True
    elif cont == 'n':
        cowardice = 260 - level
        fame -= cowardice
        print("In your cowardice, you flee the ", monname, "!")
        print('Your fame is marred by your cowardly deed. You have lost ', cowardice, ' fame. Your fame is now about ',
              fame, 'on the Bendrojh-Fimblston scale.')
        luck = randint(0, 4)                               # int(0,20)
        if luck == 0:                                      # luck in fortune(player stat)
            print("You got away!")
            home()
        else:
            mondamage = randint(monpower[0], monpower[1])
            if mondamage > defence:
                mondam = mondamage - defence
            else:
                mondam = 0
            health = health - mondam
            print("The ", monname, ' injures you as you flee!')
            print(monname, ' does ', mondam, ' damage, you have ', health, ' health left.')
            if health > 0:
                return True
            elif health <= 0:
                print('The ', monname, ' has defeated you!')
                return False


def create_thing(thing_name, thing):
    new_name = adjective_list[randint(0, 999)] + ' ' + thing_name
    attack = randint(1, 100)
    attack2 = randint(1, 100)
    defence = randint(1, 60)
    meal = randint(5, 50)
    power = [attack, attack + attack2]
    mydef = armor['defence'] + shield['defence']
    if thing == 'weapon':
        if power[1] > 70:
            new_name = adjective_list[randint(0, 999)] + ' ' + new_name
            if power[1] > 150:
                new_name = adjective_list[randint(0, 999)] + ' ' + new_name
        new_name = Weapon(new_name, power[1], power[0])
        weapons[new_name] = power                                           # dictionary
        print('The ' + new_name.name + ' ' + str(power[1]) + '-' + str(power[0]) + " is a " + thing + ".")
    elif thing == 'armor':
        if defence > 20:
            new_name = adjective_list[randint(0, 999)] + ' ' + new_name
            if defence > 40:
                new_name = adjective_list[randint(0, 999)] + ' ' + new_name
        new_name = Armor(new_name, defence)
        armors[new_name] = defence
        print('The ' + new_name.name + ' (' + str(defence) + ') is ' + thing + '.')
    elif thing == 'sheild':
        if defence > 20:
            new_name = adjective_list[randint(0, 999)] + ' ' + new_name
            if defence > 40:
                new_name = adjective_list[randint(0, 999)] + ' ' + new_name
        new_name = Sheild(new_name, defence)
        shields[new_name] = defence
        print('The ' + new_name.name + ' (' + str(defence) + ') is a ' + thing + '.')
    elif thing == 'food':
        if meal > 20:
            new_name = adjective_list[randint(0, 999)] + ' ' + new_name
            if meal > 40:
                new_name = adjective_list[randint(0, 999)] + ' ' + new_name
        new_name = Food(new_name, meal)
        foods[new_name] = meal
        print('The ' + new_name.name + ' (' + str(meal) + ') is ' + thing + '.')
    elif thing == 'monster':
        level = attack + attack2 + defence + meal
        if level > 100:
            new_name = adjective_list[randint(0, 999)] + ' ' + new_name
            if level > 200:
                new_name = adjective_list[randint(0, 999)] + ' ' + new_name
        print('The ', new_name, ' is a monster with attack (', attack, '-', power[1], '), defence (', defence,
              '), and health (', meal, ').')
        if not fight(new_name, power, defence, meal, mydef, level):
            return True
        else:
            return False


def meeting(who):
    global name
    if fame < 1000:
        print('Greetings stranger. You must be new to these parts, I have not heard tell of your adventures.')
        print('I am here to teach great heros the ancient magic.')
        print('That way when they emerge from Donegeon, I can take partial credit for all their great deeds! HEHEHE!')
        print('The mysterious stranger has disappeared...')
        home()
    elif fame >= 1000:
        print('Greetings ', name, '! I have heard of your great heroism in Donegeon!')
        print('I can mentor you in the ways of ancient magic, so that nothing may stand in your way!')
        responce = input('lesson(l)')
        if responce == 'lesson' or responce == 'l':
            print('stuff', who)
    # if who == 3056516:

    # elif who == 3056517:
        # mission
    # elif who == 3056518:


def inside(opening):
    if opening[1] == 'y':
        if amulet == 'natural':
            item_type = randint(0, 5)
        elif amulet == 'monster':
            item_type = 4
        elif amulet == 'weapon':
            item_type = 0
        elif amulet == 'armor':
            item_type = 1
        elif amulet == 'sheild':
            item_type = 2
        elif amulet == 'food':
            item_type = 3
        else:
            item_type = randint(0, 5)
        inside_box = ""
        if opening[0] == 0 or opening[0] == 4:
            inside_box = input("You throw the chest open! What's this?: ")
        elif opening[0] == 1 or opening[0] == 5:
            inside_box = input("You kick down the door with a shout! What's that behind it?: ")
        elif opening[0] == 2 or opening[0] == 6:
            inside_box = input("Something lands on the ground in front of you! What is it?: ")
        if create_thing(inside_box, item_type_list[item_type]):
            death()
        else:
            home()
    elif opening[1] in range(3056516, 3056519):
        meeting(opening[1])
    elif opening[1] == 'n':
        if opening[0] == 0 or opening[0] == 4:
            print("You pass by the chest. There may be something dangerous in there, after all.")
        elif opening[0] == 1 or opening[0] == 5:
            print("You leave the door closed and leave. A monster may have lurked behind it.")
        elif opening[0] == 3:
            print("You avoid the man's friendly smile, and leave the room quickly.")
        home()
    else:
        print("You got confused and ran away!")
        home()


inside(event())
