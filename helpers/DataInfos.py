objetos = {
    'person': {'name': 'pessoa', 'gender': 'a'},
    'bicycle': {'name': 'bicicleta', 'gender': 'a'},
    'car': {'name': 'carro', 'gender': ''},
    'motorcycle': {'name': 'motocicleta', 'gender': 'a'},
    'airplane': {'name': 'avião', 'gender': ''},
    'bus': {'name': 'ônibus', 'gender': ''},
    'train': {'name': 'trem', 'gender': ''},
    'truck': {'name': 'caminhão', 'gender': ''},
    'boat': {'name': 'barco', 'gender': ''},
    'traffic light': {'name': 'semáforo', 'gender': ''},
    'fire hydrant': {'name': 'hidrante', 'gender': ''},
    'unknown1': {'name': 'desconhecido', 'gender': ''},  # ??? 
    'stop sign': {'name': 'placa de pare', 'gender': 'a'},
    'parking meter': {'name': 'parquímetro', 'gender': ''},
    'bench': {'name': 'banco', 'gender': ''},
    'bird': {'name': 'pássaro', 'gender': ''},
    'cat': {'name': 'gato', 'gender': ''},
    'dog': {'name': 'cachorro', 'gender': ''},
    'horse': {'name': 'cavalo', 'gender': ''},
    'sheep': {'name': 'ovelha', 'gender': 'a'},
    'cow': {'name': 'vaca', 'gender': 'a'},
    'elephant': {'name': 'elefante', 'gender': ''},
    'bear': {'name': 'urso', 'gender': ''},
    'zebra': {'name': 'zebra', 'gender': 'a'},
    'giraffe': {'name': 'girafa', 'gender': 'a'},
    'unknown2': {'name': 'desconhecido', 'gender': ''},  # ??? 
    'backpack': {'name': 'mochila', 'gender': 'a'},
    'umbrella': {'name': 'guarda-chuva', 'gender': ''},
    'unknown3': {'name': 'desconhecido', 'gender': ''},  # ??? 
    'unknown4': {'name': 'desconhecido', 'gender': ''},  # ??? 
    'handbag': {'name': 'bolsa', 'gender': 'a'},
    'tie': {'name': 'gravata', 'gender': 'a'},
    'suitcase': {'name': 'mala', 'gender': 'a'},
    'frisbee': {'name': 'frisbee', 'gender': ''},
    'skis': {'name': 'esquis', 'gender': ''},
    'snowboard': {'name': 'prancha de snowboard', 'gender': 'a'},
    'sports ball': {'name': 'bola esportiva', 'gender': 'a'},
    'kite': {'name': 'pipa', 'gender': 'a'},
    'baseball bat': {'name': 'bastão de beisebol', 'gender': ''},
    'baseball glove': {'name': 'luva de beisebol', 'gender': 'a'},
    'skateboard': {'name': 'skate', 'gender': ''},
    'surfboard': {'name': 'prancha de surfe', 'gender': 'a'},
    'tennis racket': {'name': 'raquete de tênis', 'gender': 'a'},
    'bottle': {'name': 'garrafa', 'gender': 'a'},
    'unknown5': {'name': 'desconhecido', 'gender': ''},  # ??? 
    'wine glass': {'name': 'copo de vinho', 'gender': ''},
    'cup': {'name': 'xícara', 'gender': 'a'},
    'fork': {'name': 'garfo', 'gender': ''},
    'knife': {'name': 'faca', 'gender': 'a'},
    'spoon': {'name': 'colher', 'gender': 'a'},
    'bowl': {'name': 'tigela', 'gender': 'a'},
    'banana': {'name': 'banana', 'gender': 'a'},
    'apple': {'name': 'maçã', 'gender': 'a'},
    'sandwich': {'name': 'sanduíche', 'gender': ''},
    'orange': {'name': 'laranja', 'gender': 'a'},
    'broccoli': {'name': 'brócolis', 'gender': ''},
    'carrot': {'name': 'cenoura', 'gender': 'a'},
    'hot dog': {'name': 'cachorro-quente', 'gender': ''},
    'pizza': {'name': 'pizza', 'gender': 'a'},
    'donut': {'name': 'rosquinha', 'gender': 'a'},
    'cake': {'name': 'bolo', 'gender': ''},
    'chair': {'name': 'cadeira', 'gender': 'a'},
    'couch': {'name': 'sofá', 'gender': ''},
    'potted plant': {'name': 'planta em vaso', 'gender': 'a'},
    'bed': {'name': 'cama', 'gender': 'a'},
    'unknown6': {'name': 'desconhecido', 'gender': ''},  # ??? 
    'dining table': {'name': 'mesa de jantar', 'gender': 'a'},
    'unknown7': {'name': 'desconhecido', 'gender': ''},  # ??? 
    'unknown8': {'name': 'desconhecido', 'gender': ''},  # ??? 
    'toilet': {'name': 'vaso sanitário', 'gender': ''},
    'unknown9': {'name': 'desconhecido', 'gender': ''},  # ??? 
    'tv': {'name': 'televisão', 'gender': 'a'},
    'laptop': {'name': 'laptop', 'gender': ''},
    'mouse': {'name': 'mouse', 'gender': ''},
    'remote': {'name': 'controle remoto', 'gender': ''},
    'keyboard': {'name': 'teclado', 'gender': ''},
    'cell phone': {'name': 'celular', 'gender': ''},
    '???': {'name': 'desconhecido', 'gender': ''},  # ??? 
    'book': {'name': 'livro', 'gender': ''},
    'clock': {'name': 'relógio', 'gender': ''},
    'vase': {'name': 'vaso', 'gender': ''},
    'scissors': {'name': 'tesoura', 'gender': 'a'},
    'teddy bear': {'name': 'ursinho de pelúcia', 'gender': ''},
    'hair drier': {'name': 'secador de cabelo', 'gender': ''},
    'toothbrush': {'name': 'escova de dentes', 'gender': 'a'},
}


def get_object_infos(nome_objeto):
  if nome_objeto in objetos:
    return objetos[nome_objeto]
  else:
    return {'name': nome_objeto, 'gender': ''}