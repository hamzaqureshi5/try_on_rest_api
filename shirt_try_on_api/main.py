from flask import Flask, request, jsonify, render_template
import base64
from PIL import Image
from io import BytesIO
from try_on import detect
import cv2
import numpy as np

app = Flask(__name__)

def show_img(encoded_image):
        # Decode the base64 image
        decoded_image = base64.b64decode(encoded_image)

        # Open the image using PIL
        pil_image = Image.open(BytesIO(decoded_image))
        #pil_image=detect(pil_image)

        # Display the image using Image.show()
        pil_image.save('received_image.jpg', format='JPEG')

#        pil_image.show()


@app.route('/process_image', methods=['POST'])
def process_image():
    try:
        # Get the image file from the request
        img_data = request.files['image'].read()
        img_data_shirt = request.files['shirt'].read()

        # Convert the image data to base64
        encoded_image = base64.b64encode(img_data).decode('utf-8')
        encoded_image_shirt = base64.b64encode(img_data_shirt).decode('utf-8')

        decoded_image = base64.b64decode(encoded_image)
        pil_image = Image.open(BytesIO(decoded_image))


        decoded_image_shirt = base64.b64decode(encoded_image_shirt)
#        pil_image_shirt = Image.open(BytesIO(decoded_image_shirt))

        # Convert PIL image to OpenCV format
        cv_image = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)
#        cv_image_shirt = cv2.cvtColor(np.array(pil_image_shirt), cv2.IMREAD_UNCHANGED)

        # Call the detect function on the image
        #result_image = detect(cv_image,cv_image_shirt)
        result_image = detect(cv_image)


        # Convert the result image back to base64 for sending in the response
        _, encoded_result_image = cv2.imencode('.jpg', result_image)
        encoded_result_image_str = base64.b64encode(encoded_result_image).decode('utf-8')

        # Return the result image as base64 in JSON response
        return jsonify({'result_image': encoded_result_image_str, 'message': 'Image processed and detected successfully!'})



    except Exception as e:
        # Handle any exceptions that may occur during processing
        error_message = f'Error processing image: {str(e)}'
        return jsonify({'error': error_message}), 500

if __name__ == '__main__':
    app.run(debug=True)
