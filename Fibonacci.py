#Fibonacci sequence

def fibonacci(n):
    fibonacci_list =[]
    x, y = 0, 1
    count = 0
    fibonacci_list.append(x)
    fibonacci_list.append(y)
    while count < pregunta:
        siguientetermino = x + y
        fibonacci_list.append(siguientetermino)
        x = y
        y = siguientetermino
        count += 1
    return fibonacci_list

pregunta = int(input("Que cantidad de sucesiones de fibonacci deseas? : "))

if(pregunta <= 2):
    print("pregunta incompleta")
    pregunta = int(input("Que cantidad de sucesiones de fibonacci deseas? : "))

print(fibonacci(pregunta))

       

        
        
