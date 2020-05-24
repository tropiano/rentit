from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.base import TemplateView
# Import Models and Forms
from .models import House, HouseFilter
from .forms import CityForm

# Create your views here.


def house_list(request):
    f = HouseFilter(request.GET, queryset=House.objects.all())
    return render(request, 'rent/index.html', {'filter': f})


"""class HomeView(TemplateView, generic.FormView):

    template_name = 'rent/index.html'
    success_url = reverse_lazy('rent:index')
    form_class = CityForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['houses'] = House.objects.filter
        return context

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        city = form['city'].value()

        return super().form_valid(form)
"""
