from django.urls import reverse_lazy
from django.views.generic import CreateView

from app.models import Book


class Main(CreateView):
    model = Book
    fields = ('name',)
    success_url = reverse_lazy('main')
    template_name = 'main.html'

    def get_context_data(self, **kwargs):
        context = super(Main, self).get_context_data(**kwargs)
        context['books'] = Book.objects.all()
        return context
