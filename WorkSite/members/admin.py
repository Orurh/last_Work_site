from django.contrib import admin, messages
from django.utils.safestring import mark_safe
from members.models import Member, Positions


class DutiesFilter(admin.SimpleListFilter): # создаем свой фильтр
    title = 'Статус'
    parameter_name = 'status'

    def lookups(self, request, model_admin):
        return [
            ('used', 'На исполнении'),
            ('unused', 'Вакант'),
        ]

    def queryset(self, request, queryset):
        if self.value() == 'used':
            return queryset.filter(duties__isnull=False)
        elif self.value() == 'unused':
            return queryset.filter(duties__isnull=True)


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    # fields = ['name', 'rank', 'position', 'is_public'] # отображаемые поля в окне редактирования
    # exclude = [ 'position', 'is_public'] # запрет на отображение полей в окне редактирования
    readonly_fields = ['post_photo'] # список полей отображаемых но запрещенных к редактированию в окне редактирования
    filter_horizontal = ['tags']
    list_display = (
        'name', 'rank', 'position',  'post_photo', 'is_public', 'time_created', 'time_updated', 'pos',)  # отображение полей
    list_display_links = ('name', 'rank', 'position')  # выбор кликабельных полей
    list_editable = ('is_public', 'pos',)
    ordering = ['id']
    list_per_page = 5
    actions = ['set_published', 'set_chernovik']
    search_fields = ['name__iregex', 'pos__title']
    list_filter = [DutiesFilter, 'pos__title', 'is_public']
    save_on_top = True #дополнительно отображение поля сохранения сверху





    @admin.display(description='Изображение', ordering='id')  # декоратор, меняем название заголовка
    def post_photo(self, member: Member):  # добавляем столбец/поле в таблицу
        if member.photo:
            return mark_safe(f'<img src="{member.photo.url}" width = 50')
        return 'Без фото'

    @admin.action(description='Опубликовать')  # декоратор, меняем название дополнительного действия
    def set_published(self, request, queryset):
        count = queryset.update(is_public=Member.Status.PUBLIC)
        self.message_user(request, f'Изменено {count} записей')

    @admin.action(description='Снять с публикации')
    def set_chernovik(self, request, queryset):
        count = queryset.update(is_public=Member.Status.CHERNOVIK)
        self.message_user(request, f'Снято с публикации {count} записей',
                          messages.WARNING)  # warning - изменение сообщения


@admin.register(Positions)
class PositionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug')
