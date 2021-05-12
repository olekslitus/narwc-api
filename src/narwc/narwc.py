from __future__ import annotations
from enum import Enum
from typing import List, Dict, Iterator, Optional
import requests

WhaleID = str

class Gender(Enum):
    """Gender of a Whale"""

    F = "Female"
    M = "Male"

    def from_gender_code(gender_code: str) -> Gender:
        """Return Gender based on the given `gender_code`"""
        if gender_code == 'F':
            return Gender.F
        elif gender_code == 'M':
            return Gender.M
        else:
            raise ValueError(f'gender_code: {gender_code}')

class Sighting:
    """Sighting of a Whale"""
    pass

class Whale:
    """One Whale in North Atlantic Right Whale Catalog"""

    def __init__(self, whale_id: WhaleID, data: Dict) -> None:
        self.id = whale_id
        self.data = data
        
    def eg_no(self) -> WhaleID:
        """egNo (id) number of the Whale in the catalog"""
        return self.id

    def name(self) -> Optional[str]:
        """Name given to the Whale by NARWC"""
        return self.data['name']

    def is_dead(self) -> bool:
        """Is Whale dead? 
           Note: We cannot know if whale is alive
        """
        return self.data['deathYear'] is not None

    def birth_year(self) -> Optional[str]:
        """Year of the Whale birth"""
        return self.data['birthYear']

    def death_year(self) -> Optional[str]:
        """Year of the Whale death"""
        return self.data['deathYear']

    def gender(self) -> Gender:
        """Gender of the Whale"""
        gender_code = self.data['genderCode']
        return Gender.from_gender_code(gender_code)
    
    def mother_id(self) -> Optional[WhaleID]:
        """Get id of the mother"""
        mother_id = self.data['mother']
        return mother_id

    def father_id(self) -> Optional[WhaleID]:
        """Get id of the father"""
        father_id = self.data['father']
        return father_id

    def sightings(self) -> List[Sighting]:
        raise NotImplementedError

class Catalog:
    """Main access point to North Atlantic Right Whale Catalog"""

    HOME_ULR = 'https://rwcatalog.neaq.org'
    WHALES_PATH = 'whales'

    def whales() -> Iterator[Whale]:
        """Iterator over all whales in the catalog"""
        for whale_id in Catalog.whale_ids():
            yield Catalog.whale(whale_id)

    def whale_ids() -> List[WhaleID]:
        """Iterator over all whales ids in the catalog"""
        r = requests.get(Catalog.HOME_ULR + 
                         '/' + Catalog.WHALES_PATH)
        entries: Dict[str, WhaleID] = r.json()
        for entry in entries:
            yield entry['egNo']

    def whale(whale_id: WhaleID) -> Optional[Whale]:
        """Get Whale with given `whale_id`"""
        r = requests.get(Catalog.HOME_ULR + 
                         '/' + Catalog.WHALES_PATH + 
                         '/' + str(whale_id))
        if r.status_code != 200: return None
        whale_data: Dict = r.json()
        return Whale(whale_id, whale_data)