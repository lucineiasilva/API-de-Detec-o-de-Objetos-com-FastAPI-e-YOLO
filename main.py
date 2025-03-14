from fastapi import FastAPI, File, UploadFile
import cv2
import numpy as np
from ultralytics import YOLO

model = YOLO("yolov8n.pt")

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Esta página faz parte da última Atividade da Disciplina de IA - Docente: José Lucas Brandão e Discente: Lucineia Pacheco "}

@app.post("/detect/")
async def detect_objects(file: UploadFile):
    image_bytes = await file.read()
    image = np.frombuffer(image_bytes, dtype=np.uint8)
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    
    # Perform object detection with YOLOv8
    results = model.predict(image)
    
    # Extract relevant data from detections
    detections = []
    for result in results:
        for box in result.boxes:
            detections.append({
                "class": box.cls.item(),  
                "confidence": box.conf.item(),  
                "box": box.xyxy.tolist()  # 
            })
    
    return {"detections": detections}
