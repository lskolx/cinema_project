from rest_framework import serializers
from .models import Film, FilmImage

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


class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Film
        fields = "__all__"

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['images'] = FilmImageSerializer(FilmImage.objects.filter(film=instance.id), many=True).data
        # rep['reviews'] = ReviewSerializer(instance.review.filter(product=instance.id), many=True).data
        # total_rating = [i.rating for i in instance.review.all()]
        # if len(total_rating) != 0:
        #     rep['total_rating'] = sum(total_rating)/len(total_rating)
        # else:
        #     rep['total_rating'] = ""
        # rep['comments'] = CommentSerializer(Comment.objects.filter(product_id=instance), many=True).data
        return rep
