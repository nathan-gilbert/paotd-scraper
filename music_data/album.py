from dataclasses import dataclass


@dataclass
class Album:
    id: str
    name: str
    artist: str
    releaseDate: str
    isSingle: bool
    isCompilation: bool

    def __iter__(self):
        return iter([self.id, self.artist, self.name, self.releaseDate,
                     self.isSingle,self.isCompilation])
