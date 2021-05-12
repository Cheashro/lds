
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.forms import AuthenticationForm
from django.forms.fields import EmailField, CharField
from django.forms.widgets import EmailInput, PasswordInput


class LDSAuthenticationForm(AuthenticationForm):

    error_messages = {
        'invalid_login': _('帳號或密碼不正確，請重新輸入正確的帳號密碼'),
    }

    def __init__(self, request=None, *args, **kwargs):
        super().__init__(request, *args, **kwargs)

        self.fields['username'] = EmailField(
            label='',
            widget=EmailInput(attrs={'placeholder': 'Email', 'input_prepend_icon': 'cil-user'}),
        )
        self.fields['password'] = CharField(
            label='',
            widget=PasswordInput(attrs={'placeholder': 'Password', 'input_prepend_icon': 'cil-lock-locked'}),
        )
