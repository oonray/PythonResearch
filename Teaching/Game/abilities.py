"""
@author oonray
@brief Conatins all the abilities
"""
class magic():
    def __init__(self,**kwargs):
        self.cost = kwargs["cost"]
        self.type = "mana"

class ranged():
    def __init__(self,**kwargs):
        self.cost = kwargs["cost"]
        self.type = "stamina"

class melee():
    def __init__(self,**kwargs):
        self.cost = kwargs["cost"]
        self.type = "stamina"

class ability:
    """
    @brief ability Base class
    @param name the name of the ability
    """
    def __init__(self,**kwargs):
        self.name = kwargs["name"]
        self.type = None
        self.cost = 0

    def use(self,target):
        if target.check_cost(self.type,self.cost):
                pass

