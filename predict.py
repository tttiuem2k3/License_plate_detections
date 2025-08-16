# import tkinter as tk
# from tkinter import filedialog
# from PIL import Image, ImageTk
# from ultralytics import YOLO
# import numpy as np
#
# # Load the pre-trained YOLO model
# model = YOLO("D:/Download/best.pt")
# model2= YOLO("D:/Download/bestLP.pt")
# def predict_image():
#     # Hàm này sẽ được gọi khi nhấn nút "Dự đoán"
#     file_path = filedialog.askopenfilename()
#     if file_path:  # Nếu người dùng đã chọn một tệp hợp lệ
#         results = model(file_path)
#
#         # Lấy kết quả và hiển thị hình ảnh dự đoán
#         for r in results:
#             im_array = r.plot()
#             print(r.plot())
#             im = Image.fromarray(im_array[..., ::-1])
#             resized_im = im.resize((500, 400))
#             # Hiển thị hình ảnh gốc
#             original_image = ImageTk.PhotoImage(resized_im)
#             original_label.configure(image=original_image)
#             original_label.image = original_image
#
#             # Xóa các hình ảnh cũ (nếu có)
#             for widget in result_frame.winfo_children():
#                 widget.destroy()
#
#             # Cắt và hiển thị hình ảnh từng khung ảnh đã dự đoán
#             for box in r.boxes.data:
#                 # Trích xuất tọa độ từ bounding box
#                 x1, y1, x2, y2, _, _ = box.tolist()
#
#                 # Cắt ảnh theo bounding box
#                 cropped_image = im.crop((x1-1, y1-1, x2+1, y2+1))
#                 results2 = model2(cropped_image)
#                 for r1 in results2:
#                     im_array2 = r1.plot()
#                     im2 = Image.fromarray(im_array2[..., ::-1])
#
#                     # Hiển thị hình ảnh gốc
#                     cropped_photo = ImageTk.PhotoImage(im2)
#                     cropped_label = tk.Label(result_frame, image=cropped_photo)
#                     cropped_label.image = cropped_photo
#                     cropped_label.pack(pady=5)
#
#                 # # Hiển thị ảnh đã cắt
#                 # cropped_photo = ImageTk.PhotoImage(cropped_image)
#                 # cropped_label = tk.Label(result_frame, image=cropped_photo)
#                 # cropped_label.image = cropped_photo
#                 # cropped_label.pack(pady=5)
#
# # Tạo cửa sổ
# root = tk.Tk()
# root.title("Dự đoán và hiển thị ảnh đã cắt")
#
# # Tạo và định dạng các phần tử giao diện
# label = tk.Label(root, text="Chọn một hình ảnh để dự đoán và hiển thị ảnh đã cắt:")
# label.pack(pady=10)
#
# button = tk.Button(root, text="Chọn hình ảnh", command=predict_image)
# button.pack(pady=5)
#
# original_label = tk.Label(root)
# original_label.pack(pady=10)
#
# result_frame = tk.Frame(root)
# result_frame.pack(pady=10)
#
# # Chạy vòng lặp sự kiện
# root.mainloop()
# # ## -----------------------------------------------------------------------------------------
# from flask import Flask, render_template, request
# import io
# import base64
# from PIL import Image
# from ultralytics import YOLO
#
# app = Flask(__name__)
#
# # Load the pre-trained YOLO model
# model = YOLO("D:/Download/best.pt")
# model_lq = YOLO("D:/Download/bestLP.pt")
#
# @app.route("/", methods=["GET", "POST"])
# def predict_image():
#     if request.method == "POST":
#         file = request.files["file"]
#         image_bytes = file.read()
#         image = Image.open(io.BytesIO(image_bytes))
#
#         results = model(image)
#
#         image_base64 = image_to_base64(image)
#
#
#         for r in results:
#             im_array = r.plot()
#             im = Image.fromarray(im_array[..., ::-1])
#             for box in r.boxes.data:
#                 # _, _, _, _, _, cls = box.tolist()
#                 # label = model.names[int(cls)]
#                 # labels.append(label)
#                 x1, y1, x2, y2, _, _ = box.tolist()
#
#                 # Cắt ảnh theo bounding box
#                 cropped_image = im.crop((x1-1, y1-1, x2+1, y2+1))
#                 results1 = model_lq(cropped_image)
#                 labels = []
#                 for r1 in results1:
#                     for box1 in r1.boxes.data:
#                         _, _, _, _, _, cls = box.tolist()
#                         if int(cls) in model_lq.names:  # Kiểm tra cls có tồn tại trong model.names không
#                             label = model_lq.names[int(cls)]
#                         else:
#                             label = "Unknown"
#                         labels.append(label)
#         return render_template("result.html", image=image_base64, labels=labels)
#
#     return render_template("index.html")
#
# def image_to_base64(image):
#     buffered = io.BytesIO()
#     image.save(buffered, format="JPEG")
#     img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
#     return f"data:image/jpeg;base64,{img_str}"
#
# if __name__ == "__main__":
#     app.run(debug=True)
##-------------------------------------------------------------------------
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from ultralytics import YOLO
import numpy as np

# Load the pre-trained YOLO models
model = YOLO("D:/Download/best.pt")
model2 = YOLO("D:/Download/bestLP.pt")

def predict_image():
    # Hàm này sẽ được gọi khi nhấn nút "Dự đoán"
    file_path = filedialog.askopenfilename()
    if file_path:  # Nếu người dùng đã chọn một tệp hợp lệ
        results = model(file_path)

        # Lấy kết quả và hiển thị hình ảnh dự đoán
        for r in results:
            im_array = r.plot()
            im = Image.fromarray(im_array[..., ::-1])
            resized_im = im.resize((500, 400))
            # Hiển thị hình ảnh gốc
            original_image = ImageTk.PhotoImage(resized_im)
            original_label.configure(image=original_image)
            original_label.image = original_image

            # Xóa các hình ảnh cũ (nếu có)
            for widget in result_frame.winfo_children():
                widget.destroy()

            # Trích xuất các bounding box
            boxes = []
            for box in r.boxes.data:
                x1, y1, x2, y2, _, _ = box.tolist()
                boxes.append((x1, y1, x2, y2))

            # Sắp xếp các bounding box theo tọa độ x1 (từ trái sang phải)
            boxes.sort(key=lambda b: b[0])

            # Cắt và hiển thị hình ảnh từng khung ảnh đã dự đoán từ model2
            for box in boxes:
                x1, y1, x2, y2 = box
                # Cắt ảnh theo bounding box
                cropped_image = im.crop((x1-1, y1-1, x2+1, y2+1))
                results2 = model2(cropped_image)
                for r1 in results2:
                    im_array2 = r1.plot()
                    im2 = Image.fromarray(im_array2[..., ::-1])
                    resized_im2 = im2.resize((500, 150))
                    boxes2= []
                    for box2 in r1.boxes.data:
                        x1, y1, x2, y2, _, _ = box2.tolist()
                        boxes2.append((x1, y1, x2, y2))
                    boxes2.sort(key=lambda b: b[0])
                    # Hiển thị hình ảnh đã cắt
                    cropped_photo = ImageTk.PhotoImage(resized_im2)
                    cropped_label = tk.Label(result_frame, image=cropped_photo)
                    cropped_label.image = cropped_photo
                    cropped_label.pack(pady=5)

                    # In tên của nhãn từ model2
                    for box2 in r1.boxes.data:
                        label = r1.names[int(box2[-1])]
                        print(f"Detected label: {label}")

# Tạo cửa sổ
root = tk.Tk()
root.title("Dự đoán và hiển thị ảnh đã cắt")

# Tạo và định dạng các phần tử giao diện
label = tk.Label(root, text="Chọn một hình ảnh để dự đoán và hiển thị ảnh đã cắt:")
label.pack(pady=10)

button = tk.Button(root, text="Chọn hình ảnh", command=predict_image)
button.pack(pady=5)

original_label = tk.Label(root)
original_label.pack(pady=10)

result_frame = tk.Frame(root)
result_frame.pack(pady=10)

# Chạy vòng lặp sự kiện
root.mainloop()