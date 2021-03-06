# Generated by Django 2.1.4 on 2019-01-03 23:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cource', '0003_auto_20181116_2340'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContestType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('standings_name', models.CharField(max_length=200)),
                ('olymp', models.BooleanField(default=False)),
                ('max_score_for_olymp_problem', models.IntegerField(default=100)),
                ('enable_marks', models.BooleanField(default=False)),
                ('show_standings_left_link', models.BooleanField(default=False)),
                ('allow_standings', models.BooleanField(default=True)),
                ('exec_for_marks', models.TextField(default='# variables: user_score, max_possible_score, max_reached_score, num_of_problems, user_id\n# arrays: problem_score, num_of_solves_for_problem (problems are zero-numerated)\n# should assign mark to variable: marks[mark_key]')),
            ],
        ),
        migrations.RemoveField(
            model_name='contest',
            name='olymp',
        ),
        migrations.RemoveField(
            model_name='course',
            name='contest_mark_formula',
        ),
        migrations.RemoveField(
            model_name='course',
            name='distur_mark_formula',
        ),
        migrations.RemoveField(
            model_name='course',
            name='enable_disturs',
        ),
        migrations.RemoveField(
            model_name='course',
            name='enable_marks',
        ),
        migrations.AddField(
            model_name='contest',
            name='exec_for_marks',
            field=models.TextField(default='# variables: user_score, max_possible_score, max_reached_score, num_of_problems, user_id\n# arrays: problem_score, num_of_solves_for_problem (problems are zero-numerated)\n# should assign mark to variable: marks[mark_key]'),
        ),
        migrations.AddField(
            model_name='contest',
            name='show_in_standings',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='course',
            name='proxy_pass_links',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='contest',
            name='duration',
            field=models.FloatField(default=100000000),
        ),
        migrations.AddField(
            model_name='contesttype',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contest_types', to='cource.Course'),
        ),
        migrations.AddField(
            model_name='contest',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contests', to='cource.ContestType'),
        ),
    ]
