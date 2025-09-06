from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.http import Http404
from .models import Case, Judgement
from .serializers import CaseSerializer, JudgementSerializer, CaseDetailSerializer, JudgementDetailSerializer
from .permissions import IsOwnerOrReadOnly, IsSupporterOrReadOnly


class CaseList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def get(self, request):
        cases = Case.objects.all()
        serializer = CaseSerializer(cases, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = CaseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class CaseDetail(APIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    ]

    def get_object(self, pk):
        try:
            case = Case.objects.get(pk=pk)
            self.check_object_permissions(self.request, case)
            return case
        except Case.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        case = self.get_object(pk)
        serializer = CaseDetailSerializer(case)
        return Response(serializer.data)
    
    def put(self, request, pk):
        case = self.get_object(pk)
        serializer = CaseDetailSerializer(
            instance=case,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data)
        else: 
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

class JudgementList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        judgements = Judgement.objects.all()
        serializer = JudgementSerializer(judgements, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = JudgementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(supporter=request.user)
            return Response(
                serializer.data, 
                status=status.HTTP_201_CREATED,
            )
        else:
            return Response(
                serializer.errors, 
                status=status.HTTP_400_BAD_REQUEST
            )
    def put(self, request, pk):
        judgement = self.get_object(pk)
        serializer = JudgementDetailSerializer(
            instance=judgement,
            data=request.data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data)
        else: 
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
class JudgementDetail(APIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsSupporterOrReadOnly
    ]
    def get_object(self, pk):
        try:
            judgement = Judgement.objects.get(pk=pk)
            self.check_object_permissions(self.request, judgement)
            return judgement
        except Judgement.DoesNotExist:
            raise Http404
    def get(self, request, pk):
        judgement = self.get_object(pk)
        serializer = JudgementDetailSerializer(judgement)
        return Response(serializer.data)
    
    def put(self, request, pk):
        judgement = self.get_object(pk)
        serializer = JudgementDetailSerializer(
            instance=judgement,
            data=request.data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data)
        else: 
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )