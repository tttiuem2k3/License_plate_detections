# 🚘 Automatic License Plate Detection with YOLOv8

> A computer-vision project for detecting license-plate regions and plate characters using **two YOLO models**, with a simple **Tkinter desktop demo** for image-based inference.

---

## 📌 Introduction

License_plate_detections focuses on the detection side of an Automatic License Plate Recognition workflow.

The active source currently uses:

1. A first YOLO model to detect the license-plate region from an input image.
2. A second YOLO model to detect character/plate components inside each cropped region.
3. A Tkinter GUI to select an image and visualize both stages of prediction.

The repository also contains training configuration/data files and historical commented code for an earlier Flask experiment, but the active runnable demo is the Tkinter application in predict.py.

---

## 🚀 Key Features

- 🖼️ Select an image from a desktop file dialog.
- 🎯 Detect license-plate regions with YOLO.
- ✂️ Crop detected regions automatically.
- 🔎 Run a second YOLO model on each cropped plate.
- ↔️ Sort bounding boxes from left to right before visualization.
- 🏷️ Print detected class labels from the second model.
- 🖥️ Display predictions through a Tkinter GUI.
- 🏋️ Include source/configuration for YOLO model training.

---

## 🏗️ Current Inference Flow

~~~text
Input Image
    │
    ▼
YOLO Model 1
License Plate Detection
    │
    ▼
Detected Bounding Boxes
    │
    ▼
Crop Each Plate Region
    │
    ▼
YOLO Model 2
Character / Plate-part Detection
    │
    ▼
Sort Bounding Boxes
Left → Right
    │
    ▼
Tkinter Visualization
+ Detected Labels
~~~

---

## 🧠 Model Training

Main.py loads a YOLOv8 pretrained model as the starting point for training:

~~~text
YOLO("yolov8x.pt")
~~~

The repository also contains:

- mydata.yaml
- mydataLP.yaml
- Data/
- runs/

These files support the custom YOLO training/evaluation workflow.

---

## 📂 Dataset

The project documentation records a dataset of roughly 24K labeled images with YOLO-format bounding boxes.

| Split | Images |
|---|---:|
| Train | 21,173 |
| Validation | 2,046 |
| Test | 1,019 |

The original experiment notes also record a training configuration around:

- 50 epochs
- Batch size 16
- Image size 640
- RTX 3090 test environment

These values describe the project experiment and may need adjustment for a different GPU/model configuration.

---

## 🛠️ Technologies Used

- 🐍 Python
- 👁️ Ultralytics YOLOv8
- 🖼️ Pillow
- 🔢 NumPy
- 🖥️ Tkinter
- 🎮 GPU/CUDA for model training

---

## 📂 Project Structure

~~~text
License_plate_detections/
├── Data/                  # Training / validation data
├── runs/                  # YOLO training outputs
├── templates/             # Legacy Flask experiment templates
├── Main.py                # YOLO model/training entry source
├── predict.py             # Active Tkinter inference application
├── mydata.yaml            # YOLO dataset config
├── mydataLP.yaml          # License-plate dataset config
├── link_yolov8x.txt
└── README.md
~~~

---

## ⚙️ Installation

### 1. Clone repository

~~~bash
git clone https://github.com/tttiuem2k3/License_plate_detections.git
cd License_plate_detections
~~~

### 2. Install Python dependencies

At minimum, the active demo requires:

~~~bash
pip install ultralytics pillow numpy
~~~

Tkinter is normally included with standard Python installations on Windows.

### 3. Prepare model weights

The current predict.py contains local model paths:

~~~text
D:/Download/best.pt
D:/Download/bestLP.pt
~~~

Change these paths to the actual locations of your trained weights before running.

### 4. Run the desktop demo

~~~bash
python predict.py
~~~

Choose an image from the file dialog to start inference.

---

## ⚠️ Source Note

Older Flask/web inference code is still present in predict.py as commented source. It is not the active runtime path.

The current implementation also performs object/character detection rather than a PyTesseract OCR pipeline, so the README reflects the code that actually runs.

---

## 🚀 Future Development

- Re-enable a clean web/API inference layer.
- Move model paths into configuration/environment variables.
- Convert detected character labels into a normalized license-plate string.
- Add video/stream processing.
- Add evaluation metrics directly to the repository.
- Improve robustness for blur, rotation and occlusion.

---

## 📞 Contact

- 📧 Email: tttiuem2k3@gmail.com
- 👥 LinkedIn: [Thịnh Trần](https://www.linkedin.com/in/thinh-tran-04122k3/)
- 💬 Zalo / Phone: +84 329966939 | +84 336639775

---
