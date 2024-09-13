from django import forms


class TakeFilesYandexDiskOpenForm(forms.Form):
    class Filter:
        ALL = ('all', "All")
        ARCHIVE = ('archive', "Archive")
        DOCUMENT = ('document', "Document")
        IMAGE = ('image', "Image")
        EXECUTABLE = ('executable', "Executable")
        MEDIA = ('media', "Media")

        choices = [ALL, ARCHIVE, DOCUMENT, IMAGE, EXECUTABLE, MEDIA]

    link = forms.URLField(label="link")
    filter = forms.ChoiceField(label='Фильтр', choices=Filter.choices)


