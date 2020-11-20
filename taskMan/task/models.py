from django.db import models
from accounts.models import User


""" プロジェクトモデル """
class Project(models.Model):
    project_cd = models.AutoField(
        primary_key=True
    )

    name = models.CharField(
        max_length=25,
        verbose_name='プロジェクト名'
    )

    leader = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='leader',
        verbose_name='プロジェクトリーダ'
    )

    start_date = models.DateField(
        null=True,
        blank=True,
        verbose_name='開始日'
    )

    end_date = models.DateField(
        null=True,
        blank=True,
        verbose_name='終了日'
    )

    details = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        verbose_name='詳細'
    )

    update_date = models.DateField(
        auto_now=True
    )

    is_delete = models.BooleanField(
        default=False
    )


""" プロジェクト To ユーザ （1 対 多） """
class ProjectToUsers(models.Model):
    project_cd = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="account"
    )

    user_cd = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )


class Task(models.Model):
    PRIOLITY_NUMBER = (
        (0, '未選択'),
        (1, '最低'),
        (2, '低'),
        (3, '常'),
        (4, '高'),
        (5, '最高')
    )

    task_cd = models.AutoField(
        primary_key=True
    )

    task_name = models.CharField(
        max_length=100,
        verbose_name='タスク名'
    )

    user_name = models.CharField(
        max_length=30,
        null=True,
        blank=True,
        verbose_name='担当者名'
    )

    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='担当者'
    )

    start_date = models.DateField(
        null=True,
        blank=True,
        verbose_name='開始日'
    )

    end_date = models.DateField(
        null=True,
        blank=True,
        verbose_name='終了日'
    )

    details = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        verbose_name='詳細'
    )

    priolity = models.IntegerField(
        choices=PRIOLITY_NUMBER,
        default=0
    )

    update_date = models.DateField(
        auto_now=True
    )

    is_delete = models.BooleanField(
        default=False
    )

""" プロジェクト To タスク （1 対 多） """
class ProjectToTask(models.Model):
    project_cd = models.ForeignKey(
        Project,
        on_delete=models.CASCADE
    )

    task_cd = models.ForeignKey(
        Task,
        on_delete=models.CASCADE
    )