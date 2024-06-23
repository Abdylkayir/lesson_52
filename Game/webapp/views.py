from django.shortcuts import render

def index(request):
    print(request.GET.getlist('my_params'))
    context = {
        "name": "Abdy",
        "age": 32
    }
    return render(request, 'index.html', context=context)


def create_article(request):
    if request.method == 'GET':
        return render(request, "create_article.html")
    else:
        print(request.POST)