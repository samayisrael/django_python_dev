import requests
from django.shortcuts import render
from django.http import HttpResponse
import numpy
from .models import Greeting, Food, Element, Amount, ElementType
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

# Create your views here.
'''def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")'''
'''r = requests.get('http://httpbin.org/status/418')
    print(r.text)
    return HttpResponse('<pre>' + r.text + '</pre>')'''


def index(request):

    from django.core.mail import send_mail

    if request.headers['HOST'] != 'localhost:5000':
        send_mail(
            'SamayTest - this is the index page',
            'Here is the message.'+ request.headers['HOST'] +' end of text for me.',
            'samay.israel@gmail.com',
            ['samay.israel@gmail.com'],
            fail_silently=False,
        )

    logger.error('in the index function begining')

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

    from django.core.mail import send_mail

    if request.headers['HOST'] != 'localhost:5000':

        send_mail(
            'SamayTest - this is from the list page',
            'Here is the message.'+ request.headers['HOST'] +' end of text for me.',
            'samay.israel@gmail.com',
            ['samay.israel@gmail.com'],
            fail_silently=False,
        )

    project_list_info = "project_list"
    return render(request, "list.html",  {"dataset": project_list_info})

def feedme_landing(request):


    #food_obj = Food.objects.get(pk=1)

    '''
    element_objs = element.objects.filter(food_id=food_obj.id)

    context = {

        "vehicles": car_objs,

        "drivers": owner_obj,

    }
    '''

    feedme_landing_info = "feed me index page"
    return render(request, "feedme.html",  {"dataset": feedme_landing_info})



def buildings_google(request):

    import googlemaps
    from datetime import datetime
    from projects.static.secrets import google_key

    now = datetime.now()

    return render(request, "earthquakes.html",  {"google_key": google_key})

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

def portal(request):

    portal_info = "portal_info"
    return render(request, "portal.html",  {"dataset": portal_info})

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings, "foods": foods, "elements": elements, 'element_types' : element_types})


def mytest(request):
    import csv

    greetings = Greeting.objects.all()



    element = Element.objects.get(name='Zinc')
    '''
    Calcium  row[2]
    Copper   row[9]
    Iron     row[3]
    Magnesium row[5]
    Manganese row[10]
    Phosphorus row[6]
    Potassium row[4]
    Selenium  row[11]
    Sodium    row[7]
    Zinc      row[8]
    '''

    with open('food_data_working.csv', newline='') as csvfile:
        foodreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in foodreader:
            food = Food.objects.get(name=row[1])
            if row[8] != 'NULL':
                val = row[8]
            else:
                val = 0
            amount = Amount(element_id=element.id, food_id = food.id, amount=val)
            amount.save()
            # I used the code below to create the initial foods.
            #food = Food(name=row[1])
            #food.save()
            #', '.join(row)

            # Second part is getting the food and then adding in all the element amount per 100g.
            # I am only doing the 10 minerals for the time being.
            # for every food, insert calcium amounts



    return render(request, "db.html", {"greetings": greetings})


def mytest2(request):
    #  Only one food in the db so far.
    food = Food.objects.get(name='Potatoes')

    #target_amounts = Element.objects.all().order_by('id')
    #amounts_table= Amount.objects.filter(food_id = food.id).order_by('element_id')
    #food = Food.objects.get(name='Potatoes')

    return render(request, "mytest.html", {"food": food})

    #return render(request, "mytest.html", {"targets" : targets, "food_amount" : food_amount})
    #return render(request, "mytest.html", {"target_amounts" : target_amounts, "amounts_table" : amounts_table})
