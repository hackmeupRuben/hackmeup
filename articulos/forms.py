from .models import Articles, Categoria
from django import forms

class SearchForm(forms.Form):
    Categorias = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                             choices=Categoria, required=False)


class ArticlesCreateForm(forms.ModelForm):

    class Meta():
        model = Articles
        fields = [
            'titulo',
            'contenido',
            'categoria',
            'status',
        ]
        labels = {
            'titulo': 'Titulo',
            'contenido': 'Contenido',
            'categoria': 'Categorias',
            'status': 'Status'
        }
        widgets = {
   #         'nombre': forms.TextInput(attrs={'class': 'form-control'}),
    #        'apellidos': forms.TextInput(attrs={'class': 'form-control'}),
     #       'edad': forms.TextInput(attrs={'class': 'form-control'}),
        #     'contenido': forms.Textarea(attrs={'class': 'form-control'}),
             'categoria': forms.CheckboxSelectMultiple(),
        #     'status': forms.CheckboxSelectMultiple,
                      }
