
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.forms import UserCreationForm
from django.forms.fields import CharField, EmailField
from django.forms.widgets import PasswordInput, EmailInput


class CreateUserForm(UserCreationForm):

    error_messages = {
        'password_mismatch': _('您輸入的兩個密碼並不相符，請再試一次。'),
    }

    username = EmailField(
        label='',
        widget=EmailInput(attrs={'placeholder': 'Email', 'input_prepend_icon': 'cil-user'}),
    )
    password1 = CharField(
        label='',
        widget=PasswordInput(attrs={'placeholder': 'Password', 'input_prepend_icon': 'cil-lock-locked'}),
    )
    password2 = CharField(
        label='',
        widget=PasswordInput(attrs={'placeholder': 'Repeat password', 'input_prepend_icon': 'cil-lock-locked'}),
    )
