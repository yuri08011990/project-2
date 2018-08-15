from django import forms
from blog.models import Post
from django.contrib.auth import authenticate, get_user_model, login, logout

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'text',)


User = get_user_model()

class UserLoginForm(forms.Form):
	username = forms.CharField(label="Логін")
	password = forms.CharField(label="Пароль", widget=forms.PasswordInput)

	def clean(self, *args, **kwargs):
		username = self.cleaned_data.get("username")
		password = self.cleaned_data.get("password")
		if username and password:
			user = authenticate(username=username, password=password)
			if not user:
				raise forms.ValidationError("Користувача з таким іменем не знайдено")
			if not user.check_password(password):
				raise forms.ValidationError("Невірний пароль")
			if not user.is_active:
				raise forms.ValidationError("Цей користувач більше не активний")
		return super(UserLoginForm, self).clean(*args, **kwargs)


class UserRegisterForm(forms.ModelForm):
	email = forms.EmailField(label='Введіть email адресу')
	email2 = forms.EmailField(label='Підтвердіть email адресу')
	password = forms.CharField(widget=forms.PasswordInput, label='Введіть пароль')
	password2 = forms.CharField(widget=forms.PasswordInput, label='Підтвердіть пароль')
	class Meta:
		model = User
		fields = ['username', 'email', 'email2', 'password', 'password2']

	def clean_email2(self):
		email = self.cleaned_data.get('email')
		email2 = self.cleaned_data.get('email2')
		if email != email2:
			raise forms.ValidationError('Email адреси повинні співпадати')
		email_qs = User.objects.filter(email=email)
		if email_qs.exists():
			raise forms.ValidationError('Таку адресу вже зареєстровано')
		return email

	def clean_password2(self):
		password = self.cleaned_data.get('password')
		password2 = self.cleaned_data.get('password2')
		if password != password2:
			raise forms.ValidationError('Паролі повинні співпадати')
		password_qs = User.objects.filter(password=password)
		return password