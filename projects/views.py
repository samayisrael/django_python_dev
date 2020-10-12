import requests
from django.shortcuts import render
from django.http import HttpResponse
import numpy
from .models import Greeting
from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib.pyplot as plt

import logging

'''this currently works
import my_library.binary_tree as bt
tree = bt.BinaryTree(1)
tree.root.left = bt.Node(2)
tree.root.right = bt.Node(3)
tree.root.left.left = bt.Node(4)
tree.root.left.right = bt.Node(6)
logger = logging.getLogger('views')
logger.error('new2')
logger.error(tree.root.left.right.value)
this currently works
'''

import my_library.stable_matching as sm

tree = sm.StableMatching()

logger = logging.getLogger('views')
logger.error('trying')
logger.error(tree)
logger.error(tree.the_result)
# import the logging library

# Get an instance of a logger


### Taking the below out right now to troubleshoot.
from django.http import HttpResponseRedirect

from .forms import NameForm


# Log an error message
#logger.error('Something went wrong!')
#logger.log() -- doesnt' work b/c it needs a msg param

''' sm.main() and the call above are what I am using it is working as I can see it getting called in the cmd console, but
there is no output to the html on the website at all.  I'm not familiar with the framwork, so I may just getting working
the dumb way first just to see what the data looks like.  That will be first thing tomorrrow.

'''
# Create your views here.
'''def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")'''
'''r = requests.get('http://httpbin.org/status/418')
    print(r.text)
    return HttpResponse('<pre>' + r.text + '</pre>')'''


def index(request):
    logger.error('in the index function')

    '''
    dataset = pd.read_csv('Salary_Data.csv')
    X = dataset.iloc[:, :-1].values
    y = dataset.iloc[:, 1].values
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)
    # Fitting Simple Linear Regression to the Training set
    from sklearn.linear_model import LinearRegression
    regressor = LinearRegression()
    regressor.fit(X_train, y_train)

    # Predicting the Test set results
    y_pred = regressor.predict(X_test)

    # Visualising the Training set results
    plt.scatter(X_train, y_train, color = 'red')
    plt.plot(X_train, regressor.predict(X_train), color = 'blue')
    plt.title('Salary vs Experience (Training set)')
    plt.xlabel('Years of Experience')
    plt.ylabel('Salary')
    sendthis = plt.show()


    return render(request, "index.html",  {"dataset": y_pred})

    return render(request, "index.html")
    '''

    index_info = 'index_page'#tree.the_result sm.main()
    return render(request, "index.html",  {"dataset": index_info})

def list(request):

    project_list_info = "project_list"
    return render(request, "list.html",  {"dataset": project_list_info})

def stable_detail(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            #return HttpResponseRedirect('/result/')

            return render(request, 'display.html', {'form': form, 'dataset' : tree.the_result})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form, 'dataset' : 'testing'})

    #stable_project_info = "form added stable detail page"
    #return render(request, "stable_detail.html",  {"dataset": stable_project_info})



def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
