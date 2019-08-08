from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=10)  # max_length 설정 필요
    content = models.TextField()  # 글자의 제한이 없다.
    created_at = models.DateTimeField(auto_now_add=True)  # 최초에 한번 기록되고 끝.마찬가지로 필요하다.
    updated_at = models.DateTimeField(auto_now=True)  # 계속 들어갈때마다 시간을 수정해줌

    def __str__(self):
        return f'{self.id}번글 - {self.title}: {self.content}'