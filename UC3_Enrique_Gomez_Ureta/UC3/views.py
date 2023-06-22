from django.shortcuts import render, HttpResponse,redirect

def index(request):
    return render(request,'index.html')
# Create your views here.

def index(request):
    estudiantes = [ 'Microprocesadores', 
                    'Ing. de Requerimientos',
                    'Dinamica de Sistemas',
                    'Gestion de Procesos de Negocios',
                    'Legislacion Informatica',
                    'Computacion de Algoritmos Gráficos',
                    'Matematica IV']


    return render(request,'index.html', {
        'titulo':'Inicio',
        'mensaje':'Proyecto Web Con DJango',
        'estudiantes': estudiantes
    })

def primos(request, a=1, b=100):
    if a > b:
        a, b = b, a

    resultado = f"<h2>Números primos en el rango [{a}, {b}]</h2>\nResultado:<br>\n<ul>\n"

    for num in range(a, b + 1):
        if num > 1:
            is_prime = True
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                resultado += f"<li>{num}</li>"

    resultado += "</ul>"
    return HttpResponse(resultado)
