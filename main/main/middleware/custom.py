from django.http import HttpResponse
from django.utils import timezone


class LogTimeTakenMiddleware(object):
    """
    Calculates total time by adding start_time attr to the request logs to request.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.start_time = timezone.now()
        # print("Before calling next element in the chain")
        response = self.get_response(request)
        # print("After calling next element in the chain")
        total_time = timezone.now() - request.start_time
        print(f"Time taken: {total_time.total_seconds()} seconds")
        return response

    def process_exception(self, request, exception):
        return HttpResponse("In exception")
