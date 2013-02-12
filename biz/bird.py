import location
import intersect

class bird():
    def __init__(self,swarm,ifv):
        self.__ifv = ifv
        self.__ll = location.location()
        self.__ifv.drawBird(self)
        self.__swarm = swarm
        
    def getLocation(self):
        return self.__ll

    def setLocation(self,middle):
        intersections = intersect.getIntersectingPoints(self.__ll.getX(),self.__ll.getY(), g_flapperafstand, middle.getX(), middle.getY())
        if len(intersections) == 2:
            #Er worden normaal altijd 2 punten gevonden. Nu moet er bepaald worden wel punt er het dichtst bij het midden ligt
            if intersect.distanceBetweenPoints(snijpunten[0][0],snijpunten[0][1],midden.geefx(),midden.geefy()) <= intersect.distanceBetweenPoints(snijpunten[1][0],snijpunten[1][1],midden.geefx(),midden.geefy()):
                doel = snijpunten[0]               
            else:
                doel = snijpunten[1]
            #Doel is nu het wiskundige punt dat zich het dichtst bij het midden bevindt
            #Nu moet er getest worden of we dit doel kunnen bereiken (botsingen)
            if self.__zwerm.isLocationFree(doel):
                self.__ll.zetpunt(doel[0],doel[1])
        else:
            pass

    def fly(self,middle):
        self.setLocation(middle)
        self.__ifv.drawBird(self)