import random

initialize = [
  "Atenção,",
  "Identifiquei",
  "Notei",
  "Percebi",
  "Observei",
  "Vi",
  "Encontrei",
  "Localizei",
  "Descobri",
  "Reparei",
  "Estou vendo",
]

quite = [
  "um%s %object posicionado %cord",
  "um%s %object localizado %cord",
  "%cord, identifiquei um%s %object",
  "%cord, notei um%s %object",
  "%cord, percebi um%s %object",
  "%cord tem um%s %object",
]

finalize = [
  "prossiga com prudência",
  "avance com segurança",
  "continue com atenção",
  "proceda com cautela",
  "mantenha-se vigilante",
  "siga com cuidado",
  "tenha precaução ao avançar",
  "esteja consciente ao se mover",
  "mantenha a segurança ao prosseguir",
  "seja cauteloso ao continuar",
]

def capitalize_words(s):
  return ' '.join(word.capitalize() for word in s.split())

def humanize(objects):
  random_initialize = random.random()
  random_quite = random.random()
  random_finalize = random.random()

  phrase = ""
  if random_initialize > 0.5:
    phrase += random.choice(initialize)

  count_index = len(objects) - 1

  for index, (obj, cord, gender) in enumerate(objects):
    random_text = random_quite if index < count_index else random_finalize

    if index == 0 and random_text > 0.5:
      phrase += " "
    elif index > 0:
      phrase += ", " if index < count_index else " e "

    object_text = random.choice(quite)
    object_text = object_text.replace("%object", obj)
    object_text = object_text.replace("%cord", cord)
    object_text = object_text.replace("%s", gender)

    phrase += object_text

  if random_finalize > 0.5:
    phrase += ", "
    phrase += random.choice(finalize)

  phrase += "."

  return capitalize_words(phrase)
