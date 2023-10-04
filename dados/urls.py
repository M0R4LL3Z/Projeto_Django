from django.urls import path
from .views import pagina,pagina2,pagina3
from . import views


urlpatterns = [
    path('',pagina),
    path('formulario/',pagina2),
    path('formulario2/',pagina3)
    
    
]



