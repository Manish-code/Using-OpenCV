import cv2

# face and smile classifiers
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
smile_detector = cv2.CascadeClassifier('haarcascade_smile.xml')
#eyes_detector = cv2.CascadeClassifier('haarcascade_eye.xml')
# Grab webcam feed
webcam = cv2.VideoCapture(0)

while True:

    #Read current frame from webcam
    successful_frame_read, frame = webcam.read()

    # if there's an error, abort
    if not successful_frame_read:
        break

    # Change to grayscale
    frame_grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #Detect face first
    faces = face_detector.detectMultiScale(frame_grayscale)
   

     # Run smile detection 
    for (x, y, w, h) in faces:
        # Draw rectangles around the face
        cv2.rectangle(frame, (x, y), (x+w, y+h), (100, 205, 50), 4)

        # Get the sub frame ( using numpy N-dimentional array slicing)
        the_face = frame[ y:y+h,x:x+w ]
        
        # Change to grayscale
        face_grayscale = cv2.cvtColor(the_face, cv2.COLOR_BGR2GRAY)

        smiles = smile_detector.detectMultiScale(face_grayscale, scaleFactor=1.7, minNeighbors=20)
       # eyes = eyes_detector.detectMultiScale(face_grayscale, scaleFactor=1.3, minNeighbors=10)

    
        # # Run smile detection with each of the face
        # for (x_, y_, w_, h_) in smiles:
        #      # Draw rectangles around the smile
        #         cv2.rectangle(the_face, (x_, y_), (x_+w_, y_+h_), (100, 200, 50), 2)

        #   # Run smile detection with each of the face
        # for (x__, y__, w__, h__) in eyes:
        #      # Draw rectangles around the smile
        #         cv2.rectangle(the_face, (x__, y__), (x__+w__, y__+h__), (100, 200, 50), 2)       

        #label ths face as smiling
        if len(smiles) > 0:
            cv2.putText(frame, 'smiling', (x, y+h+40), fontScale=3,
            fontFace=cv2.FONT_HERSHEY_PLAIN, color = (255, 255, 255))

     # Show the current frame
    cv2.imshow('Why So Serious?', frame)

   
       

    

     #stop if Q key is pressed
    key = cv2.waitKey(1)
    if key == 81 or key == 113:
        break

   
#clean up
webcam.release()
print('Code Complete')