#This file used for both tables filteration
import django_filters
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from .models import atr_loadTestDetails,ATR
from .tables import atr_loadTestDetailsTable,ATR
#filtertion of columns in tables
class UserFilter(django_filters.FilterSet):
    class Meta:
        model = atr_loadTestDetailsTable
        fields='__all__'

class FilteredPersonListView(SingleTableMixin, FilterView):
    table_class =atr_loadTestDetailsTable
    model = atr_loadTestDetails
    template_name = 'users/loadTestDetails.html'
    filterset_class = UserFilter