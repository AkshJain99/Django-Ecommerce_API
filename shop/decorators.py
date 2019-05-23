from rest_framework.response import Response
from rest_framework.views import status


def validate_request_data(fn):
    def decorated(*args, **kwargs):
        # args[0] == GenericView Object
        full_name = args[0].request.data.get("full_name", "")
        phone_number = args[0].request.data.get("phone_number", "")
        if not full_name and not artist:
            return Response(
                data={
                    "message": "Both full_name and phone_number are required to add a song"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        return fn(*args, **kwargs)
    return decorated