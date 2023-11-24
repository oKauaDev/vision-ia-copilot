def calcDirection(imgWidth, x, width):
    center = x + width / 2
    image_center = imgWidth / 2

    if center < image_center:
        return "esquerda"
    elif center > image_center:
        return "direita"
    
    return "frente"