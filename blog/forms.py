from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    ChoiceGun = [
        ('AWP', 'AWP'),
        ('AK-47', 'AK-47'),
        ('M4A4', 'M4A4'),
        ('M4A1-S', 'M4A1-S'),
        ('Desert Eagle', 'Desert Eagle'),
        ('Glock-18', 'Glock-18'),
        ('USP-S', 'USP-S'),
        ('P250', 'P250'),
        ('Rifle', 'Rifle'),
        ('SG 553', 'SG 553'),
        ('FAMAS', 'FAMAS'),
        ('Negev', 'Negev'),
        ('Nova', 'Nova'),
        ('MP7', 'MP7'),
        ('MP9', 'MP9'),
        ('UMP-45', 'UMP-45'),
        ('P90', 'P90'),
        ('MAG-7', 'MAG-7'),
        ('Sawn-Off', 'Sawn-Off'),
        ('XM1014', 'XM1014'),
        ('CZ75-Auto', 'CZ75-Auto'),
        ('Five-SeveN', 'Five-SeveN'),
        ('Tec-9', 'Tec-9'),
        ('Bizon', 'Bizon'),
        ('PP-Bizon', 'PP-Bizon'),
        ('M249', 'M249'),
        ('AUG', 'AUG'),
        ('Galil AR', 'Galil AR'),
        ('A1-S', 'A1-S'),
        ('R8 Revolver', 'R8 Revolver'),
        ('Dual Berettas', 'Dual Berettas'),
        ('M4A1', 'M4A1')
    ]

    ChoiceDegree = [
        ('Factory New', 'Factory New'),
        ('Minimal Wear', 'Minimal Wear'),
        ('Field-Tested', 'Field-Tested'),
        ('Well-Worn', 'Well-Worn'),
        ('Battle-Scarred', 'Battle-Scarred')
    ]

    category = forms.ChoiceField(choices=ChoiceGun, label="Категория")
    nameteg = forms.CharField(max_length=50, label="Название скина")
    Degree = forms.ChoiceField(choices=ChoiceDegree, label="Степень износа")
    body = forms.IntegerField(label="Цена")

    class Meta:
        model = Post
        fields = ['category', 'nameteg', 'Degree', 'body']
