from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Пароли не совпадают")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        # Явно забираем данные
        user.email = self.cleaned_data.get("email", "")
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

# from django import forms
# from django.contrib.auth import get_user_model
# from django.contrib.auth.forms import UserCreationForm

# User = get_user_model()


# class UserCreationForm(UserCreationForm):
#     email = forms.EmailField(
#         required=True,
#         label="Email",
#         widget=forms.EmailInput(attrs={'class': 'form-control'})
#     )

#     class Meta(UserCreationForm.Meta):
#         model = User
#         fields = ('username', 'email')

#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.email = self.cleaned_data.get('email')
#         if commit:
#             user.save()
#         return user