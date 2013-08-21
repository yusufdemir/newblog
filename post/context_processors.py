from post.models import Categories
def categories(request):
    cat = Categories.objects.all()
    return {'cat': cat}