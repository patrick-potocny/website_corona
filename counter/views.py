from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from counter.forms import SubscriberForm
from counter.models import Subscriber

from counter import w_scrape_script



class HomePage(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['tested'] = w_scrape_script.tested
        context['confirmed'] = w_scrape_script.confirmed
        context['confirmed_today'] = w_scrape_script.confirmed_today
        context['deaths'] = w_scrape_script.deaths
        context['cured'] = w_scrape_script.cured
        return context


class SignUp(CreateView):
    model = Subscriber
    fields = ('name', 'email')
    template_name = 'accounts/signup.html'
    success_url = 'thanks/'


class ThanksPage(TemplateView):
    template_name = 'accounts/thanks.html'

