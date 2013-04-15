"""Admin classes for the ``md-urlunshorten-users`` app."""
from django.contrib import admin

from .models import UserCount


admin.site.register(UserCount)
