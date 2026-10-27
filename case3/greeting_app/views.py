from django.shortcuts import render
from .forms import VisitorForm
from .models import Visitor

def index(request):
    greeting_name = None

    if request.method == 'POST':
        form = VisitorForm(request.POST)
        if form.is_valid():
            visitor = form.save()
            greeting_name = visitor.name
            form = VisitorForm()  # очищаем поле после успешной отправки
    else:
        form = VisitorForm()

    recent_visitors = Visitor.objects.all()[:5]

    context = {
        'form': form,
        'greeting_name': greeting_name,
        'recent_visitors': recent_visitors,
    }
    return render(request, 'greeting_app/index.html', context)