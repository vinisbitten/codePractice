class InfoArquivo:
    def __init__(self, nome, tamanho):
        self.nome = f'{nome}'
        self.tamanho = tamanho
        self._formatos_suportados = ['txt', 'pdf', 'jpg', 'mp4','zip']

    def __str__(self):
        return f'Arquivo: {self.nome} ({self.tamanho} MB)'

    def excede_tamanho(self):
        if(self.tamanho > 1000):
            return True
        else:
            return False

    def imprime_arquivos_suportados(self):
        str = "---------------------\n"
        str += "Formatos suportados:\n"
        for formato in self._formatos_suportados:
            str += formato + "\n"
        str += "---------------------"

        print(str)