import os
import cvzone
import cv2
from cvzone.PoseModule import PoseDetector

# Initialize video capture from a video file
#cap = cv2.VideoCapture("Resources/Videos/1.mp4")

# Initialize PoseDetector with various parameters
detector = PoseDetector(
    staticMode=False,       # detector is operating in dynamic mode
    modelComplexity=1,      # A value of 1 indicates a moderate level of complexity
    smoothLandmarks=True,    # reduce jitter or noise in the landmark positions
    enableSegmentation=False,   # indicating that segmentation masks are not being used
    smoothSegmentation=True,  # this parameter has no effect.
    detectionCon=0.5,   # landmarks with a confidence score of at least 50% are saved
    trackCon=0.5
)

# Prepare to overlay shirts on the detected subject
shirtsFolderPath = "Resources/Shirts"
listShirts = os.listdir(shirtsFolderPath)
fixedRatio = 262/190  # widthOfShirt/widthOfPoint11to12
imageNumber = 0
#imgButtonRight = cv2.imread("Resources/button.png", cv2.IMREAD_UNCHANGED)
#imgButtonLeft = cv2.flip(imgButtonRight, 1)
counterRight = 0
counterLeft = 0
selectionSpeed = 10
# Main loop for processing frames from the video
# while True:
#     success, img = cap.read()    # main processing loop reads video frames

#     # Find the human pose in the frame
#     img = detector.findPose(img)   # detect human poses in each frame
#     img = cv2.flip(img, 1)       # to match the pose landmarks with the actual hand positions

#     # Find the landmarks, bounding box, and center of the body in the frame
#     # Set draw=True to draw the landmarks and bounding box on the image
#     lmList, bboxInfo = detector.findPosition(img, draw=False, bboxWithHands=False)

#     # Check if any body landmarks are detected
#     if lmList:
#         # Get the center of the bounding box around the body
#         lm11 = lmList[11][1:3]
#         lm12 = lmList[12][1:3]
#         imgShirt = cv2.imread(os.path.join(shirtsFolderPath, listShirts[0]), cv2.IMREAD_UNCHANGED)

#         # Calculate the width of the shirt
#         widthOfShirt = int((lm11[0] - lm12[0]) * fixedRatio)
#         print(widthOfShirt)
#         imgShirt = cv2.resize(imgShirt, (0, 0), None, 1.5, 2)
#         currentScale = (lm11[0] - lm12[0]) / 190
#         offset = int(44 * currentScale), int(48 * currentScale)



#         try:
#             img = cvzone.overlayPNG(img, imgShirt, (lm12[0] - offset[0], lm12[1] - offset[1]))
#         except:
#             pass

#         img = cvzone.overlayPNG(img, imgButtonRight, (1074, 293))
#         img = cvzone.overlayPNG(img, imgButtonLeft, (72, 293))

#         if lmList[16][1] < 300:
#             counterRight += 1
#             cv2.ellipse(img, (139, 360), (66, 66), 0, 0,counterRight * selectionSpeed, (0, 255, 0), 20)    #eclipse for circular path
#             if counterRight * selectionSpeed > 360:
#                 counterRight = 0
#                 if imageNumber < len(listShirts) - 1:
#                     imageNumber += 1
#         elif lmList[15][1] > 900:
#             counterLeft += 1
#             cv2.ellipse(img, (1138, 360), (66, 66), 0, 0,counterLeft * selectionSpeed, (0, 255, 0), 20)
#             if counterLeft * selectionSpeed > 360:
#                 counterLeft = 0
#                 if imageNumber > 0:
#                     imageNumber -= 1

#         else:
#             counterRight = 0   # when a certain condition is met, the count or progress is reset to zero
#             counterLeft = 0



#     cv2.imshow("Image", img)  # display the processed frame
#     if cv2.waitKey(1) == ord('q'):   # Pressing 'q' in the window will break the loop.
#         break

# cap.release()
# cv2.destroyAllWindows()





def detect(img ):
    # Find the human pose in the frame
    img = detector.findPose(img)   # detect human poses in each frame
    img = cv2.flip(img, 1)       # to match the pose landmarks with the actual hand positions

    # Find the landmarks, bounding box, and center of the body in the frame
    # Set draw=True to draw the landmarks and bounding box on the image
    lmList, bboxInfo = detector.findPosition(img, draw=True, bboxWithHands=False)

    # Check if any body landmarks are detected
    if lmList:
        # Get the center of the bounding box around the body
        lm11 = lmList[11][1:3]
        lm12 = lmList[12][1:3]
        imgShirt = cv2.imread(os.path.join(shirtsFolderPath, listShirts[0]), cv2.IMREAD_UNCHANGED)
#        imgShirt = cv2.imread("shirt.jpeg", cv2.IMREAD_UNCHANGED)

        # Calculate the width of the shirt
        widthOfShirt = int((lm11[0] - lm12[0]) * fixedRatio)
        print(widthOfShirt)
        imgShirt = cv2.resize(imgShirt, (0, 0), None, 1.5, 2)
        currentScale = (lm11[0] - lm12[0]) / 190
        offset = int(44 * currentScale), int(48 * currentScale)


        try:
            img = cvzone.overlayPNG(img, imgShirt, (lm12[0] - offset[0], lm12[1] - offset[1]))
        except Exception as e:
            print(f'Error overlaying shirt: {str(e)}')

#        img = cvzone.overlayPNG(img, imgButtonRight, (1074, 293))
#        img = cvzone.overlayPNG(img, imgButtonLeft, (72, 293))

        if lmList[16][1] < 300:
#            counterRight += 1
            counterRight=0
            cv2.ellipse(img, (139, 360), (66, 66), 0, 0,counterRight * selectionSpeed, (0, 255, 0), 20)    #eclipse for circular path
            if counterRight * selectionSpeed > 360:
                counterRight = 0
#                if imageNumber < len(listShirts) - 1:
#                    imageNumber += 1
        elif lmList[15][1] > 900:
#            counterLeft += 1
            cv2.ellipse(img, (1138, 360), (66, 66), 0, 0,counterLeft * selectionSpeed, (0, 255, 0), 20)
            if counterLeft * selectionSpeed > 360:
                counterLeft = 0
#                if imageNumber > 0:
#                    imageNumber -= 1

#        else:
#            counterRight = 0   # when a certain condition is met, the count or progress is reset to zero
#            counterLeft = 0

        return img
#    return img
    
