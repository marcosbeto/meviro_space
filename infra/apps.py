from django.apps import AppConfig
from django.contrib.admin.apps import AdminConfig

class InfraAdminConfig(AdminConfig):
    name = 'infra'
    default_site = 'infra.admin.InfraAdminSite'

    