from pathlib import Path

import numpy as np
import tensorflow as tf
from PIL import Image


BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
MODEL_PATH = BASE_DIR / "cat_dog_cnn.keras"
IMAGE_SIZE = (128, 128)


def load_image(path):
    img = Image.open(path).convert("RGB").resize(IMAGE_SIZE)
    arr = np.array(img)
    return np.expand_dims(arr, axis=0)


def main():
    if not MODEL_PATH.exists():
        raise FileNotFoundError("Chua co model. Hay chay: python train_cnn.py")

    model = tf.keras.models.load_model(MODEL_PATH)

    # image_dataset_from_directory sap xep class theo alphabet: cat = 0, dog = 1.
    class_names = ["cat", "dog"]

    image_paths = sorted(DATA_DIR.glob("*/*.png"))
    print("Ket qua du doan 10 anh:")
    print("-" * 60)

    for image_path in image_paths:
        x = load_image(image_path)
        prob_dog = float(model.predict(x, verbose=0)[0][0])
        predicted_index = 1 if prob_dog >= 0.5 else 0
        predicted_label = class_names[predicted_index]
        confidence = prob_dog if predicted_label == "dog" else 1 - prob_dog
        true_label = image_path.parent.name

        print(
            f"{image_path.name:10s} | that: {true_label:3s} | "
            f"du doan: {predicted_label:3s} | do tin cay: {confidence:.2%}"
        )


if __name__ == "__main__":
    main()
