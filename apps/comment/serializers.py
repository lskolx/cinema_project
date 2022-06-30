from rest_framework import serializers
from .models import Comment, Like


# class CommentSerializer(serializers.ModelSerializer):
#     author = serializers.CharField(read_only=True)
#     created_at = serializers.DateTimeField(read_only=True)
#     film = serializers.PrimaryKeyRelatedField(queryset=Film.objects.all(), write_only=True)

#     class Meta:
#         model = Comment
#         fields = "__all__"



class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['user'] = request.user
        review = Comment.objects.create(**validated_data)
        return review

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['like'] = instance.like.filter(like=True).count()
        rep['film'] = str(instance)
        return rep