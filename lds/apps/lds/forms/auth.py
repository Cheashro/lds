
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.forms import AuthenticationForm


class LDSAuthenticationForm(AuthenticationForm):

    error_messages = {
        'invalid_login': _('帳號或密碼不正確，請重新輸入正確的帳號密碼'),
    }

    def __init__(self, request=None, *args, **kwargs):
        super().__init__(request, *args, **kwargs)

        self.fields['username'].label = ''
        self.fields['password'].label = ''

        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['password'].widget.attrs['placeholder'] = 'Password'

        self.fields['username'].widget.attrs['input_prepend_icon'] = 'cil-user'
        self.fields['password'].widget.attrs['input_prepend_icon'] = 'cil-lock-locked'
