from django import forms
from story.models import Story, Chapter


class StoryForm(forms.models.ModelForm):

    def save(self, owner):
        self.instance.owner = owner
        return super().save()

    class Meta:
        model = Story
        fields = ('title', 'brief',)


class ChapterForm(forms.models.ModelForm):

    def save(self, story, writter,numb):
        self.instance.story = story
        self.instance.writter = writter
        self.instance.numb = numb
        return super().save()

    class Meta:
        model = Chapter
        fields = ('subtitle', 'content',)