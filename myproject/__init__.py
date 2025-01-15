from __future__ import absolute_import, unicode_literals

# اطمینان حاصل می‌کنیم که Celery در هنگام شروع پروژه بارگذاری بشه
from .celery import app as celery_app

__all__ = ('celery_app',)
