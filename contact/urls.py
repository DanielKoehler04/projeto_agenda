from django.urls import path
from contact.views import index, contact, search, create, update, delete, register, login_view, logout_view, user_update

#Definição do nome da URL principal                                                                                                                                                                                
app_name = 'contact'

#URLs ligadas ao app contactS
urlpatterns = [
    #CRUD Contact
    path('contact/create/', create, name='create'),
    path('contact/<int:contact_id>/detail/', contact, name='contact'),
    path('contact/<int:contact_id>/update/', update, name='update'),
    path('contact/<int:contact_id>/delete/', delete, name='delete'),
    
    path('search/', search, name='search'),
    path('', index, name='index'),
    
    #user
    path('user/create', register, name='register'),
    path('user/login', login_view, name='login'),
    path('user/logout', logout_view, name='logout'),
    path('user/update', user_update, name='user_update')

]
