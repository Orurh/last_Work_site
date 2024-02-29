from django import forms
from members.models import Positions, Duties, Member
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.core.exceptions import ValidationError


class AddPostForm(forms.ModelForm):
    pos = forms.ModelChoiceField(queryset=Positions.objects.all(), label='Категория', required=False,
                                     empty_label='Категория не выбрана')
    duties = forms.ModelChoiceField(queryset=Duties.objects.all(), label='Категория по сменам', required=False,
                                        empty_label='Категория не выбрана')
    class Meta:
        model = Member
        fields = ['name', 'photo', 'rank', 'position', 'reference', 'is_public', 'pos', 'duties', 'tags']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input'}),
            'reference': forms.Textarea(attrs={'cols': 40, 'rows': 4}),
        }
        labels = {
            'reference':'Краткая справка'
        }

    def clean_name(self):
        name = self.cleaned_data['name']
        ALLOWED_CHARS = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯабвгдеёжзийклмнопрстуфхцчшщьыъэюя0123456789- '
        if not set(name) <= set(ALLOWED_CHARS):
            raise ValidationError('Только русишь языкешь')

        return name


class UploadFileForm(forms.Form):
    file = forms.ImageField(label='Файл')


# class AddPostForm(forms.Form):
#     name = forms.CharField(max_length=255, min_length=5, label='Ф.И.О.', help_text='Вспомогательный текст',
#                            widget=forms.TextInput(attrs={'class': 'form-input'}),
#                            error_messages={
#                                'required': 'Без заголовка незя',
#                                'min_length': 'Минимум 5 символов',
#                            })
#     slug = forms.SlugField(max_length=255, label='URL',
#                            validators=[
#                                MinLengthValidator(5, message='Минимум 5 символов'),
#                                MaxLengthValidator(100)
#                            ]
#                            )
#     rank = forms.CharField(max_length=255, label='Звание')
#     position = forms.CharField(max_length=255, label='Должность')
#     reference = forms.CharField(widget=forms.Textarea(), label='Справка-отзыв')
#     is_public = forms.BooleanField(required=False, label='Статус')
#     pos = forms.ModelChoiceField(queryset=Positions.objects.all(), label='Категория', required=False,
#                                  empty_label='Категория не выбрана')
#     duties = forms.ModelChoiceField(queryset=Duties.objects.all(), label='Категория по сменам', required=False,
#                                     empty_label='Категория не выбрана')
#
#     def clean_name(self):
#         name = self.cleaned_data['name']
#         ALLOWED_CHARS = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯабвгдеёжзийклмнопрстуфхцчшщьыъэюя0123456789- '
#         if not set(name) <= set(ALLOWED_CHARS):
#             raise ValidationError('Только русишь языкешь')