"""Main access point to North Atlantic Right Whale Catalog"""

from typing import List, Dict, Iterator, Optional, Any, Generator
import requests as rq
from narwc.whale import Whale, WhaleID


HOME_ULR = 'https://rwcatalog.neaq.org'
WHALES_PATH = 'whales'


def whales() -> Iterator[Optional[Whale]]:
    """Iterator over all whales in the catalog"""
    for whale_id in whale_ids():
        yield whale(whale_id)


def whale_ids() -> Generator[WhaleID]:
    """Iterator over all whales ids in the catalog"""
    r = rq.get(HOME_ULR + '/' + WHALES_PATH)
    entries: Dict[str, WhaleID] = r.json()
    for entry in entries:
        yield entry['egNo']


def whale(whale_id: WhaleID) -> Optional[Whale]:
    """Get Whale with given `whale_id`"""
    r = rq.get(HOME_ULR + '/' + WHALES_PATH + '/' + str(whale_id))

    if r.status_code != 200:
        return None

    whale_data: Dict[str, Any] = r.json()
    return Whale(whale_id, whale_data)
