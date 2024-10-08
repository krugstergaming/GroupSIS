# Generated by Django 3.0.7 on 2024-08-20 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='attendance_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='leavereportstaff',
            name='leave_status',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='leavereportstudent',
            name='leave_status',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='students',
            name='address',
            field=models.TextField(default='Planet Earth'),
        ),
        migrations.AlterField(
            model_name='students',
            name='lrn',
            field=models.TextField(default=123456789102, max_length=12),
        ),
        migrations.CreateModel(
            name='StudentResult',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('subject_exam_marks', models.FloatField(default=0)),
                ('subject_assignment_marks', models.FloatField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student_management_app.Students')),
                ('subject_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student_management_app.Subjects')),
            ],
        ),
    ]
