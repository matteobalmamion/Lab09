from dataclasses import dataclass

from model.aereoporto import Aereoporto


@dataclass
class Tratta:
    _start: Aereoporto
    _arrive: Aereoporto
    _distance:float

    @property
    def arrive(self):
        return self._arrive

    @property
    def distance(self):
        return self._distance

    @property
    def start(self):
        return self._start

    def __hash__(self):
        return hash(self.start+" "+self.arrive+" "+self.distance)

    def __str__(self):
        return f' Tratta {self.start}-self.{self.arrive}: {self.distance}'