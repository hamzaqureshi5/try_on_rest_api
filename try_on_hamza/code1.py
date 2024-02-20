# import os
# import cv2
# import numpy as np
# from cvzone.PoseModule import PoseDetector
# from flask import Flask, request, render_template
# import cvzone
# import warnings
# warnings.filterwarnings("ignore", category=DeprecationWarning) 

# # Initialize PoseDetector and other configurations
# detector = PoseDetector(
#     staticMode=True,
#     modelComplexity=1,
#     smoothLandmarks=True,
#     detectionCon=0.5,
#     trackCon=0.5
# )
# shirtsFolderPath = "Resources/Shirts"
# listShirts = os.listdir(shirtsFolderPath)
# fixedRatio = 262/190  # widthOfShirt/widthOfPoint11to12
# imageNumber = 0

# app = Flask(__name__,template_folder="template")

# @app.route("/", methods=["GET"])
# def index():
#     return render_template("index.html")

# @app.route("/virtual_tryon", methods=["POST"])
# def virtual_tryon():
#     # Receive image data from Flutter
#     image_data = request.files["image"].read()
#     image = cv2.imdecode(np.fromstring(image_data, np.uint8), cv2.IMREAD_COLOR)

#     # Perform try-on processing
#     img = detector.findPose(image)
#     lmList, bboxInfo = detector.findPosition(img, draw=False, bboxWithHands=False)

#     if lmList:
#         lm11 = lmList[11][1:3]
#         lm12 = lmList[12][1:3]
#         imgShirt = cv2.imread(os.path.join(shirtsFolderPath, listShirts[0]), cv2.IMREAD_UNCHANGED) # issue here

#         # Process the image (same logic as your original code)
#         widthOfShirt = int((lm11[0] - lm12[0]) * fixedRatio)
#         imgShirt = cv2.resize(imgShirt, (0, 0), None, 1.5, 2)
#         currentScale = (lm11[0] - lm12[0]) / 190
#         offset = int(44 * currentScale), int(48 * currentScale)

#         try:
#             img = cvzone.overlayPNG(img, imgShirt, (lm12[0] - offset[0], lm12[1] - offset[1]))
#         except:
#             pass

#     # Convert the processed image to bytes
#     processed_image_bytes = cv2.imencode(".jpg", img)[1].tobytes()

#     # Return the processed image as a response
#     return processed_image_bytes, 200, {"Content-Type": "image/jpeg"}

# if __name__ == "__main__":
#     app.run(debug=True)












