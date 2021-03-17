from django.contrib import admin

# Register your models here.
from projects.models import ElementType, Element, Food, Amount

admin.site.register(ElementType)
admin.site.register(Element)
admin.site.register(Food)
admin.site.register(Amount)
