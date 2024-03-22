#Import
import keyboard
import re
# Definicja błędu
def error(error_type):
  if error_type == "brainRepeatValue":
    error_id = "b394"

  elif error_type == "brainError":
    error_id = "b395"
  elif error_type == "totalBrainError":
    error_id = "b396"
  elif error_type == "totalError":
    error_id = "b397"
  elif error_type == "TPFE":
    error_id = "b398"
  elif error_type == "functionError":
    error_id = "b399"
  elif error_type == "inputError":
    error_id = "b400"
  else:
    error("functionError")

  print(f"Error id {error_id} of type: {error_type}")






#Utworzenie POTRZEBNYCH list i zmiennych
brainContent = []
contentId = []
content = ""
id = ""
# Kod
def start():
  print("COPYRIGHT 2024 WSZELKIE PRAWA ZASTRZEŻONE!")
  print("TWÓRCĄ I WYŁĄCZNYM AUTOREM TEGO PROGRAMU JEST FRANCISZEK CHMIELEWSKI")
  print("Naucz ten program, aby następnie pytać go o dowolne rzeczy i \n uzyskiwać odpowiedź!")
  print("Aby nauczyć czegoś tego programu,")
  print("należy wpisać za każdym razem")
  print("kiedy chcemy, żeby się czegoś nauczył, \n $identyfikator== 'treść'")

def uczenie():
  zapytanieUczenia = input()
  if zapytanieUczenia.startswith("$"):
    try:
      identyfikator, content = zapytanieUczenia.split("==", 1)
      identyfikator = identyfikator.strip()
      content = content.strip()
      content = content[1:-1]
      zapisywanieDanych()
    except:
      error("inputError")
  else:
    error("inputError")

def zapisywanieDanych():
  if id in contentId:
    error("brainRepeatValue")
  else:
    contentId.append(id)
  if content in brainContent:
    pass
  else:
    brainContent.append(content)
# Najważniejsza funkcja:    


def answer(template, idBase, contentBase, answerType, question):
  userQuestion = question.lower()
  userQuestion = re.sub(r'[^a-zA-Z0-9\s]', '', y)
  mat = random.randomint(1,3)
  if mat == 1:
    answerType = "Wrong"
  elif mat == 2:
    answerType = "Friendly"
  elif mat == 3:
    answerType = "Xd"
  else:
    error("TPFE")
  if answerType == "Wrong":
    answer = answer + "But you won't understand it anyway, \n you're too stupid."
  elif answerType == "Friendly":
    answer = answer + "And as if you don't know something, although \n I  doubt it, because in my opinion you are very smart, write :)"
  elif answerType == "Xd":
    answer = answer + "Xdd."

  answer = ""
  wzorzec1 = r'\{\*\}'
  wzorzec2 = r'\[\*\]'
  if question in idBase:
    answer = contentBase[idBase.index(question)]
  else:
    error("inputError")
  # Wykonujemy zamianę
  completed_template = re.sub(wzorzec1, userQuestion, template)
  completed_template = re.sub(wzorzec2, answer, completed_template)



def odpowiadanie(question):
  content-answer = "The answer to {*} is [*]."
  random-answer-type = ""


      answer(content-answer, id, content, random-answer-type, question)
  #Poniższy kod to tylko kod do testów!!
  start()
  while True:
    uczenie()
    if keyboard.is_pressed("Enter"):
      odpowiadanie($, input())

