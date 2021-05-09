from fastapi import FastAPI, UploadFile, File
import cv2
import uuid
import shutil
import tensorflow as tf

app = FastAPI()
model_skin_classifier_cnn = tf.keras.models.load_model('skin_cancer.h5')
cancer_class = {
    4: {'nv', 'melanocytic nevi'},
    6: {'mel', 'melanoma'},
    2: {'bkl', 'benign keratosis-like lesions'},
    1: {'bcc', 'basal cell carcinoma'},
    5: {'vasc', 'pyogenic granulomas and hemorrhage'},
    0: {'akiec', 'Actinic keratoses and intraepithelial carcinomae'},
    3: {'df', 'dermatofibroma'}
}


def custom_res(condition, mes, data):
    return {'success': condition, 'message': mes, 'data': data}


@app.post("/predict")
def read_root(skin_image: UploadFile = File(...)):
    base_dir = 'tmp'

    generate_uuid = uuid.uuid4().hex
    file_name_uuid = '{}_{}'.format(generate_uuid, skin_image.filename)
    with open('{}/{}'.format(base_dir, file_name_uuid), 'wb') as image:
        shutil.copyfileobj(skin_image.file, image)

    img = cv2.imread('{}/{}'.format(base_dir, file_name_uuid))
    img = cv2.resize(img, (28, 28))
    result = model_skin_classifier_cnn.predict(img.reshape(1, 28, 28, 3))
    max_prob = max(result[0])
    class_ind = list(result[0]).index(max_prob)
    class_name = cancer_class[class_ind]
    return custom_res(True, file_name_uuid, class_name)
