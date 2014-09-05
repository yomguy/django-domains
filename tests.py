#!/usr/bin/env python
# coding: utf-8

from django.conf import settings
from django import get_version
import sys
import os


sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))


settings.configure(
    DEBUG=False,
    ROOT_URLCONF='domains.tests.urls',
    INSTALLED_APPS=(
        'django.contrib.sessions',
        'django.contrib.sites',
        'domains',
    ),
    MIDDLEWARE_CLASSES=(
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        'domains.middleware.RequestMiddleware',
        'domains.middleware.DynamicSiteMiddleware',
    ),
    TEMPLATE_LOADERS=(
        'domains.loaders.filesystem.Loader',
        'domains.loaders.app_directories.Loader',
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    ),
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': ':MEMORY:'
        }
    })


def main():
    from django.test.utils import get_runner
    import django

    if hasattr(django, 'setup'):
        django.setup()

    find_pattern = 'domains'

    if get_version() >= '1.6':
        find_pattern += '.tests'

    test_runner = get_runner(settings)(verbosity=2, interactive=True)
    failed = test_runner.run_tests([find_pattern])
    sys.exit(failed)


if __name__ == '__main__':
    main()