from users.models import RequestLog

class SaveRequest:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Create instance of our model and assign values
        request_log = RequestLog(
            url=request.get_full_path(),
            response_code=response.status_code,
            method=request.method,
            remote_address=self.get_client_ip(request),
            response=str(response.content),
            request=str(request.body)
        )

        # Assign user to log if it's not an anonymous user
        if not request.user.is_anonymous:
            request_log.user = request.user

        # Save log in db
        request_log.save() 
        return response
    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            _ip = x_forwarded_for.split(',')[0]
        else:
            _ip = request.META.get('REMOTE_ADDR')
        return _ip