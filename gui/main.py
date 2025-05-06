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

    # 1) Scan the folder for .txt files:
    try:
        filenames = sorted(f for f in os.listdir(FILES_FOLDER) if f.endswith(".txt"))
    except FileNotFoundError:
        filenames = []
    if not filenames:
        filenames = ["<no .txt found>"]

    # 2) Create the file-picker dropdown:
    file_dropdown = ft.Dropdown(
        label="Select input file",
        width=300,
        options=[ft.dropdown.Option(name) for name in filenames],
        value=filenames[0]
    )

    # 3) Your existing algorithm dropdown:
    algo_dropdown = ft.Dropdown(
        label="Choose sorting method",
        width=300,
        options=[ft.dropdown.Option(name) for name in SORT_FUNCTIONS],
        value=list(SORT_FUNCTIONS)[0]
    )

    run_button = ft.ElevatedButton(text="Run", width=100)

    output = ft.TextField(
        label="Resultado",
        multiline=True,
        width=1200,
        height=700,
        read_only=True
    )

    # 4) Updated on_run that reads the selected file:
    def on_run(e):
        sel = file_dropdown.value
        # guard against the “no files” case
        if sel.startswith("<no"):
            output.value = "❌ No .txt files in folder!"
            page.update()
            return

        path = os.path.join(FILES_FOLDER, sel)
        # read
        try:
            with open(path, "r", encoding="utf-8") as f:
                nums = [int(line.strip()) for line in f if line.strip()]
        except Exception as ex:
            output.value = f"❌ Error reading {sel}: {ex}"
            page.update()
            return

        # sort
        sort_fn = SORT_FUNCTIONS[algo_dropdown.value]

        start = time.perf_counter()
        sorted_nums = sort_fn(nums.copy())
        end = time.perf_counter()
        elapsed = end - start

        # display everything
        head = sorted_nums
        output.value =  f"Input size: {len(nums)}\n" \
                        f"Time taken: {elapsed:.4f} seconds\n" \
                        f"Output: {head}"

        # saving the elapsed time to a file
        output_path = os.path.join(FILES_FOLDER, "elapsed_time.txt")
        with open(output_path, "a", encoding="utf-8") as f:
            f.write(f"{sel} - {algo_dropdown.value} - {elapsed:.4f} seconds\n")

        page.update()

    run_button.on_click = on_run

    # 5) Layout
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
