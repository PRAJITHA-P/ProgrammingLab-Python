class time:
    def __init__(self,hour,minute,second):
        self.__hour=hour
        self.__minute=minute
        self.__second=second

    def __add__(self, other):
        self.__hour += other.__hour
        self.__minute +=other.__minute
        self.__second +=other.__second

        if (sel.__second>=60):
            extra_hour=int(self.__minute/60)
            self.__minute