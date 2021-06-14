from django.shortcuts import redirect

#Este metodo funciona para determinar cuando un usuario no esta identificado y por defecto lo envia al home
def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('eduacionapp:home')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func

