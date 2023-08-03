#  Copyright (c) 2023.
from django import forms

from tinymce.widgets import TinyMCE

from .utils import parse_and_download_images


class TinyMCEWidget(TinyMCE):
    def value_from_datadict(self, data, files, name):
        value = super().value_from_datadict(data, files, name)
        return parse_and_download_images(value)
