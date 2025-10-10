from keras.models import load_model  # Se necesita TensorFlow para que Keras funcione
from PIL import Image, ImageOps  # Instalar pillow en vez de PIL
import numpy as np


# Convertir a función
def get_class(model_path, labels_path, image_path):
    # Cargar el modelo
    model = load_model(model_path, compile=False)

    # Cargar las etiquetas
    class_names = open(labels_path, "r").readlines()

    # Crear el array de la forma correcta para alimentar al modelo de keras
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    # Cargar y procesar la imagen
    image = Image.open(image_path).convert("RGB")
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
    data[0] = normalized_image_array

    # Predicción del modelo
    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]
    return class_name[2:], confidence_score