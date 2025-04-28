from django import forms




class User_regist(forms.Form):
    email = forms.EmailField(label = "Email")
    password = forms.CharField(max_length = 128,widget=forms.PasswordInput)