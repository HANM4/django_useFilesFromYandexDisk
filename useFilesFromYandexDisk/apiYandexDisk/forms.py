from typing import List, Tuple
from django import forms


class TakeFilesYandexDiskOpenForm(forms.Form):
    class Filter:
        ALL: Tuple[str, str] = ('all', "All")
        ARCHIVE: Tuple[str, str] = ('archive', "Archive")
        DOCUMENT: Tuple[str, str] = ('document', "Document")
        IMAGE: Tuple[str, str] = ('image', "Image")
        EXECUTABLE: Tuple[str, str] = ('executable', "Executable")
        MEDIA: Tuple[str, str] = ('media', "Media")

        choices: List[Tuple[str, str]] = [ALL, ARCHIVE, DOCUMENT, IMAGE, EXECUTABLE, MEDIA]

    link: forms.URLField = forms.URLField(label="link")
    filter: forms.ChoiceField = forms.ChoiceField(label='Filter', choices=Filter.choices)