"""
Database Schemas

Define your MongoDB collection schemas here using Pydantic models.
These schemas are used for data validation in your application.

Each Pydantic model represents a collection in your database.
Model name is converted to lowercase for the collection name:
- User -> "user" collection
- Product -> "product" collection
- BlogPost -> "blogs" collection
"""

from pydantic import BaseModel, Field, HttpUrl
from typing import Optional
from datetime import datetime

# Example schemas (keep for reference):

class User(BaseModel):
    """
    Users collection schema
    Collection name: "user" (lowercase of class name)
    """
    name: str = Field(..., description="Full name")
    email: str = Field(..., description="Email address")
    address: str = Field(..., description="Address")
    age: Optional[int] = Field(None, ge=0, le=120, description="Age in years")
    is_active: bool = Field(True, description="Whether user is active")

class Product(BaseModel):
    """
    Products collection schema
    Collection name: "product" (lowercase of class name)
    """
    title: str = Field(..., description="Product title")
    description: Optional[str] = Field(None, description="Product description")
    price: float = Field(..., ge=0, description="Price in dollars")
    category: str = Field(..., description="Product category")
    in_stock: bool = Field(True, description="Whether product is in stock")

# KAIT20 Website Schemas

class News(BaseModel):
    """News items for the college website
    Collection: "news"
    """
    title: str = Field(..., description="News title")
    summary: str = Field(..., description="Short summary")
    content: Optional[str] = Field(None, description="Full content")
    image_url: Optional[HttpUrl] = Field(None, description="Optional image URL")
    published_at: Optional[datetime] = Field(None, description="Publish date/time")

class Event(BaseModel):
    """Events for the college website
    Collection: "event"
    """
    title: str = Field(..., description="Event name")
    description: str = Field(..., description="Event description")
    location: str = Field(..., description="Where it takes place")
    date: datetime = Field(..., description="Event date/time")
    link: Optional[HttpUrl] = Field(None, description="Registration or details link")

# Add your own schemas here if needed.
# The database viewer can discover these via the /schema endpoint implemented in backend.
