from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('skatistas/', views.lista_skatistas, name='lista_skatistas'),
    path('cadastrar/', views.cadastrar_skatista, name='cadastrar_skatista'),
    path("editar/<int:id>/",views.editar_skatista, name="editar_skatista"),
    path("excluir/<int:id>/",views.excluir_skatista,name="excluir_skatista"),
    path("skatista/<int:id>/",views.detalhe_skatista,name="detalhe_skatista"),
    path('cadastro-usuario/', views.cadastro_usuario, name='cadastro_usuario'),
]