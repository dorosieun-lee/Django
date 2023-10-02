from django.shortcuts import redirect, render, get_object_or_404
from .models import Chat
from .forms import CharForm
from django.views.decorators.http import require_POST, require_http_methods, require_safe

@require_POST
def delete(request,pk):
    chatting = get_object_or_404(Chat,pk=pk)
    chatting.delete()
    return redirect("chattings:index")

@require_safe
def detail(request,pk):
    chatting = get_object_or_404(Chat,pk=pk)
    context = {
        'chatting':chatting,
    }
    return render(request,'chattings/detail.html',context)

@require_http_methods(["GET","POST"])
def create(request):
    if request.method == 'POST':
        form = ChatForm(request.POST,request.FILES)
        if form.is_valid:
            chatting = form.save()
            return redirect('chattings:detail',chatting.pk)
    else:
        form = ChatForm()
    context={
        'form':form
    }
    return render(request,'chattings/create.html',context)
