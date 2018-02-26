from django.views.generic import TemplateView
from edc_base.view_mixins import EdcBaseViewMixin
from edc_navbar import NavbarViewMixin
from edc_base.view_mixins import AdministrationViewMixin


# from django.contrib.auth.decorators import login_required
# from django.utils.decorators import method_decorator
# from django.views.generic import TemplateView
#
# from edc_base.view_mixins import EdcBaseViewMixin


class AdministrationView(EdcBaseViewMixin, NavbarViewMixin,
                         AdministrationViewMixin, TemplateView):

    #     template_name = 'cancer/administration.html'
    #     app_config_name = 'cancer'
    #
    #     @method_decorator(login_required)
    #     def dispatch(self, *args, **kwargs):
    #         return super().dispatch(*args, **kwargs)
    #
    #     def get_context_data(self, **kwargs):
    #         context = super().get_context_data(**kwargs)
    #         context.update(navbar_item_selected='administration')
    #         return context

    navbar_name = 'cancer'
    navbar_selected_item = 'administration'
