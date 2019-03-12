#-*- coding: utf-8 -*-
"""

.. moduleauthor:: Martí Congost <marti.congost@whads.com>
"""
from cocktail.events import when
from cocktail.translations import translations
from woost.admin.sections import Settings
from woost.admin.sections.contentsection import ContentSection

translations.load_bundle("woost.extensions.nocaptcha.admin.sections")


class NoCaptchaSection(Settings):

    icon_uri = "woost.extensions.nocaptcha.admin.ui://images/nocaptcha.svg"

    members = [
        "x_nocaptcha_public_key",
        "x_nocaptcha_private_key",
    ]


@when(ContentSection.declared)
def fill(e):
    e.source.append(NoCaptchaSection("nocaptcha"))

