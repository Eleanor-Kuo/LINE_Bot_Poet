import tensorflow as tf
import numpy as np
import cv2 
import json

with open('animal_dict.json',encoding="utf-8") as f:
  animal_dict = json.load(f)

with open('animal_trans_dict.json',encoding="utf-8") as f:
  animal_trans_dict = json.load(f)

def picture_recognize(img_path):
    
    model = tf.keras.models.load_model('my_model.h5')  # 下載已訓練好的動物圖片辨識模型
    IMAGE_SIZE = (150, 150)

    image = cv2.imread(img_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = cv2.resize(image, IMAGE_SIZE) 
    image = image / 255.0
    
    li = []
    li.append(image)
    
    image = np.array(li, dtype = 'float32') 

    predictions = model.predict(image)  
    predictions = np.argmax(predictions,axis = 1)
    predictions = predictions[0]  # 得到預測的 label
    
    eng_name = str(list(animal_dict.keys())[list(animal_dict.values()).index(predictions)])  
    name = str(animal_trans_dict[eng_name])  # 查看已建立好的字典，將數字 label 先轉成英文名稱再轉成中文
    
    return name

