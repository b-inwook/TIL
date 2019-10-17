`create.html` 에서 image 파일 업로드할 수 있는 부분 만들어주기

```html
{% load static %}

<form action="{% url 'articles:create' %}" method="POST" enctype="multipart/form-data">
    <label for="image">Image</label>
    <input type="file" name="image" id="image" accept="image/*">
```

- `<form>` 태그 안에 인코딩타입 설정 꼭 해줘야!
  - `enctype="multipart/form-data"` 

 - `accept="image/*"` 는 업로드 가능한 이미지 파일만 보여줌
 - `{% load static %}` 이 태그가 필요한 이유는 내장된 이미지에는 주소값이  X 부여
    - 사용자가 올린 이미지(media)는 주소값이 자동 부여되니까 필요 없음



사용자가 업로드한 이미지 detail에서 보고싶은데 안보임

==> 업로드한 이미지 파일이 venv 폴더 안에 마구잡이로 들어감

==> 경로 설정해주자!!

```python
# settings.py

# STATIC_URL과 비슷
# 업로드된 파일의 주소(URL)를 만들어줌
# 실제 이미지 파일이 업로드 된 디렉토리는 아님
MEDIA_URL = '/media/'

# 사용자가 업로드한 이미지 파일의 저장 위치
# 업로드가 끝난 이미지 파일을 위치 시킬 최상위 경로
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```



```python
# url.py / 프로젝트 아래

from django.conf import settings
from django.conf.urls.static import static

# 파일이 업로드 된 이후에 프로젝트 내부에 존재하는 파일의 주소를 만들어줌
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```



```python
# 경로 설정 후 업로드한 이미지 확인
# TERMINAL

In [2]: article = Article.objects.get(pk=11)

In [3]: article.image.url
Out[3]: '/media/bighero.JPG'	# media 라는 폴더 자동 생성 후 그 안에 저장

In [4]: article.image.name
Out[4]: 'bighero.JPG'

In [5]: article.image.path
Out[5]: 'C:\\Users\\student\\TIL\\03_Django\\04_django_crud_review\\media\\bighero.JPG'
```



`input type="file"` 인 경우에는 `update.html`에서 기존 이미지를 띄우지는 못함

==> 그냥 바로 덮어쓰기 `article.image = request.FILES.get('image')`



이전에 등록한 이미지 없는 글 Error 해결하기

==> image가 없을 때 'no image' 이미지 띄워주기

```html
<!-- detail.html -->
<!-- update.html -->

{% if article.image %}
        <img src="{{ article.image.url }}" alt="{{ article.image }}">
{% else %}
        <img src="{% static 'articles/images/noimage.jpg' %}" alt="noimage">
{% endif %}
```



이미지를 resizing 하기 위한 라이브러리 설치

`$ pip install pilkit django-imagekit`

```python
# settings.py

INSTALLED_APPS = [
    'imagekit',
]
```

```python
# models.py

from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail

class Article(models.Model):
    # image = models.ImageField(blank=True)
    image = ProcessedImageField(
        processors=[Thumbnail(200, 300)], # 처리할 이미지 사이즈
        format='JPEG', # 저장 이미지 포맷
        options={'quality': 90}, # 추가 옵션(원본의 90%로 압축) | 보통 70~90
        upload_to='articles/images', # MEDIA_ROOT(media)/articles/images
    )
```



원본이미지 ==> make migrations도 필요없음

```python
# models.py
from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import Thumbnail

class Article(models.Model):
    image = models.ImageField(blank=True)
    image_thumbnail = ImageSpecField(
        source='image', # 원본 이미지 필드명
        processors=[Thumbnail(300, 200)],
        format='JPEG',
        options={'quality': 90},
    )
```



'몇 번' 글의 이미지 파일인지 경로 업데이트

```python
# models.py

# 이미지 업로드 경로 커스텀
# instance => Article 모델의 인스턴스 객체
# filename => 사용자가 업로드한 파일의 이름
def articles_image_path(instance, filename):
    return f'articles/{instance.pk}번글/images/{filename}'

class Article(models.Model):
    image = ProcessedImageField(
        processors=[Thumbnail(300, 200)], # 처리할 이미지 사이즈
        format='JPEG', # 저장 이미지 포맷
        options={'quality': 90}, # 추가 옵션(원본의 90%로 압축) | 보통 70~90
        upload_to=articles_image_path, # MEDIA_ROOT(media)/articles/images
    )
```



글을 생성한 시점에는 pk가 부여되지 않아서 ==> `None번 글`

글을 수정한 후에는 pk 부여 ==> `22번 글`



favicon 설정하기

