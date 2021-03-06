from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlockIP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('network', models.CharField(max_length=18, verbose_name='IP address or mask')),
                ('reason_for_block', models.TextField(blank=True, help_text='Optional reason for block', null=True)),
            ],
            options={
                'verbose_name': 'IPs & masks to ban',
                'verbose_name_plural': 'IPs & masks to ban',
            },
        ),
    ]
