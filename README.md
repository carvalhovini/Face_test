Face Recognition App
This is a simple face recognition application built using Tkinter and OpenCV in Python. The application allows you to perform the following tasks:

Add a new face to the database by capturing images from the camera.
Check if a face exists in the database by name.
Verify faces in real-time using the camera.
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
Clone or download the repository to your local machine.
Place the haarcascade_frontalface_default.xml file in the same directory as the Python script.
Run the Python script:
Copy code
python face_recognition_app.py
The application window will open, and you can use the provided buttons to perform various tasks.
Instructions
Adding a New Face
Enter a name in the "Nome" entry box.
Click on the "Adicionar Rosto" button.
The camera will open, and you need to position your face within the frame.
Multiple images will be captured and saved in the corresponding folder under the "data" directory.
Press 'q' on your keyboard or wait until 500 images are captured to stop the process.
A message box will appear, indicating the success or failure of adding the face.
Checking a Face in the Database by Name
Enter a name in the "Nome" entry box.
Click on the "Verificar Rosto pelo Nome" button.
A message box will appear, indicating whether the face exists in the database or not.
Verifying Faces in the Database using the Camera
Click on the "Verificar Rosto pela Câmera" button.
The camera will open, and the application will start recognizing faces in real-time.
The recognized faces will be displayed with their names in a bounding box.
Press the "Remover Rosto" button to stop the camera and return to the main window.
Removing a Face
Enter a name in the "Nome" entry box.
Click on the "Remover Rosto" button.
The corresponding face folder will be deleted from the database.
A message box will appear, indicating the success or failure of removing the face.
Note
Make sure to create a "data" directory in the same location as the script before adding or checking faces. The script automatically creates subdirectories under the "data" directory to store face images for each individual.

Please note that this application uses the LBPH (Local Binary Patterns Histograms) face recognition algorithm from OpenCV. The accuracy of face recognition may vary depending on the quality of the training data and the captured images.
