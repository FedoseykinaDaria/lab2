from django import forms

themes = [(0, 'Светлый'), (1, 'Тёмный')]
styles = [(0, "goth"), (1, "casual"), (2, "dream")]
clothes = [(0, "xs"), (1, "s"), (2, "m"), (3, "l"), (4, "xl")]


class UserForm(forms.Form):
    name = forms.CharField(max_length = 50, label = "Как тебя зовут?") 
    favStyles = forms.MultipleChoiceField(
        required = False,
        widget = forms.CheckboxSelectMultiple,
        choices = styles,
        label = "Выбери любимые стили одежды")
    favSizes = forms.MultipleChoiceField(
        required = False,
        widget = forms.CheckboxSelectMultiple,
        choices = clothes,
        label = "Выбери размеры одежды")
    themeColor = forms.ChoiceField(choices = themes, label = "Выбери цвет темы сайта")