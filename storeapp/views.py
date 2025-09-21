from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .forms import UserForm

themes = [(0, 'Светлый'), (1, 'Тёмный')]
styles = [(0, "goth"), (1, "casual"), (2, "dream")]
sizes = [(0, "xs"), (1, "s"), (2, "m"), (3, "l"), (4, "xl")]
clothes = [
    {'title': 'Котический свитер',
    'style': 'goth',
    'src': 'static/goth_sweater.jpg',
    'size': ['xs', 's', 'm'],
    'description': 'Свитер с котятами в готическом стиле согрет вас даже в самую неприветливую погоду'},
    {'title': 'Котошапка',
    'style': 'goth',
    'size': ['xs', 's', 'm', 'l', 'xl'],
    'src': 'static/goth_hat.jpg',
    'description': 'Эта шапка поможет вам не только выглядить стильно, но и не даст вашим мыслям уйти раньше времени'},
    {'title': 'Майка котопровидца',
    'style': 'goth',
    'size': ['m', 'l', 'xl'],
    'src': 'static/goth_tshirt.jpg',
    'description': 'С этой майкой вы успеете познать все тайны великой Вселенной'},
    {'title': 'Перчатки-котятки',
    'style': 'dream',
    'size': ['xs', 's', 'm', 'l', 'xl'],
    'src': 'static/dream_gloves.jpg',
    'description': 'Разноцветные перчатки не только согреют ваши руки, но и поднимут настроение'},
    {'title': 'Гипнофутболка',
    'style': 'dream',
    'size': ['s', 'm', 'l'],
    'src': 'static/dream_thsirt.jpg',
    'description': 'После того, как вы наденете эту футболку, окружающие точно не смогут оторвать от вас взляда'},
    {'title': 'Тигровые джинсы',
    'style': 'casual',
    'size': ['xs', 's'],
    'src': 'static/casual_jeans.jpg',
    'description': 'Не бойтесь, тигр на них не настоящий. Но выглядеть с ним вы будете просто устрашающе круто!'},
    {'title': 'Кошка-шарфошка',
    'style': 'casual',
    'size': ['xs', 's', 'm', 'l', 'xl'],
    'src': 'static/casual_scarf.jpg',
    'description': 'Эта кошка точно защитит вашу шею от холода и болезней'},
    {'title': 'Футболка с котятами',
    'style': 'casual',
    'size': ['s', 'm', 'l'],
    'src': 'static/casual_tshirt.jpg',
    'description': 'Кошка с котятами среди ярких звёзд точно даст вам ощущеия единения с этой вселенной'}    
]

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
                favSizes = ['0', '1', '2', '3', '4']
            favSizesName = []
            for i in favSizes:
                favSizesName.append(sizes[int(i)][1])

            response = render(request, 'store_page.html', context = {'clothes': clothes})
            #HttpResponse(f"<p>Привет, {name}!</p> <p>Тема твоего сайта: {themes[int(themeColor)][1]}. Твои любимые стили: {favStylesName}</p>")
            response.set_cookie("name", name)
            response.set_cookie("themeColor", themeColor)
            response.set_cookie("favStyles", favStylesName)
            response.set_cookie("favSizes", favSizesName)

            return response
            
    else:
        form = UserForm()

    return render(request, 'store_form.html', {'form': form})        

def homePage(request):
    return render(request, 'store_page.html')