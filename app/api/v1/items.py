from fastapi import APIRouter

router = APIRouter(prefix="/items", tags=["items"])

@router.get("/", response_model=list)
async def list_items():
    """Return a list of example items"""
    return [
        {"id": 1, "name": "Item One"},
        {"id": 2, "name": "Item Two"}
    ] 