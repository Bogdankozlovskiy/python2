from rest_framework import pagination


class MyPagination(pagination.LimitOffsetPagination):
    max_limit = 2
