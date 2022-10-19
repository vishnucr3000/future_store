
from django.shortcuts import redirect

def login_required(fn):
    def wrapper(self,request,*args,**kwargs):
        if request.user:
            return fn(request,*args,**kwargs)
        else:
            return redirect("login")
    return wrapper(fn)
