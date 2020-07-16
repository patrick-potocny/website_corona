from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from counter.forms import SubscriberForm
from counter.models import Subscriber

# BS4 web scrraping imports
from bs4 import BeautifulSoup
import requests
import re


class HomePage(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Webscrape script
        source = requests.get('https://korona.gov.sk/').text
        soup = BeautifulSoup(source, 'lxml')
        info_block = soup.find('div', id='block_5e9990d35fffd')
        numbers = [x.text for x in info_block.find_all('h2', class_='govuk-heading-l govuk-!-margin-bottom-3')]
        confirmed_today = soup.find_all('div', class_='govuk-!-margin-bottom-6 app-pane-gray govuk-!-padding-top-4 govuk-!-padding-bottom-2 govuk-!-padding-right-4 govuk-!-padding-left-4')
        confirmed_today = [x.text for x in confirmed_today]
        confirmed_today = confirmed_today[1]
        confirmed_today = (re.findall('\d+', confirmed_today ))
        # Wecsrape script
        context['tested'] = numbers[0]
        context['confirmed'] = numbers[1]
        context['confirmed_today'] = confirmed_today[2]
        context['deaths'] = numbers[2]
        context['cured'] = numbers[3]
        return context


class SignUp(CreateView):
    model = Subscriber
    fields = ('name', 'email')
    template_name = 'accounts/signup.html'
    success_url = 'thanks/'


class ThanksPage(TemplateView):
    template_name = 'accounts/thanks.html'

