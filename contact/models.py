from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# first_name (string), last_name(string), phone(string)
# email (email), created_date (data), description (text)
# category (foreign key), show (boolean), owner (foreign key)
# picture (imagem)

#Criação da tabela e coluna das Categorias
class Category(models.Model):
    #Modificação dos nomes
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=50)

    #Nome dado a cada nova linha
    def __str__(self):
        return self.name 
    

#Criação da tabela e colunas dos contatos
class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=255, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    show = models.BooleanField(default=True)
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m/')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True )
    
    #Nome dado a cada nova linha
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
