import json

from django.test import TestCase

import pytest

from metaset import MetaSet

from .django_test_app import forms as test_forms
from .django_test_app import models as test_models


# the refresh_from_db method only came in with 1.8, use our own.
def refresh_from_db(obj):
    return obj.__class__.objects.get(id=obj.id)


class DjangoTest(TestCase):
    def test_save_load(self):
        obj = test_models.TestModel.objects.create(value={"a": {1}, "b": {2, 3}})
        obj.full_clean()
        obj = refresh_from_db(obj)
        assert type(obj.value) == MetaSet, type(obj.value)
        assert obj.value == MetaSet({"a": {1}, "b": {2, 3}}), obj.value

    def test_model_form(self):
        obj = test_models.TestModel.objects.create(value={"a": {1}, "b": {2, 3}})
        form = test_forms.TestModelForm(instance=obj)
        assert json.loads(form["value"].value()) == {"a": [1], "b": [2, 3]}

    def test_query(self):
        try:
            from django.contrib.postgres.fields import JSONField  # noqa: F401
        except ImportError:
            pytest.skip(
                "JSON queries are only available " "for native Django (>=1.9) JSONField"
            )

        obj = test_models.TestModel.objects.create(value={"a": {1}, "b": {2, 3}})
        res = test_models.TestModel.objects.filter(value__b__contains=[2])
        assert obj == res.first(), res
        res = test_models.TestModel.objects.filter(value__has_key="a")
        assert obj == res.first(), res

    def test_inception(self):
        obj = test_models.TestModel.objects.create(
            value={"a": {"b": {1}, "c": {2, 3}}, "d": {"e": {4}}}
        )
        obj = refresh_from_db(obj)
        assert obj.value == MetaSet(a=MetaSet(b={1}, c={2, 3}), d=MetaSet(e={4}))
        assert type(obj.value["a"]) == MetaSet, type(obj.value["a"])
