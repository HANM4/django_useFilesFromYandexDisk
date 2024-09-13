from .forms import TakeFilesYandexDiskOpenForm
from django.views.generic.edit import FormView


class TakeListFilesYandexDiskView(FormView):
    title = 'List files Yandex Disk'
    template_name = 'list_files_yandex_disk.html'
    form_class = TakeFilesYandexDiskOpenForm
    success_url = '/'

    # add link to form from session
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        form_data = self.request.session.get(
            'take_link_files_yandex_disk_open_form_data',
            None
        )
        if form_data:
            kwargs['initial'] = form_data
        return kwargs

# check form on valid
    def form_valid(self, form):
        # add take_link_files_yandex_disk_open_form_data to session
        # from form sent data form
        self.request.session['take_link_files_yandex_disk_open_form_data'] = form.cleaned_data
        print(form.cleaned_data)
        return super().form_valid(form)

# add custom data to context for use in tags template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        return context