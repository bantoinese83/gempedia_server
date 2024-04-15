# routes.py
from fastapi import APIRouter, HTTPException
from fastapi import Path

from app.models.models import PageName
from app.services.wiki_service import get_page_details

router = APIRouter()


@router.get("/page/{page_name}", tags=["Page"], description="Get page details")
def get_page(page_name: str = Path(..., example="Python (programming language)")):
    page_name_model = PageName(page_name=page_name)
    page_details = get_page_details(page_name_model.page_name)
    if page_details is None:
        raise HTTPException(status_code=400, detail="Error getting page")
    return page_details
