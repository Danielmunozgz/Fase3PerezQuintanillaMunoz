from django import forms
from . models import Cliente, Pais, Habitacion, TipoHab

class PaisForm(forms.ModelForm):
    id_pais = forms.IntegerField(label='Id País',widget=forms.NumberInput(
        attrs={
            'class':'form-control'
        }
    ))
    
    nombre_pais = forms.CharField(label='Nombre País', max_length=100, widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))
    
    class Meta:
        model = Pais
        fields = ("id_pais","nombre_pais",)
        

class ClienteForm(forms.ModelForm):
    rut = forms.CharField(label='Rut', max_length=15,widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))
    
    nombres = forms.CharField(label='Nombres', max_length=100, widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))
    
    apellidos = forms.CharField(label='Apellidos', max_length=100, widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))
    
    pais = forms.ModelChoiceField(queryset=Pais.objects.all(),label='País', widget=forms.Select(
        attrs={
            'class':'form-control'
        }
    ))
    
    edad = forms.IntegerField(label='Edad', widget=forms.NumberInput(
        attrs={
            'class':'form-control'
        }
    ))
        
    email = forms.EmailField(label='Email', max_length=200, widget=forms.EmailInput(
        attrs={
            'class':'form-control'
        }
    ))
    
    direccion = forms.CharField(label='Dirección', max_length=200, widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))
    
    password = forms.CharField(label='Contraseña', max_length=20, widget=forms.PasswordInput(
        attrs={
            'class':'form-control'
        }
    ))
    
    class Meta:
        model = Cliente
        fields = ("rut","nombres","apellidos","pais","edad","email","direccion","password")
        
class HabitacionForm(forms.ModelForm):
    id_habitacion = forms.IntegerField(label='Id Habitación', widget=forms.NumberInput(
        attrs={
            'class':'form-control'
        }
    ))
    
    tipo_habitacion = forms.ModelChoiceField(queryset=TipoHab.objects.all(), label='Tipo Habitación', widget=forms.Select(
        attrs={
            'class':'form-control'
        }
    ))
    
    caracteristicas = forms.CharField(label='Características', max_length=1000, widget=forms.Textarea(
        attrs={
            'class':'form-control'
        }
    ))
    
    descripcion = forms.CharField(label='Descripción', max_length=1000, widget=forms.Textarea(
        attrs={
            'class':'form-control'
        }
    ))
    
    servicios = forms.CharField(label='Servicios', max_length=1000, widget=forms.Textarea(
        attrs={
            'class':'form-control'
        }
    ))
    
    equipamiento = forms.CharField(label='Equipamiento', max_length=1000, widget=forms.Textarea(
        attrs={
            'class':'form-control'
        }
    ))
    
    image_1 = forms.ImageField(label='Foto_1', widget=forms.ClearableFileInput(
        attrs={
            'class':'form-control'
        }
    ))
    
    image_2 = forms.ImageField(label='Foto_1', widget=forms.ClearableFileInput(
        attrs={
            'class':'form-control'
        }
    ))
    
    class Meta:
        model = Habitacion
        fields = ("id_habitacion","tipo_habitacion","caracteristicas","descripcion","servicios","equipamiento","image_1","image_2")
        