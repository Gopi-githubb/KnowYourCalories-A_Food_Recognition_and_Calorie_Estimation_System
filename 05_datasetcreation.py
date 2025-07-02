import os
import shutil
import random

def split_dataset(input_dir, output_dir, split_ratio=(0.7, 0.2, 0.1)):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for category in os.listdir(input_dir):
        category_dir = os.path.join(input_dir, category)
        if not os.path.isdir(category_dir):
            continue  # Skip if it's not a directory

        images = os.listdir(category_dir)
        random.shuffle(images)
        
        train_split = int(split_ratio[0] * len(images))
        val_split = int(split_ratio[1] * len(images))
        
        train_images = images[:train_split]
        val_images = images[train_split:train_split + val_split]
        test_images = images[train_split + val_split:]

        for image_set, subset in zip([train_images, val_images, test_images], ['train', 'val', 'test']):
            subset_dir = os.path.join(output_dir, subset, category)
            os.makedirs(subset_dir, exist_ok=True)
            for image in image_set:
                shutil.copy(os.path.join(category_dir, image), subset_dir)

input_dir = 'C:/Users/SUJAL/OneDrive/Desktop/FRCE/food-101/images'
output_dir = 'C:/Users/SUJAL/OneDrive/Desktop/FRCE/output_dataset'

split_dataset(input_dir, output_dir)
