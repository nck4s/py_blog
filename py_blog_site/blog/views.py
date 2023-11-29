from django.shortcuts import render



posts = [
    {
        'author': 'Администратор',
        'title': 'Новость 1',
        'content': 'Текст новости 1',
        'date_posted': '01.01.2023'
    },
    {
        'author': 'Пользователь',
        'title': 'Новость 2',
        'content': 'Текст новости 2',
        'date_posted': '02.01.2023'
    }
]
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'О блоге'})
