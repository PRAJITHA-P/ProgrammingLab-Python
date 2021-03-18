class time:
    def __init__(self,h,m,s):
        self.__h=h
        self.__m=m
        self.__s=s

    def __add__(self,obj):
        self.__h += obj.__h
        self.__m += obj.__m
        self.__s += obj.__s

        if(self.__s>=60):
            extra_minute =  int(self.__s/60)
            self.__s = self.__s%60
            self.__m += extra_minute

        if (self.__m >= 60):
            extra_hour = int(self.__m / 60)
            self.__m = self.__m % 60
            self.__h += extra_hour

        return "sum of 2 times= "+str(self.__h)+"h:"+str(self.__m)+"m:"+str(self.__s) +"s"
print("time1=6h:30m:2s")
print("time2=3h:80m:10s")
obj1 = time(6,30,2)
obj2  = time(3,80,10)

print(obj1+obj2)
