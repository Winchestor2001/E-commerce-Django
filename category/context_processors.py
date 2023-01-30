from .models import Category

def menu_lists(request):
    links = Category.objects.all()
    return dict(links=links) 