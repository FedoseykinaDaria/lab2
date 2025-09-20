from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .forms import UserForm

themes = [(0, 'Светлый'), (1, 'Тёмный')]
styles = [(0, "goth"), (1, "casual"), (2, "dream")]
sizes = [(0, "xs"), (1, "s"), (2, "m"), (3, "l"), (4, "xl")]

def userInitialezed(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            
            themeColor = form.cleaned_data['themeColor']

            favStyles = form.cleaned_data['favStyles']
            if len(favStyles) == 0:
                favStyles = ['0', '1', '2']
            favStylesName = []
            for i in favStyles:
                favStylesName.append(styles[int(i)][1])

            favSizes = form.cleaned_data['favSizes']
            if len(favSizes) == 0:
                favSizes = ['0', '1', '2', '3']
            favSizesName = []
            for i in favSizes:
                favSizesName.append(sizes[int(i)][1])

            response = HttpResponse(f"<p>Привет, {name}!</p> <p>Тема твоего сайта: {themes[int(themeColor)][1]}. Твои любимые стили: {favStylesName}</p>")
            response.set_cookie("name", name)
            response.set_cookie("themeColor", themeColor)
            response.set_cookie("favStyles", favStyles)
            response.set_cookie("favSizes", favSizes)

            return response
            
    else:
        form = UserForm()

    return render(request, 'store.html', {'form': form})        