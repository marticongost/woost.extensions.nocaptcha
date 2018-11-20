#-*- coding: utf-8 -*-
u"""

.. moduleauthor:: Martí Congost <marti.congost@whads.com>
"""
from cocktail import schema
from cocktail.translations import translations
from woost.models import add_setting, Configuration

translations.load_bundle("woost.extensions.nocaptcha.settings")

add_setting(
    schema.String(
        "x_nocaptcha_public_key",
        text_search = False
    )
)

add_setting(
    schema.String(
        "x_nocaptcha_private_key",
        text_search = False
    )
)

