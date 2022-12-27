from keras_preprocessing import image
from keras.models import load_model
from keras.applications.vgg16 import preprocess_input
import numpy as np
import os
import cv2
filename = os.listdir("media")

model=load_model('our_model.h5')
file= 'media/' + filename[0]


img=image.load_img(file,target_size=(224,224))
# imag = cv2.imread(file)
# imag_bw = cv2.cvtColor(imag,cv2.COLOR_BGR2GRAY)

# clahe=cv2.createCLAHE(clipLimit=2.5)
# final_img = clahe.apply(imag_bw)+12
# final_cimg = final_img[:,int((final_img.shape[1])*.06):(final_img.shape[1])-int((final_img.shape[1])*.06)]

imagee=image.img_to_array(img) 
imagee=np.expand_dims(imagee, axis=0)
img_data=preprocess_input(imagee)
prediction=model.predict(img_data)
print(prediction)
def passdata(prediction):
    return prediction

if prediction[0][0]>prediction[0][1]:
    result = 'You are safe'
    print('Person is safe.')
else:
    result = 'You are not safe. Affected with pneumonia'
    print('Person is affected with Pneumonia.')
try:
    os.remove(file)
except:pass

print(f'Predictions: {prediction}')
