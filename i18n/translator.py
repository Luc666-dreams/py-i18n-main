
class Translator:
    def __init__(self, files, language, split= None):
        self.files = files
        self.language = language
        self.split = '|' if split is None else split

    def get(self, path, values={}):
        #Passar o valor da tradução por uma slipt
        keys = path.split(self.split)
        #Puxar o json com o valor da language selecionado.
        string = self.files.strings[self.language]
        #Passar o valor do split em um for é obter o valor desejado.
        for key in keys:
            string = string[key]
        #Caso tenha algum valor dict no json converter.
        if values:
            return string.format(**values)
        #Retonar o valor puro.
        return string