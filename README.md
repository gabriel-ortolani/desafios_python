# 💻 Desafios Iniciais em Python

Este repositório contém uma série de desafios simples que desenvolvi enquanto aprendo Python. Eles cobrem conceitos básicos como entrada de dados, condicionais, loops, funções, listas e manipulação de strings.

---

## 🕹️ Desafios Feitos

### 1. Par ou Ímpar  
Um joguinho onde o usuário escolhe par ou ímpar, digita um número e o computador também. O programa soma os dois valores e informa quem venceu.

### 2. Adivinhe o Número  
O computador escolhe um número aleatório de 1 a 20, e o usuário precisa adivinhar. O programa informa se o palpite foi alto ou baixo até acertar.

### 3. Lista de Compras  
Um pequeno sistema de lista de compras com opções para adicionar, remover e visualizar itens. Feito usando listas e laços `while`.

### 4. Verificador de Palíndromo  
Programa que verifica se uma palavra ou frase é um palíndromo, desconsiderando espaços e letras maiúsculas.

### 5. Lista de Números Primos  
Programa com menu simples no terminal que permite ao usuário adicionar números a uma lista e, ao escolher a opção de visualização, exibe apenas os números primos.

**🧠 Conceitos usados:**  
- Laço `while` com menu interativo  
- Função para verificar números primos  
- Listas e `append()`  
- Compreensão de listas (`[x for x in lista if ...]`)

---

### 6. Gerador de Senhas Seguras  
Gera uma senha aleatória do tamanho desejado pelo usuário, contendo obrigatoriamente:
- uma letra maiúscula  
- uma letra minúscula  
- um caractere especial  

Utiliza `random.choices()` e embaralha os caracteres para evitar padrões previsíveis.

**🔐 Conceitos usados:**  
- Biblioteca `random`  
- Strings (`string.ascii_letters`, `string.digits`, `string.punctuation`)  
- Funções auxiliares (`isupper()`, `islower()`, `in`)  
- `any()` e `join()`  
- Validação de senha com regras mínimas

---

## 📚 Conceitos gerais usados

- `input()` e `print()`
- Condicionais `if / elif / else`
- Laços `while`
- Funções (`def`)
- Listas (`append`, `remove`, `in`)
- Operador módulo (`%`)
- Compreensão de listas (`[x for x in lista if ...]`)
- Validação com `any()` e métodos de string (`islower()`, `isupper()`, `in`)
- Uso do módulo `random` para gerar valores aleatórios

---

## 🚀 Próximos passos

- Aprender estruturas mais avançadas (dicionários, classes)  
- Criar interfaces gráficas simples com `tkinter`  
- Usar arquivos para salvar e carregar dados (`open`, `read`, `write`)

---

## 🛠️ Como usar qualquer desafio

1. Certifique-se de ter o **Python 3** instalado.
  ```bash
   python --version
  ```
2. Entre no terminal e escreva Python e o nome do arquivo escolhido **Ex: Python ParOuImpar.py**
