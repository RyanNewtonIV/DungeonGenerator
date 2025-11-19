import time
import random

class consoulsGameData:

    dictAttackTypes = {
        'slashing': {
            'minDodgeTime': .2,
            'maxDodgeTime': .7,
            'minParryTime': .1,
            'maxParryTime': .3,
        },
        'piercing': {
            'minDodgeTime': .2,
            'maxDodgeTime': .7,
            'minParryTime': .1,
            'maxParryTime': .3,
        },
        'blunt': {
            'minDodgeTime': .2,
            'maxDodgeTime': .7,
            'minParryTime': .1,
            'maxParryTime': .3,
        }
    }

    def getDictAllAttackTypes(self):
        return self.dictAttackTypes()

    def getDictSpecificAttackData(self,attackType):
        return self.dictAttackTypes[attackType]

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
    def __init__(self,StringAttackName,numberOfAttacks,startTime,endTime):


        # for i in range(0,numberOfAttacks):
        #
        # self.attackDict = {
        #     'startTime': startTime,
        #     'endTime': endTime,
        #     'listOfAttackObjects': listOfAttackObjects
        # }

        pass


    """
    WIP need to finish the createNewAttackSequenceList method. This should finish with a list
    populated with 'numberOfStrikes' number of attack objects, each with an appropriately populated
    dodge/parry/damage window to correspond with the attackType in the consoulsGameData class's dictionary
    """
    def createNewAttackSequenceList(self,StringAttackName,numberOfStrikes,listOfAvailableAttackTypes,windUpTime,minSpacing,maxSpacing):
        newAttackList = []
        attackSpacer = 0.0
        for i in range(0,numberOfStrikes):
            baseDodgeWindow = random.uniform(0,.5)+.2
            baseParryWindow = random.uniform(0,.2)+.1
            secstillAttackLands = baseDodgeWindow+baseParryWindow
            attackSpacer += secstillAttackLands
            damageType = random.choice(listOfAvailableAttackTypes)
            newAttack = Attack(secstillAttackLands,baseDodgeWindow,baseParryWindow,)
            newAttackList.append(Attack())





    def setAttackDict(self,dictionaryOfAttacks):
        self.attackDict = dictionaryOfAttacks
