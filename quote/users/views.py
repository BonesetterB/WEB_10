from django.shortcuts import render,redirect
from django.views import View
from .forms import RegistForm
from django.contrib import messages

class RegistView(View):
    template_name='users/log.html'
    form_class=RegistForm

    def get(self,request):
        return render(request,self.template_name,{'form':self.form_class})

    def post(self,request):
        form=self.form_class(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            messages.success(request, f"Вітаємо {username}. Ваш акаунт успішно створено")
            return redirect('users:Sign')
        return render(request,self.template_name,{'form':form})





