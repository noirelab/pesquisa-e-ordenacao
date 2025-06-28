import random
import flet as ft
import os
import time

from sorting_methods import *

SORT_FUNCTIONS = {
    "Bubble Sort": bubble_sort,
    "Selection Sort": selection_sort,
    "Insertion Sort": insertion_sort,
    "Shell Sort": shell_sort,
    "Merge Sort": merge_sort,
    "Quick Sort": quick_sort,
    "Heap Sort": heap_sort,
    "Radix Sort": radix_sort
}

# 1. pasta onde este arquivo está
HERE = os.path.dirname(__file__)
# 2. sobe um nível para a raiz do projeto
BASE_DIR = os.path.abspath(os.path.join(HERE, os.pardir))
# 3. monta o path até a pasta modelos
FILES_FOLDER = os.path.join(BASE_DIR, 'files')


def main(page: ft.Page):
    page.title = "Pesquisa e Ordenação - Algoritmos de Ordenação"

    # scanear os arquivos
    try:
        filenames = sorted(f for f in os.listdir(FILES_FOLDER) if f.endswith(".txt"))
    except FileNotFoundError:
        filenames = []
    if not filenames:
        filenames = ["<no .txt found>"]

    # file-picker
    file_dropdown = ft.Dropdown(
        label="Selecionar arquivo",
        width=300,
        options=[ft.dropdown.Option(name) for name in filenames],
        value=filenames[0]
    )

    # dropdown para os métodos de ordenação
    algo_dropdown = ft.Dropdown(
        label="Método de Ordenação",
        width=300,
        options=[ft.dropdown.Option(name) for name in SORT_FUNCTIONS],
        value=list(SORT_FUNCTIONS)[0]
    )

    run_button = ft.ElevatedButton(text="Ordenar", width=100)

    output = ft.TextField(
        label="Resultado",
        multiline=True,
        width=1200,
        height=700,
        read_only=True
    )

    # funcao para o botão de ordenação
    def on_run(e):
        sel = file_dropdown.value
        # checa se o arquivo existe
        if sel.startswith("<no"):
            output.value = "Nenhum .txt na pasta!"
            page.update()
            return

        path = os.path.join(FILES_FOLDER, sel)
        # read
        try:
            with open(path, "r", encoding="utf-8") as f:
                nums = [int(line.strip()) for line in f if line.strip()]
        except Exception as ex:
            output.value = f"ERRO AO LER {sel}: {ex}"
            page.update()
            return

        # sort
        sort_fn = SORT_FUNCTIONS[algo_dropdown.value]

        start = time.perf_counter()
        sorted_nums = sort_fn(nums.copy())
        end = time.perf_counter()
        elapsed = end - start

        # mostra tudo
        head = sorted_nums
        output.value =  f"Tamanho: {len(nums)}\n" \
                        f"Tempo: {elapsed:.4f} segundos\n" \
                        f"Resultado: {head}"

        # salva pra elapsed_time.txt
        output_path = os.path.join("elapsed_time.txt")
        with open(output_path, "a", encoding="utf-8") as f:
            f.write(f"{sel} - {algo_dropdown.value} - {elapsed:.4f} segundos\n")

        page.update()

    run_button.on_click = on_run

    # Layout
    page.add(
        ft.Column([
            file_dropdown,
            algo_dropdown,
            run_button,
            ft.Divider(),
            output
        ], spacing=20)
    )

if __name__ == "__main__":
    ft.app(target=main)
