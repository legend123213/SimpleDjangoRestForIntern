from djoser.serializers import UserSerializer as BaseUserSerializer,UserCreateSerializer as BaseCreate

class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ['id','username','email']

class UserCreateSerializer(BaseCreate):
    class Meta(BaseCreate.Meta):
        fields = ['id','email','username','password']
    