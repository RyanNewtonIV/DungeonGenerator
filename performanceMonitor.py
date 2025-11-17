from collections import deque
import time

class performanceMonitor():

    processesMonitoring = {}
    listOfAverages = []
    updateTicker = 0
    def __init__(self):
        pass

    def startLogProcessTime(self,stringIDForProcess):
        if stringIDForProcess in self.processesMonitoring:
            dequeProcessTimeLog = self.processesMonitoring.get(stringIDForProcess)
            dequeProcessTimeLog.appendleft(float(time.time()))
            if len(dequeProcessTimeLog) > 60:
                dequeProcessTimeLog.pop()
        else:
            self.processesMonitoring.update({stringIDForProcess: deque([time.time()])})

    def endLogProcessTime(self,stringIDForProcess):
        if stringIDForProcess in self.processesMonitoring:
            dequeProcessTimeLog = self.processesMonitoring.get(stringIDForProcess)
            oldtime = dequeProcessTimeLog.popleft()
            currentTime = time.time()
            newtime = currentTime-oldtime
            # print(f"{currentTime:,.4f}-{oldtime:,.4f}={newtime:,.4f}")
            # time.sleep(3)
            dequeProcessTimeLog.appendleft(newtime)

    def returnAverageStringsList(self,fps):
        if fps == 0:
            fps = 1
        if self.updateTicker == 0:
            self.listOfAverages = []
            for i in self.processesMonitoring:
                averageTime = 0.0
                for j in self.processesMonitoring.get(i):
                    averageTime += j
                averageTime = averageTime/len(self.processesMonitoring.get(i))
                self.listOfAverages.append(f"{i} {averageTime/(1/fps)*100:.1f}% | {averageTime:,.4f}(s) ")
            self.updateTicker = 100

        else:
            self.updateTicker -= 1
        return self.listOfAverages

    # processTime = time.time() - timeKeeper
    # framePercentage = processTime / (1 / fps) * 100
    # return f"{processLabelString}: {framePercentage:.1f}% | {processTime:,.4f}(s)"


    """
    A Dictionary with the keys being the different processes I am monitoring.
    Each item in the dictionary is itself a dictionary that has
    -a string for the name of the process
    -and then a list of the past 60 times that is averaged each second
    """