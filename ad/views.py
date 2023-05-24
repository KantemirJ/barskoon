from django.shortcuts import render
from main.models import Ad
from .models import Comment
from .forms import CommentForm


def ad_page(request, ad_id):
    ad = Ad.objects.get(id=ad_id)
    user = request.user.username
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            com = Comment(username=request.user, name=ad, comment=request.POST['comment'])
            com.save()
    form = CommentForm()
    comments = Comment.objects.all().filter(name=ad).order_by('-id')[:10]
    context = {'ad': ad, 'user': user, 'form': form, 'comments': comments}
    return render(request, 'ad/ad_page.html', context)