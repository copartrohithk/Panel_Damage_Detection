import os
import random
import shutil

# Paths
dataset_path = '/Users/rokokkula/Documents/Panel_Damage_Detection/data'
images_path = os.path.join(dataset_path, 'images')
labels_path = os.path.join(dataset_path, 'labels')

train_path = os.path.join(dataset_path, 'train')
val_path = os.path.join(dataset_path, 'val')
test_path = os.path.join(dataset_path, 'test')

# Create directories if they don't exist
os.makedirs(train_path, exist_ok=True)
os.makedirs(val_path, exist_ok=True)
os.makedirs(test_path, exist_ok=True)

# Split ratios
train_ratio = 0.7
val_ratio = 0.2
test_ratio = 0.1

all_images = [f for f in os.listdir(images_path) if os.path.isfile(os.path.join(images_path, f))]
random.shuffle(all_images)  # Shuffle the dataset

total_images = len(all_images)
train_count = int(total_images * train_ratio)
val_count = int(total_images * val_ratio)
test_count = total_images - train_count - val_count

train_images = all_images[:train_count]
val_images = all_images[train_count:train_count + val_count]
test_images = all_images[train_count + val_count:]

def move_files(image_list, destination_folder):
    for image in image_list:
        # Move image files
        image_path = os.path.join(images_path, image)
        shutil.copy(image_path, os.path.join(destination_folder, 'images', image))

        # Move corresponding label files
        label_name = os.path.splitext(image)[0] + '.txt'
        label_path = os.path.join(labels_path, label_name)
        if os.path.exists(label_path):
            shutil.copy(label_path, os.path.join(destination_folder, 'labels', label_name))

# Create subdirectories
os.makedirs(os.path.join(train_path, 'images'), exist_ok=True)
os.makedirs(os.path.join(train_path, 'labels'), exist_ok=True)
os.makedirs(os.path.join(val_path, 'images'), exist_ok=True)
os.makedirs(os.path.join(val_path, 'labels'), exist_ok=True)
os.makedirs(os.path.join(test_path, 'images'), exist_ok=True)
os.makedirs(os.path.join(test_path, 'labels'), exist_ok=True)

# Move the files
move_files(train_images, train_path)
move_files(val_images, val_path)
move_files(test_images, test_path)
