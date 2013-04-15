"""Implementation of the ``md-urlunshorten-users`` widget."""
import json

from django.utils.timezone import now

import requests

from metrics_dashboard.messenger import broadcast_channel
from metrics_dashboard.widget_base import DashboardWidgetBase
from metrics_dashboard.widget_pool import dashboard_widget_pool

from .models import UserCount


class UrlunshortenUsers(DashboardWidgetBase):
    """Displays a graph of the user count of urlunshorten.com."""
    template_name = 'md_urlunshorten_users/urlunshorten_users.html'

    sizex = 1
    sizey = 1

    update_interval = 10800

    def get_context_data(self):
        ctx = super(UrlunshortenUsers, self).get_context_data()
        try:
            user_count = UserCount.objects.all().order_by(
                'creation_date')[0].value
        except IndexError:
            user_count = "n/a"
        ctx.update({
            'user_count': user_count,
        })
        return ctx

    def update_widget_data(self):
        resp = requests.get('https://urlunshorten.com/api/v1/users/count/',
            verify=False)
        user_count = UserCount()
        user_count.creation_date = now()
        user_count.value = int(json.loads(resp.content))
        user_count.save()
        broadcast_channel(self.get_name(), 'update')


dashboard_widget_pool.register_widget(UrlunshortenUsers)
