from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'common/home-page.html'


class ThanksPageView(TemplateView):
    template_name = 'common/thanks-page.html'
