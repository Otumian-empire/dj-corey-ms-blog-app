from django.shortcuts import render

posts = [
    {
        'author': "Daniel",
        'title': "Who Goes There",
        'date_posted': "2nd December, 2000",
        'content': "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Eligendi ullam ad quaerat rem libero sequi, tenetur velit cumque explicabo magni dolore eum dolores corrupti cupiditate unde omnis illum aliquid possimus?"
    },
    {
        'author': "Michael",
        'title': "What Went There",
        'date_posted': "22nd Match, 2002",
        'content': "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Eligendi ullam ad quaerat rem libero sequi, tenetur velit cumque explicabo magni dolore eum dolores corrupti cupiditate unde omnis illum aliquid possimus?"
    }
]

def home(request):
    context = { "posts": posts }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About Us'})

