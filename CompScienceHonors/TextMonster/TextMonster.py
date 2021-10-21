import GameClasses
import random
import sys

#Make sure the other file in this folder is named "GameClasses" or it won't import properly

def Battle(player: GameClasses.Player, monster: GameClasses.Monster):
    ongoing = True
    playerTurn = True
    print(monster.introduction)
    print("\n(Enter '/ss' and an item's name to get its stats!)\n")
    while (ongoing):
        if (playerTurn):
            print("\nPlayer HP: " + str(player.currentHp) + "/" + str(player.maxHp) + 
              "\n" + monster.name + " HP: " + str(monster.currentHp) + "/" + str(monster.maxHp))
            print("ITEMS:")
            for bi in player.battleItems:
                print("\n>" + bi.itemName)
            useItem = input("Which item would you like to use?\n>>> ").lower()
            for bi in player.battleItems:
                if (useItem == bi.itemName.lower()):
                    if (bi.heal):
                        player.Heal(bi.UseItem())
                    else:
                        monster.TakeDamage(bi.UseItem())
                    playerTurn = False
            if ("/ss " in useItem):
                useItem = useItem.replace("/ss ", "")
                for battleitem in player.battleItems:
                    if (battleitem.itemName.lower() == useItem):
                        if (battleitem.heal):
                            print("\nThis magic stone heals the player for a number between " + str(battleitem.minHeal) + " and " 
                                  + str(battleitem.maxHeal) + ".")
                        else:
                            print("\nThis sword damages the monster for a number between " + str(battleitem.minDamage) + " and " 
                                  + str(battleitem.maxDamage) + ".")
                        break
        else:
            #Having to simply remember method names because Python's types are dynamic really makes me appreciate C# and its
            #compiler very very much!
            player.TakeDamage(monster.battleItems[random.randint(0, len(monster.battleItems) - 1)].UseItem())
            playerTurn = True
        if (player.currentHp == 0):
            print("\nPlayer HP: " + str(player.currentHp) + "/" + str(player.maxHp) + 
              "\n" + monster.name + " HP: " + str(monster.currentHp) + "/" + str(monster.maxHp))
            print("You have been bested. Game over.")
            sys.exit()
        elif (monster.currentHp == 0):
            print("\nPlayer HP: " + str(player.currentHp) + "/" + str(player.maxHp) + 
              "\n" + monster.name + " HP: " + str(monster.currentHp) + "/" + str(monster.maxHp))
            print("You have beaten " + monster.name + "!")
            ongoing = False
            
def PrintLocation(player: GameClasses.Player):
    print("You are now in room " + str(player.currentRoomIndex + 1) + ", floor " + str(player.currentFloorIndex + 1) + ".")

building = GameClasses.Building()
building.GenerateLayout()

player = GameClasses.Player("Player", 100)

gameRunning = True
print("Welcome to Text Monster.")
print("You begin in a room seemingly empty. Enter /a to see your available actions.")
while (gameRunning):
    playerInput = input(">>> ").lower()
    #Action search command
    if (playerInput == "/a"):
        player.GetRoom(building).PrintActions()
    #Move to next room command
    elif (playerInput == "next room"):
        if (player.currentRoomIndex == 4):
            print("There is no next room.")
        else:
            player.currentRoomIndex += 1
            PrintLocation(player)
    #Move to last room command
    elif (playerInput == "last room"):
        if (player.currentRoomIndex == 0):
            print("There is no room preceding this.")
        else:
            player.currentRoomIndex -= 1
            PrintLocation(player)
    #Search room items by keyword, return found item and append player's respective inventory
    elif ("take " in playerInput):
        playerInput = playerInput.replace("take ", "")
        foundItem = player.GetRoom(building).Search(playerInput)
        if (foundItem == None):
            pass
        elif (foundItem.battleItem):
            player.battleItems.append(foundItem)
        else:
            player.inventory.append(foundItem)
    #Quit game command
    elif (playerInput == "quit"):
        gameRunning = False
        print("Goodbye.")
    #Initiate battle command
    elif ("fight" in playerInput):
        if (player.GetRoom(building).bossRoom):
            Battle(player, player.GetRoom(building).boss)
            
            if (player.currentFloorIndex == 2):
                print("You found the treasure! You win.")
                sys.exit()
            player.currentHp = player.maxHp
            player.currentRoomIndex = 0
            player.currentFloorIndex += 1
            PrintLocation(player)
        else:
            print("There is nothing to fight in this room.")
            
    #---HIDDEN COMMANDS---        
    
    #Check room's content command (debug)
    elif (playerInput == "/cc"):
        player.GetRoom(building).CheckContent()
    #Print player's inventory command (debug)
    elif (playerInput == "/pi"):
        player.PrintInventory()
    #Gives player completely overpowered weapon command
    elif (playerInput =="/ilcs!"):
        print("You're a filthy cheater but that's ok becuase itlcs!")
        player.battleItems.append(building.secretWeapon)
        player.name = "Cheater"
    #No found command
    else:
        actions = ["/a", "next room", "last room", "take"]
        foundAction = False
        for action in actions:
            if (GameClasses.CorrectionSuggestor.CheckSimilarity(playerInput, action)):
                print("That is not an action (you may have meant '" + action + "')")
                foundAction = True
                break
        if (foundAction == False):    
            print("That is not an action.")