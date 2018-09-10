# -*- coding: utf-8 -*-
from django.forms import ModelForm

from . import models


class TestModelForm(ModelForm):
    class Meta:
        model = models.TestModel
        fields = "__all__"
