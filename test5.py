# 5) Escreva um programa que inverta os caracteres de um string.

# IMPORTANTE:
# a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
# b) Evite usar funções prontas, como, por exemplo, reverse;

string = input("Digite a string a ser invertida: ")

res = ""
for i in range(len(string) - 1, -1, -1):
    res += string[i]

stringInv = res

print("String invertida:", stringInv)