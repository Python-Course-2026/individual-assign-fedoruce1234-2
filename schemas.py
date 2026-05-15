from pydantic import BaseModel, Field


class ColorRequest(BaseModel):
    color: str = Field(..., min_length=1, description="Цвет в формате HEX, RGB или HSL")


class ColorConvertResponse(BaseModel):
    hex: str = Field(..., description="Цвет в формате HEX")
    rgb: str = Field(..., description="Цвет в формате RGB")
    hsl: str = Field(..., description="Цвет в формате HSL")