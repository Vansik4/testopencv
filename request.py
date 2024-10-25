import streamlit as st
import cv2
import numpy as np


def main():
    st.title("Streamlit con OpenCV")

    # Crea un elemento en la interfaz para mostrar el video.
    frame_window = st.image([])

    # Captura de video desde la cámara (0 es el índice de la cámara predeterminada)
    cap = cv2.VideoCapture(1)

    # Comprueba si la cámara se abrió correctamente
    if not cap.isOpened():
        st.error("No se puede abrir la cámara")
        return

    run = st.button('Run/Pause')
    if 'capture' not in st.session_state:
        st.session_state.capture = False

    if run:
        st.session_state.capture = not st.session_state.capture

    while st.session_state.capture:
        ret, frame = cap.read()
        if not ret:
            st.error("No se puede obtener el frame de la cámara")
            break

        # Convierte la imagen de BGR a RGB
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Muestra el frame en la interfaz de Streamlit
        frame_window.image(frame)

    cap.release()


if __name__ == '__main__':
    main()
