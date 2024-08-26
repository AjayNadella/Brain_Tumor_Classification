import joblib
import numpy as np
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from tensorflow.keras.preprocessing import image
from io import BytesIO
import tensorflow as tf
from fastapi.staticfiles import StaticFiles
from fastapi import HTTPException

# Load the trained model
model = joblib.load('C:/Users/ajayn/Desktop/ML/brain_tumor_classification/models/model.pkl')

app = FastAPI()
app.mount("/static", StaticFiles(directory="frontend"), name="static")

class_names = ['Glioma', 'Meningioma', 'No Tumor', 'Pituitary']

def predict_image(img):
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)  # Create a batch

    predictions = model.predict(img_array)
    predicted_class = class_names[np.argmax(predictions[0])]
    confidence = round(100 * np.max(predictions[0]), 2)

    return predicted_class, confidence

@app.get("/")
def read_root():
    return {"message": "Welcome to the Brain Tumor Classification API!"}

@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        img = image.load_img(BytesIO(contents), target_size=(256, 256))
        predicted_class, confidence = predict_image(img)
        return JSONResponse(content={
            "predicted_class": predicted_class,
            "confidence": confidence
        })
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# To run the server use:
# uvicorn main:app --reload
