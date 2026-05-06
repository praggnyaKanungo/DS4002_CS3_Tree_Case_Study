# Can We Use ML to Identify Trees Around UVA?

## A DS 4002 Case Study by Praggnya Kanungo

![Tree Classification Banner]((https://unsplash.com/photos/green-leaf-tree-under-blue-sky-tGTVxeOr_Rs))

---

# Quick Overview

This case study looks at how we can use convolutional neural networks (CNNs) to classify tree species from images. Students will create and ensure high performance of their model based on a real world dataset of tree images. Then they will use images they take around Charlottesville to test their model on.

---

# Hook and Rubric Documents

The hook document is found in the `HookDocument` directory. In this directory, you will find one pdf which is the hook document, which aims to "hook" or encouragingly introduce the students to this project. The rubric is in the `Rubric` directory, as the only pdf in that folder. This describes the requirements the deliverable needed completing this case study successfully.

---

# Data

The dataset that the students will use in this project contains labeled images of 23 different tree species divided into training, validation, and testing splits. There is a script provided so the student can download this dataset, and once they download it, it will appear in the DATA directory of their local clone of this repo.

The dataset can be downloaded by running:

```bash
python download_data.py
```

from the `SCRIPTS` directory.

---

# Materials

In the `Materials` folder, you will find many different resources that will hopefully aid students in achieving their goal of completing this case study. This directory contains different subdirectories:

## Data Context
This has the paper that introduced the tree dataset used for this project.

## Documentations
This folder contains different technical articles to help to learn and understand the following concepts needed for this case study: 
- convolutional neural networks (CNNs)
- data augmentation
- neural network fundamentals

## Explainer
This has an article that describes a similar project of using CNNs to classify trees species. This article is a great beginning article to read as an "explainer" for this project as it shows students how such a project can be used in real life and the impact it can have. 

You will also find a README.md in the `Materials` folder with links to each of these articles in case you find the pdfs hard to read.

---

# Example Scripts

In the `Scripts` directory, you will find the following scripts:

- download_data.py: The student will need to run this to download the dataset.
- Example_eda_plots.py: This is something the student can refer to when they are attempting to create EDA plots. This is an EXAMPLE script! They do not have to follow what is given in this script and are encouraged to try something different.
- Example_Analysis_Final.ipynb: This is a Jupyter Notebook with example code for the CNN classifer here. Once again, this is an EXAMPLE script. Students do not need to follow this exactly as is and are encouraged to do something different.

---

# References

The following sources were consulted in creating this case study (and the project that is it based on):


- CPRE. (n.d.). Tree time: 20 facts about trees you might not know. Tree time: 20 facts about trees you might not know
- Gianpiero Andrenacci, “A Simple Image Classifier With a Python Neural Network,” Medium, 3 Nov. 2024, https://medium.com/data-bistrot/a-simple-image-classifier-with-a-python-neural-network-82a5522fe48b
- Jacob Murel, Eda Kavlakoglu, “What is Data Augmentation,” IBM, ​​https://www.ibm.com/think/topics/data-augmentation
- Tingting Yang, Suyin Zhou, Zhijie Huang, Aijun Xu, Junhua Ye, Jianxin Yin, Urban street tree dataset for image classification and instance segmentation, Computers and Electronics in Agriculture, Volume 209, 2023, 107852, ISSN 0168-1699, https://doi.org/10.1016/j.compag.2023.107852.

