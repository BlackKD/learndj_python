from django.shortcuts import render,redirect
from story.forms import StoryForm, ChapterForm
from story.models import Story, Chapter

# Create your views here.

def new_story(request):
    if request.method == 'POST':
        storyform = StoryForm(data=request.POST)
        if storyform.is_valid():
            storyform.save(request.user)
            return redirect('author', request.user.username)
    return redirect(request.META.get('HTTP_REFERER'))

def view_story(request, id):
    story = Story.objects.get(id=id)
    return render(request, 'story.html', {'story':story,})

def new_chapter(request, id):
    story = Story.objects.get(id=id)
    if request.method == 'POST':
        chapterform = ChapterForm(data=request.POST)
        if chapterform.is_valid():
            chapterform.save(story,request.user)
        return redirect('viewstory',id)
    return render(request, 'story.html', {'story': story,})

def change_chapter(request, sid, cid):
    chapter = Chapter.objects.get(id=cid)
    if request.method == 'POST':
        chapterform = ChapterForm(data=request.POST)
        if chapterform.is_valid():
            chapter.subtitle = chapterform.cleaned_data['subtitle']
            chapter.content = chapterform.cleaned_data['content']
            chapter.save()
    return redirect('viewstory',sid)