def calcPositionX(imgWidth, x, width):
    center_x = x + width / 2
    image_center_x = imgWidth / 2

    diff_percent_x = (center_x - image_center_x) / image_center_x * 100

    if diff_percent_x < -15:
        return 2  # esquerda
    elif diff_percent_x > 15:
        return 0  # direita
    else:
        return 1  # centro

def calcPositionY(imgHeight, y, height):
    center_y = y + height / 2
    image_center_y = imgHeight / 2

    diff_percent_y = (center_y - image_center_y) / image_center_y * 100

    if diff_percent_y < -10:
        return 0  # em cima
    elif diff_percent_y > 10:
        return 2  # em baixo
    else:
        return 1  # centro

def calcDirection(imgWidth, imgHeight, x, y, width, height):
    xStrings = { 0: "direita", 1: "centro", 2: "esquerda" }
    yStrings = { 0: "em cima", 1: "centro", 2: "em baixo" }
    
    x = calcPositionX(imgWidth, x, width)
    y = calcPositionY(imgHeight, y, height)
    
    if (x == 1 and y == 1):
        return "á sua frente"

    if (x == 0 and y == 1):
        return "á sua esquerda"
    
    if (x == 2 and y == 1):
        return "á sua direita"
    
    if (x == 1):
        return f"{yStrings[y]} no {xStrings[x]}"
    
    return f"{yStrings[y]} á {xStrings[x]}"