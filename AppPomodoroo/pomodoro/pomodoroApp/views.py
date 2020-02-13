from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect
from datetime import date
from django.template import loader
from .models import Actividades

def index(request):
    template = loader.get_template("pomodoroApp/index.html")
    list= []

    filtered_task = Actividades.objects.all()
    listnoComp = None
    for e in filtered_task:
        if e.tiempofinal ==0 :
            listnoComp = e
        list.append(e)
    context = {
        "listtask": list,
        "listNoComp": listnoComp,
        "alarma":None
    }
    return HttpResponse(template.render(context, request))

def add_task(request):
    if request.method == 'PUT' or request.method == 'POST':
        alarma = None
        nombreTarea = request.POST['nombreTarea']
        try:
            tarea = Actividades.objects.get(nombreTarea=nombreTarea)
            alarma = "No Valid: Name repeated"
        except:
            tiempoTarea = request.POST['tiempoTarea']
            time = float(tiempoTarea)
            if time >= 1:
                nombreTarea = nombreTarea.replace(" ", "")
                tiempofinal = 0
                fechaTarea = date.today()
                tareas = Actividades(nombreTarea=nombreTarea, tiempoTarea=tiempoTarea, tiempofinal=tiempofinal,
                                     fechaTarea=fechaTarea)
                tareas.save()
            else:
                alarma = "No Valid: Time should be higher than 0"

    template = loader.get_template("pomodoroApp/index.html")
    list= []
    filtered_task = Actividades.objects.all()
    listnoComp = None
    for e in filtered_task:
        if e.tiempofinal ==0 :
            listnoComp = e
        list.append(e)
    context = {
        "listtask": list,
        "listNoComp": listnoComp,
        "alarma":alarma
    }
    return HttpResponse(template.render(context, request))

def finish_task(request):
    if request.method == 'PUT' or request.method == 'POST':
        nombreTarea = request.POST['nombreTareas']
        tarea = Actividades.objects.get(nombreTarea=nombreTarea)
        tiempo = request.POST['tiempoenmarchas']
        tiempof = float(tiempo)
        tarea.tiempofinal = int(round(tiempof))
        if tarea.tiempofinal == 0:
            tarea.tiempofinal=1
        tarea.save()
    template = loader.get_template("pomodoroApp/index.html")
    list= []
    filtered_task = Actividades.objects.all()
    listnoComp = None
    for e in filtered_task:
        if e.tiempofinal == 0 :
            listnoComp = e
        list.append(e)
    context = {
        "listtask": list,
        "listNoComp": listnoComp,
        "alarma":None
    }
    return HttpResponse(template.render(context, request))

def remove_task(request):
    if request.method == 'PUT' or request.method == 'POST':
        nombreTarea = request.POST['nombreTareasR']
        try:
            tarea = Actividades.objects.get(nombreTarea=nombreTarea)
            tarea.delete()
        except:
            alarma = "No Valid: Nothing to erase"
    template = loader.get_template("pomodoroApp/index.html")
    list= []
    filtered_task = Actividades.objects.all()
    listnoComp = None
    for e in filtered_task:
        if e.tiempofinal == 0 :
            listnoComp = e
        list.append(e)
    context = {
        "listtask": list,
        "listNoComp": listnoComp,
        "alarma":None
    }
    return HttpResponse(template.render(context, request))