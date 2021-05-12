
from django.shortcuts import redirect, render
from apps.lds.forms.user import CreateUserForm


def create_user(request):

    create_user_form = CreateUserForm(request.POST or None)
    if create_user_form.is_valid():
        create_user_form.save()

        return redirect('login')

    context = {
        'create_user_form': create_user_form,
    }

    return render(request, 'lds/accounts/create_user.html', context)
