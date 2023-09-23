alunos = []
nota1 = []
nota2 = []
sequencia = 1

num_alunos = input("Digite a quantidade de alunos:")
num_alunos = int(num_alunos)

for rodada in range(1, num_alunos + 1):
    alunos = input("Digite o {}° aluno:".format(sequencia))
    nota1  = input("Digite a primeira nota:")
    nota2  = input("Digite a segunda nota:")
    print("tudo certo {} {} {}".format(alunos, nota1, nota2))
    sequencia = sequencia+1

print(alunos)