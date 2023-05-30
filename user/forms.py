from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class KayitForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(KayitForm, self).__init__(*args, **kwargs)
        # self.fields['username'].widget.attrs.update(
        #     {'class': 'form-control'})
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
