num1 = float (input("Insira o primeiro número!") )
op = input("Insira a operação!")
num2 = float (input("Insira o segundo número!") )
result = ()
historico = []

match op:
    case "+":
        result = num1+num2
    case "-":
        result = num1-num2
    case "*":
        result = num1*num2
    case "/":
        result = num1/num2
print (result)

historico.append(result)
print(historico)
