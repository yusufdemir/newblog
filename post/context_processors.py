from post.models import Category
def categories(request):
    cat = Category.objects.all()
    return {'cat': cat}