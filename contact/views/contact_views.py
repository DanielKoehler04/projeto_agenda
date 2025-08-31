from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.core.paginator import Paginator
from contact.models import Contact
from django import forms
from django.contrib.auth.decorators import login_required

# Create your views here.

#View da página princial
def index(request):

    #Extrai os contatos da Base de Dados
    contacts = Contact.objects.filter(show=True).order_by('-id')

    paginator = Paginator(contacts, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    #Dicionário com os dados enviados ao template
    context = {
        'page_obj': page_obj,
        'site_title': 'Contatos - Agenda'
    }
    
    #Retorno da view, com template e o que será enviado
    return render(
        request,
        'contact/index.html',
        context
    )

#View da pesquisa de contatos
def search(request):

    #Capturao valor enviado no campo de pesquisa
    search_value = request.GET.get('q', '').replace('-', '').strip()
    
    if search_value == '':
        return redirect('contact:index')

    #Filtra os contatos com o resultado do "search_value"
    contacts = Contact.objects.filter(show=True).filter(
        Q(first_name__icontains=search_value) |
        Q(last_name__icontains=search_value) |
        Q(phone__icontains=search_value) |
        Q(email__icontains=search_value) 
        ).order_by('-id')

    paginator = Paginator(contacts, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

     #Dicionário com os dados enviados ao template
    context = {
        'page_obj': page_obj,
        'site_title': 'Search -'
    }
    
    #Retorno da view, com template e o que será enviado
    return render(
        request,
        'contact/index.html',
        context
    )


#View das páginas individuais de contato
def contact(request, contact_id):
    
    #Captura cada contato 
    single_contact = get_object_or_404(Contact, pk=contact_id, show=True)

    #Criação do Titulo da Página
    contact_name = f'{single_contact.first_name} {single_contact.last_name} - Agenda'

    #Dicionário com os Dados Enviados ao template
    context = {
        'contact': single_contact,
        'site_title': contact_name
    }

    #Retorno da view, com template e o que será enviado
    return render(
        request,
        'contact/contact.html',
        context

    )
