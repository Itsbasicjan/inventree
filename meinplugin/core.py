from django.urls import path
from django.utils.translation import gettext_lazy as _
from plugin import InvenTreePlugin
from plugin.mixins import NavigationMixin, SettingsMixin, UrlsMixin
from . import views

class meinplugin(UrlsMixin, SettingsMixin, NavigationMixin, InvenTreePlugin):
    NAME = "meinplugin"
    SLUG = "meinplugin"
    TITLE = "Bestandszuweisungen"
    DESCRIPTION = "Verwaltung von Kunden-Bestandszuweisungen mit Zeitfenstern"
    VERSION = "0.1.0"

    NAVIGATION_TAB_NAME = "Bestandszuweisungen"
    NAVIGATION_TAB_ICON = "fas fa-calendar-alt"

    NAVIGATION = [
        {
            'name': _("Zuweisungsliste"),
            'link': 'plugin:meinplugin:allocations_list',
            'icon': 'fas fa-list',
            'permission': 'meinplugin.view_customerallocation'
        },
        {
            'name': _("Neue Zuweisung"),
            'link': 'plugin:meinplugin:allocations_create',
            'icon': 'fas fa-plus-circle',
            'permission': 'meinplugin.add_customerallocation'
        }
    ]

    SETTINGS = {
        'DEFAULT_DAYS': {
            'name': _("Standardzeitraum"),
            'description': _("Voreingestellte Dauer in Tagen"),
            'default': 7,
            'validator': int
        }
    }

    def setup_urls(self):
        return [
            path('allocations/', views.AllocationListView.as_view(), name='allocations_list'),
            path('allocations/new/', views.AllocationCreateView.as_view(), name='allocations_create'),
        ]