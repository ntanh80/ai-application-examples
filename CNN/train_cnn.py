from pathlib import Path

import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras import layers, models


BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
MODEL_PATH = BASE_DIR / "cat_dog_cnn.keras"
IMAGE_SIZE = (128, 128)
BATCH_SIZE = 2
EPOCHS = 20


def build_model():
    model = models.Sequential(
        [
            layers.Input(shape=(128, 128, 3)),
            layers.Rescaling(1.0 / 255),
            layers.Conv2D(16, (3, 3), activation="relu"),
            layers.MaxPooling2D(),
            layers.Conv2D(32, (3, 3), activation="relu"),
            layers.MaxPooling2D(),
            layers.Conv2D(64, (3, 3), activation="relu"),
            layers.MaxPooling2D(),
            layers.Flatten(),
            layers.Dense(64, activation="relu"),
            layers.Dense(1, activation="sigmoid"),
        ]
    )

    model.compile(
        optimizer="adam",
        loss="binary_crossentropy",
        metrics=["accuracy"],
    )
    return model


def main():
    if not DATA_DIR.exists():
        raise FileNotFoundError(
            "Chua co thu muc data. Hay chay: python create_demo_images.py"
        )

    train_ds = tf.keras.utils.image_dataset_from_directory(
        DATA_DIR,
        labels="inferred",
        label_mode="binary",
        image_size=IMAGE_SIZE,
        batch_size=BATCH_SIZE,
        shuffle=True,
        seed=42,
    )

    class_names = train_ds.class_names
    print("Cac lop du lieu:", class_names)

    model = build_model()
    model.summary()

    history = model.fit(train_ds, epochs=EPOCHS)
    model.save(MODEL_PATH)
    print(f"Da luu model tai: {MODEL_PATH}")

    plt.figure(figsize=(8, 4))
    plt.plot(history.history["accuracy"], label="Do chinh xac")
    plt.plot(history.history["loss"], label="Ham mat mat")
    plt.title("Qua trinh huan luyen CNN")
    plt.xlabel("Epoch")
    plt.legend()
    plt.tight_layout()
    chart_path = BASE_DIR / "training_history.png"
    plt.savefig(chart_path)
    print(f"Da luu bieu do tai: {chart_path}")


if __name__ == "__main__":
    main()
