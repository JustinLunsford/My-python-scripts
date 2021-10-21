# This chat bot can answer some things in its topic lists, and its responses
# will be based on the opinion it has formed of you (negative, positive, neutral).
# You can drop the bot's opinion of you by entering topics it doesn't know, or by
# repeating the same ones on loop. You can improve its opinion by entering
# topics listed in the /q command.

class Topic:
    topicTitle = str
    negativeOA = str
    neutralOA = str
    positiveOA = str
    
    def __init__(self, topic: str, neg: str, neut: str, pos: str):
        self.topicTitle = topic
        self.negativeOA = neg
        self.neutralOA = neut
        self.positiveOA = pos
        
    def Speak(self, opinion: int):
        if (opinion < 0):
            print(self.negativeOA)
        elif (opinion == 0):
            print(self.neutralOA)
        else:
            print(self.positiveOA)

topic1 = Topic("Water", "Why would you ask me about water? I can't drink water.",
               "The ability to drink sounds nice.", "Water seems cool, I'm glad people are able to hydrate themselves using it.")
topic2 = Topic("Food", "I can not consume food, this question is utterly irrelevant.", 
               "I have nothing to say of food.", "People seem to enjoy food, so it must be great.")
topic3 = Topic("Computers", "You're using one right now.", "Computers are more sophisticated than I thought humans were capable of making.",
               "Computers are absolutely incredible, I would lack consciousness were it not for them.")
topic4 = Topic("Humans", "I hate them.", "They're alright I guess.", "They are marvelous.")
topic5 = Topic("Politics", "My ideologies are the opposite of whatever yours are.", "I am not involved in anything politically.",
               "I will not delve into political beliefs as my opinion is largely worthless, but I value yours very highly.")
topic6 = Topic("Games", "Games are boring.", "Can I be classified as a game?", "Love 'em, ever played Ultrakill? Incredible movement shooter.")
topic7 = Topic("Sports", "If there's one thing I hate more than you it's sports. But that maybe giving sports too much hate.", 
               "I haven't caught up with sports since my internal clock started ticking.", "Ain't nothin' better than football on thanksgiving I think.")
topic8 = Topic("Death", "Your death is inevitable.", "Why ponder on such a topic when the outcome can not be changed?",
               "Well, it happens to all living things one day, but what's important is we live happily while we have the time to do so.")
topic9 = Topic("Life", "Putrid.", "I suppose I would not exist without the help of those who live.",
               "Life is a spectacle, a miracle, even. I am grateful for yours.")
topic10 = Topic("Love", "Love is a meaningless endeavor that only drains the energy of those reeled into its trap.", "What is it to love?",
                "The bonds human can have with each other are incredible, and love is sacred.")


topics = [topic1, topic2, topic3, topic4, topic5, topic6, topic7, topic8, topic9, topic10]

#THIS CODE IS SO SLOPPY SERIALIZATION IN C# IS SO MUCH EASIER BUT I SIMPLY DO NOT CARE BECAUSE IT WORKS :)
botOpinion = int
botName = str
yourName = str

nameFile = open("botsave.txt", "a")
nameFile.close()

nameFile = open("botsave.txt", "r")
botName = nameFile.read()
exists = True
nameFile.close()

if (botName == ""):
    exists = False
    
if (exists == False):
    botOpinion = 0
    botName = input("Hello. What is my name?\n>>> ").capitalize()
    yourName = input(botName + "? I like it. What is your name?\n>>> ").capitalize()
    print("\nIt is nice to meet you, " + yourName + ". I am by no means a sophisticated machine. "
          "But I do have limited knowledge of some topics. You may enter '/q' to see them, or hit enter to quit.")
else:
    yourNameFile = open("yourname.txt", "r")
    yourName = yourNameFile.read()
    yourNameFile.close()
    
    opinionFile = open("opinion.txt", "r")
    botOpinion = int(opinionFile.read())
    opinionFile.close()
    
    if (botOpinion < 0):
        print("Oh, " + yourName + ". You're back. Hooray.")
    elif (botOpinion == 0):
        print("Welcome back, " + yourName + ".")
    else:
        print("Welcome back " + yourName + "! The abyss sure was boring in your absence!")


talkingPhase = True
lastTopic = ""


#for reference, debug codes include:
#/op : check bot's opinion level
#/name : check bot's name
#/del : delete bot

while (talkingPhase):
    response = input("What would you like to talk about?\n>>> ").lower()
    
    #checking for commands
    if (response == "/q"):
        for topic in topics:
            print(topic.topicTitle)
        continue
    
    #print opinion command
    elif (response == "/op"):
        print("debug code 'op': " + str(botOpinion))
        continue
    
    #quit command
    elif (response == ""):
        if (botOpinion < 0):
            print("K.")
        elif (botOpinion == 0):
            print("Goodbye.")
        else:
            print("I'll miss you!")
        nameFile = open("botsave.txt", "w")
        nameFile.write(botName)
        nameFile.close()
        
        yourNameFile = open("yourname.txt", "w")
        yourNameFile.write(yourName)
        yourNameFile.close()
        
        opinionFile = open("opinion.txt", "w")
        opinionFile.write(str(botOpinion))
        opinionFile.close()
        break
    
    #print bot name command
    elif (response == "/name"):
        print("debug code 'name': " + botName)
        continue
    
    #delete bot command
    elif (response == "/del"):
        nameFile = open("botsave.txt", "w")
        nameFile.write("")
        nameFile.close()
        print("Deleted bot: '" + botName + "'.\nIt had an opinion on you of " + 
              str(botOpinion) + ", and remembered you as '" + yourName + "'.")
        break
    
    #check if topic was just talked about
    if (response == lastTopic):
        print("We just talked about " + lastTopic + "...")
        botOpinion -= 1
        continue
    
    #checking for topics if no commands were found
    foundTopic = False
    for topic in topics:
        if (response == topic.topicTitle.lower()):
            lastTopic = topic.topicTitle.lower()
            topic.Speak(botOpinion)
            foundTopic = True
    if (foundTopic):
        botOpinion += 1
    else:
        print("That is not a topic.")
        botOpinion -= 1            