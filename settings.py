# -*- coding: utf-8 -*-

INSTALLED_ADDONS = [
    # <INSTALLED_ADDONS>  # Warning: text inside the INSTALLED_ADDONS tags is auto-generated. Manual changes will be overwritten.
    'aldryn-addons',
    'aldryn-django',
    'aldryn-sso',
    'aldryn-django-cms',
    'aldryn-devsync',
    'djangocms-file',
    'djangocms-googlemap',
    'djangocms-history',
    'djangocms-link',
    'djangocms-modules',
    'djangocms-picture',
    'djangocms-snippet',
    'djangocms-style',
    'djangocms-text-ckeditor',
    'djangocms-transfer',
    'djangocms-video',
    'django-filer',
    # </INSTALLED_ADDONS>
    # 'djangocms-icon'
]

import aldryn_addons.settings
aldryn_addons.settings.load(locals())


# all django settings can be altered here

INSTALLED_APPS.extend([
    'djangocms_icon',
    'djangocms_bootstrap4',
    "djangocms_bootstrap4.contrib.bootstrap4_alerts",
    "djangocms_bootstrap4.contrib.bootstrap4_badge",
    "djangocms_bootstrap4.contrib.bootstrap4_card",
    "djangocms_bootstrap4.contrib.bootstrap4_carousel",
    "djangocms_bootstrap4.contrib.bootstrap4_collapse",
    "djangocms_bootstrap4.contrib.bootstrap4_grid",
    "djangocms_bootstrap4.contrib.bootstrap4_jumbotron",
    "djangocms_bootstrap4.contrib.bootstrap4_link",
    "djangocms_bootstrap4.contrib.bootstrap4_listgroup",
    "djangocms_bootstrap4.contrib.bootstrap4_media",
    "djangocms_bootstrap4.contrib.bootstrap4_picture",
    "djangocms_bootstrap4.contrib.bootstrap4_tabs",
    "djangocms_bootstrap4.contrib.bootstrap4_utilities",
    "djangocms_bootstrap4.contrib.bootstrap4_content"

])
