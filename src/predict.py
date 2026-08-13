
import numpy as np

def predict_image(img):
    # placeholder inference
    h,w = img.shape[:2]
    age = int((h+w)%40 + 18)
    gender = "Male" if (h*w)%2 else "Female"
    return gender, age
