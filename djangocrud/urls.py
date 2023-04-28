"""
URL configuration for djangocrud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tasks import views
# comentario 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,  name='home'),
    path('signup/', views.signup, name='signup'),
    path('tasks_completed/', views.tasks_completed, name='tasks_completed'),
    path('tasks/<int:task_id>/complete', views.complete_task, name='complete_task'),
    #tasks
    path('tasks/create/', views.create_task, name='create_task'),
    path('tasks/', views.tasks, name='tasks'),
    path('tasks/<int:task_id>/', views.task_detail, name='task_detail'),
    path('tasks/<int:task_id>/update', views.task_detail, name='update_task'),
    path('tasks/<int:task_id>/delete', views.delete_task, name='delete_task'),
    #boveda
    # path('boveda/create/', views.create_boveda, name='create_boveda'),
    # path('boveda/', views.boveda, name='boveda'),
    # path('boveda/<int:boveda_id>/', views.boveda_detail, name='boveda_detail'),
    # path('boveda/<int:boveda_id>/update', views.boveda_detail, name='update_boveda'),
    # path('boveda/<int:boveda_id>/delete', views.delete_boveda, name='delete_boveda'),
    # #difunto
    # path('difunto/create/', views.create_difunto, name='create_difunto'),
    # path('difunto/', views.difunto, name='difunto'),
    # path('difunto/<int:difunto_id>/', views.difunto_detail, name='difunto_detail'),
    # path('difunto/<int:difunto_id>/update', views.difunto_detail, name='update_difunto'),
    # path('difunto/<int:difunto_id>/delete', views.delete_difunto, name='delete_difunto'),
    #familiarDifunto
    # path('familiarDifunto/create/', views.create_familiarDifunto, name='create_familiarDifunto'),
    # path('familiarDifunto/', views.familiarDifunto, name='familiarDifunto'),
    # path('familiarDifunto/<int:familiarDifunto_id>/', views.familiarDifunto_detail, name='familiarDifunto_detail'),
    # path('familiarDifunto/<int:familiarDifunto_id>/update', views.familiarDifunto_detail, name='update_familiarDifunto'),
    # path('familiarDifunto/<int:familiarDifunto_id>/delete', views.delete_familiarDifunto, name='delete_familiarDifunto'),
    # #propietario
    path('propietario/create/', views.create_propietario, name='create_propietario'),
    path('propietario/', views.propietarios, name='propietarios'),
    # path('propietario/<int:propietario_id>/', views.propietario_detail, name='propietario_detail'),
    # path('propietario/<int:propietario_id>/update', views.propietario_detail, name='update_propietario'),
    # path('propietario/<int:propietario_id>/delete', views.delete_propietario, name='delete_propietario'),
    # login y logout
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin')
]
