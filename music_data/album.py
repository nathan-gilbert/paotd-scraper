from dataclasses import dataclass


@dataclass
class Album:
    id: str
    name: str
    artist: str
    releaseDate: str
    isSingle: bool
    isCompilation: bool
