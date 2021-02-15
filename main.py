import os
import sys

import pygame
import requests


def get_map():
    map_request = f"http://static-maps.yandex.ru/1.x/?ll={COORDS}&z={SCALE}&l={cur_spn}"
    response = requests.get(map_request)

    if not response:
        print("Ошибка выполнения запроса:")
        print(map_request)
        print("Http статус:", response.status_code, "(", response.reason, ")")
        sys.exit(1)

    map_file = "map.png"
    with open(map_file, "wb") as file:
        file.write(response.content)
    return map_request, response, map_file


SCALE = 13
COORDS = '56.229421,58.022833'
cur_spn = 'map'

pygame.init()
screen = pygame.display.set_mode((600, 450))
pygame.display.set_caption('Maps App!')
map_request, response, map_file = get_map()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            try:
                os.remove(map_file)
            except Exception:
                pass
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_PAGEUP:
                if SCALE + 1 < 18:
                    SCALE += 1
                    map_request, response, map_file = get_map()

            if event.key == pygame.K_PAGEDOWN:
                if 8 < SCALE + 1:
                    SCALE -= 1
                    map_request, response, map_file = get_map()

            if event.key == pygame.K_SPACE:
                if cur_spn == 'map':
                    cur_spn = 'sat'
                elif cur_spn == 'sat':
                    cur_spn = 'sat,skl'
                else:
                    cur_spn = 'map'

                map_request, response, map_file = get_map()

    screen.blit(pygame.image.load(map_file), (0, 0))
    pygame.display.flip()
