import streamlit as st
import cv2
import numpy as np

def main():
    st.title("Captura de Imagen con la Cámara")

    # Widget de entrada de cámara en Streamlit
    img_file_buffer = st.camera_input("Take a picture")

    # Procesamiento del buffer de imagen si el usuario ha capturado una foto
    if img_file_buffer is not None:
        try:
            # Convertir los bytes del buffer a un array de numpy que OpenCV puede usar
            bytes_data = img_file_buffer.getvalue()
            cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)

            # Verificación del tipo y forma de la imagen procesada
            st.write("Tipo de imagen procesada:", type(cv2_img))
            st.write("Forma de la imagen capturada:", cv2_img.shape)

            # Mostrar la imagen en Streamlit
            st.image(cv2_img, caption='Imagen Capturada', use_column_width=True)

            # Aquí puedes agregar más procesamiento de imágenes con OpenCV
            # Por ejemplo, convertir a escala de grises, detectar bordes, etc.
            gray_img = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2GRAY)
            edges = cv2.Canny(gray_img, 100, 200)
            st.image(edges, caption='Bordes detectados', use_column_width=True)

        except Exception as e:
            st.error(f"Error procesando la imagen: {e}")

if __name__ == '__main__':
    main()
