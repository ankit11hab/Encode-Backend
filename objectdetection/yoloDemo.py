import cv2
import numpy as np
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 900)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 900)
classNames = []
classFile = 'labels.txt'
with open(classFile, 'rt') as f:
    classNames = f.read().rstrip('\n').split('\n')

model_cfg = 'yolov3.cfg'
model_weight = 'yolov3.weights'
confThreshold = 0.3
nmsThreshold = 0.3
net = cv2.dnn.readNetFromDarknet(model_cfg,model_weight)
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)

def findObjects(outputs,img):
    hT,wT,cT = img.shape
    bbox = []
    classIds = []
    confs = []

    for output in outputs:
        for det in output:
            scores = det[5:]
            classId = np.argmax(scores)
            confidence = scores[classId]
            if confidence > confThreshold:
                w,h = int(det[2]*wT),int(det[3]*hT)
                x,y = int((det[0]*wT)-w/2),int((det[1]*hT)-h/2)
                bbox.append([x,y,w,h])
                classIds.append(classId)
                confs.append(float(confidence))
    indices = cv2.dnn.NMSBoxes(bbox,confs,confThreshold,nmsThreshold)
    # print(indices)
    numSeat,numPer = 0,0
    for i in indices:
        # box = bbox[i]
        # x,y,w,h = box[0],box[1],box[2],box[3]
        # cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,255),2)
        # cv2.putText(img,f'{classNames[classIds[i]].upper()} {int(confs[i]*100)}%',(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.6,(255,0,255),2)
        if classNames[classIds[i]].upper() == "CHAIR":
            numSeat = numSeat+1
        if classNames[classIds[i]].upper() == "PERSON":
            numPer = numPer+1
    cv2.putText(img, f'Occupied:{numPer}    Empty:{numSeat}', (10,25),cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 0, 255), 2)



while True:
    success,img = cap.read()
    blob = cv2.dnn.blobFromImage(img,1/255,(320,320),[0,0,0],1,crop=False)
    net.setInput(blob)
    layerNames = net.getLayerNames()
    outputNames = [layerNames[i-1] for i in net.getUnconnectedOutLayers()]
    outputs = net.forward(outputNames)
    # print(outputs[0].shape)
    # print(outputs[1].shape)
    # print(outputs[2].shape)
    findObjects(outputs,img)
    cv2.imshow('Image',img)
    cv2.waitKey(1)

# img = cv2.imread('filled_seat_2.jpg')
# blob = cv2.dnn.blobFromImage(img,1/255,(320,320),[0,0,0],1,crop=False)
# net.setInput(blob)
# layerNames = net.getLayerNames()
# outputNames = [layerNames[i-1] for i in net.getUnconnectedOutLayers()]
# outputs = net.forward(outputNames)
#     # print(outputs[0].shape)
#     # print(outputs[1].shape)
#     # print(outputs[2].shape)
# findObjects(outputs,img)
# cv2.imshow('Image',img)
# cv2.waitKey(0)