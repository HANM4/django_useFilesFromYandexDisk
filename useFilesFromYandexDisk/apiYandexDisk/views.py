from typing import List, Dict, Any, Optional
from django.core.cache import cache
from django.views.generic.edit import FormView
from django.http import HttpResponse

from django.shortcuts import render
from .api import get_public_files_yandex_disk
from .forms import TakeFilesYandexDiskOpenForm
from .utils import get_file_type


class TakeListFilesYandexDiskView(FormView):
    title: str = 'List files Yandex Disk'
    template_name: str = 'list_files_yandex_disk.html'
    form_class = TakeFilesYandexDiskOpenForm
    success_url: str = '/'

    # add link to form from session
    def get_form_kwargs(self) -> Dict[str, Any]:
        kwargs = super().get_form_kwargs()
        form_data: Optional[Dict[str, Any]] = self.request.session.get(
            'take_link_files_yandex_disk_open_form_data',
            None
        )
        if form_data:
            kwargs['initial'] = form_data
        return kwargs

    # check form on valid
    def form_valid(self, form: TakeFilesYandexDiskOpenForm) -> HttpResponse:
        # add take_link_files_yandex_disk_open_form_data to session
        # from form sent data form
        self.request.session[
            'take_link_files_yandex_disk_open_form_data'] = form.cleaned_data

        files: List[Dict[str, Any]] = []
        if self.request.method == "POST" and form.is_valid():
            link: str = form.cleaned_data["link"]
            file_type: str = form.cleaned_data["filter"]

            cache_key: str = f"yandex_disk_files_{link}"
            files = cache.get(cache_key)

            if files is None:
                data: Optional[Dict[str, Any]] = get_public_files_yandex_disk(
                    link)
                if data and "_embedded" in data:  # Checking for files in a public link
                    files = data["_embedded"]["items"]
                    cache.set(cache_key, files,
                              timeout=600)  # We save the list of files to the cache for 10 minutes

            if file_type != "all" and files:  # We filter files if a type other than "all" is selected
                files = [file for file in files if
                         file_type == get_file_type(file["name"])]
        print(files)
        context = self.get_context_data()
        context['files'] = files
        return self.render_to_response(context)

    # add custom data to context for use in tags template
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        return context
