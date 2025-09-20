from django import forms

class UserForm(forms.Form):
    name = forms.CharField(max_length = 50, label = "Как тебя зовут?")
    themeColor = forms.ChoiceField(choices = ((0, 'Светлый'), (1, 'Тёмный')), label = "Выбери цвет темы сайта") 
    favStyles = forms.MultipleChoiceField(
        required = False,
        widget = forms.CheckboxSelectMultiple,
        choices = ((0, "goth"), (1, "casual"), (2, "dream")),
        label = "Выберите предпочитаемые стили одежды")
    favSizes = forms.MultipleChoiceField(
        required = False,
        widget = forms.CheckboxSelectMultiple,
        choices = ((0, "xs"), (1, "s"), (2, "m"), (3, "l"), (4, "xl")),
        label = "Выберите предпочитаемые размеры одежды")