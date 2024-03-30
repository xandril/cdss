from fastapi import UploadFile
from pydantic import BaseModel


class BoundingBox(BaseModel):
    x0: int
    y0: int
    x1: int
    y1: int


class Predictions(BaseModel):
    labels: list[str]
    scores: list[float]
    bboxes: list[BoundingBox]


class PredictRequest(BaseModel):
    file: UploadFile


class PredictResponse(BaseModel):
    predictions: Predictions
