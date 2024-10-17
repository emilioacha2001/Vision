import cv2
import numpy as np
# profe me basare en la siguiente imagen https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.pinterest.com%2Fpin%2Fminecraft-pixel-art-templates-pokeball--532621093403996478%2F&psig=AOvVaw1H--J7EgCTNoH2wvvD6ANd&ust=1725499991763000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqFwoTCIjozsKSqIgDFQAAAAAdAAAAABAR
# Emilio Chaparro 189304

colors = {
    "white": [255, 255, 255],
    "red": [0, 0, 255],
    "black": [0, 0, 0],
    "grey": [169, 169, 169]
}

# crear matriz 14x14
poke_array = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 2, 2, 2, 2, 0, 0, 0, 0, 0],
    [0, 0, 0, 2, 2, 1, 1, 1, 1, 2, 2, 0, 0, 0],
    [0, 0, 2, 1, 1, 0, 1, 1, 1, 1, 1, 2, 0, 0],
    [0, 0, 2, 1, 0, 0, 0, 1, 1, 1, 1, 2, 0, 0],
    [0, 2, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 2, 0],
    [0, 2, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2, 0],
    [0, 2, 2, 1, 1, 2, 0, 3, 2, 1, 1, 2, 2, 0],
    [0, 2, 0, 2, 2, 2, 3, 3, 2, 2, 2, 3, 2, 0],
    [0, 0, 2, 0, 0, 0, 2, 2, 3, 3, 3, 2, 0, 0],
    [0, 0, 2, 3, 0, 0, 0, 3, 3, 3, 3, 2, 0, 0],
    [0, 0, 0, 2, 2, 3, 3, 3, 3, 2, 2, 0, 0, 0],
    [0, 0, 0, 0, 0, 2, 2, 2, 2, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

height, width = len(poke_array), len(poke_array[0])
img = np.zeros((height, width, 3), dtype=np.uint8)

for i in range(height):
    for j in range(width):
        if poke_array[i][j] == 0:
            img[i, j] = colors["white"]
        elif poke_array[i][j] == 1:
            img[i, j] = colors["red"]
        elif poke_array[i][j] == 2:
            img[i, j] = colors["black"]
        else:
            img[i, j] = colors["grey"]

scaled_img = cv2.resize(img, (300, 300), interpolation=cv2.INTER_NEAREST)

output_path = "pokeball_opencv.png"
cv2.imwrite(output_path, scaled_img)

output_path