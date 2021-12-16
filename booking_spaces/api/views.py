from api.mixins import ListViewSet
from api.permissions import AdminManagerOrReadOnly
from api.serializers import ListDatesSerializer, ParkingSpaceSerializer
from booking.models import ParkingSpace, Schedule
from django.shortcuts import get_object_or_404
from rest_framework import filters, viewsets
from rest_framework.pagination import LimitOffsetPagination


class ParkingSpaceViewSet(viewsets.ModelViewSet):
    queryset = ParkingSpace.objects.all()
    serializer_class = ParkingSpaceSerializer
    pagiantion_class = LimitOffsetPagination
    permission_classes = (AdminManagerOrReadOnly,)
    lookup_field = 'slug'
    filter_backends = (filters.SearchFilter,)
    search_fields = ('title',)


class ListDatesViewSet(ListViewSet):
    pagiantion_class = LimitOffsetPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('reserved_dates',)
    serializer_class = ListDatesSerializer

    def get_queryset(self):
        parkingspace_slug = self.kwargs.get('parkingspace_slug')
        space = get_object_or_404(ParkingSpace, slug=parkingspace_slug)
        return Schedule.objects.filter(space=space, is_reserved=False)
