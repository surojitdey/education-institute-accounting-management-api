import requests
import time
import os

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password



from rest_framework import viewsets, status, permissions
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.parsers import JSONParser
from rest_framework.request import Request
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.views import APIView

from oauth2_provider.contrib.rest_framework import TokenHasScope, TokenHasReadWriteScope

from jist_api.models import *
from jist_api.serializers import *


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = studentSerializer
    # authentication_classes = [TokenAuthentication,]
    # authentication_classes = [TokenAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser, TokenHasReadWriteScope]
    # permission_classes = [AllowAny]

    # def post(self, request, *args, **kwargs):
    #     serializer = studentSerializer(data=request.data)
    #     print("*****************************************************")
    #     print(request.data['depertment'])
    #     print("*****************************************************")
    #     depertment_instance = depertment.objects.get(dept_name=request.data['depertment'])
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save(depertment_id=depertment_instance.id)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)

class getStudentsFromQuery(viewsets.ModelViewSet):
    serializer_class = AdmissonSerializer
    # permission_classes = [IsAuthenticated, IsAdminUser, TokenHasReadWriteScope]
    permission_classes = [AllowAny,]

    def get_queryset(self):
        return Admission.objects.filter(depertment_id=self.request.query_params.get('depertment'))

class Transfer_StudentViewSet(viewsets.ModelViewSet):
    queryset = Transfer_Students.objects.all()
    serializer_class = transfer_studentSerializer
    permission_classes = [IsAuthenticated, IsAdminUser, TokenHasReadWriteScope]
    # permission_classes = [AllowAny]

class DepertmentViewSet(viewsets.ModelViewSet):
    queryset = Depertment.objects.all()
    serializer_class = depertmentSerializer
    # permission_classes = [IsAuthenticated, IsAdminUser, TokenHasReadWriteScope]
    permission_classes = [AllowAny,]

class getDepertmentDetails(viewsets.ModelViewSet):
    serializer_class = depertmentSerializer
    # permission_classes = [IsAuthenticated, IsAdminUser, TokenHasReadWriteScope]
    permission_classes = [AllowAny,]

    def get_queryset(self):
        return Depertment.objects.filter(id=self.request.query_params.get('depertment_id'))

class getDepertmentIdViewSet(viewsets.ModelViewSet):
    serializer_class = depertmentIdSerializer
    # permission_classes = [IsAuthenticated, IsAdminUser, TokenHasReadWriteScope]
    permission_classes = [AllowAny,]

    def get_queryset(self):
        return Depertment.objects.filter(dept_name__exact=self.request.query_params.get('depertment'))

class BranchViewSet(viewsets.ModelViewSet):
    queryset = Branch.objects.all()
    serializer_class = branchSerializer
    # permission_classes = [IsAuthenticated, IsAdminUser, TokenHasReadWriteScope]
    permission_classes = [AllowAny,]

class GetBranchViewSet(viewsets.ModelViewSet):
    serializer_class = getBranchSerializer
    # permission_classes = [IsAuthenticated, IsAdminUser, TokenHasReadWriteScope]
    permission_classes = [AllowAny,]

    def get_queryset(self):
        return Branch.objects.filter(depertment=self.request.query_params.get('depertment'))

#To get the client's ip address
def get_client_ip(request):
    """Returns the IP of the request, accounting for the possibility of being
    behind a proxy.
    """
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR', None)
    print(x_forwarded_for)
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
        print(ip)
    return ip
    # ip = request.META.get("HTTP_X_FORWARDED_FOR", None)
    # if ip:
    #     # X_FORWARDED_FOR returns client1, proxy1, proxy2,...
    #     ip = ip.split(", ")[0]
    # else:
    #     ip = request.META.get("REMOTE_ADDR")
    # return ip

#to get the time.
def get_time():
    import datetime
    now = datetime.datetime.now()
    return now

@csrf_exempt
def signinInfoView(request):
    if request.method == "GET":
        signinInfoQueryset = signinInfo.objects.all()
        serializer_context = {
            'request' : Request(request),
        }
        serializer = signinInfoSerializer(signinInfoQueryset, context=serializer_context, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == "POST":
        time.sleep(0.01)
        json_parser = JSONParser()
        data = {
            "client_ip": get_client_ip(request),
            "timestamp": get_time(),
        }
        serializer = signinInfoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@api_view(['POST'])
@permission_classes([AllowAny])
def token(request):
    '''
    Gets tokens with username and password. Input should be in the format:
    {"username": "username", "password":"password123"}
    '''
    time.sleep(0.01)
    r = requests.post(
        os.getenv('TOKEN_URL'),
        data = {
                'grant_type':'password',
                'username': request.data['username'],
                'password': request.data['password'],
                'client_id': os.getenv('CLIENT_ID'),
                'client_secret': os.getenv('CLIENT_SECRET'),
        },
        verify = False
    )
    data = r.json()
    return Response(r.json())

@api_view(['POST'])
@permission_classes([AllowAny])
def refresh_token(request):
    '''
    Register user to the server. Input should be in the format:
    {"refresh_token":"<token>"}
    '''
    time.sleep(0.01)
    r = requests.post(
        os.getenv('TOKEN_URL'),
        data = {
                'grant_type': 'refresh_token',
                'refresh_token': request.data['refresh_token'],
                'client_id': os.getenv('CLIENT_ID'),
                'client_secret': os.getenv('CLIENT_SECRET'),
        },
        verify = False
    )
    return Response(r.json())

# Function to logged out user.
@api_view(['POST'])
@permission_classes([AllowAny])
def revoke_token(request):
    '''
    Method to revoke tokens.
    {"token":"<token>"}
    '''
    time.sleep(0.01)

    r = requests.post(
        os.getenv('REVOKE_TOKEN_URL'),
        data = {
                'token': request.data['token'],
                'client_id': os.getenv('CLIENT_ID'),
                'client_secret': os.getenv('CLIENT_SECRET'),
        },
        verify = False
    )
    # If it goes well return success message (would be empty otherwise)
    if r.status_code == requests.codes.ok:
        return Response({'message': 'token revoked'}, r.status_code)
    # Return the error if it goes badly
    return Response(r.json(), r.status_code)

class UserCreateViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    # print(len(queryset))
    serializer_class = UserSerializer
    permission_classes = [AllowAny,]

    # @action(detail=True, methods=['post'])
    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        # user = self.get_object()
        # serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            if 'password' not in serializer.validated_data:
                return Response({
                    'error': 'Password required for creating account.'
                }, status=status.HTTP_400_BAD_REQUEST)

            user = User.objects.create_user(**serializer.validated_data)

            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)

        return Response({
            'error': 'Account could not be created with received data.'
        }, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        # Hash password but passwords are not required
        if ('password' in self.request.data):
            password = make_password(self.request.data['password'])
            serializer.save(password=password)
        else:
            serializer.save()

    def perform_update(self, serializer):
        # Hash password but passwords are not required
        if ('password' in self.request.data):
            password = make_password(self.request.data['password'])
            serializer.save(password=password)
        else:
            serializer.save()

class PasswordChangeViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = PasswordChangeSerializer
    permission_classes = [IsAuthenticated, IsAdminUser, TokenHasReadWriteScope]
    # permission_classes = [AllowAny,]

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def put(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            if not self.object.check_password(request.data.get("old_password")):
                return Response("Invalid Current Password", status=status.HTTP_400_BAD_REQUEST)

            self.object.set_password(request.data.get("new_password"))
            self.object.save()
            return Response("Password changed successfully", status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# To view the admission fee details of each depertment except BE depertment.
class OddSemesterFeeViewSet(viewsets.ModelViewSet):
    queryset = semester_fees.objects.all()
    serializer_class = OddSemesterFeeSerializer
    permission_classes = [IsAuthenticated, IsAdminUser, TokenHasReadWriteScope]
    # permission_classes = [AllowAny,]

# To view the BE depertment admission fee details.
class BEFeeViewSet(viewsets.ModelViewSet):
    queryset = be_fee_table.objects.all()
    serializer_class = BEFeeSerializer
    permission_classes = [IsAuthenticated, IsAdminUser, TokenHasReadWriteScope]
    # permission_classes = [AllowAny,]

# To view the Hostel admission fee details.
class HostelFeeViewSet(viewsets.ModelViewSet):
    queryset = hostel_fee_table.objects.all()
    serializer_class = HostelAdmissionFeeSerializer
    # permission_classes = [IsAuthenticated, IsAdminUser, TokenHasReadWriteScope]
    permission_classes = [AllowAny]

# To view the Hostel admission fee Odd semester details.
class OddHostelFeeViewSet(viewsets.ModelViewSet):
    serializer_class = HostelAdmissionFeeSerializer
    # permission_classes = [IsAuthenticated, IsAdminUser, TokenHasReadWriteScope]
    permission_classes = [AllowAny]

    def get_queryset(self):
        return hostel_fee_table.objects.filter(semester="Odd")

# To view the Hostel admission fee Even semester details.
class EvenHostelFeeViewSet(viewsets.ModelViewSet):
    serializer_class = HostelAdmissionFeeSerializer
    # permission_classes = [IsAuthenticated, IsAdminUser, TokenHasReadWriteScope]
    permission_classes = [AllowAny]

    def get_queryset(self):
        return hostel_fee_table.objects.filter(semester="Even")

class HostelAdmissionViewSet(viewsets.ModelViewSet):
    queryset = HostelAdmission.objects.all()
    serializer_class = HostelAdmissonSerializer
    # permission_classes = [IsAuthenticated, IsAdminUser, TokenHasReadWriteScope]
    permission_classes = [AllowAny]

# To view the students details who are submit their admission fee.
class AdmissionViewSet(viewsets.ModelViewSet):
    queryset = Admission.objects.all()
    serializer_class = AdmissonSerializer
    # permission_classes = [IsAuthenticated, IsAdminUser, TokenHasReadWriteScope]
    permission_classes = [AllowAny,]

# To view the examination fee details of each depertment.
class ExamFeeViewSet(viewsets.ModelViewSet):
    queryset = Exam_fee_table.objects.all()
    serializer_class = ExamFeeSerializer
    # permission_classes = [IsAuthenticated, IsAdminUser, TokenHasReadWriteScope]
    permission_classes = [AllowAny,]

# To view the spot admission fee details.
class SpotAdmissionFeeViewSet(viewsets.ModelViewSet):
    queryset = Spot_Admission_Fee.objects.all()
    serializer_class = SpotAdmissionFeeSerializer
    # permission_classes = [IsAuthenticated, IsAdminUser, TokenHasReadWriteScope]
    permission_classes = [AllowAny,]

# To view the students details who are submit their examination fee.
class ExaminationViewSet(viewsets.ModelViewSet):
    queryset = Examination_fee_table.objects.all()
    serializer_class = ExaminationSerializer
    # permission_classes = [IsAuthenticated, IsAdminUser, TokenHasReadWriteScope]
    permission_classes = [AllowAny,]

# To view the students details who are submit their examination fee.
class CompartmentalViewSet(viewsets.ModelViewSet):
    queryset = Compartmental_fee_table.objects.all()
    serializer_class = CompartmentalSerializer
    # permission_classes = [IsAuthenticated, IsAdminUser, TokenHasReadWriteScope]
    permission_classes = [AllowAny,]

# To view the students details who are submit their examination fee.
class BettermentViewSet(viewsets.ModelViewSet):
    queryset = Betterment_fee_table.objects.all()
    serializer_class = BettermentSerializer
    # permission_classes = [IsAuthenticated, IsAdminUser, TokenHasReadWriteScope]
    permission_classes = [AllowAny,]

# To view the sell records of form and prospectus
class FormAndProspectusViewSet(viewsets.ModelViewSet):
    queryset = form_and_prospectus_table.objects.all()
    serializer_class = FormAndProspectusSerializer
    permission_classes = [IsAuthenticated, IsAdminUser, TokenHasReadWriteScope]
    # permission_classes = [AllowAny,]
