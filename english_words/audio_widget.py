from django import forms


class AudioUrlWidget(forms.widgets.URLInput):
    template_name = 'audio_widget.html'
