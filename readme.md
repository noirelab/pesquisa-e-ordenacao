# Algoritmos de Ordenação - Análise Comparativa

Este repositório contém uma análise empírica completa de oito algoritmos de ordenação, incluindo implementações em C++, ferramentas de teste com interface gráfica em Python, e um artigo científico detalhando os resultados.

## Sobre o Projeto

Este trabalho apresenta uma comparação de desempenho entre oito algoritmos clássicos de ordenação:

- Bubble Sort
- Insertion Sort
- Selection Sort
- Shell Sort
- Merge Sort
- Quick Sort
- Heap Sort
- Radix Sort (LSD)

Os algoritmos são avaliados em três cenários diferentes:
- Dados já ordenados
- Dados inversamente ordenados (pior caso)
- Dados aleatórios (caso médio)

Cada algoritmo foi testado com conjuntos de dados de tamanhos variados (até 1,35 milhão de elementos), gerando medições precisas de tempo de execução para determinar sua eficiência prática.

## Estrutura do Repositório

```
pesquisa-e-ordenacao/
├── artigo/               # Artigo LaTeX com análise científica completa
│   ├── Artigo.tex        # Texto fonte do artigo
│   └── images/           # Gráficos de desempenho
├── files/                # Arquivos de entrada e código C++
│   ├── file_generator.py # Gerador de arquivos de teste
│   ├── sorter.cpp        # Implementação C++ dos algoritmos
│   └── *.txt             # Arquivos de entrada gerados
└── gui/                  # Interface gráfica para testes
    ├── main.py           # Aplicação principal
    └── sorting_methods.py# Implementações Python dos algoritmos
```

## Como Utilizar a GUI

A interface gráfica permite testar facilmente os algoritmos com diferentes conjuntos de dados.

### Requisitos

- Python 3.6+
- Biblioteca Flet: `pip install flet`

### Executando a Interface

1. Clone este repositório:
   ```
   git clone https://github.com/noirelab/pesquisa-e-ordenacao.git
   cd pesquisa-e-ordenacao
   ```

2. Execute a aplicação:
   ```
   python gui/main.py
   ```

### Funcionalidades da GUI

1. **Seleção de Arquivo**: Escolha o arquivo de entrada com os dados a serem ordenados
   - Os arquivos seguem o padrão: `numeros_[tipo]_[tamanho].txt`
   - Tipos disponíveis: ordenados, invertidos, randomicos

2. **Seleção de Algoritmo**: Escolha qual dos oito algoritmos deseja testar

3. **Botão Run**: Executa o algoritmo selecionado e exibe os resultados

4. **Área de Resultados**: Mostra:
   - Tamanho da entrada
   - Tempo de execução em segundos
   - Primeiros elementos do array ordenado

Os resultados de cada execução são automaticamente registrados no arquivo elapsed_time.txt para análise posterior.

## Gerando Arquivos de Teste

Para criar novos arquivos de teste:

```
python files/file_generator.py
```

O script solicitará o tamanho desejado e gerará três arquivos com diferentes ordenações dos mesmos números.

## Resultados e Conclusões

A análise completa dos resultados está disponível no artigo científico na pasta artigo. Alguns destaques:

- Algoritmos quadráticos (Bubble, Insertion, Selection) são impraticáveis para grandes volumes de dados
- Quick Sort com pivô aleatório oferece o melhor equilíbrio entre desempenho médio e robustez
- Heap Sort demonstra consistência excepcional em todos os cenários
- Shell Sort surpreende com eficiência acima do esperado para sua complexidade teórica
- Radix Sort, apesar de complexidade linear teórica, não supera consistentemente os melhores algoritmos baseados em comparação

O estudo confirma que a escolha do algoritmo de ordenação deve considerar não apenas sua complexidade teórica, mas também fatores como padrões de acesso à memória, características dos dados e requisitos específicos da aplicação.
