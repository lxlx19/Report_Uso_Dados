from solution import Solution

url = "./usuarios.txt"

data_byte = Solution(url)

data_byte.abrir_arquivo()

data_byte.unidata()

data_byte.relatorio()
