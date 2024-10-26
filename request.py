import streamlit as st
import cv2
import mediapipe as mp
import math
import time
from collections import deque
import numpy as np

# Inicializar mediapipe para FaceMesh y detección facial
mp_face_mesh = mp.solutions.face_mesh
mp_drawing = mp.solutions.drawing_utils
mp_face_detection = mp.solutions.face_detection

# Parámetros
confThreshold = 0.5  # Umbral de confianza para detección de rostros
max_blink_duration = 1  # Duración máxima del parpadeo para ser considerado un microsueño (en segundos)
alert_threshold = 3  # Número de microsueños permitidos antes de lanzar la alerta
alert_time_window = 600  # Ventana de tiempo para detectar microsueños (en segundos, equivalente a 10 minutos)
yawn_duration_threshold = 3

def main():
    st.title("Detección de fatiga con Streamlit y MediaPipe")

    # Variables
    blink_start_time = None
    blinks = deque(maxlen=alert_threshold)
    microsleep_count = 0
    blink_duration = 0
    alert_raised = False
    yawn_start_time = None
    yawning = False

    # Configuración de la cámara
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1600)  # Ajuste del ancho de la ventana
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 900)  # Ajuste de la altura de la ventana

    # Iniciar el temporizador para registrar el tiempo transcurrido
    start_time = time.time()

    # Detección de rostros y máscara de malla facial
    with mp_face_mesh.FaceMesh(max_num_faces=1) as face_mesh:
        frameST = st.empty()
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            # Conversión de BGR a RGB
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Detección de la malla facial
            results = face_mesh.process(rgb_frame)

            # Detección de parpadeos y bostezos
            frame, alert_raised, yawning = process_frame(frame, results, start_time,
                                                         blink_start_time, blinks,
                                                         microsleep_count, blink_duration,
                                                         yawn_start_time, yawning)

            # Mostrar la imagen en Streamlit en lugar de cv2.imshow
            frameST.image(frame, channels="BGR", use_column_width=True)
            
            # Esto permite que el loop de Streamlit continúe sin bloquear la GUI
            if st.button('Stop'):
                break

    # Liberar la cámara y recursos
    cap.release()

def process_frame(frame, results, start_time, blink_start_time, blinks,
                  microsleep_count, blink_duration, yawn_start_time, yawning):
    # Tu lógica de procesamiento aquí, actualizada para funcionar dentro de la función
    # y retornar los valores necesarios.
    return frame, False, False  # Actualiza estos valores según la lógica de tu aplicación

if __name__ == '__main__':
    main()
