from django.shortcuts import render
from pages.forms import summarize
from transformers import pipeline
from pages.models import Summary
from django.http import HttpResponse
from django.http import Http404
from django.template.response import TemplateResponse
# Create your views here.

def home(request):
    summary = None
    summarizer = pipeline("summarization", model="Falconsai/text_summarization")
    if request.method == 'POST':
        # create an instance of our form, and fill it with the POST data
        form = summarize(request.POST)

        if form.is_valid():
            summary = str(summarizer(request.POST.get('Text'), max_length=283, min_length=30, do_sample=False))
            summary = summary.replace("[{'summary_text': '","")
            summary = summary.replace("}]","")

        thisSummary = Summary
        thisSummary.summary = summary

    # if the form is not valid, we let execution continue to the return
    # statement below, and display the form again (with errors).

    else:
        form = summarize()
    if summary:
        args = {}
        args['form'] = form
        args['Summary'] = thisSummary
        return render(request, 'pages/home.html', args)
    else:
        return render(request, 'pages/home.html', {'form':form})
