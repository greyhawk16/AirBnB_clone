from django.contrib import admin
from .models import Room, Amenity

# Register your models here.


@admin.action(description='Set all prices to zero')
def reset_prices(model_admin, request, rooms):
    for room in rooms.all():
        room.price = 0
        room.save()


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    actions = (reset_prices,)

    list_display = (
        'name',
        'price',
        'kind',
        'total_amenities',
        'rating',
        'owner',
        'created_at',
    )
    list_filter = (
        "country",
        "city",
        "rooms",
        "pet_friendly",
        "kind",
        "amenities",
        'created_at',
        'updated_at',
    )

    search_fields = (
        'name',
        '=price',
        'owner__username',
    )

    # def total_amenities(self, room):
    #     print(room)
    #     return room.amenities.count()


@admin.register(Amenity)
class AmemityAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'created_at',
        'updated_at',
    )
    readonly_fields = (
        'created_at',
        'updated_at',
    )
