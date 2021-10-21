import random
#I seperated the classes from the game's streamlined functionality like this to avoid clutter.
#It'll be a bit more of a pain to turn in, but writing it will be easier.

class Entity:
    battleItems = []
    name = str
    maxHp = int
    currentHp = int
    
    def TakeDamage(self, dmg: int):
        self.currentHp -= dmg
        if (dmg > 0):
            print("\n" + self.name + " took " + str(dmg) + " damage!")
        if (self.currentHp < 0):
            self.currentHp = 0
        
    def Heal(self, healAmount: int):
        self.currentHp += healAmount
        print("\n" + self.name + " healed for " + str(healAmount) + " HP!")
        if (self.currentHp > self.maxHp):
            self.currentHp = self.maxHp
        


class Item:
    battleItem = bool
    heal = bool
    itemName = str
    def __init__(self, name: str):
        self.battleItem = False
        self.heal = False
        self.itemName = name
    def UseItem(self) -> int:
        pass

class Weapon(Item):
    minDamage = int
    maxDamage = int
    accuracy = int
    
    def __init__(self, name: str, mindamage: int, maxdamage: int, accuracy: int):
        self.battleItem = True
        self.heal = False
        self.itemName = name
        self.minDamage = mindamage
        self.maxDamage = maxdamage
        self.accuracy = accuracy
    def UseItem(self) -> int:
        damage = random.randint(self.minDamage, self.maxDamage)
        if (self.accuracy < random.randint(1, 100)):
            print("\nThe " + self.itemName + " missed!")
            damage = 0
        return damage
class MagicStone(Item):
    minHeal = int
    maxHeal = int
    
    def __init__(self, name: str, minheal: int, maxheal: int):
        self.battleItem = True
        self.heal = True
        self.itemName = name
        self.minHeal = minheal
        self.maxHeal = maxheal
    def UseItem(self) -> int:
        return random.randint(self.minHeal, self.maxHeal)
        

class Monster(Entity):
    introduction = str
    
    def __init__(self, name: str, hp: int, introduction: str, items: []):
        self.battleItems = items
        self.name = name
        self.maxHp = hp
        self.currentHp = hp
        self.introduction = introduction


class Room:
    #I hate non-specific array type declaration!
    bossRoom: bool

    items = []
    actions = []
    def __init__(self, content: []):
        self.bossRoom = False
        self.items = content
        self.MakeActions()
    def MakeActions(self):
        self.actions = ["\n>Next room", "\n>Quit"]
        for item in self.items:
            self.actions.append("\n>Take " + item.itemName)
        
    def Search(self, searchEntry: str) -> Item:
        itemIndex = 0
        for item in self.items:
            if (item.itemName.lower() == searchEntry):
                self.items.remove(item)
                self.actions.remove("\n>Take " + item.itemName)
                print("You picked up a " + item.itemName.lower() + "!")
                return item
            itemIndex += 1
        #Item not found
        for item in self.items:
            if (CorrectionSuggestor.CheckSimilarity(item.itemName.lower(), searchEntry)):
                suggestion = input("There is no '" + searchEntry + "' in this room, did you mean " + item.itemName.lower() +"?(y/n)\n>>> ").lower()
                if (suggestion == "y"):
                    return self.Search(item.itemName.lower())
                return None
        print("There is no " + searchEntry + " in this room.")
        return None
    def PrintActions(self):
        for action in self.actions:
            if (action != ""):
                print(action)
            
    #debug function
    def CheckContent(self):
        for item in self.items:
            print(item.itemName)
        for action in self.actions:
            print(action)
            
class BossRoom(Room):
    boss = Monster
    def __init__(self, monster: Monster):
        self.bossRoom = True
        self.boss = monster
    def PrintActions(self):
        print("\n>Fight " + self.boss.name)

class Floor:
    rooms = []
    def __init__(self, rooms: []):
        self.rooms = rooms
    
class Building:
    secretWeapon = Weapon
    floors = []
    #Create and customize the game here
    def GenerateLayout(self):
        
        #Weapon declaration
        badSword = Weapon("Wooden Sword", 10, 15, 80)
        decentSword = Weapon("Stone Sword", 40, 60, 85)
        greatSword = Weapon("Claymore", 80, 90, 90)
        
        badMagicStone = MagicStone("Dirty Magic Stone", 10, 20)
        decentMagicStone = MagicStone("Polished Magic Stone", 30, 50)
        greatMagicStone = MagicStone("Supreme Magic Stone", 95, 100)
        
        #Item declaration
        coin = Item("Coin")
        bucket = Item("Bucket")
        debris = Item("Debris")
        rope = Item("Rope")
        meat = Item("Meat")
        book = Item("Book")
        chicken = Item("Chicken")
        stone = Item("Stone")
        waterBottle = Item("Water Bottle")
        doubloon = Item("Shiny Doubloon")
        meltedIceCube = Item("Melted Ice Cube")
        
        firstMonster = Monster("Feeble Monster", 80, "\nYou wanna get to the next floor? You gotta get through me first!",
                               [badSword])
        secondMonster = Monster("Mighty Monster", 150, "\nYou will not pass.", [badSword, decentSword])
        finalMonster = Monster("Almighty Monster", 400, "\nI will guard my treasure to myy last breath!", [badSword, decentSword, greatSword])
        
        #Room declaration
        f1r1 = Room([meltedIceCube])
        f1r2 = Room([coin, bucket])
        f1r3 = Room([debris, badSword])
        f1r4 = Room([coin, badMagicStone, bucket])
        f1r5 = BossRoom(firstMonster)
        
        f2r1 = Room([rope, bucket, debris])
        f2r2 = Room([meat, stone, decentMagicStone])
        f2r3 = Room([book, coin, chicken])
        f2r4 = Room([decentSword, stone, bucket, rope])
        f2r5 = BossRoom(secondMonster)
        
        f3r1 = Room([bucket, doubloon, greatSword])
        f3r2 = Room([waterBottle, stone, book])
        f3r3 = Room([greatMagicStone, doubloon])
        f3r4 = Room([meat, rope, stone])
        f3r5 = BossRoom(finalMonster)
        
        f1 = Floor([f1r1, f1r2, f1r3, f1r4, f1r5])
        f2 = Floor([f2r1, f2r2, f2r3, f2r4, f2r5])
        f3 = Floor([f3r1, f3r2, f3r3, f3r4, f3r5])
        
        secretWeapon = Weapon("Horrifying Weapon That Can Kill Anything Instantly (with the caviat that its name is really hard to enter)",
                     1000, 2000, 95)
        self.secretWeapon = secretWeapon
        
        self.floors = [f1, f2, f3]
        #Floor declaration
    
class Player(Entity):
    inventory = []
    currentFloorIndex = 0
    currentRoomIndex = 0
    
    def __init__(self, name: str, hp: int):
        self.name = name
        self.maxHp = hp
        self.currentHp = hp
    
    def PrintInventory(self):
        for item in self.inventory:
            print(item)
    
    def GetRoom(self, building: Building) -> Room:
        return building.floors[self.currentFloorIndex].rooms[self.currentRoomIndex]

class CorrectionSuggestor:
    
    #Is this function very optimized? Probably not, but it does work.
    def CheckSimilarity(userInput: str, check: str) -> bool:
        if (len(check) == len(userInput)):
            totalLetters = len(check)
            charsInCommon = 0
            
            charIndex = 0
            for character in check:
                if (userInput[charIndex] == character):
                    charsInCommon += 1
                charIndex += 1
            
            if ((charsInCommon / totalLetters) >= 0.75):
                return True
            return False
        return False
        