# Generated by Django 4.2 on 2023-12-29 02:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CertificationAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True, null=True)),
                ('correct', models.BooleanField(blank=True, null=True)),
                ('ball', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CertificationLevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.IntegerField()),
                ('requirements', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Competency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certification_level', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teachers', to='Certification.certificationlevel')),
                ('competencies', models.ManyToManyField(blank=True, null=True, related_name='teachers', to='Certification.competency')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teacher', to=settings.AUTH_USER_MODEL)),
                ('сategory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teachers', to='Certification.category')),
            ],
        ),
        migrations.CreateModel(
            name='CertificationTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('content', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='certification_tasks')),
                ('competency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='Certification.competency')),
                ('level', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='Certification.certificationlevel')),
                ('сategory', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='Certification.category')),
            ],
        ),
        migrations.CreateModel(
            name='CertificationSession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('end_time', models.DateTimeField(blank=True, null=True)),
                ('score', models.IntegerField(blank=True, null=True)),
                ('passed', models.BooleanField(blank=True, default=False, null=True)),
                ('answer', models.ManyToManyField(null=True, related_name='certification_sessions', to='Certification.certificationanswer')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='certification_sessions', to='Certification.category')),
                ('competency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='certification_sessions', to='Certification.competency')),
                ('task', models.ManyToManyField(null=True, related_name='certification_sessions', to='Certification.certificationtask')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='certification_sessions', to='Certification.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='CertificationAnswerFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='certification_answers')),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='Certification.certificationanswer')),
            ],
        ),
        migrations.AddField(
            model_name='certificationanswer',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='Certification.certificationtask'),
        ),
        migrations.AddField(
            model_name='category',
            name='level',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='certification_sessions', to='Certification.certificationlevel'),
        ),
    ]
