from django.views.generic import ListView, DetailView
from .models import CV

class CVListView(ListView):
    model = CV
    template_name = "main/cv_list.html"
    context_object_name = "cvs"
    paginate_by = 12
    ordering = ['lastname', 'firstname']  

    def get_queryset(self):
        # Prefetch related M2M to avoid N+1 queries
        return super().get_queryset().prefetch_related("skills", "projects")

class CVDetailView(DetailView):
    model = CV
    template_name = "main/cv_detail.html"
    context_object_name = "cv"

    def get_queryset(self):
        return super().get_queryset().prefetch_related("skills", "projects")
