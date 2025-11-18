import keyboard
import time

class keyManager():

    trackedKey = {
        'Esc': {},
        'w': {},
        'a': {},
        's': {},
        'd': {}
    }

    def __init__(self):
        for key in self.trackedKey:
            self.trackedKey[key] = {"Pressed": False,
            "Held": False,
            "Released": False}

    def keyUpdate(self):
        for key in self.trackedKey:
            try:
                if keyboard.is_pressed(key):
                    if self.trackedKey[key]["Held"] == True:
                        pass
                    elif self.trackedKey[key]["Pressed"] == True:
                        self.trackedKey[key]["Held"] = True
                        self.trackedKey[key]["Pressed"] = False
                    else:
                        self.trackedKey[key]["Pressed"] = True
                else:
                    if self.trackedKey[key]["Held"] == True or self.trackedKey[key]["Pressed"] == True:
                        self.trackedKey[key]["Released"] = True
                        self.trackedKey[key]["Pressed"] = False
                        self.trackedKey[key]["Held"] = False
                    elif self.trackedKey[key]["Released"] == True:
                        self.trackedKey[key]["Released"] = False
                    else:
                        pass
            except:
                return False

    def checkKeyPressed(self,keyToCheck):
        return self.trackedKey[keyToCheck]["Pressed"]
    def checkKeyHeld(self,keyToCheck):
        return self.trackedKey[keyToCheck]["Held"]
    def checkKeyReleased(self,keyToCheck):
        return self.trackedKey[keyToCheck]["Released"]
