import os
import sys

import pygame
import requests

SCALE = 14
COORDS = '56.229421,58.022833'
map_request = f"http://static-maps.yandex.ru/1.x/?ll={COORDS}&z={SCALE}&l=map"
response = requests.get(map_request)

if not response:
    print("Ошибка выполнения запроса:")
    print(map_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)

map_file = "map.png"
with open(map_file, "wb") as file:
    file.write(response.content)

pygame.init()
screen = pygame.display.set_mode((600, 450))
pygame.display.set_caption('Maps App!')
screen.blit(pygame.image.load(map_file), (0, 0))
pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()

os.remove(map_file)
