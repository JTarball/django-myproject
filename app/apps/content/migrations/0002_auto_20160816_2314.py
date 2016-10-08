# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


def load_stores_from_fixture(apps, schema_editor):
    from django.core.management import call_command
    call_command("loaddata", "apps/content/fixtures/initial_data.json")


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_stores_from_fixture),
    ]
