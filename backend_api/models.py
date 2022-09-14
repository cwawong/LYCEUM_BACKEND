from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=50, null=True)
    message = models.TextField(null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE, null=True)
    tags = models.ManyToManyField('Tag', null=True)

    def __str__(self):
        return self.title if self.title else 'No Name found'


class User(models.Model):
    name = models.CharField(max_length=30)
    gender = models.CharField(max_length=1, choices=[('M', 'M'), ('F', 'F')])
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
    password_hash = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.name if self.name else 'No Name found'


class SubPost(models.Model):
    message = models.TextField(null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE, null=True)
    main_post = models.ForeignKey('Post', on_delete=models.CASCADE)

    def __str__(self):
        return 'Reply to ' + self.main_post.title


class Tag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
