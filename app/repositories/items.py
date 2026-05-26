from app.models.base import Item

from .base import BaseRepository


class ItemRepository(BaseRepository[Item]):
    def __init__(self):
        super().__init__(Item)


item_repo = ItemRepository()
