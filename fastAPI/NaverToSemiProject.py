#이거 잘 작동하려나...
from fastapi import FastAPI, File, UploadFile
from typing import List
import numpy as np
import io
import torch
import cv2
from PIL import Image
from pydantic import BaseModel

# 모델 로드
model = torch.hub.load('ultralytics/yolov5', 'yolov5x', pretrained=True)

# FastAPI 인스턴스 생성
app = FastAPI()

# POST /predict 엔드포인트 생성
class ImageRequest(BaseModel):
    image: bytes

class Prediction(BaseModel):
    image: str
    predictions: List[dict]

@app.post("/predict", response_model=Prediction)
async def predict(image_request: ImageRequest):
    # 이미지 바이너리 데이터를 PIL Image 객체로 변환
    img = Image.open(io.BytesIO(image_request.image)).convert('RGB')

    # 이미지 전처리
    img = np.array(img)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    # 모델에 이미지를 입력하여 예측 결과 생성
    results = model(img)

    # 예측 결과에서 필요한 정보를 추출하여 Response 모델에 담아 반환
    predictions = []
    for result in results.xyxy[0]:
        prediction = {}
        prediction['class'] = int(result[5])
        prediction['score'] = float(result[4])
        prediction['bbox'] = [int(i) for i in result[:4]]
        predictions.append(prediction)

    # 이미지와 레이블 정보 추출
    image = results.render()
    image = cv2.imencode('.jpg', image)[1].tostring()
    image = base64.b64encode(image).decode()
    label = results.pandas().xyxy[0].to_dict(orient='records')

    return Prediction(image=image, predictions=predictions, label=label)

#uvicorn main:app --reload