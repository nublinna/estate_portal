from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import User, Role

class SignUpForm(UserCreationForm):
    role = forms.ModelChoiceField(
        queryset=Role.objects.all(),
        empty_label=None,
        widget=forms.RadioSelect,
    )

    class Meta(UserCreationForm):
        model = User
        fields = ('username', 'role')