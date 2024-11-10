def fibonacci(num):
    ant, prox = 0, 1
    while ant < num: 
        ant, prox = prox, ant + prox
    return ant == num

num = int(input("Digite um número: "))
if fibonacci(num):
    print("O número está na sequência de Fibonacci")
else:
    print("O número não está na sequência de Fibonacci")




