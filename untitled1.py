# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 16:18:30 2024

@author: drops
"""



import cv2
import numpy as np

def calculate_turbidity(image):
    # Convertir la imagen a escala de grises
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Calcular el valor promedio de los píxeles en la imagen
    mean_intensity = np.mean(gray)
    
    # Convertir el valor promedio de intensidad a NTU
    # Esta fórmula es un ejemplo y debe ajustarse según la calibración específica de tu sistema
    ntu = (255 - mean_intensity) * 10 / 255
    
    return ntu

# Iniciar la captura de video
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: No se pudo abrir la cámara.")
    exit()

while True:
    # Capturar frame por frame
    ret, frame = cap.read()
    
    if not ret:
        print("Error: No se pudo capturar el frame.")
        break
    
    # Calcular la turbidez
    turbidity = calculate_turbidity(frame)
    
    # Mostrar el valor de la turbidez en el frame
    cv2.putText(frame, f"Turbidity: {turbidity:.2f} NTU", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    # Mostrar el frame
    cv2.imshow('Turbidity Measurement', frame)
    
    # Salir del bucle al presionar la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la captura de video y cerrar todas las ventanas
cap.release()
cv2.destroyAllWindows()