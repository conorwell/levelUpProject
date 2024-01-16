from django.shortcuts import render
from pages.forms import summarize
from transformers import pipeline
# Create your views here.

def home(request):
    summary = ""
    summarizer = pipeline("summarization", model="Falconsai/text_summarization")
    if request.method == 'POST':
        # create an instance of our form, and fill it with the POST data
        form = summarize(request.POST)

        if form.is_valid():
            summary = summarizer(form.cleaned_data['Text'], max_length=230, min_length=30, do_sample=False)
    # if the form is not valid, we let execution continue to the return
    # statement below, and display the form again (with errors).

    else:
        form = summarize()

    return render(request, "pages/home.html", {'form':form})
