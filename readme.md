# 🧮 Calculadora em Python com Histórico

Este projeto é uma **calculadora simples em Python** executada no terminal.
Ela permite realizar operações matemáticas básicas e armazenar um **histórico das operações realizadas** durante a execução do programa.

---

## 📌 Funcionalidades

* ➕ Soma
* ➖ Subtração
* ✖️ Multiplicação
* ➗ Divisão
* 📜 Visualização do histórico de cálculos
* ❌ Encerramento do programa pelo menu


## 🛠️ Tecnologias Utilizadas

* **Python 3.10+**
* Estrutura `match case`
* Execução em **terminal / console**

---

## ▶️ Como Executar

1. Certifique-se de ter o **Python 3.10 ou superior** instalado.
2. Clone este repositório:

```bash
git clone https://github.com/seu-usuario/nome-do-repositorio.git
```

3. Entre na pasta do projeto:

```bash
cd nome-do-repositorio
```

4. Execute o programa:

```bash
python calculadora.py
```

---

## 📋 Menu do Programa

Quando executado, o programa exibirá as seguintes opções:

```
Selecione a ação que deseja fazer:
1 - Calcular
2 - Histórico
3 - Finalizar
```

### 1️⃣ Calcular

Permite inserir:

* Primeiro número
* Operação matemática (`+`, `-`, `*`, `/`)
* Segundo número

O resultado será exibido na tela e salvo no histórico.

### 2️⃣ Histórico

Mostra todas as operações realizadas durante a execução do programa.

Exemplo:

```
[5.0, '+', 3.0, '=', 8.0, '||', 10.0, '*', 2.0, '=', 20.0, '||']
```

### 3️⃣ Finalizar

Encerra o programa.

---

## 💻 Código do Projeto

```python
menu1 = 1
historico = []

while menu1 == 1:
    menu2 = input("Selecione a ação que deseja fazer: 1-Calcular, 2-Histórico, 3-Finalizar")
    match menu2:
        case "1":
            n1=float(input("Insira o primeiro número:"))
            op=input("Insira a operação:")
            n2=float(input("Insira o segundo número"))

            match op:
                case "+":
                    result = n1+n2
                case "-":
                    result = n1-n2
                case "*":
                    result = n1*n2
                case "/":
                    result = n1/n2

            print(result)
            historico.extend([n1, op, n2, "=", result, "||"])
        case "2":
            print(historico)
        case "3":
            menu1 = 0
```

---

## 🚀 Possíveis Melhorias

* Melhor formatação do histórico
* Tratamento de erros (ex: divisão por zero)
* Interface gráfica
* Salvar histórico em arquivo
* Aceitar mais operações matemáticas

---

## 📄 Licença

Este projeto é livre para estudo e aprendizado.
