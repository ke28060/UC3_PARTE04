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
