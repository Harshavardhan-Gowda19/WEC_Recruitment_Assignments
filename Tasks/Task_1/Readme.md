---

# DeepFake Image Classification

This project addresses DeepFake detection by combining traditional image processing techniques with machine learning. The model uses a combination of feature extraction methods, such as Canny edge detection and Local Binary Pattern (LBP), with an SVM classifier for accurate classification of images as real or fake.

## Table of Contents
1. [Project Overview](#project-overview)
2. [Techniques and Methodologies](#techniques-and-methodologies)
3. [Model Pipeline](#model-pipeline)
4. [Future Improvements](#future-improvements)

---

### 1. Project Overview <a name="project-overview"></a>
This project leverages edge and texture analysis to enhance DeepFake detection. The model’s architecture, built without deep learning layers, captures subtle features through traditional ML techniques, aiming for better accuracy in discerning authentic and manipulated images.

### 2. Techniques and Methodologies <a name="techniques-and-methodologies"></a>
- **Canny Edge Detection**: Highlights prominent edges to reveal boundary inconsistencies that suggest manipulation.
- **Local Binary Pattern (LBP)**: Encodes texture patterns, identifying differences between natural and synthetic textures.
- **DFT Visualization**: Computes and visualizes the Discrete Fourier Transform (DFT) of an image to analyze frequency components for potential anomalies.
  
### 3. Model Pipeline <a name="model-pipeline"></a>
- **Feature Extraction**: Canny edge detection and LBP extract crucial image characteristics.
- **DFT Computation**: Visualizes the frequency spectrum of images to detect subtle inconsistencies.
- **Classification**: An SVM classifier integrates extracted features to classify images as real or fake.

### 4. Future Improvements <a name="future-improvements"></a>
- **Refinement of Edge Detection**: Testing advanced edge techniques for subtle manipulation detection.
- **Feature Set Expansion**: Exploring additional texture or frequency features to enhance model performance.

---
