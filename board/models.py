from django.db import models

# Create your models here.

# --------------------------
# Board 모델(테이블)은
# --------------------------
# 제목(subject),
# 내용(content), 
# 작성일시(datetimefieldcd ) 속성

class Board(models.Model):
    subject=models.CharField(max_length=200)
    content=models.TextField()
    create_date=models.DateTimeField(auto_now_add=True)
