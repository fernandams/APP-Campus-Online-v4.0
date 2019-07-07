from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class _UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

class _UserChangeForm(UserChangeForm):
    pass