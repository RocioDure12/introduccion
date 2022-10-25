file_path="C:/Users/Rocio/Desktop/Python/introduccion/files_txt/pi_digits.txt"
with open(file_path,"r") as file_object:
    contenido=file_object.read()
    print(contenido.rstrip())