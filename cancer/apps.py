from datetime import datetime

from dateutil.relativedelta import MO, TU, WE, TH, FR, SA, SU
from dateutil.tz import gettz
from django.apps import AppConfig as DjangoAppConfig
from django.apps import apps as django_apps
from django.core.checks import register
from django.core.management.color import color_style
from django.db.models.signals import post_migrate
from edc_appointment.appointment_config import AppointmentConfig
from edc_appointment.apps import AppConfig as BaseEdcAppointmentAppConfig
from edc_appointment.constants import COMPLETE_APPT
from edc_base.apps import AppConfig as BaseEdcBaseAppConfig
from edc_constants.constants import FAILED_ELIGIBILITY
from edc_data_manager.apps import AppConfig as BaseEdcDataManagerAppConfig
from edc_device.apps import AppConfig as BaseEdcDeviceAppConfig
from edc_device.constants import CENTRAL_SERVER
from edc_facility.apps import AppConfig as BaseEdcFacilityAppConfig
from edc_identifier.apps import AppConfig as BaseEdcIdentifierAppConfig
from edc_lab.apps import AppConfig as BaseEdcLabAppConfig
from edc_locator.apps import AppConfig as BaseEdcLocatorAppConfig
from edc_metadata.apps import AppConfig as BaseEdcMetadataAppConfig
from edc_protocol.apps import AppConfig as BaseEdcProtocolAppConfig
from edc_timepoint.apps import AppConfig as BaseEdcTimepointAppConfig
from edc_timepoint.timepoint import Timepoint
from edc_timepoint.timepoint_collection import TimepointCollection
from edc_visit_tracking.apps import AppConfig as BaseEdcVisitTrackingAppConfig
from edc_visit_tracking.constants import SCHEDULED, UNSCHEDULED, LOST_VISIT
from cancer_dashboard.patterns import subject_identifier

from .sites import cancer_sites, fqdn
from .system_checks import cancer_check


style = color_style()


def post_migrate_update_sites(sender=None, **kwargs):
    from edc_base.sites.utils import add_or_update_django_sites
    add_or_update_django_sites(
        apps=django_apps, sites=cancer_sites, fqdn=fqdn)


class AppConfig(DjangoAppConfig):
    name = 'cancer'

    def ready(self):
        register(cancer_check)
        post_migrate.connect(post_migrate_update_sites, sender=self)


class EdcProtocolAppConfig(BaseEdcProtocolAppConfig):
    protocol = 'BHP045'
    protocol_name = 'Cancer'
    protocol_number = '045'
    protocol_title = ''
    study_open_datetime = datetime(
        2010, 5, 2, 0, 0, 0, tzinfo=gettz('UTC'))
    study_close_datetime = datetime(
        2021, 12, 31, 23, 59, 59, tzinfo=gettz('UTC'))


class EdcLabAppConfig(BaseEdcLabAppConfig):
    requisition_model = 'cancer_subject.subjectrequisition'
    result_model = 'edc_lab.result'


class EdcBaseAppConfig(BaseEdcBaseAppConfig):
    project_name = 'Cancer'
    institution = 'Botswana-Harvard AIDS Institute'


class EdcDeviceAppConfig(BaseEdcDeviceAppConfig):
    device_role = CENTRAL_SERVER
    device_id = '99'


class EdcVisitTrackingAppConfig(BaseEdcVisitTrackingAppConfig):
    report_datetime_allowance = -1
    visit_models = {
        'cancer_subject': ('subject_visit', 'cancer_subject.subjectvisit')}


class EdcIdentifierAppConfig(BaseEdcIdentifierAppConfig):
    identifier_prefix = '045'


class EdcMetadataAppConfig(BaseEdcMetadataAppConfig):

    reason_field = {'cancer_subject.subjectvisit': 'reason'}
    other_visit_reasons = [
        'off study', 'deferred', 'Lost to follow-up', 'Death',
        'Missed quarterly visit']
    other_create_visit_reasons = [
        'Quarterly visit/contact', 'Unscheduled visit/contact']
    create_on_reasons = [SCHEDULED, UNSCHEDULED] + other_create_visit_reasons
    delete_on_reasons = [LOST_VISIT, FAILED_ELIGIBILITY] + other_visit_reasons


class EdcAppointmentAppConfig(BaseEdcAppointmentAppConfig):
    configurations = [
        AppointmentConfig(
            model='cancer_subject.appointment',
            related_visit_model='cancer_subject.subjectvisit',
            appt_type='hospital')]


class EdcFacilityAppConfig(BaseEdcFacilityAppConfig):
    country = 'botswana'
    definitions = {
        '5-day clinic': dict(days=[MO, TU, WE, TH, FR],
                             slots=[100, 100, 100, 100, 100])}


class EdcLocatorAppConfig(BaseEdcLocatorAppConfig):
    name = 'edc_locator'
    reference_model = 'cancer_subject.subjectlocator'


class EdcTimepointAppConfig(BaseEdcTimepointAppConfig):

    timepoints = TimepointCollection(
        timepoints=[
            Timepoint(
                model='cancer_subject.appointment',
                datetime_field='appt_datetime',
                status_field='appt_status',
                closed_status=COMPLETE_APPT),
            Timepoint(
                model='cancer_subject.historicalappointment',
                datetime_field='appt_datetime',
                status_field='appt_status',
                closed_status=COMPLETE_APPT)
        ])


class EdcDataManagerAppConfig(BaseEdcDataManagerAppConfig):
    identifier_pattern = subject_identifier
    extra_assignee_choices = {
        'td_clinic': [
                ('cancer_clinic', 'Cancer Clinic'),
                ['inkele@bhp.org.bw', 'ojohn@bhp.org.bw', 'scott_peterson@post.harvard.edu']],
            'td_ras': [
                ('cancer_ras', 'Cancer RAs'),
                ['gmotswetla@bhp.org.bw', 'bmotladiile@bhp.org.bw']],
            'se_dmc': [
                ('se_dmc', 'SE & DMC'),
                ['adiphoko@bhp.org.bw', 'ckgathi@bhp.org.bw', 'imosweu@bhp.org.bw']]
    }
