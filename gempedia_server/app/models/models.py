from pydantic import BaseModel, Field
from sqlalchemy import Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Page(Base):
    """
    SQLAlchemy model that represents a page in the database.
    """
    __tablename__ = "gemini_summary"

    id = Column(Integer, primary_key=True, index=True)
    gemini_summary = Column(Text, nullable=True)


class PageName(BaseModel):
    """
    Pydantic model for validating page name data.
    """
    page_name: str = Field(..., min_length=1, description="The name of the page")
