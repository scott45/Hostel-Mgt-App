from django.contrib import admin
from .models import Classification, List, Student, Room, Booking, MobilePayment
from Gyobera.models import UserProfile

admin.autodiscover()


class ClassificationAdmin(admin.ModelAdmin):
    list_display = ('name', 'views', 'likes')
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Classification, ClassificationAdmin)


class ListAdmin(admin.ModelAdmin):
    list_display = ('title', 'classification', 'url')


admin.site.register(List, ListAdmin)


class StudentAdmin(admin.ModelAdmin):
    list_display = ('Names', 'Sex', 'Registration_Number')


admin.site.register(Student, StudentAdmin)


class RoomAdmin(admin.ModelAdmin):
    list_display = ('Hostel', 'Room_Number')


admin.site.register(Room, RoomAdmin)


class BookingAdmin(admin.ModelAdmin):
    list_display = ('Room_Number', 'Booked_by', 'Booked_on')


admin.site.register(Booking, BookingAdmin)


class MobilePaymentAdmin(admin.ModelAdmin):
    list_display = ('Booked_by', 'Hostel', 'Amount_deposited', 'Mobile_No')


admin.site.register(MobilePayment, MobilePaymentAdmin)

admin.site.register(UserProfile)
