from os import listdir
from json import load as to_json
import re, os

class Files:
    def __init__(self, path=None, file_extension=None):
        self.path = './json/translate/' if path is None else path
        self.file_extension = 'json' if file_extension is None else file_extension
        self.strings = {}
    
    def load_json(self, folder, path=None):
        #Puxar o local custom ou base que as pasta das traduções estão.
        path = f"{self.path}{folder}/" if path is None else path
        #Array
        strings = {}
        #Pegar todo os json do diretorio e passar no for.
        for file_name in os.listdir(path):
           #Abrir o arquivo.
           with open(f"{path}{file_name}", encoding='utf-8') as file:
               #Jogar os valores no array.
               file_extension = self.file_extension
               count = - len(file_extension) - 1
               if self.file_extension == 'json':
                  strings[file_name[:count]] = to_json(file)
        
        self.strings[folder] = strings

    def load_folder(self, path=None, pattern=None):
    	#Puxar o local custom ou base que as pasta das traduções estão.
        path = self.path if path is None else path
        #Código do regex das pastas, se for custom ou base.
        pattern = '^[a-z]{2}((_|-)[A-Z]{2})?$' if pattern is None else pattern
        #Passar o resultado pelo re, e compilar o valor.
        pattern = re.compile(pattern)
        #Pegar a lista de pasta da rota e verificar se elas são validas passando pelo regex.
        for folder in [folder for folder in os.listdir(path) if pattern.match(folder)]:
        	self.load_json(folder=folder, path=f"{self.path}{folder}/")





