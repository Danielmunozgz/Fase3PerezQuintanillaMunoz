from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('habitacion/',views.habitacion,name='habitacion'),
    path('registrarse/', views.registrarse, name='registrarse'),
    path('clientes/', views.ClienteListView.as_view(), name='clientes'),
    path('clientes/<str:pk>', views.ClienteDetailView.as_view(), name='cliente-detail'),
    path('habitacion-adm/', views.HabitacionListView.as_view(), name='habitacion-adm'),
    path('habitacion-adm/<str:pk>', views.HabitacionDetailView.as_view(), name='habitacion-detail'),
]

urlpatterns += [
    path('registrarse/cliente', views.cliente_nuevo, name='cliente_create'),
    path('habitacion-adm', views.habitacion_nuevo, name='habitacion_create'),
    path('cliente/<str:pk>/update/', views.cliente_editar, name='cliente_update'),
    path('cliente/<str:pk>/delete/', views.ClienteDeleteView.as_view(), name='cliente_delete'),
    path('habitacion/<str:pk>/update/', views.habitacion_editar, name='habitacion_update'),
    path('habitacion/<str:pk>/delete/', views.HabitacionDeleteView.as_view(), name='habitacion_delete'),
]
