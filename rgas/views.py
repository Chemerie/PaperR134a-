from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Comment
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
def index(request):
	if request.method == "POST":
		name = request.POST["name"]
		comment = request.POST["comment"]
		f= Comment(name=name, text=comment)
		f.save()
	comments = Comment.objects.all().order_by('-id')
	return render(request, "rgas/index.html", {
		"comments": comments,
		})


def about(request):
	return render(request, "rgas/about.html")

@csrf_exempt
def  addlike(request):
	email = Comment()
	if request.method == "POST":
		data = json.loads(request.body)
		if data.get("name") is not None:
			email.name = data["name"]
		if data.get("comment") is not None:
			email.text = data["comment"]
		email.save()
		return HttpResponse(status=204)


