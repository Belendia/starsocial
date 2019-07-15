from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class UserSignUpForm(UserCreationForm):

    class Meta:
        fields = ('username', 'email', 'password1', 'password2')
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # field name in the html view
        self.fields['username'].label = 'Display Name'
        self.fields['email'].label = 'Email Addiress'
