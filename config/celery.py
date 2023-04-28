import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "drug_store.settings")

app = Celery("drug_store")
app.config_from_object("django.conf:settings", namespace="CELERY")
# namespace for preventing overlap with settings variable and config celery settings with CELERY_ prefixe
app.autodiscover_tasks()  # look for celery tasks from apps installed in settings
# automatically discovers tasks.py files in apps


@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")