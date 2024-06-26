from django.contrib import admin

from users.models import User, Payment

admin.site.register(User)


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('user', 'payment_date', 'paid_course', 'paid_lesson', 'amount', 'payment_mode')
    list_filter = ('user',)
    search_fields = ('user',)
