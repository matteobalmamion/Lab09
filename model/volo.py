from dataclasses import dataclass

from model.aereoporto import Aereoporto


@dataclass
class Volo:
    _id: int
    _start: int
    _arrive: int
    _distance:int

    @property
    def id(self):
        return self._id

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
        return hash(self.id)

    def __str__(self):
        return f'Volo {self.id}'