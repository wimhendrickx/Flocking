import abc

class ivisualizer(object):
    __metaclass__ = abc.ABCMeta
    '''Het contract waaraan de kinderen moeten voldoen'''
    
    @abc.abstractmethod
    def drawBird(self,vogel,nieuw):
        return
       
class graphicvisualizer(ivisualizer):
    '''Hier wordt de grafische interface gedefinieerd'''
    def __init__(self):
       self.client = ThreadedClient()
       print ('en hier')
    
    def drawBird(self,vogel):
        pass    

class testvisualizer(ivisualizer):
    def __init__(self):
        pass

    def drawBird(self,vogel):
        pass