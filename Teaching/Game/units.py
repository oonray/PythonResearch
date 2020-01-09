"""
@author oonray
@brief This is the unit module

This module contains all the units in the game.
"""
import re

class unit:
    """
        @brief This is the base unit class.
        @param health the health of the unit
        @param name the name of the unit

        This is the base unit class.
        It contains health and the fuctions to manipulate it.

        @note the parameters are passed as keyword arguments

        """
    def __init__(self,**kwargs):
        """
        @brief The unit constructor
        @param health the health of the unit.
        """
        self.name = kwargs["name"]
        self.health=kwargs["health"]
        self.pools = {}

        if "mana" in kwargs: self.pools["mana"] = kwargs["mana"]
        else: self.pools["mana"] = 0
        if "stamina" in kwargs: self.pools["stamina"] = kwargs["stamina"]
        else: self.pools["stamina"] = 0

        if "title" in kwargs: self.title = kwargs["title"]

        if "abilities" in kwargs: self.abilities = kwargs["abilities"]
        else: self.abilities = {}

    def damage(self,amount):
        """
        @brief allows the unit to take n damage
        @param amount the amount of damage taken
        """
        self.health = self.health - amount

    def heal(self,amount):
        """
        @brief allows the unit to be healed
        @param amount the amount of healing recieved
        """
        self.health = self.health + amount

    def show_health(self):
        """
        @brief Displays the health
        @returns int the health of the unit.
        """
        return self.health

    def give_title(self,title):
        """
        @brief Award unti with legendary title
        @param title the title to award it
        """
        self.title = title

    def learn_ability(self,ability):
        """
        @brief updates the abilities of the character
        @param ability (class ability) the new ability
        """
        self.abilities[ability.name] = ability

    def get_abilities(self):
        """
        @brief Lists avalibale abilities
        @returns (list) abilities
        """
        return self.abilities.keys()

    def use_abillity_self(self,name):
        """
        @brief Use ability on self
        @param name name of the ability
        """
        self.abilities[name].use(self)

    def use_abillity_target(self,name,target):
        """
        @brief  Use ability on target
        @param name name of the ability
        """
        self.abilities[name].use(target)

    def check_cost(self,name,cost):
        """
        @brief checks if we have enough action points to preform an action
        @param name The name of the pool
        @param cost The cost of the action
        """
        if self.pools[name] >= cost:
            return True
        else: return False

    def __str__(self):
        if hasattr(self,"title"):
            return "{}: {} {}, Health: {}".format(
                    self.__class__.__name__.capitalize(),
                    self.name,
                    self.title,
                    self.health)
        else:
            return "{}: {}, Health: {}".format(
                    self.__class__.__name__.capitalize(),
                    self.name,
                    self.health)


class hero(unit):
    def __init__(self,**kwargs):
        unit.__init__(self,**kwargs)

class enemy(unit):
    def __init__(self,**kwargs):
        unit.__init__(self,**kwargs)

if __name__ == "__main__":
    title="The Bringer OF Darkness"
    bob = enemy(health=100,name="Bob")
    bob.damage(10)
    if(bob.show_health() == 90):
        print("Pass! Damage Function Works! {}".format(bob))
    else:
        print("Fail! {} took no damage!".format(bob))

    if re.search(title,bob.__str__()) is None:
        print("Pass! {} has no title".format(bob))
    else:
        print("Fail! {} has title".format(bob))

    bob.give_title(title)
    bob.heal(10)

    if(bob.show_health() == 100):
        print("Pass! Heal Function Works! {}".format(bob))
    else:
        print("Fail! {} was not healed".format(bob))

    if re.search(title,bob.__str__()) is not None:
        print("Pass! {} has title".format(bob))
    else:
        print("Fail! {} has no title".format())

