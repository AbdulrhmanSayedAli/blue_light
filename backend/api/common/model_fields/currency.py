# from django.db import models
# from currency.data import get_primary_currency_id


# class CurrencyField(models.ForeignKey):
#     def __init__(self, *args, **kwargs):
#         kwargs["to"] = "currency.Currency"
#         kwargs.setdefault("on_delete", models.DO_NOTHING)
#         kwargs.setdefault("default", get_primary_currency_id)
#         kwargs.setdefault("related_name", "+")
#         super().__init__(*args, **kwargs)

#     def deconstruct(self):
#         name, path, args, kwargs = super().deconstruct()

#         del kwargs["to"]

#         if kwargs.get("on_delete") == models.DO_NOTHING:
#             kwargs.pop("on_delete")

#         if kwargs.get("default") == get_primary_currency_id:
#             kwargs.pop("default")

#         if kwargs.get("related_name") == "+":
#             kwargs.pop("related_name")

#         return name, path, args, kwargs
