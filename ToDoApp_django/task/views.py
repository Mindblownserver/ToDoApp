from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Todo
from .serializer import ToDoSerializer
# Create your views here.
class ToDoView(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self,request):
        user = request.user
        todos=Todo.objects.filter(user=user)
        serializer = ToDoSerializer(todos,many=True)
        return Response({
            "status":True,
            "data":serializer.data,
            "message": "ToDo fetched successfully"
        })
    def post(self,request):
        try:
            user = request.user
            data = request.data
            data["user"] = user.id
            serializer = ToDoSerializer(data=data)
            
            if serializer.is_valid():
                serializer.save()
                print("Here")
                return Response({
                "status":True,
                "message": "ToDo added successfully",
                "data": serializer.data
            })
            else:
                return Response({
                    "status": False,
                    "message":"Invalid fields",
                    "data":
                    serializer.errors
                })
        except Exception as e:
            print(e)
            return Response({
                "status":False,
                "message":"Something went wrong",
                "data": {}
            })
    def patch(self,request):
        try:
            data  = request.data # data is JSON body
            if not data.get("uid"):
                return Response({
                    "status":False,
                    "message":"UID required ",
                    "data": {}
            })
            obj = Todo.objects.filter(uid=data.get("uid"))
            if not obj.exists():
                return Response({
                    "status":False,
                    "message":"Invalid UID ",
                    "data": {}
            })
            serializer = ToDoSerializer(obj[0],data=data,partial=True)
            if not serializer.is_valid():
                return Response({
                "status":False,
                "message": "Invalid fields",
                "data": serializer.errors
            })
            serializer.save()
            return Response({
                "status": True,
                "message":"ToDo is updated",
                "data":serializer.data
            })
        except Exception as e:
            print(e)
            return Response({
                "status":False,
                "message":"Something went wrong",
                "data": {}
            })