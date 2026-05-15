from fastapi import APIRouter, HTTPException
from schemas import ColorRequest, ColorConvertResponse
from service import convert_color

router = APIRouter(prefix="/color", tags=["color"])


@router.post("/convert", response_model=ColorConvertResponse)
def convert(data: ColorRequest):
    if not data.color.strip():
        raise HTTPException(status_code=400, detail="Цвет не может быть пустым")
    result = convert_color(data.color.strip())
    return result