menu = [{'title': 'Служба пожаротушения', 'url_name': 'home'},
        {'title': 'Реагирование подразделений', 'url_name': 'fire_home'},
        {'title': 'Добавить статью', 'url_name': 'addpage'},
        {'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Обратная связь', 'url_name': 'contact'},
        ]


class DataMixin:
    paginate_by = 3 # отображение количества записей на странице
    title_page = None
    pos_selected = None
    extra_context = {}

    def __init__(self):
        if self.title_page:
            self.extra_context['title'] = self.title_page

        if self.pos_selected is not None:
            self.extra_context['pos_selected'] = self.pos_selected

    def get_mixin_context(self, context, **kwargs):
        context['pos_selected'] = None
        context.update(kwargs)
        return context