# 🚀 Face Detection and Blurring app with Streamlit

Welcome to our **Face Detection and Blurring ** app! This application leverages a pre-trained Haar cascade model to detect faces in uploaded images and blur them. Let's get started! 📸

## 🛠️ Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/salmamuhammede/Face-Detection-and-Blurring-Streamlit-app.git
   cd repository
2. **Install Dependencies**:
Ensure you have Python 3.8+ installed. Then, create a virtual environment and install the required packages:

# ▶️ Running the App
1. **Start the Streamlit App**:
   ```bash
   streamlit run app.py
   #if you face problems with file uploder try this:
   streamlit run app.py --server.enableXsrfProtection false
   #make sure you are in the correct directory
This will open the app in your web browser. If not, navigate to http://localhost:8501.

2. **Upload Images**:

Use the upload button to select images from your device.
The app will automatically display detected Faces with bounding boxes and blur.

3.  **Download Images**:
After processing, you can download both the detected and blurred versions of the image using the provided download buttons.

# 📂 Test Cases
Here are some sample images you can use to test the object detection capabilities of the app. Download and upload these images to see the model in action:

1. 🏙️ Friends Tv show
![Friends](.\friendsPhoto.PNG)
2. 🚗 Group of friends
![People](.\test3result.PNG)
3. 🏠 people at 1950s
![1950 Family](.\1950Photo.PNG)
# Hope you enjoy my app 😄





