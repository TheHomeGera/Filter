from PIL import Image
import numpy as np


def pixel_art_filter(mosaic_side: int, step: int):
    img_length, img_height = len(img_arr), len(img_arr[1])
    segment_x, segment_y = np.arange(0, img_length, mosaic_side), np.arange(0, img_height, mosaic_side)
    [[pixel_coloring(x, y, mosaic_side, step) for y in segment_y] for x in segment_x]


def find_average_brightness(x, y, mosaic_side):
    result = 0
    for n, m in np.nditer([np.arange(x, x + mosaic_side)[:, None], np.arange(y, y + mosaic_side)]):
        result += img_arr[n][m][0] / 3 + img_arr[n][m][1] / 3 + img_arr[n][m][2] / 3
    return int(result) // (mosaic_side * mosaic_side)


def pixel_coloring(x, y, mosaic_side, step):
    avg_brightness = find_average_brightness(x, y, mosaic_side)
    for n in range(x, x + mosaic_side):
        for m in range(y, y + mosaic_side):
            img_arr[n][m][range(3)] = int(avg_brightness // step) * step


def start_program():
    global img_arr
    print("Введите имя исходного изображения:")
    original_img_name = input()
    print("Введите имя конечного изображения:")
    filtered_img_name = input()
    print("Задайте значения размера мозайки и шага:")
    mosaic_side, step = map(int, input().split())
    img_arr = np.array(Image.open(original_img_name))
    pixel_art_filter(mosaic_side, step)
    changed_img = Image.fromarray(img_arr)
    changed_img.save(filtered_img_name)
    print("Обработка успешно завершена")


np.seterr(over='ignore')
start_program()