from dataclasses import dataclass


@dataclass
class Album:
    id: str
    name: str
    artist: str
    release_date: str
    is_single: bool
    is_compilation: bool

    def __iter__(self):
        return iter([self.id, self.artist, self.name, self.release_date,
                     self.is_single, self.is_compilation])
