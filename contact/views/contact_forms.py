from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib import messages
from contact.forms import ContactForm
from contact.models import Contact
from django.contrib.auth.decorators import login_required
# Create your views here.


#View da página de criação de contato
@login_required(login_url='contact:login')
def create(request):
    form_action = reverse('contact:create')
    
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)

        context = {
            'form': form,
            'form_action': form_action,
             'update': {'value': False}
        }
        
        if form.is_valid():
            contact = form.save(commit=False)
            contact.owner = request.user
            contact.save()
            messages.success(request, 'Contato adicionado com sucesso!')
            return redirect('contact:update', contact_id=contact.pk)  
        
        
    else:
        context = {
            'form': ContactForm(),
             'update': {'value': False}
        }
    
    #Retorno da view, com template e o que será enviado
    return render(
        request,
        'contact/create.html',
        context
    )

@login_required(login_url='contact:login')
def update(request, contact_id):

    contact = get_object_or_404(Contact, pk=contact_id, show=True, owner=request.user)
    form_action = reverse('contact:update', args=(contact_id,))
    
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES, instance=contact)

        context = {
            'form': form,
            'form_action': form_action,
            'update': {'value': True}
        }
        
        if form.is_valid():
            contact = form.save()
            messages.success(request, 'Contato Editado com sucesso!')
            return redirect('contact:index')  
        
        
    else:
        context = {
            'form': ContactForm(instance=contact),
            'form_action': form_action,
             'update': {'value': True}
        }
    
    #Retorno da view, com template e o que será enviado
    return render(
        request,
        'contact/create.html',
        context
    )

@login_required(login_url='contact:login')
def delete(request, contact_id):
    contact = get_object_or_404(
        Contact, pk=contact_id, show=True, owner=request.user
    )

    confirmation = request.POST.get('confirmation', 'no')
    
    if confirmation == 'yes':
        contact.delete()
        return redirect('contact:index')

    return render( 
        request,
        'contact/contact.html',
        {
            'contact': contact,
            'confirmation': confirmation
        }
    )

