from .models import *
from django.forms import ModelForm


class UrunForm(ModelForm):
    class Meta:
        model = Urun
        fields = ['kategori', 'kategori', 'alt',
                  'isim', 'aciklama', 'fiyat', 'resim']

    def __init__(self, *args, **kwargs):
        super(UrunForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
