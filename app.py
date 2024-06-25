import streamlit as st
import cv2
import numpy as np
from PIL import Image
import io

####################general
st.write("Welcome to our **_Face Detector_** app")

# Loadong the model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
image=''
grayedImage=''
blurredImage=''
detectedImage=''
###################################################################################file uploading
file = st.file_uploader(label="Upload the photo you want", type=["jpeg", "jpg", "png"]) 

def detectFace(image):
    # Convert to grayscale ->>>>>>>>>>>>>>>>>>>
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurredImage=image.copy()
    # Detect faces 
    faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.2, minNeighbors=5, minSize=(20, 20))
    # I noticed that 1.2 is suitable form my testcases photos
    
    # Drawing rectangle around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y),(x+w, y+h), (220, 20, 60), 3)
        face = image[y:y+h, x:x+w]
        blurred_face = cv2.GaussianBlur(face, (99, 99), 30)
        blurredImage[y:y+h, x:x+w] = blurred_face    
    return image,blurredImage

def download_Dimage(image, filename):
    # Convert image array to bytes
    image_pil = Image.fromarray(image)
    image_io = io.BytesIO()
    image_pil.save(image_io, format='JPEG')
    image_bytes = image_io.getvalue()   
    st.download_button(
        label="Download detected Image",
        data=image_bytes,
        file_name=filename,
        mime='image/jpeg'
    )
def download_Bimage(image, filename):
    # Convert image array to bytes AND CORRECTLY DOWNLOAD THEM
    image_pil = Image.fromarray(image)
    image_io = io.BytesIO()
    image_pil.save(image_io, format='JPEG')
    image_bytes = image_io.getvalue()
    st.download_button(
        label="Download Blurred Image",
        data=image_bytes,
        file_name=filename,
        mime='image/jpeg'
    )    

def process(file):
    if file is not None:        
        image = Image.open(file).convert("RGB")  
        #st.write(np.array(image)) 
                
        image_bgr = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        
        # Detect and blur faces       
        detectedImage,blurredImage = detectFace(image_bgr.copy())   
        
       
        detectedImage = cv2.cvtColor(detectedImage, cv2.COLOR_BGR2RGB)
        blurredImage = cv2.cvtColor(blurredImage, cv2.COLOR_BGR2RGB)
   
        st.image(detectedImage, caption='Image with Face Detections')
        st.image(blurredImage, caption='Image with Blurred Faces')
        if detectedImage is not None:
            download_Dimage(detectedImage,"detected_image.jpg")
        if blurredImage is not None:
            download_Dimage(blurredImage,"blurred_image.jpg") 
        return        
process(file)


   
