def calcDirection(imgWidth, x, width):
    center = x + width / 2
    image_center = imgWidth / 2

    margem_de_erro = 5

    if center < image_center - margem_de_erro:
        return "esquerda"
    elif center > image_center + margem_de_erro:
        return "direita"
    
    return "frente"