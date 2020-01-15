import time


class Loggable():

    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))

class LoggableList(Loggable, list):

    def append(self, _T) -> None:
        self._T = _T
        Loggable.log(self, self._T)
        list.append(self, _T)