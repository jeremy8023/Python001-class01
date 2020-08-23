from django import forms


class LoginForm(forms.Form):
    user_name = forms.CharField(label="用户名")
    passwd = forms.CharField(widget=forms.PasswordInput, min_length=8, label="密码")