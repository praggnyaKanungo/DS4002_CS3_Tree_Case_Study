import os
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
from collections import Counter

# Paths
base_path = os.path.dirname(__file__)
data_path = os.path.join(base_path, "..", "DATA", "tree")
output_path = os.path.join(base_path, "..", "OUTPUTS")

os.makedirs(output_path, exist_ok=True)

def plot_class_distribution(split="train"):
    split_path = os.path.join(data_path, split)
    
    class_counts = {}
    
    for class_name in os.listdir(split_path):
        class_folder = os.path.join(split_path, class_name)
        if os.path.isdir(class_folder):
            class_counts[class_name] = len(os.listdir(class_folder))
    
    plt.figure()
    plt.bar(class_counts.keys(), class_counts.values())
    plt.xticks(rotation=90)
    plt.title(f"Class Distribution ({split})")
    plt.xlabel("Tree Species")
    plt.ylabel("Number of Images")
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_path, f"class_distribution_{split}.png"))
    plt.close()

def plot_sample_images(split="train", num_classes=5):
    split_path = os.path.join(data_path, split)
    
    classes = os.listdir(split_path)[:num_classes]
    
    plt.figure(figsize=(10, 5))
    
    for i, class_name in enumerate(classes):
        class_folder = os.path.join(split_path, class_name)
        img_name = os.listdir(class_folder)[0]
        img_path = os.path.join(class_folder, img_name)
        
        img = Image.open(img_path)
        
        plt.subplot(1, num_classes, i + 1)
        plt.imshow(img)
        plt.title(class_name)
        plt.axis("off")
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_path, f"sample_images_{split}.png"))
    plt.close()

def plot_image_sizes(split="train", max_images=1000000):
    split_path = os.path.join(data_path, split)
    
    widths = []
    heights = []
    
    count = 0
    
    for class_name in os.listdir(split_path):
        class_folder = os.path.join(split_path, class_name)
        
        for img_name in os.listdir(class_folder):
            img_path = os.path.join(class_folder, img_name)
            
            try:
                img = Image.open(img_path)
                w, h = img.size
                widths.append(w)
                heights.append(h)
                
                count += 1
                if count >= max_images:
                    break
            except:
                continue
        
        if count >= max_images:
            break
    
    plt.figure()
    plt.scatter(widths, heights, alpha=0.3)

    plt.xlabel("Width")
    plt.ylabel("Height")
    plt.title(f"Image Size Distribution (N = {len(widths)})")

    plt.savefig(os.path.join(output_path, "image_sizes.png"))
    plt.close()

def get_image_sizes(split):
    split_path = os.path.join(data_path, split)
    
    widths = []
    heights = []
    
    for class_name in os.listdir(split_path):
        class_folder = os.path.join(split_path, class_name)
        
        if not os.path.isdir(class_folder):
            continue
        
        for img_name in os.listdir(class_folder):
            img_path = os.path.join(class_folder, img_name)
            
            if not os.path.isfile(img_path):
                continue
            
            try:
                img = Image.open(img_path)
                w, h = img.size
                widths.append(w)
                heights.append(h)
            except:
                continue
    
    return widths, heights

def plot_size_scatter_all_splits():
    for split in ["train", "val", "test"]:
        widths, heights = get_image_sizes(split)
        
        plt.figure()
        plt.scatter(widths, heights, alpha=0.3)
        
        plt.xlabel("Width")
        plt.ylabel("Height")
        plt.title(f"{split.capitalize()} Image Sizes (N = {len(widths)})")
        
        plt.savefig(os.path.join(output_path, f"scatter_{split}.png"))
        plt.close()

def plot_width_distribution():
    all_widths = []
    labels = []

    for split in ["train", "val", "test"]:
        widths, _ = get_image_sizes(split)
        all_widths.append(widths)
        labels.append(split.capitalize())

    plt.figure()
    plt.boxplot(all_widths, labels=labels)

    plt.ylabel("Width (pixels)")
    plt.title("Width Distribution Across Splits")

    plt.savefig(os.path.join(output_path, "width_boxplot.png"))
    plt.close()

def plot_height_distribution():
    all_heights = []
    labels = []

    for split in ["train", "val", "test"]:
        _, heights = get_image_sizes(split)
        all_heights.append(heights)
        labels.append(split.capitalize())

    plt.figure()
    plt.boxplot(all_heights, labels=labels)

    plt.ylabel("Height (pixels)")
    plt.title("Height Distribution Across Splits")

    plt.savefig(os.path.join(output_path, "height_boxplot.png"))
    plt.close()

    
if __name__ == "__main__":
    print("Running")

    plot_class_distribution("train")
    plot_class_distribution("val")
    plot_class_distribution("test")

    plot_sample_images("train")

    plot_image_sizes("train")
    plot_size_scatter_all_splits()
    plot_width_distribution()
    plot_height_distribution()

    print("EDA complete!")