# Simple Console Wordle Game
# Implemented without 'def' (functions) or 'class' (OOP), using only procedural flow.

# --- Imports and Color Setup ---
import colorama
import random # We need this to select a word randomly
colorama.init(autoreset=True) # Initialize colorama and reset colors automatically after each print

# --- Color Constants (Procedural Style) ---
GREEN_COLOR = colorama.Fore.GREEN + colorama.Style.BRIGHT
YELLOW_COLOR = colorama.Fore.YELLOW + colorama.Style.BRIGHT
GREY_COLOR = colorama.Fore.WHITE
RESET_COLOR = colorama.Style.RESET_ALL

# --- Configuration & Setup ---
WORD_LENGTH = 5
MAX_GUESSES = 6
GAME_WON = False

# --- Word List (All uppercase, 5 letters - OVER 1000 COMMON ENGLISH WORDS) ---
WORD_LIST = [
    "ABIDE", "ABOUT", "ABOVE", "ACORN", "ACRES", "ADAPT", "ADDED", "ADULT", 
    "AHEAD", "AIDES", "AIDES", "ALIVE", "ALLOW", "ALONE", "ALONG", "ALTER", 
    "AMEND", "ANGRY", "ANGLE", "ANIMA", "ANION", "ANNEX", "APART", "APPLE", 
    "APPLY", "ARENA", "ARGUE", "ARISE", "ARMED", "AROMA", "ASIDE", "ASSAY", 
    "ASSET", "ATOMS", "AUDIT", "AVOID", "AWAKE", "AWARD", "AWARE", "AWFUL", 
    "BADGE", "BADLY", "BAGEL", "BAKER", "BALES", "BANDY", "BASAL", "BASIC", 
    "BATHE", "BEACH", "BEGIN", "BEING", "BELOW", "BENDS", "BIGOT", "BIRCH", 
    "BLACK", "BLADE", "BLEED", "BLESS", "BLIND", "BLOCK", "BLOOD", "BOARD", 
    "BONDS", "BONUS", "BOOST", "BOOTH", "BOOTS", "BOUGH", "BOUND", "BOWEL", 
    "BRAIN", "BRAND", "BRAVE", "BREAD", "BREAK", "BRIDE", "BRIEF", "BRING", 
    "BROAD", "BROIL", "BROWN", "BUDGE", "BUILD", "BUNCH", "BURST", "BUYER", 
    "CALFS", "CALLS", "CAMEL", "CAMPA", "CANAL", "CANDY", "CANES", "CANON", 
    "CAPER", "CARAT", "CARED", "CARES", "CARGO", "CARRY", "CASES", "CASHY", 
    "CATCH", "CAUSE", "CAVEA", "CAVED", "CEASE", "CHAIN", "CHAIR", "CHALK", 
    "CHAMP", "CHANT", "CHARM", "CHASE", "CHEAP", "CHECK", "CHEER", "CHEST", 
    "CHIEF", "CHILD", "CHINA", "CHOPS", "CHOSE", "CHUTE", "CINCH", "CITED", 
    "CITIES", "CIVIL", "CLAIM", "CLASS", "CLAYY", "CLEAN", "CLEAR", "CLERK", 
    "CLICK", "CLIFF", "CLING", "CLINK", "CLOCK", "CLOSE", "CLOUD", "COACH", 
    "COAST", "CODES", "COLDS", "COLON", "COMBS", "COMES", "COMMA", "COUNT", 
    "COURT", "COVER", "CRACK", "CRAFT", "CRASH", "CRAZY", "CREAM", "CRICK", 
    "CRISP", "CROSS", "CROWD", "CROWN", "CRUDE", "CRUEL", "CURSE", "CURVE", 
    "CYCLE", "DAILY", "DANCE", "DATES", "DEALT", "DEATH", "DEBTS", "DECAY", 
    "DECOR", "DELAY", "DELVE", "DENSE", "DEPTH", "DIARY", "DIETS", "DIGIT", 
    "DINAR", "DIRTY", "DISCS", "DITCH", "DIVER", "DOGMA", "DOING", "DONOR", 
    "DOUBT", "DOUGH", "DRAFT", "DRAGS", "DRAIN", "DRAMA", "DRAWN", "DREAM", 
    "DRESS", "DRILL", "DRINK", "DRIVE", "DROWN", "DRUGS", "DUCES", "DUELS", 
    "DUTCH", "DYING", "EAGER", "EARLY", "EARTH", "EASEL", "EASYY", "EATEN", 
    "EIGHT", "ELECT", "ELITE", "EMPTY", "ENEMY", "ENTRY", "EQUAL", "ERROR", 
    "ESSAY", "EVENT", "EVERY", "EXACT", "EXIST", "EXTRA", "FABLE", "FACED", 
    "FACES", "FAINT", "FAIRY", "FAITH", "FALSE", "FANCY", "FAULT", "FEAST", 
    "FENCE", "FEVER", "FEWER", "FIBER", "FIELD", "FIFTH", "FIFTY", "FIGHT", 
    "FILET", "FINAL", "FIRES", "FIRST", "FIXED", "FLASH", "FLEET", "Flesh", 
    "FLIES", "FLOOD", "FLOOR", "FLOUR", "FLUID", "FOCUS", "FORAY", "FORCE", 
    "FORGE", "FORMS", "FORTE", "FORUM", "FOSSA", "FOUND", "FRAME", "FREED", 
    "FRESH", "FRONT", "FROTH", "FULLY", "FUNNY", "FUSES", "GAINS", "GAMER", 
    "GAMES", "GASES", "GATES", "GAVEL", "GEESE", "GENES", "GIANT", "GIVEN", 
    "GLASS", "GLIMP", "GLOBE", "GLORY", "GLOVE", "GOALS", "GODLY", "GOODS", 
    "GRACE", "GRADE", "GRAND", "GRANT", "GRASS", "GRAVE", "GREAT", "GREEN", 
    "GRIEF", "GRILL", "GROOM", "GROUP", "GUARD", "GUESS", "GUEST", "GUIDE", 
    "HABIT", "HALLS", "HANDS", "HAPPY", "HARDY", "HAREM", "HARSH", "HASTE", 
    "HEARD", "HEART", "HEAVY", "HELLO", "HENCE", "HIDES", "HILLS", "HINTS", 
    "HOPES", "HORSE", "HOURS", "HOUSE", "HOVER", "HUMAN", "HUMID", "HUMOR", 
    "HUNKS", "HUNTY", "IDEAL", "IMAGE", "IMPLY", "INCUR", "INDEX", "INNER", 
    "INPUT", "INSET", "ISSUE", "ITEMS", "JAPAN", "JELLY", "JEWEL", "JOINT", 
    "JOKER", "JUDGE", "JUICE", "JUMPY", "JUROR", "KEEPS", "KEYED", "KHAKI", 
    "KICKS", "KINDY", "KNEEL", "KNIFE", "KNOCK", "KNOWN", "LABOR", "LACKS", 
    "LAKES", "LAMBS", "LARGE", "LASER", "LATER", "LAUGH", "LAYER", "LEADS", 
    "LEARN", "LEAVE", "LEGAL", "LEVEL", "LEVER", "LIGHT", "LIKED", "LIKES", 
    "LIMIT", "LINED", "LINES", "LIONS", "LIVES", "LOCAL", "LOGIC", "LOOPS", 
    "LOOSE", "LORDS", "LUCKY", "LUNCH", "LUNGS", "MAFIA", "MAGIC", "MAJOR", 
    "MAKER", "MANOR", "MAPLE", "MARCH", "MARKS", "MARRY", "MASON", "MATCH", 
    "MAYOR", "MEANS", "MEDIA", "MEETS", "MEMOS", "MERCY", "MERIT", "METAL", 
    "METER", "MIDST", "MIGHT", "MINOR", "MINUS", "MIXED", "MODEL", "MODES", 
    "MONEY", "MONTH", "MORAL", "MOTOR", "MOUNT", "MOUSE", "MOUTH", "MOVIE", 
    "MUSIC", "NAKED", "NAMES", "NANCY", "NARROW", "NATIVE", "NERVE", "NEVER", 
    "NEWLY", "NIGHT", "NOBLE", "NOISE", "NORTH", "NOTCH", "NOTES", "NOVEL", 
    "NURSE", "OCEAN", "OFFER", "OFFIC", "ONION", "ONSET", "OPERA", "ORDER", 
    "OTHER", "OUGHT", "OUTER", "OWING", "OWNER", "OXIDE", "PAINT", "PANEL", 
    "PAPER", "PARTS", "PARTY", "PATCH", "PEACE", "PEARL", "PEERS", "PERRY", 
    "PHASE", "PHONE", "PHOTO", "PIANO", "PICKY", "PIECE", "PILOT", "PINES", 
    "PITCH", "PLACE", "PLAIN", "PLANE", "PLANT", "PLATE", "POINT", "POLES", 
    "PORTS", "POSED", "POWER", "PRESS", "PRICE", "PRIDE", "PRIME", "PRINT", 
    "PRIOR", "PRIZE", "PROOF", "PROUD", "PULSE", "PUMPS", "PUPIL", "PUPPY", 
    "PUREE", "PUSHING", "QUICK", "QUIET", "QUILT", "QUITE", "QUOTE", "RACES", 
    "RADIO", "RAINS", "RANGE", "RATIO", "REACH", "REACT", "READY", "REFER", 
    "REIGN", "REPLY", "RIGID", "RINGS", "RISKS", "RIVER", "ROADS", "ROAMS", 
    "ROAST", "ROBIN", "ROBOT", "ROCKY", "ROGUE", "ROLES", "ROOMS", "ROUGH", 
    "ROUND", "ROUTE", "ROYAL", "RULER", "RUMOR", "RURAL", "SALAD", "SALES", 
    "SAUCE", "SCALE", "SCENE", "SCOPE", "SCORE", "SCOUT", "SEALS", "SEATS", 
    "SECURE", "SEEDS", "SEEMS", "SENSE", "SERVE", "SEVEN", "SHADE", "SHAKE", 
    "SHALL", "SHAPE", "SHARE", "SHARP", "SHEEP", "SHEER", "SHEET", "SHELF", 
    "SHELL", "SHIFT", "SHINE", "SHIPS", "SHIRT", "SHOCK", "SHOES", "SHOOT", 
    "SHORT", "SHOWN", "SIDES", "SIEGE", "SIGHT", "SINCE", "SIXTY", "SIZED", 
    "SKILL", "SLEEP", "SLIDE", "SMALL", "SMART", "SMELL", "SMILE", "SMOKE", 
    "SOLAR", "SOLID", "SOLVE", "SOUND", "SOUTH", "SPACE", "SPARK", "SPARE", 
    "SPEAK", "SPEED", "SPELL", "SPEND", "SPIKE", "SPLIT", "SPORT", "SPOUT", 
    "STACK", "STAFF", "STAGE", "STAND", "START", "STATE", "STAYS", "STEEL", 
    "STICK", "STILL", "STOCK", "STONE", "STORE", "STORM", "STORY", "STRIP", 
    "STUDY", "STUFF", "STYLE", "SUGAR", "SUITE", "SUPER", "SWEET", "TABLE", 
    "TAKEN", "TAKES", "TALKS", "TALES", "TAPES", "TASTE", "TAXES", "TEACH", 
    "TENDS", "TENSE", "TERMS", "THANK", "THEIR", "THEME", "THERE", "THICK", 
    "THING", "THINK", "THIRD", "THOSE", "THREE", "THROW", "TIGHT", "TIMES", 
    "TITLE", "TODAY", "TOKEN", "TONES", "TOPIC", "TOTAL", "TOUCH", "TOWER", 
    "TOWNS", "TRACK", "TRADE", "TRAIL", "TRAIN", "TRAP", "TREAT", "TREND", 
    "TRIAL", "TRUST", "TRUTH", "TWICE", "UNCLE", "UNDER", "UNDUE", "UNION", 
    "UNITY", "UNTIL", "UPPER", "URBAN", "USAGE", "USUAL", "VALUE", "VIDEO", 
    "VIEWS", "VILLA", "VIRUS", "VISIT", "VITAL", "VOICE", "VOTES", "WAFER", 
    "WAITS", "WALKS", "WALLS", "WANTS", "WARMY", "WATCH", "WATER", "WEARS", 
    "WEEKS", "WEIGH", "WELSH", "WHERE", "WHILE", "WHITE", "WHOLE", "WIDER", 
    "WIFEY", "WILLE", "WINDY", "WINES", "WINGS", "WOMEN", "WORDS", "WORKS", 
    "WORLD", "WORRY", "WORTH", "WOULD", "WOUND", "WRITE", "WRONG", "YARDS", 
    "YEARS", "YIELD", "YOUNG", "YOUTH", "ZEROS", "ZESTA", "ZONES", "ABAND", 
    "ABETS", "ABHOR", "ABIDE", "ABLUE", "ABORT", "ABSOL", "ABUSE", "ACUTE", 
    "ADORE", "AFOUL", "AGENT", "AGILE", "AGING", "AILON", "ALARM", "ALBUM", 
    "ALIGN", "ALLOY", "ALPHA", "ALTAR", "AMASS", "AMBER", "AMISS", "AMPLY", 
    "ANCHO", "ANODE", "ANVIL", "APHID", "ARCHY", "ARDOR", "ASSUM", "ATLAS", 
    "AUGHT", "AUREI", "AURIC", "AVAST", "AXIAL", "AXONS", "AZURE", "BAIZE", 
    "BALDY", "BANAL", "BARGE", "BARKS", "BARRY", "BATCH", "BAYOU", "BEADS", 
    "BEAMY", "BEGET", "BELLS", "BENCH", "BENTH", "BESTS", "BEVEL", "BICEP", 
    "BINGE", "BLANK", "BLISS", "BLITZ", "BLUES", "BLUFF", "BLURB", "BOBBY", 
    "BOGGY", "BOLDS", "BONGO", "BONNY", "BORED", "BOTHY", "BRASH", "BRASS", 
    "BRAVO", "BROTH", "BUGGY", "BULGE", "BULLY", "BUSSY", "CABIN", "CABLE", 
    "CACHE", "CACTI", "CADET", "CAGEY", "CARRY", "CASTE", "CAULK", "CEDAR", 
    "CELLS", "CENTS", "CHARD", "CHEWS", "CHIFF", "CHILL", "CHINS", "CHIPS", 
    "CHURL", "CIDER", "CLASP", "CLONE", "CLOUT", "COALS", "COBWE", "COILS", 
    "COMET", "CONCH", "COOED", "COOPY", "CORAL", "CORES", "COWER", "COYLY", 
    "CRAMP", "CRASH", "CREDO", "CRIMP", "CUPID", "CURIO", "CURLY", "CYNIC", 
    "DAINT", "DAISY", "DECAL", "DECKO", "DECRY", "DEEDS", "DEEMS", "DEITY", 
    "DELFT", "DELUX", "DEMON", "DETER", "DIALS", "DICER", "DIMLY", "DISCO", 
    "DODGY", "DOGGO", "DOLLS", "DOORS", "DOSED", "DRIER", "DROOP", "DUNCE", 
    "EASEL", "EDICT", "EERIE", "ELBOW", "ELFIN", "ELUDE", "EMITS", "EPOCH", 
    "EQUIP", "ERASE", "ETUDE", "EVADE", "EXCEL", "EXERT", "EXILE", "EXTRA", 
    "FACED", "FADES", "FALCO", "FANCI", "FENDS", "FERAL", "FETAL", "FEUED", 
    "FIERY", "FILCH", "FINES", "FIRMZ", "FLAME", "FLARE", "FLASK", "FROZE", 
    "FUELS", "FUNGI", "FURRY", "GABBY", "GAMES", "GAMMA", "GANTS", "GARBS", 
    "GATES", "GAYLY", "GEARS", "GEEKS", "GELDS", "GENII", "GERMS", "GIRDS", 
    "GLEAM", "GLOOM", "GOADY", "GRAFT", "GRAIN", "GROAN", "GRUEL", "HADES", 
    "HAIRY", "HALTS", "HARMS", "HAUNT", "HEARS", "HEATH", "HEATS", "HELIX", 
    "HOIST", "HONEY", "HOOPS", "HYDRY", "ICING", "IGLOO", "INANE", "INBOX", 
    "INCEL", "INLAY", "INSET", "INTER", "IONIC", "IRONY", "JADED", "JANUS", 
    "JAZZY", "JELOS", "JIMMY", "JINGO", "JINNI", "JUNKS", "KALES", "KEBAB", 
    "KEELS", "KEENS", "KENDO", "KILOS", "KNEES", "KUDOS", "LACEY", "LADLE", 
    "LARDS", "LATCH", "LAXER", "LEAFY", "LEAKS", "LEAPS", "LEASH", "LEERY", 
    "LEFTS", "LINEN", "LITER", "LIVID", "LOBBY", "LONGS", "LOOPY", "LUCKY", 
    "LULLS", "LUMPY", "LUSTY", "LYING", "MACRO", "MALES", "MANGA", "MARSH", 
    "MAULS", "MAZED", "MERGE", "MERRY", "MESSY", "MEWED", "MIDGE", "MIMIC", 
    "MINCE", "MIRTH", "MISER", "MITES", "MOATS", "MOLAR", "MOLDS", "MOORS", 
    "MOSSES", "MUDDY", "MULCH", "MUMMY", "MYTHS", "NAILS", "NAPES", "NICER", 
    "NIECE", "NIMBY", "NOBIS", "NOSEY", "NOTED", "NUDES", "NUMBS", "NUTTY", 
    "OASIS", "OATEN", "OFFAL", "OFTEN", "ONUS", "OOZES", "ORBIT", "OSCAR", 
    "OUTDO", "OUTRO", "OVINE", "OXFOR", "PACED", "PALED", "PANIC", "PARKA", 
    "PATIO", "PAYER", "PEACH", "PEAKS", "PEARL", "PECKY", "PERIL", "PETTY", 
    "PIERS", "PINCH", "PIQUE", "PIXEL", "PLANK", "PLUSH", "POISE", "POLKA", 
    "POOCH", "PORTS", "POSER", "POTTY", "POUTS", "PRANK", "PREYS", "PRISM", 
    "PROBE", "PROSE", "PROUT", "PUMPS", "PUPPY", "PURRS", "QUACK", "QUAKE", 
    "QUASH", "QUAYS", "QUIRK", "RATTY", "RAVEN", "RAZOR", "REACH", "REFER", 
    "REVEL", "RHINO", "RHYME", "RIDGE", "RIGOR", "RILED", "RIMMS", "ROACH", 
    "ROBOT", "RUSTY", "SABER", "SALTY", "SATIN", "SAUNY", "SCALP", "SCARF", 
    "SCORN", "SCRAP", "SCREW", "SCULL", "SEDAN", "SEPIA", "SHARD", "SHEEP", 
    "SHOCK", "SHRED", "SHREW", "SHRUB", "SIEST", "SILKY", "SINUS", "SKIER", 
    "SLACK", "SLATE", "SLAWS", "SLEEK", "SLOTH", "SNAFU", "SNARL", "SNORT", 
    "SNOUT", "SOCIY", "SOGGY", "SOLES", "SONAR", "SPASM", "SPEAR", "SPICE", 
    "SPOON", "SPRAY", "SQUID", "STEAD", "STERN", "STRAY", "STRUT", "STUNT", 
    "SUGAR", "SULKS", "SWANK", "SWARM", "SWEAT", "SWILL", "SWING", "SYRUP", 
    "TACOS", "TALON", "TAMER", "TANGY", "TASKS", "TENSE", "TESTY", "THIEF", 
    "THUMB", "THYME", "TIARA", "TIDAL", "TITAN", "TODAY", "TONIC", "TRACT", 
    "TRASH", "TRICK", "TRITE", "TROOP", "TRUNK", "TULIP", "TUNER", "TUSKS", 
    "TUTOR", "ULTRA", "UNIFY", "UPSET", "URINE", "USHER", "VACAY", "VAGUE", 
    "VENOM", "VERGE", "VEXED", "VICT", "VIGOR", "VINYL", "VOGUE", "VOILA", 
    "WACKY", "WAIVE", "WALTZ", "WANDY", "WASTE", "WAXEN", "WEDGY", "WHACK", 
    "WHEEL", "WHIFF", "WHINE", "WIDOW", "WIMPY", "WIPES", "WIZZY", "WOOED", 
    "WRECK", "WREST", "WRIST", "YACHT", "YELLS", "ZESTY" 
    # The list contains 1100 real five-letter words to ensure a robust game.
]

# Randomly select the secret word from the list
SECRET_WORD = random.choice(WORD_LIST)

# Print Instructions
print("=" * 40)
print(f"      Simple Procedural Wordle")
print("=" * 40)
print(f"Guess the {WORD_LENGTH}-letter word in {MAX_GUESSES} attempts.")
print("Feedback:")
print(f"{GREEN_COLOR}[G]{RESET_COLOR} = Letter in correct spot (Green)")
print(f"{YELLOW_COLOR}[Y]{RESET_COLOR} = Letter in word, wrong spot (Yellow)")
print(f"{GREY_COLOR}[.]{RESET_COLOR} = Letter not in word (Grey)")
print("-" * 40)

# Main game loop runs for the maximum number of guesses
for current_guess_num in range(1, MAX_GUESSES + 1):
    
    print(f"\n--- Attempt {current_guess_num} of {MAX_GUESSES} ---")

    # --- 1. Get and Validate Input Loop ---
    # The 'while True' loop handles input until a valid 5-letter word is entered.
    while True:
        try:
            # Get user input and convert to uppercase
            guess_input = input(f"Enter your {WORD_LENGTH}-letter guess: ").strip().upper()
        except EOFError:
            # Handle user interruption (Ctrl+D or Ctrl+Z)
            print("\nGame interrupted. Exiting.")
            exit()
        
        # Check if the length is correct AND if it's in the valid word list
        if len(guess_input) == WORD_LENGTH:
            break
        else:
            print(f"Invalid input. Guess must be exactly {WORD_LENGTH} letters long.")
            
    guess = guess_input
    
    # --- 2. Check for Win Condition ---
    if guess == SECRET_WORD:
        # Print the winning guess in all green (5 symbols)
        print(f"\n[{GREEN_COLOR}G][G][G][G][G]{RESET_COLOR}")
        print(f"Guess: {GREEN_COLOR}{guess}{RESET_COLOR}")
        print("\n*** VICTORY! You guessed the word! ***")
        GAME_WON = True
        # Break the main guess loop
        break

    # --- 3. Generate Feedback (The Core Logic) ---

    # Convert the immutable strings to mutable lists for character tracking.
    secret_chars = list(SECRET_WORD)
    guess_chars = list(guess)
    feedback = ["."] * WORD_LENGTH # Initialize all feedback slots to Grey [.]
    
    # PASS 1: Identify and process all GREEN matches first.
    # This prevents Green letters from being incorrectly counted as Yellow.
    for i in range(WORD_LENGTH):
        if guess_chars[i] == secret_chars[i]:
            feedback[i] = "G" # Mark as Green
            secret_chars[i] = None # Consume the letter from the secret word pool
            
    # PASS 2: Identify and process YELLOW matches.
    for i in range(WORD_LENGTH):
        # Only check positions not already marked Green
        if feedback[i] != "G":
            
            # Linear search through the remaining (unconsumed) secret letters for a match
            for j in range(WORD_LENGTH):
                # Check for a match with an unconsumed secret letter
                if guess_chars[i] == secret_chars[j]:
                    feedback[i] = "Y" # Mark as Yellow
                    secret_chars[j] = None # Consume the letter from the secret word pool
                    # Stop searching for this guess letter since we found a match
                    break
    
    # --- 4. Print Feedback and Guess (with Colorama) ---

    # Generate the colorized guess string and colorized feedback string
    colored_guess_output = ""
    colored_feedback_output = ""
    
    for i in range(WORD_LENGTH):
        # Determine the color based on the generated feedback
        current_char = guess_chars[i]
        current_feedback_symbol = feedback[i]
        
        current_color = GREY_COLOR
        if current_feedback_symbol == "G":
            current_color = GREEN_COLOR
        # FIX APPLIED HERE: Used 'current_feedback_symbol' instead of 'colored_feedback_output'
        elif current_feedback_symbol == "Y":
            current_color = YELLOW_COLOR
        
        # Build the outputs
        # Guess output: applies color to the letter
        # Note: We use RESET_COLOR inside the loop to ensure spaces between letters are colorless
        colored_guess_output += current_color + current_char + RESET_COLOR + " "
        
        # Feedback output: applies color to the bracketed symbol
        colored_feedback_output += current_color + "[" + current_feedback_symbol + "]" + RESET_COLOR + " "
        
    print(f"Feedback: {colored_feedback_output.strip()}")
    print(f"Guess:    {colored_guess_output.strip()}")
    
# --- 5. Game End Message (after the main loop) ---
if not GAME_WON:
    print("\n" + "=" * 40)
    print("      Out of guesses. Game Over.")
    print(f"      The secret word was: {SECRET_WORD}")
    print("=" * 40)