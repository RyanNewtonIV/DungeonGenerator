import time


class Attack():
    attackProperties = {}
    def __init__(self,secondsTillAttackLands,dodgeWindowinSeconds,parryWindowinSeconds,stringKeyDamageType):
        self.attackProperties = {
            'secondsTillAttackLands': secondsTillAttackLands,
            'dodgeWindowinSeconds': dodgeWindowinSeconds,
            'parryWindowinSeconds': parryWindowinSeconds,
            'DamageType': stringKeyDamageType

        }


class AttackContainer():
    attackDict = {}
    def __init__(self,startTime,endTime,listOfAttackObjects):
        self.attackDict = {
            'startTime': startTime,
            'endTime': endTime,
            'listOfAttackObjects': listOfAttackObjects
        }
