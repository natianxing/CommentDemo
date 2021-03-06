# Generated by Django 3.0.3 on 2020-04-20 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CommentModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(default='userName', max_length=32)),
                ('userID', models.IntegerField()),
                ('paperID', models.IntegerField()),
                ('contentView', models.TextField(null=True)),
                ('pubTime', models.DateTimeField(auto_now=True)),
                ('likeNum', models.IntegerField()),
                ('dislikeNum', models.IntegerField()),
                ('hot', models.IntegerField()),
                ('replyCommentID', models.IntegerField()),
            ],
            options={
                'ordering': ('-pubTime',),
            },
        ),
    ]
