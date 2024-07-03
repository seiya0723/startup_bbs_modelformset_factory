from django.shortcuts import render,redirect

from django.views import View
from .models import Topic

from .forms import TopicFormSet


class IndexView(View):

    def get(self, request, *args, **kwargs):

        context = {}
        context["topics"]   = Topic.objects.all()

        #                                     ↓これがないとこれまで投稿されたデータまで表示される。
        context["formset"]  = TopicFormSet(queryset=Topic.objects.none())

        return render(request,"bbs/index.html",context)

    def post(self, request, *args, **kwargs):

        formset = TopicFormSet(request.POST)

        if formset.is_valid():
            formset.save()
        else:
            print(formset)
            print(formset.errors)


        return redirect("bbs:index")

index   = IndexView.as_view()
