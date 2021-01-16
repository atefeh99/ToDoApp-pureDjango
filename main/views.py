from django.shortcuts import render, redirect
from .models import Todolist, Item
from .forms import CreateNewList

# Create your views here.


def index(response, id):
    if response.user.is_authenticated:
        ls = Todolist.objects.get(id=id)
        if ls in response.user.todolist.all():
            if response.method == "POST":
                if response.POST.get("save"):
                    for item in ls.item_set.all():
                        if response.POST.get("c" + str(item.id)) == "clicked":
                            item.complete = True
                        else:
                            item.complete = False
                        item.save()

                elif response.POST.get("newItem"):
                    txt = response.POST.get("new")

                    if len(txt) > 2:
                        ls.item_set.create(text=txt, complete=False)
                    else:
                        print("invalid")
            return render(response, "main/list.html", {"ls": ls})
    else:
        return redirect("/home")


def home(response):
    return render(response, "main/home.html", {})


def create(response):
    if response.user.is_authenticated:
        if response.method == "POST":
            form = CreateNewList(response.POST)
            if form.is_valid():
                n = form.cleaned_data["name"]
                t = Todolist(name=n)
                t.save()
                response.user.todolist.add(t)
                return redirect("/%i" % t.id)
        else:
            form = CreateNewList()
        context = {"form": form}
        return render(response, "main/create.html", context)
    else:
        return redirect("/home")


def view(response):
    if response.user.is_authenticated:
        todo = response.user.todolist.all()
        return render(response, 'main/view.html', {"todo":todo})
    else:
        return redirect("/home")
