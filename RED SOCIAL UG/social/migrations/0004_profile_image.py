from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0003_auto_20201007_0744'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='logoUgbat.jpg', upload_to=''),
        ),
    ]
