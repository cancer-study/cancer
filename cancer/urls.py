from cancer_subject.admin_site import cancer_subject_admin
from cancer_prn.admin_site import cancer_prn_admin
from django.contrib import admin
from django.urls.conf import path, include
from django.views.generic.base import RedirectView
from django.contrib.auth.views import LogoutView
from edc_action_item.admin_site import edc_action_item_admin
from edc_appointment.admin_site import edc_appointment_admin
from edc_data_manager.admin_site import edc_data_manager_admin
from edc_identifier.admin_site import edc_identifier_admin
from edc_lab.admin_site import edc_lab_admin
from edc_locator.admin_site import edc_locator_admin
from edc_metadata.admin_site import edc_metadata_admin
from edc_reference.admin_site import edc_reference_admin
from edc_registration.admin_site import edc_registration_admin
from edc_sync.admin import edc_sync_admin
from edc_sync_files.admin_site import edc_sync_files_admin
from edc_visit_schedule.admin_site import edc_visit_schedule_admin
from .views import HomeView, AdministrationView
from django.conf import settings

urlpatterns = [
    path('accounts/', include('edc_base.auth.urls')),
    path('admin/', include('edc_base.auth.urls')),
    path('admin/', admin.site.urls),
    path('admin/', edc_appointment_admin.urls),
    path('admin/', cancer_subject_admin.urls),
    path('admin/', edc_lab_admin.urls),
    path('admin/', edc_locator_admin.urls),
    path('admin/', edc_identifier_admin.urls),
    path('admin/', edc_metadata_admin.urls),
    path('admin/', edc_registration_admin.urls),
    path('admin/', edc_reference_admin.urls),
    path('admin/', edc_sync_admin.urls),
    path('admin/', edc_action_item_admin.urls),
    path('admin/', edc_data_manager_admin.urls),
    path('admin/edc_visit_schedule/', edc_visit_schedule_admin.urls),
    path('admin/edc_sync_files/', edc_sync_files_admin.urls),
    path('admin/cancer_prn/', cancer_prn_admin.urls),
    path('administration/', AdministrationView.as_view(),
         name='administration_url'),
    path('admin/cancer_subject/', RedirectView.as_view(url='admin/cancer_subject/'),
         name='subject_models_url'),
    path('cancer_subject/', include('cancer_subject.urls')),
    path('cancer_prn/', include('cancer_prn.urls')),
    path('subject/', include('cancer_dashboard.urls')),
    path('appointment/', include('edc_appointment.urls')),
    path('edc_action_item/', include('edc_action_item.urls')),
    path('edc_base/', include('edc_base.urls')),
    path('edc_consent/', include('edc_consent.urls')),
    path('edc_data_manager/', include('edc_data_manager.urls')),
    path('edc_device/', include('edc_device.urls')),
    path('edc_lab/', include('edc_lab.urls')),
    path('edc_lab_dashboard/', include('edc_lab_dashboard.urls')),
    path('edc_locator/', include('edc_locator.urls')),
    path('edc_label/', include('edc_label.urls')),
    path('edc_metadata/', include('edc_metadata.urls')),
    path('edc_protocol/', include('edc_protocol.urls')),
    path('edc_identifier/', include('edc_identifier.urls')),
    path('edc_reference/', include('edc_reference.urls')),
    path('edc_registration/', include('edc_registration.urls')),
    path('edc_subject_dashboard/', include('edc_subject_dashboard.urls')),
    path('edc_sync/', include('edc_sync.urls')),
    path('edc_sync_files/', include('edc_sync_files.urls')),
    path('edc_visit_schedule/', include('edc_visit_schedule.urls')),
    path('switch_sites/', LogoutView.as_view(next_page=settings.INDEX_PAGE),
         name='switch_sites_url'),
    path('home/', HomeView.as_view(), name='home_url'),
    path('', HomeView.as_view(), name='home_url'),
]
