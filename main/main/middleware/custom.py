from django.http import HttpResponse
from django.utils import timezone
from user_agents import parse


class LogTimeTakenMiddleware(object):
    """
    Calculates total time taken for the response to get.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        start_time = timezone.now()

        # Call
        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.
        total_time = timezone.now() - start_time
        print(f"Time taken: {total_time.total_seconds()} seconds")
        return response

    def process_exception(self, request, exception):
        # If we return HttpResponse object here, other middlewares won't be called at all
        # in case of exception
        return HttpResponse("In LogTimeTakenMiddleware", status=400)


class CountRequestsMiddleware(object):
    """
    Counts number of requests and exceptions.
    """

    def __init__(self, get_response):
        self.get_response = get_response
        self.requests_count = 0
        self.exceptions_count = 0

    def __call__(self, request):
        self.requests_count += 1
        response = self.get_response(request)
        print(f"Handled {self.requests_count} requests so far")
        return response

    def process_exception(self, request, exception):
        self.exceptions_count += 1
        print(f"Encountered {self.exceptions_count} exceptions so far")


class SetUserAgentMiddleware(object):
    """
    Adds user_agent attr with meaningful info of user agent to the request.

    This middleware is basically a reimplementation of the middleware
    in django-user-agents python package.

    I made this for learning purposes.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user_agent = parse(request.META["HTTP_USER_AGENT"])
        request.user_agent = user_agent
        response = self.get_response(request)
        return response


class BlockMobileMiddleware(object):
    """
    Blocks all incoming requests if they are from mobile browsers.

    This middleware uses SetUserAgentMiddleware's user_agent attr to detect
    whether it is mobile browser. So it should always go after SetUserAgentMiddleware.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # You can test it locally by replacing is_mobile with is_pc
        # It will block all requests from desktop browsers
        if request.user_agent.is_mobile:
            return HttpResponse("Mobile devices are not supported", status=400)
        response = self.get_response(request)
        return response
