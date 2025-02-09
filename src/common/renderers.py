from rest_framework.renderers import JSONRenderer
from rest_framework.views import exception_handler


class CommonResponseRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        renderer_context = renderer_context or {}
        response = renderer_context.get("response")

        # If no exception, wrap the data in your standard structure.
        if response and not response.exception:
            wrapped_data = {
                "success": response.status_code >= 200 and response.status_code < 300,
                "detail": data,
            }
        else:
            # For errors, assume your custom exception handler has already set the format.
            wrapped_data = data

        return super().render(wrapped_data, accepted_media_type, renderer_context)


def custom_exception_handler(exc, context):
    # Call DRF's default exception handler first to get the standard error response.
    response = exception_handler(exc, context)

    # If DRF could handle the exception, customize the response.
    if response is not None:
        # Customize the response data.
        customized_response = {
            "success": False,
            "detail": {
                # Try to extract a detailed message, or use a default.
                "message": response.data.get("detail", "An error occurred."),
            },
        }
        response.data = customized_response

    # Optionally, handle exceptions that DRF doesn't catch (response is None).
    # You can add logging here if needed.
    return response
