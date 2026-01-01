import os
import cv2
import numpy as np
from PIL import Image


recognizer = cv2.face.LBPHFaceRecognizer_create()
path = "dataset"

def getImagewithId(path):
    imagePath = [os.path.join(path,f) for f in os.listdir(path)]
    faces = []
    ids = []
    for singleImagePath in imagePath:
        faceImg = Image.open(singleImagePath).convert('L')
        faceNp = np.array(faceImg,np.uint8)
        id = int(os.path.split(singleImagePath)[-1].split(".")[1])
        print(id)
        faces.append(faceNp)
        ids.append(id)
        cv2.imshow("Training",faceNp)
        cv2.waitKey(100)

    return np.array(ids),faces

ids,faces = getImagewithId(path)
recognizer.train(faces, ids)
recognizer.save("recognizer/trainningdata.yml")
cv2.destroyAllWindows()