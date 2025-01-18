import pandas as pd
import pyautogui
import time

pyautogui.PAUSE = 1.5

# abrir o navegador
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(2)
pyautogui.click(x=332, y=679)
time.sleep(2)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(2)

# logar no sistema
pyautogui.press("tab")
pyautogui.write("email@gmail.com")
pyautogui.press("tab")
pyautogui.write("123")
pyautogui.press("enter")

# importar a base de dados dos produtos
tabela = pd.read_csv("produtos.csv")
print(tabela)
time.sleep(1.5)

# cadastrar os produtos
for linha in tabela.index:
  pyautogui.click(x=757, y=258)
  codigo = tabela.loc[linha, "codigo"]
  pyautogui.write(str(codigo))
  pyautogui.press("tab")

  pyautogui.write(str(tabela.loc[linha, "marca"]))
  pyautogui.press("tab")
  pyautogui.write(str(tabela.loc[linha, "tipo"]))
  pyautogui.press("tab")
  pyautogui.write(str(tabela.loc[linha, "categoria"]))
  pyautogui.press("tab")
  pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
  pyautogui.press("tab")
  pyautogui.write(str(tabela.loc[linha, "custo"]))
  pyautogui.press("tab")
  obs = tabela.loc[linha, "obs"]
  if not pd.isna(obs):
     pyautogui.write(str(tabela.loc[linha, "obs"]))
  pyautogui.press("enter")

  #subir com scroll
  pyautogui.scroll(5000)
  time.sleep(.5)