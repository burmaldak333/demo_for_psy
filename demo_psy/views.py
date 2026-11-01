from django.shortcuts import render
from .models import Psychologist, Service, Package


def index(request):
    # Берем первого психолога из базы (Ирину)
    shop = Psychologist.objects.first()

    # Если база пустая, выводим заглушку (чтобы сайт не упал)
    if not shop:
        return render(request, 'demo_psy/index.html', {'shop': None})

    services = Service.objects.all()
    packages = Package.objects.all()

    context = {
        'shop': shop,
        'services': services,
        'packages': packages,
    }
    return render(request, 'demo_psy/index.html', context)