from fastapi import APIRouter

router = APIRouter(
    prefix="/summary",
    tags=["summary"]
)

@router.get("/")
async def summary_status():
    return {"message": "summary router working"}