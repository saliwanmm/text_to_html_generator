from django.shortcuts import render, redirect

from django.shortcuts import render
from .forms import GeneratorForm
from .models import GeneratorModel


def create_generator_View(request):
    if request.method == "POST":
        form = GeneratorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/generator/result")
        return render(request, "generator/add_generate.html", {
            "form": form,
        })
    else:
        form = GeneratorForm()
    return render(request, "generator/add_generate.html", {
        "form": form,
    })


def result_generator_View(request):
    try:
        last_data = GeneratorModel.objects.order_by("-id").first()
        if last_data is not None:
            result_html = f'<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>{last_data.title}</title></head><body><h1>{last_data.title}</h1><p>{last_data.description}</p></body></html>'
        else:
            result_html = ''
    except GeneratorModel.DoesNotExist:
        result_html = ''
    return render(request, "generator/result_generator.html", {
        "result_html": result_html,
    })