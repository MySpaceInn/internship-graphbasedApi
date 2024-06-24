# from rest_framework import serializers
# from project.app.model.user import MyUser

# class RegisterSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True)

#     class Meta:
#         model = MyUser
#         fields = ('email', 'password')

#     def create(self, validated_data):
#         user = MyUser.objects.create_user(
#             email=validated_data['email'],
#             password=validated_data['password']
#         )
#         return user
