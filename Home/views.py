from django.views.generic import TemplateView

from Us.models import Customer, TeamMember, WhatDoCustomersEarn, ModasOperandi


class HomeView(TemplateView):
    template_name = 'Home/index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)

        customers = Customer.objects.all()
        team_members = TeamMember.objects.all()
        what_do_customers_earn = WhatDoCustomersEarn.objects.all()
        modas_operandies = ModasOperandi.objects.all()

        context['customers'] = customers
        context['team_members'] = team_members
        context['what_do_customers_earn'] = what_do_customers_earn
        context['modas_operandies'] = modas_operandies

        return context
