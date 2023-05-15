import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.camera import Camera
from kivy.core.window import Window
from kivy.graphics.texture import Texture
from kivy.uix.image import Image
from kivy.clock import Clock
import cv2
import numpy as np

kivy.require('1.11.1')

class MainWidget(BoxLayout):
    def _init_(self, **kwargs):
        super(MainWidget, self)._init_(**kwargs)

        # Configura la cámara
        self.camera = Camera(index=0, resolution=(640, 480))
        self.camera.play()

        # Crea una textura para la cámara
        self.texture = Texture.create(size=self.camera.resolution)
        self.texture.flip_vertical()
        self.texture.blit_buffer(self.camera._buffer, colorfmt='bgr')

        # Crea una imagen para mostrar la cámara
        self.image = Image(texture=self.texture)
        self.add_widget(self.image)

        # Configura la detección de parpadeo
        self.last_brightness = None
        self.blink_threshold = 15
        Clock.schedule_interval(self.detect_blink, 1 / 30)  # 30 FPS

    def detect_blink(self, dt):
        # Obtener el marco actual de la cámara
        frame = self.camera._buffer

        # Convertir la imagen a escala de grises
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Aplicar un filtro gaussiano para suavizar la imagen
        gray = cv2.GaussianBlur(gray, (7, 7), 0)

        # Detectar los ojos en la imagen
        eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
        eyes = eye_cascade.detectMultiScale(gray)

        # Si no se detectan ojos, no se puede detectar el parpadeo
        if len(eyes) == 0:
            return

        # Calcular la media de los valores de los ojos detectados
        mean_eye_value = np.mean([gray[y:y+h, x:x+w] for (x,y,w,h) in eyes])

        # Si no hay un brillo previo, inicializa el brillo previo
        if self.last_brightness is None:
            self.last_brightness = mean_eye_value
            return

        # Calcula la diferencia de brillo
        brightness_diff = abs(mean_eye_value - self.last_brightness)

        # Si la diferencia es mayor que el umbral, se detecta el parpadeo
        if brightness_diff > self.blink_threshold:
            print("¡Pestañaste!")

        # Actualiza el brillo previo
        self.last_brightness = mean_eye_value

class MyApp(App):
    def build(self):
        return MainWidget()

if __name__ == '__main__':
    MyApp().run()