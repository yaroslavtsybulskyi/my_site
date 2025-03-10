from django.http import HttpResponseBadRequest, HttpRequest, HttpResponse
from django.shortcuts import render

from datetime import datetime


def home_view(request: HttpRequest) -> HttpResponse:
    """
    Renders the home page.

    :param request: The HTTP request object.
    :return: Rendered home page.
    """
    return render(request, template_name='home/home.html')


def about_view(request: HttpRequest) -> HttpResponse:
    """
    Renders the about page.

    :param request: The HTTP request object.
    :return: Rendered about page.
    """
    return render(request, template_name='home/about.html')


def contact_view(request: HttpRequest) -> HttpResponse:
    """
    Renders the contact page.

    :param request: The HTTP request object.
    :return: Rendered contact page.
    """
    return render(request, template_name='home/contact.html')


def post_view(request: HttpRequest, id: int) -> HttpResponse:
    """
    Renders a post page with a given ID.

    :param request: The HTTP request object.
    :param id: The ID of the post.
    :return: Rendered post page with the post ID.
    """
    return render(request, template_name='home/post.html', context={'id': id})


def profile_view(request: HttpRequest, username: str) -> HttpResponse:
    """
    Renders a user profile page.

    :param request: The HTTP request object.
    :param username: The username of the profile being viewed.
    :return: Rendered profile page with the username.
    """
    return render(request, template_name='home/profile.html', context={'username': username})


def event_view(request: HttpRequest, year: str, month: str, day: str) -> HttpResponse:
    """
    Renders an event page based on the given date.

    :param request: The HTTP request object.
    :param year: The year of the event (4-digit format).
    :param month: The month of the event (2-digit format).
    :param day: The day of the event (2-digit format).
    :return: Rendered event page with the formatted event date.
    :raises HttpResponseBadRequest: If the date is not in the correct format.
    """
    try:
        event_date = datetime.strptime(f"{year}-{month}-{day}", "%Y-%m-%d")
        return render(request, 'home/event.html', context={'event_date': event_date.strftime('%Y-%m-%d')})
    except ValueError:
        return HttpResponseBadRequest("Incorrect Date. Please, check the date format YYYY-MM-DD.")
