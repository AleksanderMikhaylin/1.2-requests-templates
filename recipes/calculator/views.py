from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }

def home_view(request):
    template_name = 'calculator/home.html'

    if not request.GET.get('item') == None:
        return item_view(request)

    pages = {}
    for item in DATA:
        pages.setdefault(item, item)

    context = {
        'pages': pages
    }
    return render(request, template_name, context)

def item_view(request):
    template_name = 'calculator/index.html'

    items = DATA.get(request.GET.get('item'))
    if items == None:
        return error_view(request)

    qty_str = request.GET.get('qty', '1')

    qty = 1
    if qty_str.isnumeric():
        qty = int(qty_str)

    recipe = {}
    for item in items.items():
        recipe[item[0]] = round(item[1] * qty, 2)

    context = {
        'item': request.GET.get('item'),
        'portion': qty,
        'qty': [a for a in range(1, 11)],
        'recipe': recipe
    }
    return render(request, template_name, context)

def error_view(request):
    template_name = 'calculator/error.html'
    return render(request, template_name)