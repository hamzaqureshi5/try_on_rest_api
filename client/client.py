import requests
import base64
from PIL import Image
from io import BytesIO

def show_img(encoded_image):
        # Decode the base64 image
        decoded_image = base64.b64decode(encoded_image)

        # Open the image using PIL
        pil_image = Image.open(BytesIO(decoded_image))

        # Display the image using Image.show()
        pil_image.show()

    

def send_image_to_api(api_url, image_path, shirt_path):
#    try:
        # Open the image file
        with open(image_path, 'rb') as file:
            # Prepare the payload with the image file
            files = {'image': (image_path, file, 'image/jpeg'),'shirt': (shirt_path, file, 'image/jpeg')}
            
            # Send a POST request to the API
            response = requests.post(api_url, files=files)

            in_memory_file = BytesIO(response.content)
            im = Image.open(in_memory_file)
            im.show()
            # Print the API response
#            print(response.json())
#            print(response.content)
#            print(response.json()["image"])
#            show_img(response.json()["result_image"])
            #show_img(response.content)

#    except Exception as e:
#        print(f'Error: {str(e)}')

if __name__ == '__main__':
    # Replace 'http://127.0.0.1:5000/process_image' with your API endpoint
    api_url = 'http://127.0.0.1:5000/virtual_tryon'

    # Replace 'path/to/your/image.jpg' with the path to your image file
    image_path = 'man.jpeg'
    shirt_path = 'shirt.jpeg'

    send_image_to_api(api_url, image_path, shirt_path)
