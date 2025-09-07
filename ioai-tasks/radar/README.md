# U-Net for Radar Heatmap Segmentation

This project is a binary image segmentation task from the at-home stage of the International Olympiad in Artificial Intelligence (IOAI).

The input consists of radar heatmaps (2D grayscale images), and the goal is to classify **each pixel** as either:
- Human presence (positive class)
- Background (negative class)

---

## Key Idea

I implemented a simple **U-Net architecture** with dropout layers as a baseline model. The goal was to test whether a basic segmentation network could detect human presence from noisy radar data **without any preprocessing or domain-specific feature engineering**.

Despite the simplicity of the setup, the model produced visually reasonable masks and learned the task structure effectively.

---

## Input Data
The radar data consisted of multi-channel heatmaps encoding various physical signals, such as:

- Elevation angles
- Object velocities
- Spatial coordinates

---

## Techniques Used

- U-Net architecture with dropout regularization
- Pixel-wise binary cross-entropy loss
- No preprocessing or augmentation
- PyTorch

---

## Files

- `unet_segmentation.ipynb`: Notebook with model definition and a training loop

---

## Dataset

The dataset is no longer publicly accessible and was part of a closed competition platform.

