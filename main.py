from fastapi import FastAPI, status, HTTPException
from fastapi.responses import JSONResponse
import uuid

app = FastAPI(
    title="MLOPs first API",
    description="MLOPs API",
    version="0.0.1"
)


@app.post("/users", tags=["Users"])
async def create_user(data: dict):
    name = data["name"]
    email = data["email"]

    return {
        "status_code": 200,
        "message": f"user {name}, with email {email}"
                   f"created successfully with the ID {str(uuid.uuid4())}",
    }


@app.post("/products", tags=["Products"])
async def create_product(product_name: str, product_price: float):

    try:
        return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content={
                "message": f"product {product_name}, with price"
                           f" {product_price}",
                "id": str(uuid.uuid4())
            }
        )
    except Exception as e:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )


@app.get("/get-users/{user_id}", tags=["Users"])
async def get_users(user_id: str):
    users_db = {
        "70": {
            "name": "Napster",
            "email": "testing@napster.com",
        },
        "91": {
            "name": "Jorge",
            "email": "napster@napster.com",
        }
    }

    try:
        user = users_db[user_id]
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "message": f"user {user['name']}, with email {user['email']}"
            }
        )
    except Exception as e:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )
