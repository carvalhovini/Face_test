FACE RECOGNITION APP

This is a simple face recognition application built using Tkinter and OpenCV in Python. The application allows you to perform the following tasks:

1 Add a new face to the database by capturing images from the camera.
2 Check if a face exists in the database by name.
3 Verify faces in real-time using the camera.

Installation

To run this application, you need to have Python and the following libraries installed:

Tkinter
OpenCV
numpy
PIL
You can install these dependencies using pip:

Copy code

pip install tkinter opencv-python numpy pillow
Additionally, you need to download the haarcascade_frontalface_default.xml file, which is the pre-trained face detection classifier used by OpenCV. You can download it from here.

Usage

1 Clone or download the repository to your local machine.
2 Place the haarcascade_frontalface_default.xml file in the same directory as the Python script.
3 Run the Python script:
4 Copy code
5 python face_recognition_app.py
6 The application window will open, and you can use the provided buttons to perform various tasks.

Instructions

1 Adding a New Face
2 Enter a name in the "Nome" entry box.
3 Click on the "Adicionar Rosto" button.
4 The camera will open, and you need to position your face within the frame.
5 Multiple images will be captured and saved in the corresponding folder under the "data" directory.
6 Press 'q' on your keyboard or wait until 500 images are captured to stop the process.
7 A message box will appear, indicating the success or failure of adding the face.

Checking a Face in the Database by Name

1 Enter a name in the "Nome" entry box.
2 Click on the "Verificar Rosto pelo Nome" button.
3 A message box will appear, indicating whether the face exists in the database or not.

Verifying Faces in the Database using the Camera

1 Click on the "Verificar Rosto pela Câmera" button.
2 The camera will open, and the application will start recognizing faces in real-time.
3 The recognized faces will be displayed with their names in a bounding box.
4 Press the "Remover Rosto" button to stop the camera and return to the main window.

Removing a Face

1 Enter a name in the "Nome" entry box.
2 Click on the "Remover Rosto" button.
3 The corresponding face folder will be deleted from the database.
4 A message box will appear, indicating the success or failure of removing the face.

Note

Make sure to create a "data" directory in the same location as the script before adding or checking faces. The script automatically creates subdirectories under the "data" directory to store face images for each individual.

Please note that this application uses the LBPH (Local Binary Patterns Histograms) face recognition algorithm from OpenCV. The accuracy of face recognition may vary depending on the quality of the training data and the captured images.
