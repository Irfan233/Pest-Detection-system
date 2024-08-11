import os
import cv2
from PIL import Image
import numpy as np
# 

# 
data=[]
labels=[]
# 
# ----------------
# LABELS
# ants 0
# bees 1
# beetle 2
# catterpillar 3
# earthworms 4
# earwig 5
# grasshopper 6
# moth 7
# alug 8
# snail 9
# wasp 10
# weevil 11
# ----------------

# ants 0
ants = os.listdir(os.getcwd() + "/CNN/data/ants/")
for x in ants:
    imag=cv2.imread(os.getcwd() + "/CNN/data/ants/" + x)
    img_from_ar = Image.fromarray(imag, 'RGB')
    resized_image = img_from_ar.resize((50, 50))
    data.append(np.array(resized_image))
    labels.append(0)

# bees 1
bees = os.listdir(os.getcwd() + "/CNN/data/bees/")
for x in bees:
    imag=cv2.imread(os.getcwd() + "/CNN/data/bees/" + x)
    img_from_ar = Image.fromarray(imag, 'RGB')
    resized_image = img_from_ar.resize((50, 50))
    data.append(np.array(resized_image))
    labels.append(1)

# beetle 2
beetle = os.listdir(os.getcwd() + "/CNN/data/beetle/")
for x in beetle:
    imag=cv2.imread(os.getcwd() + "/CNN/data/beetle/" + x)
    img_from_ar = Image.fromarray(imag, 'RGB')
    resized_image = img_from_ar.resize((50, 50))
    data.append(np.array(resized_image))
    labels.append(2)

# catterpillar 3
catterpillar = os.listdir(os.getcwd() + "/CNN/data/catterpillar/")
for x in catterpillar:
    imag=cv2.imread(os.getcwd() + "/CNN/data/catterpillar/" + x)
    img_from_ar = Image.fromarray(imag, 'RGB')
    resized_image = img_from_ar.resize((50, 50))
    data.append(np.array(resized_image))
    labels.append(3)

# earthworms 4
earthworms = os.listdir(os.getcwd() + "/CNN/data/earthworms/")
for x in earthworms:
    imag=cv2.imread(os.getcwd() + "/CNN/data/earthworms/" + x)
    img_from_ar = Image.fromarray(imag, 'RGB')
    resized_image = img_from_ar.resize((50, 50))
    data.append(np.array(resized_image))
    labels.append(4)

# earwig 5
earwig = os.listdir(os.getcwd() + "/CNN/data/earwig/")
for x in earwig:
    imag=cv2.imread(os.getcwd() + "/CNN/data/earwig/" + x)
    img_from_ar = Image.fromarray(imag, 'RGB')
    resized_image = img_from_ar.resize((50, 50))
    data.append(np.array(resized_image))
    labels.append(5)
    
# grasshopper 6
grasshopper = os.listdir(os.getcwd() + "/CNN/data/grasshopper/")
for x in grasshopper:
    imag=cv2.imread(os.getcwd() + "/CNN/data/grasshopper/" + x)
    img_from_ar = Image.fromarray(imag, 'RGB')
    resized_image = img_from_ar.resize((50, 50))
    data.append(np.array(resized_image))
    labels.append(6)
    
# moth 11
moth = os.listdir(os.getcwd() + "/CNN/data/moth/")
for x in moth:
     imag=cv2.imread(os.getcwd() + "/CNN/data/moth/" + x)
     img_from_ar = Image.fromarray(imag, 'RGB')
     resized_image = img_from_ar.resize((50, 50))
     data.append(np.array(resized_image))
     labels.append(7)
    
# slug 8
slug = os.listdir(os.getcwd() + "/CNN/data/slug/")
for x in slug:
    imag=cv2.imread(os.getcwd() + "/CNN/data/slug/" + x)
    img_from_ar = Image.fromarray(imag, 'RGB')
    resized_image = img_from_ar.resize((50, 50))
    data.append(np.array(resized_image))
    labels.append(8)
   
   # snail 9
snail = os.listdir(os.getcwd() + "/CNN/data/snail/")
for x in snail:
    imag=cv2.imread(os.getcwd() + "/CNN/data/snail/" + x)
    img_from_ar = Image.fromarray(imag, 'RGB')
    resized_image = img_from_ar.resize((50, 50))
    data.append(np.array(resized_image))
    labels.append(9)

  # wasp 10
wasp = os.listdir(os.getcwd() + "/CNN/data/wasp/")
for x in wasp:
     imag=cv2.imread(os.getcwd() + "/CNN/data/wasp/" + x)
     img_from_ar = Image.fromarray(imag, 'RGB')
     resized_image = img_from_ar.resize((50, 50))
     data.append(np.array(resized_image))
     labels.append(10)
    
     # weevil 11
weevil = os.listdir(os.getcwd() + "/CNN/data/weevil/")
for x in weevil:
     imag=cv2.imread(os.getcwd() + "/CNN/data/weevil/" + x)
     img_from_ar = Image.fromarray(imag, 'RGB')
     resized_image = img_from_ar.resize((50, 50))
     data.append(np.array(resized_image))
     labels.append(11)



pests=np.array(data)
labels=np.array(labels)

np.save("pests",pests)
np.save("labels",labels)