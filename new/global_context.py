from .models import NewImagePost, Category, Status


def get_base(request):
    try:
        image_list = NewImagePost.objects.filter(status=Status.Published)[:6]
        first = NewImagePost.objects.filter(status=Status.Published).first()
        category_list = Category.objects.all()
    except:
        image_list = ['']
        category_list = ['']
        first = ['']
    context = {
        'object_list': image_list,
        'category_list': category_list,
        'first': first,
    }
    return context
