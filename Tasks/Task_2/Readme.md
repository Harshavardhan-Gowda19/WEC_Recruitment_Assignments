# Underwater Image Enhancement Project

This project implements various image generation techniques to enhance the quality of underwater images. The project is divided into four subtasks, each exploring a different approach to image enhancement.

## Project Structure

The project consists of four main GoogleCollab notebooks, each corresponding to a subtask:

- **VAE_task2A.ipynb**: Variational Autoencoders (VAEs)
- **GAN_task2B.ipynb**: Generative Adversarial Networks (GANs) - MNIST Practice
- **GAN_task2C.ipynb**: GANs for Underwater Image Enhancement
- **Diffusion_model_task2D.ipynb**: Diffusion Models

## Subtasks and Architectures

### Subtask 1: Variational Autoencoders (VAEs)

- **Architecture**: Encoder-Decoder network with a latent space
- **Encoder**: Convolutional layers followed by dense layers
- **Decoder**: Dense layers followed by transposed convolutional layers
- **Loss**:  KL divergence

### Subtask 2: Generative Adversarial Networks (GANs) - MNIST Practice

- **Generator**: Fully connected layers with LeakyReLU activation
- **Discriminator**: Fully connected layers with LeakyReLU activation
- **Loss**: adversarial_loss

### Subtask 3: GANs for Underwater Image Enhancement

- **Generator**: U-Net-like architecture with skip connections
- **Discriminator**: PatchGAN discriminator
- **Loss**: L1 loss

### Subtask 4: Diffusion Models

- **Architecture**: Simple U-Net-like model for denoising
- **Forward process**: Linear noise schedule
- **Reverse process**: Iterative denoising
- **Loss**: Mean Squared Error (MSE)

## Evaluation Metrics

Each subtask includes the following evaluation metrics:

- Mean Squared Error (MSE)
- Peak Signal-to-Noise Ratio (PSNR)
- Structural Similarity Index (SSIM)

## Conclusion

Based on the evaluation metrics, here's a comparison of the four models:

| Subtask                               | Mean MSE                                                             | Mean PSNR | Mean SSIM |
| ------------------------------------- | -------------------------------------------------------------------- | --------- | --------- |
| VAE (VAE_task2A)                       | 0.08615907281637192                                                              | 10.881352121899013   | 0.23851041495800018    |
| GAN - MNIST (GAN_task2B)               | 0.1512 | 9.47 | 0.2403 |
| GAN for Underwater Images (GAN_task2C) | 0.01947583749057039                                                               | 18.910640776784795   | 0.8239411484254034    |
| Diffusion Model (Diffusion_model_task2D)           | 0.2130                                                              | 12.1094  | 0.1199    |

Based on these results, we can conclude that:

- The GAN for Underwater Images (GAN_task2C) performed the best overall, with the lowest MSE, highest PSNR, and highest SSIM scores.
- The Diffusion Model (Diffusion_model_task2D) came in second, showing promising results across all metrics.
- The VAE (VAE_task2A) had the lowest performance among the three applicable models for underwater image enhancement.
- The GAN trained on MNIST (GAN_task2B) was not directly applicable to underwater image enhancement but served as a learning exercise for GAN implementation.

---

The GAN architecture has shown promising results for underwater image enhancement in this task. However, I believe the diffusion model holds greater potential. Due to limited computational resources, I could only train the diffusion model for 10 epochs, whereas the GAN and other models received more extensive training. With sufficient training, the diffusion model may ultimately surpass the others in performance.
