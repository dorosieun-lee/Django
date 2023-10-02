from django.shortcuts import render, redirect
from django.http import Http404
from .models import Memo
from .form import MemoForm


# Create your views here.
def index(request):
    memos = Memo.objects.all()
    content = {
        'memos': memos,
    }
    return render(request, 'memos/index.html', content)

def detail(request, pk):
    try:
        memo = Memo.objects.get(pk=pk)
        content = {
            'memo': memo,
        }
    except Memo.DoesNotExist:
        raise Http404('존재하지 않는 페이지입니다.')
    return render(request, 'memos/detail.html', content)
        

def create(request):
    if request.method == "POST":
        memo = request.POST.get('memo')
        summary = request.POST.get('summary')
        item = Memo(memo=memo, summary=summary)
        item.save()
        return redirect('memos:detail', item.pk)
    else:
        form = MemoForm()
        content = {
            'form': form,
        }
        return render(request, 'memos/create.html', content)

def delete(request, pk):
    memo = Memo.objects.get(pk=pk)
    memo.delete()
    return redirect('memos:index')


