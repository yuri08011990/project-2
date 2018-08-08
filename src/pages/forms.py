from django import forms
from pagedown.widgets import PagedownWidget
from blog.models import Post
from django.contrib.auth import authenticate, get_user_model, login, logout

class PostForm(forms.ModelForm):
	text = forms.CharField(widget=PagedownWidget)

	class Meta:
		model = Post
		fields = ('title', 'text',)


User = get_user_model()

class UserLoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)

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