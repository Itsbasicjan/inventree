from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from .models import CustomerAllocation

class AllocationListView(PermissionRequiredMixin, ListView):
    permission_required = "meinplugin.view_customerallocation"
    model = CustomerAllocation
    template_name = "meinplugin/allocations_list.html"
    context_object_name = "allocations"

    def get_queryset(self):
        return CustomerAllocation.objects.filter(
            part__stock__gt=0
        ).select_related('part', 'customer')

class AllocationCreateView(PermissionRequiredMixin, CreateView):
    permission_required = "meinplugin.add_customerallocation"
    model = CustomerAllocation
    template_name = "meinplugin/allocations_form.html"
    fields = ['part', 'quantity', 'customer', 'start_date', 'end_date', 'notes']
    success_url = reverse_lazy('plugin:meinplugin:allocations_list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)