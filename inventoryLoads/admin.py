from django.contrib import admin
from inventoryLoads.models import Provider, InventoryLoad, InventoryLoadDetail
# Register your models here.

admin.site.register(Provider)
admin.site.register(InventoryLoad)
admin.site.register(InventoryLoadDetail)