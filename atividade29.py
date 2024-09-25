# Crie um programa que receba uma lista com os nomes dos alunos presentes em uma aula e exiba quantos alunos estão presentes e a lista dos nomes. Se o total de alunos presentes for menor que 5, exiba uma mensagem sugerindo uma revisão da lista de chamada.

# Exemplo de entrada:
# Alunos presentes: ['Ana', 'Bruno', 'Carlos', 'Daniela']

# Exemplo de saída:
# Alunos presentes: 4
# Lista de alunos presentes: Ana, Bruno, Carlos, Daniela
# Aviso: Poucos alunos presentes. Revisar lista de chamada.

def verificar_presenca():
    
    alunos_presentes = input("Digite os nomes dos alunos presentes, separados por vírgula: ")
    
    lista_alunos = [aluno.strip() for aluno in alunos_presentes.split(",")]

    total_presentes = len(lista_alunos)

    print(f"\nAlunos presentes: {total_presentes}")
    print("Lista de alunos presentes:", ", ".join(lista_alunos))

    if total_presentes < 5:
        print("Aviso: Poucos alunos presentes. Revisar lista de chamada.")

verificar_presenca()
