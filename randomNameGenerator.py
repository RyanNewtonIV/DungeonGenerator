from random import Random

class RandomNameGenerator():

    boyNameDirectory = "Names/BoyFirstNames.csv"
    girlNameDirectory = "Names/GirlFirstNames.csv"
    lastNameDirectory = "Names/LastNames.csv"
    rand = Random()

    def returnRandomFirstName(self,gender):
        boyOrGirl = 0
        output = None
        if (str(gender).lower()[0] == "m"):
            boyOrGirl = 0
        elif (str(gender).lower()[0] == "f"):
            boyOrGirl = 1
        else:
            boyOrGirl = self.rand.randint(0, 1)

        if (boyOrGirl):
            output = self.pullRandomNameFromCSV(self.girlNameDirectory)
        else:
            output = self.pullRandomNameFromCSV(self.boyNameDirectory)
        return output.replace("\n","")

    def returnRandomLastName(self):
        return self.pullRandomNameFromCSV(self.lastNameDirectory).replace("\n","")

    def returnRandomFullName(self,gender):
        output = self.returnRandomFirstName(gender)
        output += " "
        output += self.pullRandomNameFromCSV(self.lastNameDirectory)
        return output.replace("\n","")

    def pullRandomNameFromCSV(self,filePathAndName):
        file = open((filePathAndName), "r", encoding="utf-8")
        dataList = file.readlines()
        file.close()
        return str(dataList[self.rand.randint(0,len(dataList))])
