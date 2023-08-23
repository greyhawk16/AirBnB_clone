from django.contrib import admin
from .models import Room, Amenity

# Register your models here.


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
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
