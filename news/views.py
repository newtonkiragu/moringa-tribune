from django.shortcuts import render
from django.http  import HttpResponse,Http404
import datetime as dt

# Create your views here.
def welcome(request):
    '''
    function for the landing page on the news route
    '''
    return HttpResponse('Welcome to the Moringa Tribune')

def news_of_day(request):
    """
    function that adds dynamic content(date) to the website
    """
    date = dt.date.today()
    html = f'''
        <html>
            <body>
                <h1> {date.day}-{date.month}-{date.year}</h1>
            </body>
        </html>
            '''
    return HttpResponse(html)

def convert_dates(dates):
    """
    function that gets the weekday number for the dates
    """
    day_number = dt.date.weekday(dates)

    days = ['Monday', 'Tuesday','Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    # returning the actual day of the weekday
    day = days[day_number]

    return day

def news_of_day(request):
    '''
    function to display news of that specific day
    '''
    date = dt.date.today()

    # FUNCTION TO CONVERT DATE OBJECT TO FIND EXACT DAY
    day = convert_dates(date)
    html = f'''
        <html>
            <body>
                <h1>News for {day} {date.day}-{date.month}-{date.year}</h1>
            </body>
        </html>
            '''
    return HttpResponse(html)

def past_days_news(request,past_date):
    '''
    function to display news from dates that have already passed
    '''

    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()

    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()

    day = convert_dates(date)
    html = f'''
        <html>
            <body>
                <h1>News for {day} {date.day}-{date.month}-{date.year}</h1>
            </body>
        </html>
            '''
    return HttpResponse(html)
