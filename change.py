import os
import xmltodict
from tqdm import tqdm
from PIL import Image

# Đường dẫn đến thư mục chứa ảnh và chú thích
images_dir = 'LPcharacters/images'
annotations_dir = 'LPcharacters/annotations'
labels_dir = 'LPcharacters/labels'

# Tạo thư mục labels nếu chưa tồn tại
os.makedirs(labels_dir, exist_ok=True)

# Danh sách các class (thêm class 'licence')
class_names = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']  # Thay đổi theo class của bạn

# Chuyển đổi bounding box từ VOC sang YOLO
def convert_voc_to_yolo(annotation, image_size):
    objects = annotation['annotation'].get('object')
    if objects is None:
        return []

    if not isinstance(objects, list):
        objects = [objects]

    yolo_format = []
    for obj in objects:
        class_name = obj['name']
        if class_name not in class_names:
            print(f"Warning: Class '{class_name}' not found in class_names.")
            continue

        class_id = class_names.index(class_name)
        bbox = obj['bndbox']
        xmin = int(bbox['xmin'])
        ymin = int(bbox['ymin'])
        xmax = int(bbox['xmax'])
        ymax = int(bbox['ymax'])

        # Chuyển đổi tọa độ sang định dạng YOLO
        x_center = (xmin + xmax) / 2 / image_size[0]
        y_center = (ymin + ymax) / 2 / image_size[1]
        width = (xmax - xmin) / image_size[0]
        height = (ymax - ymin) / image_size[1]

        # Lưu định dạng YOLO
        yolo_format.append(f"{class_id} {x_center} {y_center} {width} {height}")

    return yolo_format

# Lấy danh sách các file ảnh
image_files = [f for f in os.listdir(images_dir) if f.endswith(('.jpg', '.png'))]
print(f"Found {len(image_files)} images.")

if not image_files:
    print("No images found. Please check the images directory.")
    exit()

# Lấy danh sách các file chú thích
annotation_files = [f for f in os.listdir(annotations_dir) if f.endswith('.xml')]
print(f"Found {len(annotation_files)} annotation files.")

if not annotation_files:
    print("No annotation files found. Please check the annotations directory.")
    exit()

for image_file in tqdm(image_files):
    # Đường dẫn đến file ảnh và file chú thích tương ứng
    image_path = os.path.join(images_dir, image_file)
    annotation_path = os.path.join(annotations_dir, image_file.replace('.jpg', '.xml').replace('.png', '.xml'))
    label_path = os.path.join(labels_dir, image_file.replace('.jpg', '.txt').replace('.png', '.txt'))

    # Kiểm tra file chú thích có tồn tại không
    if not os.path.exists(annotation_path):
        print(f"Warning: Annotation file not found for image {image_file}")
        continue

    # Lấy kích thước ảnh
    try:
        image = Image.open(image_path)
        width, height = image.size
    except Exception as e:
        print(f"Error: Unable to open image {image_file}. Error: {e}")
        continue

    # Đọc file chú thích và chuyển đổi định dạng
    try:
        with open(annotation_path) as file:
            annotation = xmltodict.parse(file.read())
    except Exception as e:
        print(f"Error: Unable to read annotation file {annotation_path}. Error: {e}")
        continue

    yolo_format = convert_voc_to_yolo(annotation, (width, height))

    if not yolo_format:
        print(f"No valid objects found in annotation file {annotation_path}")
        continue

    # Ghi định dạng YOLO vào file nhãn
    with open(label_path, 'w') as label_file:
        label_file.write('\n'.join(yolo_format))

print("Conversion complete.")
# # import os
# #
# # def replace_text_in_file(file_path, old_text, new_text):
# #     # Đọc nội dung file
# #     with open(file_path, 'r', encoding='utf-8') as file:
# #         file_data = file.read()
# #
# #     # Thay thế các ký tự
# #     file_data = file_data.replace(old_text, new_text)
# #
# #     # Ghi lại nội dung vào file
# #     with open(file_path, 'w', encoding='utf-8') as file:
# #         file.write(file_data)
# #
# # def replace_text_in_folder(folder_path, old_text="2 ", new_text="0 "):
# #     # Duyệt qua tất cả các file trong thư mục
# #     for filename in os.listdir(folder_path):
# #         # Kiểm tra xem có phải là file .txt không
# #         if filename.endswith('.txt'):
# #             file_path = os.path.join(folder_path, filename)
# #             replace_text_in_file(file_path, old_text, new_text)
# #             print(f"Đã thay thế trong file: {filename}")
# #
# # # Gọi hàm với đường dẫn đến thư mục chứa các file .txt
# # folder_path = 'D:/Code/Python/bien_so/datasets/labels/train'
# # replace_text_in_folder(folder_path)
