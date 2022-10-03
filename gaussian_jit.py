from numba import jit
import numpy as np


@jit(nopython=True)
def GaussianBlur(image, kernel):
    height, width = image.shape
    output = np.zeros_like(image)
    kernel_height, kernel_width = kernel.shape
    pad_height, pad_width = kernel_height // 2, kernel_width // 2
    padded_image = np.zeros(
        (height + (2 * pad_height), width + (2 * pad_width)))
    padded_image[pad_height:-pad_height, pad_width:-pad_width] = image
    for x in range(width):
        for y in range(height):
            output[y, x] = (kernel * padded_image[y: y +
                            kernel_height, x: x + kernel_width]).sum()
    return output


if __name__ == "__main__":
    image = np.random.randint(0, 255, size=(300, 300), dtype=np.uint8)
    kernel = np.array([[1, 2, 1],
                       [2, 4, 2],
                       [1, 2, 1]], dtype=np.float32) / 16.0
    output = GaussianBlur(image, kernel)
    print(output)
