import random

def gerar_sequencias(n):
    seq_ordenada = list(range(1, n + 1))
    seq_invertida = seq_ordenada[::-1]
    seq_randomica = seq_ordenada.copy()
    random.shuffle(seq_randomica) # apenas copia a ordenada e da o shuffle
    return seq_ordenada, seq_invertida, seq_randomica

def salvar_em_arquivo(numeros, nome_arquivo):
    with open(nome_arquivo, "w", encoding="utf-8") as f:
        for num in numeros:
            f.write(f"{num}\n")

def escolher_tamanho():
    opcoes = [750000, 850000, 950000, 1250000, 1350000]
    print("Escolha o tamanho do arquivo:")
    for i, tamanho in enumerate(opcoes, start=1):
        print(f"{i}. {tamanho}")
    escolha = int(input("Opção (1-5): ").strip())
    if 1 <= escolha <= len(opcoes):
        return opcoes[escolha - 1]
    else:
        raise ValueError("Opção inválida.")

def main():
    try:
        n = escolher_tamanho()
    except Exception as e:
        print("Erro na seleção de tamanho:", e)
        return

    seq_ord, seq_inv, seq_rand = gerar_sequencias(n)

    salvar_em_arquivo(seq_ord,  f"numeros_ordenados_{n}.txt")
    salvar_em_arquivo(seq_inv,  f"numeros_invertidos_{n}.txt")
    salvar_em_arquivo(seq_rand, f"numeros_randomicos_{n}.txt")

    print(f"Arquivos gerados para n = {n}:")
    print(f"numeros_ordenados_{n}.txt")
    print(f"numeros_invertidos_{n}.txt")
    print(f"numeros_randomicos_{n}.txt")

main()
