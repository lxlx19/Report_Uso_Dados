from collections import defaultdict
from itertools import chain


class Solution:
    def __init__(self, url):
        self.url = url
        self.data = {}
        self.mb = {}
        self.perc = {}
        self.report = defaultdict(list)
        self.total = 0
        self.media = 0

    def abrir_arquivo(self):
        with open(self.url, "r") as data_in:
            for linha in data_in:
                valores = linha.split()
                self.data[valores[0]] = int(valores[1])
        for nome in self.data:
            self.mb[nome] = round(self.data[nome] / (1024 ** 2), 2)

        i = 0
        for nome in self.mb:
            self.total += self.mb[nome]
            i += 1
        self.media = round(self.total / i, 2)
        for nome in self.mb:
            self.perc[nome] = round((self.mb[nome] / self.total) * 100, 2)

    def unidata(self):
        for k, v in chain(self.mb.items(), self.perc.items()):
            self.report[k].append(v)

    def relatorio(self):
        with open("report.txt", "w", encoding="utf-8") as file:
            cabecalho = "ACME INC.     Uso do espaço em disco pelos usuários"
            separador = "_______________________________________________________\n"
            file.write(cabecalho + "\n")
            file.write(separador + "\n")
            for nome in self.report:
                usodisco = f"Usuário: {nome} | Uso de disco: {self.report[nome][0]} MB"
                usoperc = f" | % de uso: {self.report[nome][1]}%"
                report = usodisco + usoperc
                file.write(report + "\n")
            espaco_total = f"\nEspaço total ocupado: {self.total} MB"
            espaco_medio = f"Espaço medio ocupado: {self.media} MB"
            file.write(espaco_total + "\n")
            file.write(espaco_medio + "\n")
            file.close()
