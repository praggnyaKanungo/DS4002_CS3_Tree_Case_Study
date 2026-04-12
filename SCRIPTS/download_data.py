import os
import kagglehub
import shutil

base_path = os.path.dirname(__file__)  # SCRIPTS folder
data_path = os.path.join(base_path, "..", "DATA")

os.makedirs(data_path, exist_ok=True)

dataset_path = kagglehub.dataset_download(
    "erickendric/tree-dataset-of-urban-street-classification-tree"
)


for item in os.listdir(dataset_path):
    src = os.path.join(dataset_path, item)
    dst = os.path.join(data_path, item)

    if os.path.exists(dst):
        print(f"Skipping existing: {item}")
        continue

    shutil.move(src, dst)
