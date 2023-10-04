from django.shortcuts import render,redirect
from .forms import Estudante,Curso


def pagina(request):
    return render(request,'base.html')

def pagina2(request):
    if request.method == 'POST':
        form = Estudante(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('/dados/')  
    else:
        form = Estudante()
    
    return render(request, 'formulario.html', {'form': form})

def pagina3(request):
    if request.method == 'POST':
        form = Curso(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('/dados/')  
    else:
        form = Curso()
    
    return render(request, 'formulario2.html', {'form': form})






