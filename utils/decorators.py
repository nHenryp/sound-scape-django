from songs.models import Song
from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.response import Response


def handle_exceptions(handler_func):
    def wrapper(*args, **kwargs):
        try:
            return handler_func(*args, **kwargs)
        except (Song.DoesNotExist, NotFound) as e:
            print(e)
            return Response({ 'message': str(e) }, 404)
        except PermissionDenied as e:
            print(e)
            return Response({ 'message': str(e)}, 403)
        except Exception as e:
            print(e.__class__.__name__)
            print(e)
            return Response('Un unknown error occurred', 500)
    return wrapper