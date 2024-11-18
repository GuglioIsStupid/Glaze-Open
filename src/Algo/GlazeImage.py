# GlazeImage.py

import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import sys
import random
import math
import asyncio

class GlazeImage():
    def __init__(self, img_path, output_path="output", output_name="output", glaze_intensity=0.5, glaze_quality=1):
        self.img_path = img_path
        self.output_path = output_path
        self.output_name = output_name
        self.glaze_intensity = glaze_intensity
        self.glaze_quality = glaze_quality

        self.img = cv2.imread(self.img_path)
        self.img = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)
        
        self.img_height, self.img_width, _ = self.img.shape

        self.estimation_time = self.estimate_time()
        print(f"Estimated time to glaze image: {self.estimation_time} seconds")

        asyncio.run(self.glaze())

    async def glaze(self):
        self.glazed_img = np.zeros((self.img_height, self.img_width, 3), np.uint8)

        for y in range(self.img_height):
            for x in range(self.img_width):
                pixel = self.img[y, x]

                new_pixel = self.apply_glaze(pixel)

                self.glazed_img[y, x] = new_pixel

        self.save_image()

    def apply_glaze(self, pixel):
        r, g, b = pixel
        r = int(r)
        g = int(g)
        b = int(b)

        seed = (r + g + b) / 3 * (self.glaze_intensity * 0.15)
        random.seed(seed)
        
        r += random.randint(0, int(75 * (self.glaze_intensity * 0.4)))
        g += random.randint(0, int(75 * (self.glaze_intensity * 0.4)))
        b += random.randint(0, int(75 * (self.glaze_intensity * 0.4)))


        r = max(0, min(255, r))
        g = max(0, min(255, g))
        b = max(0, min(255, b))

        return (r, g, b)

    
    def save_image(self):
        if not os.path.exists(self.output_path):
            os.makedirs(self.output_path)

        output_file = os.path.join(self.output_path, f"{self.output_name}.jpg")
        cv2.imwrite(output_file, cv2.cvtColor(self.glazed_img, cv2.COLOR_RGB2BGR))

        print(f"Glazed image saved to {output_file}")

    def estimate_time(self):
        # TODO: Actually calculate the time based on the glaze intensity and quality
        time_per_pixel = 0.00001 # Rough Estimataion
        total_time = self.img_height * self.img_width * time_per_pixel

        return total_time

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python GlazeImage.py <image_path>")
        sys.exit(1)

    img_path = sys.argv[1]
    glaze_intensity = 0.5 # higher = more noticeable glaze effect
    glaze_quality = 1

    glaze = GlazeImage(img_path, glaze_intensity=glaze_intensity, glaze_quality=glaze_quality)