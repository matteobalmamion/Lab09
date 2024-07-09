from dataclasses import dataclass

@dataclass
class Aereoporto:
    _id: int
    _name: str
    _city:str
    _state:str

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def city(self):
        return self._city

    @property
    def state(self):
        return self._state

    def __hash__(self):
        return hash(self._id)

    def __str__(self):
        return f"Aereoporto {self._name} di {self._city}, {self._state}"