from django.core.exceptions import PermissionDenied

class StaffRequiredMixin:
    """Mixin that requires the user to be staff to access."""
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_staff:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied
