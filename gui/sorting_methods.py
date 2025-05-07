import random
from typing import List, Any


def bubble_sort(arr: List[Any]) -> List[Any]:
    # bubble sort otimizado: interrompe se não houver trocas em uma iteração
    # bubble sort funciona comparando pares adjacentes e trocando-os se estiverem na ordem errada
    n = len(arr)
    for i in range(n):
        swapped = False
        # após cada iteração, os últimos i elementos já estão ordenados
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


def selection_sort(arr: List[Any]) -> List[Any]:
    # selection sort estável: seleciona o mínimo da parte não ordenada
    # seleciona o menor elemento e troca com o primeiro não ordenado
    # é estável pois não troca elementos iguais

    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # troca o elemento mínimo com o elemento da posição i
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def insertion_sort(arr: List[Any]) -> List[Any]:
    # insertion sort estável: insere elementos na posição correta
    # percorre o array e insere cada elemento na posição correta
    # é estável pois não troca elementos iguais

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # move elementos maiores que key uma posição à direita
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def shell_sort(arr: List[Any]) -> List[Any]:#
    # shell sort: generalização do insertion sort usando gaps decrescentes
    # divide o array em subarrays e aplica insertion sort em cada um

    n = len(arr)
    gap = n // 2
    # reduz gaps até chegar a 1
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            # ordena elementos distantes pelo gap atual
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr


def merge_sort(arr: List[Any]) -> List[Any]:
    # merge sort estável: divide e conquista, usa espaço extra
    # divide o array em duas metades, ordena cada uma e mescla
    # é estável pois não troca elementos iguais
    # usa recursão para dividir o array em metades até chegar a 1 elemento

    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    merged = []
    i = j = 0
    # mescla duas metades ordenadas
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i]); i += 1
        else:
            merged.append(right[j]); j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


def quick_sort(arr: List[Any]) -> List[Any]:
    # quick sort in-place: usa pivô aleatório para reduzir pior caso
    # funciona dividindo o array em duas partes: menores e maiores que o pivô
    # é instável pois pode trocar elementos iguais

    def _qs(a: List[Any], low: int, high: int) -> None: # função auxiliar recursiva
        if low < high:
            p = partition(a, low, high)
            _qs(a, low, p - 1)
            _qs(a, p + 1, high)

    def partition(a: List[Any], low: int, high: int) -> int:
        # escolhe pivô aleatório e posiciona em a[high]
        rand_idx = random.randint(low, high)
        a[rand_idx], a[high] = a[high], a[rand_idx]
        pivot = a[high]
        i = low
        for j in range(low, high):
            if a[j] <= pivot:
                a[i], a[j] = a[j], a[i]
                i += 1
        a[i], a[high] = a[high], a[i]
        return i

    _qs(arr, 0, len(arr) - 1)
    return arr


def heap_sort(arr: List[Any]) -> List[Any]:
    # heap sort in-place: constrói max-heap e extrai o máximo iterativamente
    # funciona construindo um heap binário e ordenando os elementos
    # i e ((i - 2) / 2) são os índices do filho esquerdo e direito de i
    # é instável pois pode trocar elementos iguais

    def heapify(a: List[Any], size: int, root: int) -> None:
        largest = root
        left = 2 * root + 1
        right = 2 * root + 2
        # verifica se filho esquerdo é maior que o nó raiz
        if left < size and a[left] > a[largest]:
            largest = left
        # verifica se filho direito é maior que o nó maior atual
        if right < size and a[right] > a[largest]:
            largest = right
        if largest != root:
            a[root], a[largest] = a[largest], a[root]
            heapify(a, size, largest)

    n = len(arr)
    # constrói max-heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    # extrai elementos do heap
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
    return arr


def radix_sort(arr: List[int]) -> List[int]:
    # radix sort lsd para inteiros não-negativos, estável
    # funciona ordenando os números por cada dígito, do menos significativo para o mais significativo

    if not arr:
        return arr
    assert all(isinstance(x, int) and x >= 0 for x in arr), \
        "radix sort só suporta inteiros não-negativos"
    max_val = max(arr)
    exp = 1
    n = len(arr)
    output = [0] * n

    while max_val // exp > 0:
        count = [0] * 10
        # conta ocorrências de cada dígito
        for num in arr:
            idx = (num // exp) % 10
            count[idx] += 1
        # converte em prefix sum
        for i in range(1, 10):
            count[i] += count[i - 1]
        # constrói array de saída estável
        for num in reversed(arr):
            idx = (num // exp) % 10
            output[count[idx] - 1] = num
            count[idx] -= 1
        # copia resultado de volta para arr
        arr[:] = output[:]
        exp *= 10
    return arr
