from datetime import datetime

storyTime = True

while (storyTime):
    mainCharacter = input("Choose a main character.\n>>> ").capitalize()
    location = input("Where does this story take place?\n>>> ").capitalize()
    weather = input("What's the weather like in " + location + "?\n>>> ").lower()
    attitude = input("How is " + mainCharacter + " feeling on this " + weather + " day?\n>>> ")
    friend = input("Who is " + mainCharacter + "'s best friend?\n>>> ").capitalize()
    friendAttitude = input("How is " + friend + " feeling on this " + weather + " day?\n>>> ")
    meal = input("What is " + mainCharacter + "'s favorite meal?\n>>> ")
    age = input("How old is " + mainCharacter + "?\n>>> ")
    friendAge = input("How old is " + friend + "?\n>>> ")
    timeUntilDeath = input("Exactly how many days remain until " + mainCharacter + "'s death?\n>>> ")
    time = input("What time is it?\n>>> ")
    
    now = datetime.now()
    currentTime = now.strftime("%H:%M")
    if (time != currentTime):
        print("Liar.\n")
    print("It's " + currentTime + " in " + location + ", a rather " + attitude + " day for " + mainCharacter +
          " who will die in " + timeUntilDeath + " days.")
    print("Things take a turn for the better as " + mainCharacter + " sees their best friend, " + friend +
          " approaching with their favorite meal, " + meal + ".")
    print("Suddenly, the weather changes, it is now " + weather + ". This change doesn't bother " + friend +
          " though, who seems " + friendAttitude + " as can be.")
    print('"Why the ' + meal + '?", ' + mainCharacter + " asks.")
    print('"Because it is your birthday!", exclaims ' + friend + '. You are ' + age + ' now, so you will die in ' 
          + timeUntilDeath + ' days.')
    print(mainCharacter + " almost forgot it's their birthday, and is reminded they need to get ready for " +
          friend + "'s " + friendAge + "th birthday which is next week.")
    print("The two blissfully celebrate this occassion, only perpetuating the descent of their poor souls into limbo.")
    print("The end. Would you like to create another story?(y/n)")
    yn = input(">>> ")
    if (yn == "y"):
        continue
    else:
        print("Goodbye.")
        storyTime = False
    