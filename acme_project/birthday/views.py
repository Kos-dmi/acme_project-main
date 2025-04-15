from .forms import BirthdayForm
from .models import Birthday
from .utils import calculate_birthday_countdown
from django.views.generic import (
    CreateView, DeleteView, DetailView, ListView, UpdateView
)
from django.urls import reverse_lazy


class BirthdayListView(ListView):
    model = Birthday
    ordering = 'id'
    paginate_by = 10


class BirthdayCreateView(CreateView):
    form_class = BirthdayForm
    success_url = reverse_lazy('birthday:list')


class BirthdayUpdateView(UpdateView):
    form_class = BirthdayForm
    success_url = reverse_lazy('birthday:list')


class BirthdayDeleteView(DeleteView):
    form_class = BirthdayForm
    success_url = reverse_lazy('birthday:list')


class BirthdayDetailView(DetailView):
    model = Birthday

    def get_context_data(self, **kwargs):
        # Получаем словарь контекста:
        context = super().get_context_data(**kwargs)
        # Добавляем в словарь новый ключ:
        context['birthday_countdown'] = calculate_birthday_countdown(
            # Дату рождения берём из объекта в словаре context:
            self.object.birthday
        )
        # Возвращаем словарь контекста.
        return context
