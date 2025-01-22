import json
from sprites.tank import Tank
from enums import Directions

def save_game(map, seconds, tank1: Tank, tank2: Tank):
    data = {
        'map': map,
        'seconds': seconds,
        'tank1': {
            'x': tank1.rect.x,
            'y': tank1.rect.y,
            'width': tank1.rect.width if tank1.direction == Directions.TOP or tank1.direction == Directions.BOTTOM else tank1.rect.height,
            'height': tank1.rect.height if tank1.direction == Directions.TOP or tank1.direction == Directions.BOTTOM else tank1.rect.width,
            'v': tank1.v,
            'bullet_v': tank1.bullet_v,
            'score': tank1.score.value
        },
        'tank2': {
            'x': tank2.rect.x,
            'y': tank2.rect.y,
            'width': tank2.rect.width if tank2.direction == Directions.TOP or tank2.direction == Directions.BOTTOM else tank2.rect.height,
            'height': tank2.rect.height if tank2.direction == Directions.TOP or tank2.direction == Directions.BOTTOM else tank2.rect.width,
            'v': tank2.v,
            'bullet_v': tank2.bullet_v,
            'score': tank2.score.value
        }
    }

    with open('save.json', 'w') as file:
        text = json.dumps(data)
        file.write(text)