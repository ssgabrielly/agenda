from django.urls import path
from . import views

urlpatterns = [
    path('agenda', views.index, name='agenda-events-index'),
    path('all', views.all, name='agenda-events-all'),
    path('<int:id>', views.show, name='agenda-events-show'),
    path('<int:year>/<int:month>/<int:day>', views.day, name='agenda-events-day'),
    path('new', views.new, name='agenda-events-new'),
    path('delete/<int:id>', views.delete, name='agenda-events-delete'),
    path('edit', views.edit, name='agenda-events-edit'),
    path('cad', views.cad_list, name='cad_list'),
    path('cad/<int:pk>/', views.cad_detail, name='cad_detail'),
    path('cad/new/', views.cad_new, name="cad_new"),
    path('cad/<int:pk>/edit/', views.cad_edit, name="cad_edit"),
]