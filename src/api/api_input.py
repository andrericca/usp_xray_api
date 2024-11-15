from fastapi import APIRouter

router = APIRouter(prefix="/xray")

@router.get("/")
async def get_clients_data():
    print(1)

    return 1