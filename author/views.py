from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from story.models import Story,Chapter

# Create your views here.
def home_page(request):
    stories = Story.objects.all()
    return render(request, 'home.html', { 'stories':stories, })

def user_page(request, username):
    if request.user.username == username:
        user = request.user
    else:
        user = User.objects.get(username=username)
    return render(request, 'author.html',{'user':user,})

def search(request):
    if request.method == 'POST':
        keyword = request.POST['keyword']
        if keyword == "":
            return redirect(request.META.get('HTTP_REFERER'))
        story_result = []
        for story in Story.objects.all():
            if story.title == keyword:
                story_result.append(story)
        author_result = []
        for author in User.objects.all():
            if author.username == keyword:
                author_result.append(author)
        return render(request,'search.html', {'story_result':story_result,'author_result':author_result})
    return redirect(request.META.get('HTTP_REFERER'))


def checkchapter(request):
    if request.method == 'POST':
        chapterid = request.POST['chapter']
        storyid = request.POST['story']
        mychapter = Chapter.objects.get(id=chapterid)
        mystory = Story.objects.get(id =storyid)
        mychapter.ifallow = "yes"
        mychapter.save()
        nownum = mychapter.numb
        for chapter in mystory.chapter_set.all():
            if chapter.numb == nownum and chapter.ifallow =='no':
                chapter.delete()
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect(request.META.get('HTTP_REFERER'))
