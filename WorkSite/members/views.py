from django.http import HttpResponse, HttpResponseNotFound

from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, FormView, CreateView, UpdateView, DeleteView

from members.forms import AddPostForm, UploadFileForm
from members.models import Member, Positions, TagPost, UploadFiles
import uuid

from members.utils import DataMixin

# Create your views here.


menu = [{'title': 'Служба пожаротушения', 'url_name': 'home'},
        {'title': 'Реагирование подразделений', 'url_name': 'fire_home'},
        {'title': 'Добавить статью', 'url_name': 'addpage'},
        {'title': 'Войти', 'url_name': 'login'},
        {'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Обратная связь', 'url_name': 'contact'},
        ]

categors = [
    {'id': 1, 'name': 'Начальник СПТ'},
    {'id': 2, 'name': 'Начальники дежурных смен'},
    {'id': 3, 'name': 'Диспетчерский состав'},
    {'id': 4, 'name': 'Водительский состав'},
]


# def index(request):
#     mmbrs = Member.published.all().select_related('pos')
#     date = {'title': 'Главная страница',
#             'menu': menu,
#             'mmbrs': mmbrs,
#             'pos_selected': 0,
#             }
#     return render(request, 'members/index.html', date)


class MemberHome(DataMixin, ListView):  # вместо функции index

    # model = Member # для работы ListView необходимо передать модель, но она будет показывать все открытые и закрытые данные
    template_name = 'members/index.html'
    context_object_name = 'mmbrs'
    title_page = 'Главная страница'
    pos_selected = 0


    def get_queryset(self):
        return Member.published.all().select_related('pos')  # передаем определенный сет без Черноваика из модели Member

# class MemberHome(TemplateView):
#     template_name = 'members/index.html'
#     extra_context = {
#         'title': 'Главная страница',
#         'menu': menu,
#         'mmbrs': Member.published.all().select_related('pos'),
#         'pos_selected': 0,
#     }

# def get_context_data(self, **kwargs):
#     context = super().get_context_data(**kwargs)
#     context['pos_selected'] = int(self.request.GET.get('pos_id', 0))
#     return context


# def members(request, post_slug):
#     post = get_object_or_404(Member, slug=post_slug)
#     date = {'title': 'Главная страница',
#             'menu': menu,
#             'post': post,
#             'pos_selected': 1,
#             }
#     return render(request, 'members/member.html', date)

class Members(DataMixin, DetailView):
    template_name = 'members/member.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'


    def get_context_data(self, **kwargs):
        context = super(Members, self).get_context_data(**kwargs)
        return self.get_mixin_context(context, title = context['post'].name)

    def get_object(self):
        return get_object_or_404(Member.published, slug=self.kwargs[self.slug_url_kwarg])


# def categories(request, cat_slug):
#     category = get_object_or_404(Positions, slug=cat_slug)
#     posts = Member.published.filter(pos_id=category.pk).select_related('pos')
#     date = {'title': f'Должность: {category.title}',
#             'menu': menu,
#             'mmbrs': posts,
#             'pos_selected': category.pk,
#             }
#     return render(request, 'members/index.html', date)

class MemberCategory(ListView):
    template_name = 'members/index.html'
    context_object_name = 'mmbrs'
    allow_empty = False  # генерирует 404 при пустом списке

    def get_queryset(self):
        return Member.published.filter(pos__slug=self.kwargs['cat_slug']).select_related('pos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cat = context['mmbrs'][0].pos
        context['title'] = 'Должность - ' + cat.title
        context['menu'] = menu
        context['pos_selected'] = cat.pk
        return context


# def handle_uploaded_file(f):
#     sec_name = str(uuid.uuid4())
#     first_name, exstension = f.name
#     with open(f"uploads/{f.name}_{sec_name}.{exstension}", "wb+") as destination:
#         for chunk in f.chunks():
#             destination.write(chunk)

# в def about(request):
# if form.is_valid():
# handle_uploaded_file(form.cleaned_data['file'])  # <p><input type="file" name="file_upload"></p>

def about(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # handle_uploaded_file(form.cleaned_data['file'])  # <p><input type="file" name="file_upload"></p>
            fp = UploadFiles(file=form.cleaned_data['file'])
            fp.save()
            # return redirect('about')
    else:
        form = UploadFileForm()
    return render(request, 'members/about.html', {'title2': 'О сайте', 'menu': menu, 'form': form})


def login(request):
    return HttpResponse(f'Авторизация')


# ______________________________addpage___________________________________________
# def addpage(request):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             print(form.cleaned_data)  # cleaned_data отображает очищенные данные POST
#             try:
#                 Member.objects.create(**form.cleaned_data)
#                 return redirect('home')
#             except:
#                 form.add_error(None, 'Ошибка добавления данных')
#             form.save()
#             return redirect('home')
#     else:
#         form = AddPostForm()
#
#     date = {
#         'menu': menu,
#         'title': 'Добавление статьи',
#         'form': form,
#     }
#     return render(request, 'members/addpage.html', context=date)

class AddPage(DataMixin, CreateView):
    # form_class = AddPostForm # Можно использовать класс форм,
    # либо класс модели, при модели будет использоваться get_abcolute_url
    model = Member
    fields = '__all__' #можно выбрать поля при использовании класса модели (обязательные поля выбирать строго ВСЕ)
    template_name = 'members/addpage.html'
    # success_url = reverse_lazy('home')  # reverse_lazy выстраивает маршрут не сразу
    title_page = 'Добавление статьи'

class UpdatePage(DataMixin, UpdateView):
    model = Member
    fields = '__all__'
    template_name = "members/addpage.html"
    success_url = reverse_lazy('home')
    title_page = 'Редактирование статьи'

class DeletePage(DataMixin, DeleteView):
    model = Member
    fields = '__all__'
    template_name = "members/delete_page.html"
    success_url = reverse_lazy('home')
    title_page = 'Удаление статьи'
    # extra_context = {
    #     'menu': menu,
    #     'title': 'Удаление статьи',
    # }


# class AddPage(FormView): Пример использования FormView
#     form_class = AddPostForm
#     template_name = 'members/addpage.html'
#     success_url = reverse_lazy('home')  # reverse_lazy выстраивает маршрут не сразу
#     extra_context = {'menu': menu, 'title': 'Добавление статьи', }
#
#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)


# class AddPage(View): #Пример использования View
#     def get(self, request):
#         form = AddPostForm()
#         date = {
#             'menu': menu,
#             'title': 'Добавление статьи',
#             'form': form,
#         }
#         return render(request, 'members/addpage.html', context=date)
#
#     def post(self, request):
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#         date = {
#             'menu': menu,
#             'title': 'Добавление статьи',
#             'form': form,
#         }
#         return render(request, 'members/addpage.html', context=date)

#______________________________________________________________________________________________
def contact(request):
    return HttpResponse(f'Обратная связь')


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена!</h1>')


def tags_list(request, tag_slug):
    tag = get_object_or_404(TagPost, slug=tag_slug)
    posts = tag.tags.all()

    date = {'title': f'Тег: {tag.tag}',
            'menu': menu,
            'mmbrs': posts,
            'pos_selected': None,
            }

    return render(request, 'members/index.html', context=date)


class MemberTag(ListView):
    template_name = 'members/index.html'
    context_object_name = 'mmbrs'
    allow_empty = False

    def get_queryset(self):
        return Member.published.filter(tags__slug=self.kwargs['tag_slug']).select_related('pos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tag = context['mmbrs'][0].tags.all()[0]
        context['title'] = f'Тег - {tag.tag}'
        context['menu'] = menu
        context['pos_selected'] = None
        return context
