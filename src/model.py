from dataclasses import dataclass


@dataclass
class Album:
    artist: str
    title: str
    release_year: int
    label: str
    cover_url: str
