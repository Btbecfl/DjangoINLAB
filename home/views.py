from django.shortcuts import render


# Create your views here.
def home(request):
    import random
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    c = a + b
    return render(request, template_name='home/home.html', context={'a': a, 'b': b, 'c': c})