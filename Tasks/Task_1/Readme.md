# DeepFake Image Classification

This project combines CNNs with image processing techniques to detect DeepFake images. By integrating Canny edge detection and Local Binary Pattern (LBP) texture analysis, the model identifies subtle differences in authenticity that CNNs alone may overlook.

## Table of Contents
1. [Project Overview](#project-overview)
2. [Model Architecture](#model-architecture)
3. [Techniques Used](#techniques-used)
4. [Results](#results)
5. [Future Work](#future-work)

---

### 1. Project Overview <a name="project-overview"></a>
The goal is to classify images as real or fake by enhancing traditional CNNs with feature extraction methods that capture edge and texture inconsistencies.

### 2. Model Architecture <a name="model-architecture"></a>
- **CNN Layers**: Extract core features.
- **Canny Edge Detection**: Highlights unnatural boundaries typical in fakes.
- **LBP Texture Analysis**: Captures texture patterns, aiding in real vs. fake differentiation.
- **SVM Classifier**: Consolidates features for final classification.

### 3. Techniques Used <a name="techniques-used"></a>
- **Canny Edge Detection**: Reveals unnatural edges in fake images.
- **LBP**: Identifies subtle texture variations.
- **SVM**: Final classifier for accurate predictions.

### 4. Results <a name="results"></a>
Integrating Canny and LBP improved feature visibility, helping the SVM classifier distinguish DeepFakes more effectively.

### 5. Future Work <a name="future-work"></a>
Plans include exploring additional edge detection methods, enhancing dataset diversity, and testing ensemble models for greater accuracy.
