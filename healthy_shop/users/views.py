from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login
from .forms import UserCreationForm
from django.contrib.auth.models import User

class Register(View):
    template_name = 'registration/register.html'

    def get(self, request):
        context = {'form': UserCreationForm()}
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Теперь этот save() гарантированно сохраняет email
            
            # Логиним пользователя
            auth_user = authenticate(username=user.username, password=request.POST.get('password1'))
            if auth_user is not None:
                login(request, auth_user)
                
            return redirect('homepage:index_page')
            
        # Если форма невалидна, выводим ошибки в консоль
        print("ОШИБКИ ФОРМЫ:", form.errors)
        return render(request, self.template_name, {'form': form})


# from django.shortcuts import render, redirect
# from django.views import View
# from django.contrib.auth import authenticate, login
# from django.contrib.auth.forms import UserCreationForm

# class Register(View):
#     template_name = 'registration/register.html'

#     def get(self, request):
#         context = {'form': UserCreationForm()}
#         return render(request, self.template_name, context)

#     def post(self, request):
#         form = UserCreationForm(request.POST)

#         if form.is_valid():
#             # 1. Сохраняем пользователя без фиксации в БД
#             user = form.save(commit=False)

#             # 2. Явно переносим email из формы в объект модели
#             user.email = form.cleaned_data.get('email')

#             # 3. Если email вдруг пустой (None), ставим пустую строку, чтобы не было ошибки
#             if user.email is None:
#                 user.email = ''

#             # 4. Сохраняем в БД
#             user.save()

#             # 5. Авторизуем и редиректим
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=password)
#             login(request, user)

#             print(f"Зарегистрирован пользователь: {username}, email: '{user.email}'")
#             return redirect('homepage:index_page')

#         context = {'form': form}
#         return render(request, self.template_name, context)

#     # def post(self, request):
#     #     form = UserCreationForm(request.POST)
#     #     if form.is_valid():
#     #         user = form.save(commit=False)
#     #         user.email = form.cleaned_data.get('email')
#     #         user.save()
#     #         username = form.cleaned_data.get('username')
#     #         password = form.cleaned_data.get('password1')
#     #         user = authenticate(username=username, password=password)
#     #         login(request, user)
#     #         print(f"Зарегистрирован пользователь: {username} ({user.email})")
#     #         return redirect('homepage:index_page')

#     #     context = {'form': form}
#     #     return render(request, self.template_name, context)