# app/api/endpoints/cafes.py
from fastapi import APIRouter, HTTPException ,Query, status
from app.db.connection import get_connection
from app.schemas.cafe import Cafe, CafeBase, CafeCreate  
from app.core.config import settings



router = APIRouter()


#TODO: Add a method to fetch all the cafes from the database
# Api to fetch all cafes
@router.get("/")
async def get_all_cafes():
    conn = await get_connection()
    try:
        rows = await conn.fetch("SELECT * FROM cafes;")
        return [dict(row) for row in rows]
    finally:
        await conn.close()
        
#TODO: Add a method to add cafe to the database
# Api to add a cafe    
@router.post("/addcafe", response_model=Cafe, status_code=201)
async def create_cafe(cafe: CafeCreate):
    conn = await get_connection()
    try:
        # Insert a record into the cafes table and return the inserted row.
        row = await conn.fetchrow('''
            INSERT INTO cafes (name, city, has_wifi, rating)
            VALUES ($1, $2, $3, $4)
            RETURNING *
        ''', cafe.name, cafe.city, cafe.has_wifi, cafe.rating)
        return dict(row)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        await conn.close()
        
# Todo: Method to Get cafe by id
# Api to get cafe by id
@router.get("/{cafe_id}", response_model=Cafe)
async def get_cafe(cafe_id: int):
    conn = await get_connection()
    try:
        row = await conn.fetchrow("SELECT * FROM cafes WHERE id = $1;", cafe_id)
        if row is None:
            raise HTTPException(status_code=404, detail="Cafe not found")
        return dict(row)
    finally:
        await conn.close()

#TODO: Method to update cafe by id
# Api to update cafe by id
@router.put("/update_cafe/{cafe_id}", response_model=Cafe)
async def update_cafe(cafe_id: int, cafe: CafeBase):
    conn = await get_connection()
    try:
        row = await conn.fetchrow('''
            UPDATE cafes
            SET name = $1, city = $2, has_wifi = $3, rating = $4
            WHERE id = $5
            RETURNING *
        ''', cafe.name, cafe.city, cafe.has_wifi, cafe.rating, cafe_id)
        if row is None:
            raise HTTPException(status_code=404, detail="Cafe not found")
        return dict(row)
    finally:
        await conn.close()
        
# Method to delete cafe by id
# Api to delete cafe by id
@router.delete("/delete_cafe/{cafe_id}", status_code=status.HTTP_200_OK)
async def delete_cafe(
    cafe_id: int,
    secret_key: str = Query(..., description="Secret key for authentication")
):
    if secret_key != settings.secret_key: # delete cafe by id when secret key is valid
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Forbidden: Invalid secret key"
        )
    
    conn = await get_connection()
    try:
        row = await conn.fetchrow("DELETE FROM cafes WHERE id = $1 RETURNING *;", cafe_id)
        if row is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Cafe not found"
            )
        return {"message": f"Cafe with ID {cafe_id} deleted successfully."}
    finally:
        await conn.close()