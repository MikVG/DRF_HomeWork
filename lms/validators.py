from rest_framework.serializers import ValidationError


class VideoLinkValidator:

    def __init__(self, link):
        self.link = link

    def __call__(self, value):
        tmp_val = dict(value).get(self.link)
        if 'youtube.com' not in tmp_val:
            raise ValidationError("Можно прикреплять только ссылки с youtube.com")
