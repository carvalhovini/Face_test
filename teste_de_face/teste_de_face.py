import tkinter as tk
from tkinter import messagebox
import os
import cv2
import numpy as np
import shutil
from PIL import Image, ImageTk

DATA_DIR = "data"
FACE_CASCADE_FILE = "haarcascade_frontalface_default.xml"
FACE_RECOGNIZER_FILE = "face_recognizer.yml"

# Carrega o arquivo XML do classificador de faces
face_cascade = cv2.CascadeClassifier(FACE_CASCADE_FILE)

# Função para treinar o modelo de reconhecimento facial
def train_face_recognition_model():
    global label_ids
    x_train = []
    y_labels = []
    label_ids = {}
    current_id = 0

    for root, dirs, files in os.walk(DATA_DIR):
        for file in files:
            if file.endswith("jpg") or file.endswith("png"):
                path = os.path.join(root, file)
                label = os.path.basename(root).replace(" ", "-").lower()

                if label not in label_ids:
                    label_ids[label] = current_id
                    current_id += 1

                id_ = label_ids[label]
                pil_image = Image.open(path).convert("L")
                image_array = np.array(pil_image, "uint8")
                faces = face_cascade.detectMultiScale(image_array, scaleFactor=1.3, minNeighbors=5)

                for (x, y, w, h) in faces:
                    roi = image_array[y:y + h, x:x + w]
                    x_train.append(roi)
                    y_labels.append(id_)

    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.train(x_train, np.array(y_labels))

    return recognizer

def get_name_by_label(label):
    global label_ids
    for key, value in label_ids.items():
        if value == label:
            return key

    return None

class FaceRecognitionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Teste de Reconhecimento Facial")
        self.root.geometry("600x400")
        self.root.configure(background="#f2f2f2")

        self.label_name = tk.Label(self.root, text="Nome:", font=("Arial", 12), bg="#f2f2f2")
        self.label_name.pack(pady=5)

        self.entry_name = tk.Entry(self.root, font=("Arial", 12))
        self.entry_name.pack(pady=5)

        self.btn_add_face = tk.Button(self.root, text="Adicionar Rosto", font=("Arial", 12), command=self.add_new_face, bg="#4caf50", fg="white")
        self.btn_add_face.pack(pady=5)

        self.btn_check_face_by_name = tk.Button(self.root, text="Verificar Rosto pelo Nome", font=("Arial", 12), command=self.check_face_in_database_by_name, bg="#2196f3", fg="white")
        self.btn_check_face_by_name.pack(pady=5)

        self.btn_check_face_by_camera = tk.Button(self.root, text="Verificar Rosto pela Câmera", font=("Arial", 12), command=self.check_face_in_database_by_camera, bg="#ff5722", fg="white")
        self.btn_check_face_by_camera.pack(pady=5)

        self.btn_remove_face = tk.Button(self.root, text="Remover Rosto", font=("Arial", 12), command=self.remove_face, bg="#f44336", fg="white")
        self.btn_remove_face.pack(pady=5)

        self.video_label = tk.Label(self.root)
        self.video_label.pack(pady=5)

        self.is_camera_open = False
        self.capture = None

    def add_new_face(self):
        name = self.entry_name.get()
        if name:
            folder_path = os.path.join(DATA_DIR, name)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
                self.capture = cv2.VideoCapture(0)

                count = 0
                while True:
                    ret, frame = self.capture.read()

                    if not ret:
                        break

                    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

                    for (x, y, w, h) in faces:
                        roi_gray = gray[y:y + h, x:x + w]
                        cv2.imwrite(os.path.join(folder_path, f"{count}.jpg"), roi_gray)
                        count += 1

                        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

                    cv2.imshow("Adicionar Rosto", frame)
                    if cv2.waitKey(1) == ord('q') or count >= 500:
                        break

                self.capture.release()
                cv2.destroyAllWindows()

                messagebox.showinfo("Adicionar Rosto", f"O rosto de {name} foi adicionado com sucesso!")
            else:
                messagebox.showwarning("Adicionar Rosto", f"O rosto de {name} já existe no banco de dados.")
        else:
            messagebox.showwarning("Adicionar Rosto", "Por favor, digite um nome válido.")

    def check_face_in_database_by_name(self):
        name = self.entry_name.get()
        if name:
            folder_path = os.path.join(DATA_DIR, name)
            if os.path.exists(folder_path):
                messagebox.showinfo("Verificar Rosto", f"O rosto de {name} está presente no banco de dados.")
            else:
                messagebox.showwarning("Verificar Rosto", f"O rosto de {name} não está presente no banco de dados.")
        else:
            messagebox.showwarning("Verificar Rosto", "Por favor, digite um nome válido.")

    def check_face_in_database_by_camera(self):
        face_recognizer = train_face_recognition_model()
        self.capture = cv2.VideoCapture(0)
        self.is_camera_open = True

        while self.is_camera_open:
            ret, frame = self.capture.read()

            if not ret:
                break

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

            for (x, y, w, h) in faces:
                roi_gray = gray[y:y + h, x:x + w]
                label, confidence = face_recognizer.predict(roi_gray)

                if confidence < 50:
                    name = get_name_by_label(label)
                    cv2.putText(frame, name, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
                else:
                    cv2.putText(frame, "Desconhecido", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

            cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(cv2image)
            imgtk = ImageTk.PhotoImage(image=img)
            self.video_label.imgtk = imgtk
            self.video_label.configure(image=imgtk)
            self.root.update()

        self.capture.release()
        cv2.destroyAllWindows()

    def remove_face(self):
        name = self.entry_name.get()
        if name:
            folder_path = os.path.join(DATA_DIR, name)
            if os.path.exists(folder_path):
                shutil.rmtree(folder_path)
                messagebox.showinfo("Remover Rosto", f"O rosto de {name} foi removido com sucesso!")
            else:
                messagebox.showwarning("Remover Rosto", f"O rosto de {name} não está presente no banco de dados.")
        else:
            messagebox.showwarning("Remover Rosto", "Por favor, digite um nome válido.")

    def quit_camera(self):
        self.is_camera_open = False

    def start(self):
        self.root.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    app = FaceRecognitionApp(root)
    app.start()
