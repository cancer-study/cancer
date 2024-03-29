from django.conf import settings
from edc_lab_dashboard.dashboard_urls import dashboard_urls as lab_dashboard_urls
from edc_navbar import NavbarItem, site_navbars, Navbar


cancer = Navbar(name='cancer')


cancer.append_item(
    NavbarItem(
        name='consented_subject',
        label='Subjects',
        fa_icon='far fa-user-circle',
        url_name=settings.DASHBOARD_URL_NAMES.get('subject_listboard_url')))

cancer.append_item(
    NavbarItem(
        name='lab',
        label='Specimens',
        fa_icon='fa-flask',
        url_name=lab_dashboard_urls.get('requisition_listboard_url')))

site_navbars.register(cancer)
