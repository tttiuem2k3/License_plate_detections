# Automatic License Plate Recognition (ALPR) with YOLOv8 and PyTesseract

## 📌 Overview
This project implements an **Automatic License Plate Recognition (ALPR)** system using **YOLOv8** for object detection and **PyTesseract** for Optical Character Recognition (OCR).  
The system detects and reads license plates from both **images** and **videos** in real-time, achieving high accuracy (90–95%) even with low-resolution images.

## 🎯 Objectives
- Build a robust license plate recognition system for traffic monitoring and security.
- Apply **YOLOv8** for plate detection and **PyTesseract** for character recognition.
- Develop a web application for real-time processing.

## 🔍 Features
- **Image & Video Input**: Supports static images and video streams.
- **Real-Time Detection**: Fast frame processing for surveillance.
- **Multi-Format Support**: Handles different plate sizes, colors, orientations, and layouts.
- **High Accuracy**: Works in varied lighting and weather conditions.


## 🛠️ System Architecture
1. **Data Collection & Labeling** – Collected ~24k labeled images from RoboFlow.
2. **Model Training** – YOLOv8 (`yolov8n.pt` pretrained) on RTX 3090:  
   - Epochs: 50  
   - Batch Size: 16  
   - Image Size: 640px
3. **License Plate Detection** – YOLOv8 detects plate regions (ROI).
4. **Character Extraction** – PyTesseract OCR for text recognition.
5. **API Integration** – RESTful API for plate recognition.


## 📂 Dataset
- **Training Set**: 21,173 images  
- **Validation Set**: 2,046 images  
- **Test Set**: 1,019 images  
Each image has a YOLO-format label file with class ID and bounding box coordinates.

## 📈 Model Performance
- **Precision & Recall**: High detection accuracy.
- **mAP & IoU**: Strong results with potential improvements.
- **Challenges**: Misclassification in some cases; reduced performance on blurry/occluded plates.

##  📞 Contact
- 📧 Email: tttiuem2k3@gmail.com
- 👥 Linkedin: [Thịnh Trần](https://www.linkedin.com/in/thinh-tran-04122k3/)
- 💬 Zalo / Phone: +84 329966939 | +84 336639775
