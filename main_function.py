
import numpy as np
import os
import mediapipe as mp
import cv2
from my_functions import *
import keyboard
from gtts import gTTS
from playsound import playsound
import random
from tensorflow.keras.models import load_model
import tkinter as tk



r1 = random.randint(1, 10000000)
r2 = random.randint(1, 10000000)
randfile = str(r2) + "randomtext" + str(r1) + ".mp3"

PATH = os.path.join('data')

actions = np.array(os.listdir(PATH))

model = load_model('my_model')

sentence, keypoints = [' '], []


with mp.solutions.holistic.Holistic(min_detection_confidence=0.75, min_tracking_confidence=0.75) as holistic:
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            print("Cannot access camera.")
            exit()  

    
        while cap.isOpened():
            _, image = cap.read()

            results = image_process(image, holistic)
            draw_landmarks(image, results)
            keypoints.append(keypoint_extraction(results))

            if len(keypoints) == 30:
                keypoints = np.array(keypoints)
                prediction = model.predict(keypoints[np.newaxis, :, :])
                keypoints = []
                
                if np.amax(prediction) > 0.9:
                    if sentence[-1] != actions[np.argmax(prediction)]:
                        sentence.append(actions[np.argmax(prediction)])
                        randfile = str(r2) + "randomtext" + str(r1) + ".mp3"
                        tts = gTTS(actions[np.argmax(prediction)], lang='tl', slow=False)
                        tts.save(randfile)
                        playsound(randfile)
                        print(randfile)
                        os.remove(randfile)

            if len(sentence) > 2:
                sentence = sentence[-1:]
            
            if keyboard.is_pressed(' '):
                sentence = [' ']
                
            textsize = cv2.getTextSize(' '.join(sentence), cv2.FONT_HERSHEY_SIMPLEX, 1, 2)[0]
            text_X_coord = (image.shape[1] - textsize[0]) // 2
                
            cv2.putText(image, ' '.join(sentence), (text_X_coord, 470), 
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 27, 227), 2, cv2.LINE_AA)
                            
            
            cv2.namedWindow("Camera", cv2.WINDOW_NORMAL)
            cv2.imshow("Camera", image)
            cv2.setWindowProperty("Camera", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
            cv2.resizeWindow("Camera", 700,500)
            cv2.moveWindow("Camera", 300, 100)
            
            if cv2.getWindowProperty('Camera',cv2.WND_PROP_VISIBLE) < 1:
                break
            cv2.waitKey(1)
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()
