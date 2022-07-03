from rest_framework import serializers
from .models import Film, FilmImage, Favorites
from ..comment.models import Comment
from ..comment.serializers import CommentSerializer
from ..rating.serializers import RatingSerializer

class FilmImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = FilmImage
        fields = ('image',)

    def _get_image_url(self, obj):
        if obj.image:
            url = obj.image.url
            request = self.context.get('request')
            if request is not None:
                url = request.build_absolute_uri(url)
        else:
                url = ""
        return url

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['image'] = self._get_image_url(instance)
        return rep


class FavoritesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorites
        fields = "__all__"

    def get_favorite(self, obj):
            if obj.is_favorite:
                return obj.is_favorite
            return ''

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['favorites'] = self.get_favorite(instance)
        return rep


class FilmSerializer(serializers.ModelSerializer):

    # author = serializers.ReadOnlyField(source='author.email')
    
    class Meta:
        model = Film
        fields = "__all__"
    
    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['author'] = request.user
        favorites = Film.objects.create(**validated_data)
        return favorites

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['images'] = FilmImageSerializer(FilmImage.objects.filter(film=instance.id), many=True).data
        rep['ratings'] = RatingSerializer(instance.rating.filter(film=instance.id), many=True).data
        total_rating = [i.rating for i in instance.rating.all()]
        if len(total_rating) != 0:
            rep['total_rating'] = sum(total_rating)/len(total_rating)
        else:
            rep['total_rating'] = ""
        rep['comments'] = CommentSerializer(Comment.objects.filter(film_id=instance), many=True).data
        # rep['like'] = instance.like.filter(like=True).count()
        return rep
        