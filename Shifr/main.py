import pyAesCrypt

password = input("Enter Password --> : ")
file = input("Enter File --> : ")

def Aes(file, password):
   try:
      try:
         return pyAesCrypt.decryptFile(file, file.replace('.txt.aes', '.txt') , password)
      except:
         return pyAesCrypt.encryptFile(file, f'{file}.aes', password)
   except:
      return None

Aes(file, password)