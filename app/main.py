import os
import numpy as np
import uuid
import shutil
import tensorflow as tf
from fastapi import FastAPI, UploadFile, File
from keras.preprocessing import image

app = FastAPI()
model_skin_classifier_cnn = tf.keras.models.load_model('skin_cancer.h5')
cancer_class = {
    4: 'melanocytic nevi',
    6: 'melanoma',
    2: 'benign keratosis-like lesions',
    1: 'basal cell carcinoma',
    5: 'pyogenic granulomas and hemorrhage',
    0: 'Actinic keratoses and intraepithelial carcinomae',
    3: 'dermatofibroma'
}


def custom_res(condition, mes, data):
    return {'success': condition, 'message': mes, 'data': data}


@app.post("/predict")
def read_root(skin_image: UploadFile = File(...)):
    base_dir = 'tmp'

    generate_uuid = uuid.uuid4().hex
    file_name_uuid = '{}_{}'.format(generate_uuid, skin_image.filename)
    path = '{}/{}'.format(base_dir, file_name_uuid)
    with open(path, 'wb') as img:
        shutil.copyfileobj(skin_image.file, img)

    img = image.load_img(path, target_size=(28, 28))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = np.vstack([x])
    result = model_skin_classifier_cnn.predict(x)
    max_prob = max(result[0])
    class_index = list(result[0]).index(max_prob)
    class_name = cancer_class[class_index]
    os.remove(path)

    return custom_res(True, file_name_uuid, class_name)
