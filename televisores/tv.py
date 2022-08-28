class TV:
    numTV=0
    def __init__(self,marca,boolean):
        self.__marca=marca
        self.__estado=boolean
        self.__canal=1
        self.__volumen=1
        self.__precio=500
        numTV=numTV+1
        self.__control=None
    def turnOn(self):
        if (self.__estado==False):
            self.__estado=True
    def turnOff(self):
        if (self.__estado==True):
            self.__estado=False
    def getEstado(self):
        return self.__estado
    def getMarca(self):
        return self.__marca
    def getControl(self):
        return self.__control
    def getPrecio(self):
        return self.__precio
    def getVolumen(self):
        return self.__volumen
    def getCanal(self):
        return self.__canal
    def setMarca(self,marca):
        self.__marca=marca
    def setControl(self,control):
        self.__control=control
    def setPrecio(self,precio):
        self.__precio=precio
    def setVolumen(self,volumen):
        if(0<=volumen and volumen<=7):
            self.__volumen=volumen
    def setCanal(self,canal):
        if(1<=canal and canal<=120):
            self.__canal=canal
    def volumenUp(self):
        if(0<=self.__volumen and self.__volumen<7):
            self.__volumen=self.__volumen+1
    def canalUp(self):
        if(1<=self.__canal and self.__canal<120):
            self.__canal=self.__canal+1
    def volumenDown(self):
        if(0<self.__volumen and self.__volumen<=7):
            self.__volumen=self.__volumen-1
    def canalDown(self):
        if(1<self.__canal and self.__canal<=120):
            self.__canal=self.__canal-1

    @classmethod
    def getNumTV(cls):
        return cls.numTV
    def setNumTV(cls,num):
        cls.numTV=num

