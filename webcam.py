import time
import cv2
import PySimpleGUI as sg

# Camera Settings
camera_Width1  = 320 # 480 # 640 # 1024 # 1280
camera_Heigth1 = 240 # 320 # 480 # 780  # 960
camera_Width2  = 480 # 640 # 1024 # 1280
camera_Heigth2 = 320 # 480 # 780  # 960
frameSize = (camera_Width2, camera_Heigth2)
frameSize2 = (camera_Width1, camera_Heigth1)

xml_path = 'haarcascade_frontalface_alt2.xml'
clf = cv2.CascadeClassifier(xml_path)

video_capture = cv2.VideoCapture("rtsp://admin:IACNCZ@10.0.0.105:554/cam/realmonitor?channel=1&subtype=0")
video_capture2 = cv2.VideoCapture(0)

# init Windows Manager
sg.theme("DarkBlue")

COLOR = (255, 255, 0)
STROKE = 2

# def webcam col
colwebcam1_layout = [[sg.Text("Camera View", size=(60, 1), justification="center")],[sg.Image(filename="", key="cam1")]]
colwebcam1 = sg.Column(colwebcam1_layout, element_justification='center')

colwebcam2_layout = [[sg.Text("Camera View GrayScale", size=(60, 1), justification="center")],[sg.Image(filename="", key="cam1gray")]]
colwebcam2 = sg.Column(colwebcam2_layout, element_justification='center')

rowebcam3_layout = [[sg.Text("Camera View 3", size=(60, 1), justification="center")],[sg.Image(filename="", key="cam3")]]
rowebcam3 = sg.Column (rowebcam3_layout, element_justification='center')


colslayout = [colwebcam1, colwebcam2, rowebcam3]

layout = [colslayout] #, rowfooter]

window = sg.Window("Leandro – Webcams com PySimpleGUI", layout, 
                    no_titlebar=False, alpha_channel=1, grab_anywhere=False, 
                    return_keyboard_events=True, location=(100, 100)) 

while True:
    start_time = time.time()
    event, values = window.read(timeout=20)

    if event == sg.WIN_CLOSED:
        break

    # get camera frame
    ret, frameOrig = video_capture.read()
    # ret2, frameOrig2 = video_capture2.read()

    frame = cv2.resize(frameOrig, frameSize)
    # frame2 = cv2.resize(frameOrig, frameSize)

    frame3 = cv2.resize(frameOrig, frameSize2)
    
    

    # update webcam1
    imgbytes = cv2.imencode(".png", frame)[1].tobytes()
    window["cam1"].update(data=imgbytes)

    # transform frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


    faces = clf.detectMultiScale(gray)
    for x, y, w, h in faces:
        cv2.rectangle(gray, (x, y), (x+w, y+h), COLOR, STROKE)
   
    # update webcam2
    imgbytes2 = cv2.imencode(".png", gray)[1].tobytes()
    window["cam1gray"].update(data=imgbytes2)    
    
    # update webcam3
    imgbytes3 = cv2.imencode(".png", frame3)[1].tobytes()
    window["cam3"].update(data=imgbytes3) 

video_capture.release()
cv2.destroyAllWindows()
