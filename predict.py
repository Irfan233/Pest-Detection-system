import os
import cv2
from PIL import Image
import numpy as np

import tensorflow as tf
from django.conf import settings

# Display the result
imag=cv2.imread(os.getcwd() +'/CNN/data/beetle/image.jpg')
img_from_ar = imag.fromarray(imag, 'RGB')
resized_imag = img_from_ar.resize((50, 50))

test_imag =np.expand_dims(resized_imag, axis=0) 

# load model
model = tf.keras.models.load_model(os.getcwd() + '/model.h5')

result = model.predict(test_image) 
print(result) 
print("Result is: ", result[0][0])
print("Prediction: " + str(np.argmax(result)))
