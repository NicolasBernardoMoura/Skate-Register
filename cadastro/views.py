from django.shortcuts import render, redirect
from .forms import SkatistaForm
from django.shortcuts import get_object_or_404
from .models import Skatista
from django.db.models import Count
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


def cadastro_usuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')

    else:
        form = UserCreationForm()

    return render(request, 'cadastro/cadastro_usuario.html', {
        'form': form
    })




def home(request):

    total = Skatista.objects.count()

    street = Skatista.objects.filter(modalidade="Street").count()

    park = Skatista.objects.filter(modalidade="Park").count()

    ultimos = Skatista.objects.order_by("-id")[:5]

    return render(
        request,
        "cadastro/home.html",
        {
            "total": total,
            "street": street,
            "park": park,
            "ultimos": ultimos,
        },
    )




def lista_skatistas(request):

    pesquisa = request.GET.get('pesquisa')

    if pesquisa:

        skatistas = Skatista.objects.filter(nome__icontains=pesquisa)

    else:

        skatistas = Skatista.objects.all()

    return render(
        request,
        'cadastro/lista.html',
        {
            'skatistas': skatistas,
            'pesquisa': pesquisa
        }
    )





@login_required 
def cadastrar_skatista(request):

    if request.method == 'POST':

        form = SkatistaForm(request.POST, request.FILES)

        if form.is_valid():

            form.save()

            return redirect('lista_skatistas')

    else:

        form = SkatistaForm()

    return render(
        request,
        'cadastro/formulario.html',
        {
            'form': form,
            'titulo': 'Cadastrar Skatista',
            'botao': 'Salvar'
        }
    )








def editar_skatista(request, id):

    skatista = get_object_or_404(Skatista, id=id)

    if request.method == "POST":

        form = SkatistaForm(request.POST,
                            request.FILES,
                            instance=skatista)

        if form.is_valid():

            form.save()

            return redirect("lista_skatistas")

    else:

        form = SkatistaForm(instance=skatista)

    return render(
        request,
        'cadastro/formulario.html',
        {
            'form': form,
            'titulo': 'Editar Skatista',
            'botao': 'Salvar Alterações'
        }
    )






def excluir_skatista(request, id):

    skatista = get_object_or_404(Skatista, id=id)

    if request.method == "POST":
        skatista.delete()
        return redirect("lista_skatistas")

    return render(
        request,
        "cadastro/excluir.html",
        {
            "skatista": skatista
        }
    )






def detalhe_skatista(request, id):

    skatista = get_object_or_404(Skatista, id=id)

    return render(
        request,
        "cadastro/detalhe.html",
        {
            "skatista": skatista
        }
    )

