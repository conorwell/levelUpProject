from django.shortcuts import render
from pages.forms import summarize

# Create your views here.

def home(request):

    if request.method == 'POST':
        # create an instance of our form, and fill it with the POST data
        form = summarize(request.POST)

        if form.is_valid():
            textToSummarize = form.cleaned_data['Text']

    # if the form is not valid, we let execution continue to the return
    # statement below, and display the form again (with errors).

    else:
        form = summarize()

    return render(request, "pages/home.html", {'form':form})
