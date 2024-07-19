class Character:
    def __init__(self, name: str, health: int, power: int) -> None:
        self.name = name
        self.health = health
        self.power = power
        
    def attack(self) -> None:
        """Does nothing without a character object made."""
        pass
    
    def defend(self) -> None:
        """Does nothing without a character object made."""
        pass
    
class Warrior(Character):
    def __init__(self, name, health, power, weapon: list[str]) -> None:
        super().__init__(name, health, power)
        self.name = name
        self.health = health
        self.power = power
        self.weapon = weapon
        
    def attack(self) -> str:
        """Describes the attack move that the Warrior class makes."""
        return f"{self.name} swings their {self.weapon[0]} fiercely."
    
    def defend(self) -> str:
        """Describes the defend move that the Warrior class makes."""
        return f"{self.name} raises their {self.weapon[1]} to block the attack."
    
    def __str__(self) -> str:
        """Prints the character attributes and their attack and defend moves."""
        return f"""
{self.name}:
Health: {self.health}
Power: {self.power}
{self.attack()}
{self.defend()}"""

    def __repr__(self) -> str:
        """For debugging the object attributes and methods."""
        return f"Warrior({self.name}, {self.health}, {self.power}, {self.weapon})"
    
class Mage(Character):
    def __init__(self, name, health, power, spell: list[str]) -> None:
        super().__init__(name, health, power)
        self.name = name
        self.health = health
        self.power = power
        self.spell = spell
        
    def attack(self) -> str:
        """Describes the attack move that the Mage class makes."""
        return f"{self.name} casts the {self.spell[0]} spell at the enemy."
    
    def defend(self) -> str:
        """Describes the defend move that the Mage class makes."""
        return f"{self.name} summons a {self.spell[1]} for protection."
    
    def __str__(self) -> str:
        """Prints the character attributes and their attack and defend moves."""
        return f"""
{self.name}:
Health: {self.health}
Power: {self.power}
{self.attack()}
{self.defend()}"""
    
    def __repr__(self) -> str:
        """For debugging the object attributes and methods."""
        return f"Mage({self.name}, {self.health}, {self.power}, {self.spell})"
    
class Rogue(Character):
    def __init__(self, name, health, power, agility: list[str]) -> None:
        super().__init__(name, health, power)
        self.name = name
        self.health = health
        self.power = power
        self.agility = agility
        
    def attack(self) -> str:
        """Describes the attack move that the Rogue class makes."""
        return f"{self.name} strikes swiftly from the shadows with {self.agility[0]}."
    
    def defend(self):
        """Describes the defend move that the Rouge class makes."""
        return f"{self.name} uses their {self.agility[1]} to dodge the opponent's attack."
    
    def __str__(self) -> str:
        """Prints the character attributes and their attack and defend moves."""
        return f"""
{self.name}:
Health: {self.health}
Power: {self.power}
{self.attack()}
{self.defend()}"""
    
    def __repr__(self) -> str:
        """For debugging the object attributes and methods."""
        return f"Rouge({self.name}, {self.health}, {self.power}, {self.agility})"

    
Aldric = Warrior('Aldric', 100, 20, ['Broadsword', 'shield'])
Elara = Mage('Elara', 80, 30, ['Fireball', 'magical barrier'])
Kai = Rogue('Kai', 90, 25, ['stealth agility', 'quick reflexes'])
characters = [Aldric, Elara, Kai]

def list_characters(object_list: list[object]) -> str:
    """Takes a list of objects and prints their attributes and moveset."""
    for character in object_list:
        print(character)
        
def debug_characters(object_list: list[object]) -> str:
    """Prints a list of raw object attributes and class-specific methods."""
    for character in object_list:
        print(repr(character))

list_characters(characters)
#debug_characters(characters)
