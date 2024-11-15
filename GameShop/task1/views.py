from django.shortcuts import render
from task1.models import Buyer, Game


def main_page(request):
    return render(request, 'main_page.html')


def shop(request):
    Games = Game.objects.all()
    games = []
    for i in Games:
        games.append(f"{i.title} | {i.description} Стоимость: {i.cost}")
    buy = 'Купить билет'
    context = {'games': games,
               'buy': buy}
    return render(request, 'shop.html', context)


def basket(request):
    return render(request, 'basket.html')


def sign_up(request):
    Buyers = Buyer.objects.all()
    buyers = []
    info = {}
    name = None
    balance = 10000
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        for i in Buyers:
            buyers.append(i.name)
        if name in buyers:
                info['error'] = 'Пользователь уже существует'
        elif int(age) < 18:
                info['error'] = 'Вы должны быть старше 18'

        if not info:
            Buyer.objects.create(name=name, balance=balance, age=age)

    context = {'error': info, 'welcome': f'Приветствуем, {name}!', 'name': name,
               'error_message': info.get('error')}
    return render(request, 'registration_page.html', context)