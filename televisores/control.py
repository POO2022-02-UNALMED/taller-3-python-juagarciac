class Control:
    def __init__(self):
        self.__tv=None
    def enlazar(self,tv):
        self.__tv=tv
        tv.setControl(self)
    def getTv(self):
        return self.__tv
    def setTv(self,tv):
        self.__tv=tv
   