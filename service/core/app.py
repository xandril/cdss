import io
import logging

from PIL import Image
from fastapi import FastAPI, UploadFile, File
from ultralytics import YOLO

from service.core.config import WEIGHTS_PATHS
from service.core.data_model import Predictions, BoundingBox

app = FastAPI()


def get_yolo_output(image, yolo_model: YOLO) -> dict[str]:
    yolo_outputs = yolo_model.predict(image)
    class_names = yolo_model.names
    labels = []
    confidences = []
    bboxes = []
    for yolo_output in yolo_outputs:
        yolo_output = yolo_output.cpu()
        cur_labels = [class_names[i] for i in yolo_output.boxes.cls.to(int).tolist()]
        labels.extend(cur_labels)

        cur_confidences = yolo_output.boxes.conf.tolist()
        confidences.extend(cur_confidences)
        cur_bboxes = map(lambda bbox: BoundingBox(x0=(bbox[0]), y0=(bbox[1]), x1=(bbox[2]), y1=(bbox[3])),
                         yolo_output.boxes.xyxy.to(int).tolist())

        bboxes.extend(cur_bboxes)
    return {'labels': labels,
            'scores': confidences,
            'bboxes': bboxes,
            }


def make_predictions(image: Image.Image) -> Predictions:
    bboxes = []
    scores = []
    labels = []
    for yolo_model in models:
        cur_predictions = get_yolo_output(image, yolo_model)
        cur_models_labels = cur_predictions['labels']
        cur_model_scores = cur_predictions['scores']
        cur_model_bboxes = cur_predictions['bboxes']
        bboxes.extend(cur_model_bboxes)
        scores.extend(cur_model_scores)
        labels.extend(cur_models_labels)
    print("dfsfasfaf")
    return Predictions(labels=labels, scores=scores, bboxes=bboxes)


# # Endpoint for object detection
@app.post("/detect_objects/")
async def detect_objects(file: UploadFile = File(...)):
    image = Image.open(io.BytesIO(await file.read()))
    predictions = make_predictions(image)
    logging.info(predictions)
    return predictions


models: list[YOLO] = None


@app.on_event("startup")
def startup_event():
    global models
    models = [YOLO(weight_path) for weight_path in WEIGHTS_PATHS]


@app.get("/")
def index():
    return {"it's alive": "42"}
