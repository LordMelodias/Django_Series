# your_app/middleware.py
from django.utils.deprecation import MiddlewareMixin

class UserAgentMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # Get the User-Agent string from the request headers
        user_agent = request.META.get('HTTP_USER_AGENT', 'Unknown')
        
        # Attach the User-Agent to the request object for use in views
        request.user_agent = user_agent
        
        # Optional: Log the User-Agent (you can customize this)
        print(f"User-Agent: {user_agent}")
        
        # Return None to continue processing the request
        return None

    def process_response(self, request, response):
        # You can modify the response here if needed (optional)
        # For example, add User-Agent to response headers (just for demo)
        if hasattr(request, 'user_agent'):
            response['X-User-Agent'] = request.user_agent
        return response