from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .forms import UserForm

themes = [(0, 'Светлый'), (1, 'Тёмный')]
styles = [(0, "goth"), (1, "casual"), (2, "dream")]
clothes = [(0, "xs"), (1, "s"), (2, "m"), (3, "l"), (4, "xl")]

def userInitialezed(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            themeColor = form.cleaned_data['themeColor']

            favStyles = form.cleaned_data['favStyles']
            favStylesName = []
            for i in favStyles:
                favStylesName.append(styles[int(i)][1])

            favSizes = form.cleaned_data['favSizes']
            favSizessName = []
            for i in favSizes:
                favSizesName.append(sizes[int(i)][1])

            return HttpResponse(f"<p>Привет, {name}! Тема твоего сайта: {themes[int(themeColor)][1]}. Твои любимые стили: {favStylesName}</p>")
    else:
        form = UserForm()

    return render(request, 'store.html', {'form': form})        