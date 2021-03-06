# Generated by Django 2.0.2 on 2019-03-06 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0012_startslider'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aboutus',
            options={'verbose_name_plural': '1.3 AboutUs'},
        ),
        migrations.AlterModelOptions(
            name='belowaboutus',
            options={'verbose_name_plural': '1.4 BelowAboutUs'},
        ),
        migrations.AlterModelOptions(
            name='calltoaction',
            options={'verbose_name_plural': '1.5 Calltoaction'},
        ),
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name_plural': '3.3 Contact'},
        ),
        migrations.AlterModelOptions(
            name='contactdescription',
            options={'verbose_name_plural': '3.2 ContactDescription'},
        ),
        migrations.AlterModelOptions(
            name='footer',
            options={'verbose_name_plural': '3.4 Footer'},
        ),
        migrations.AlterModelOptions(
            name='portfoliocategories',
            options={'verbose_name_plural': '2.3 PortfolioCategories'},
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'verbose_name_plural': '2.4 Projects'},
        ),
        migrations.AlterModelOptions(
            name='skill',
            options={'verbose_name_plural': '2.2 Skill'},
        ),
        migrations.AlterModelOptions(
            name='skillsdescription',
            options={'verbose_name_plural': '2.1 SkillsDescription'},
        ),
        migrations.AlterModelOptions(
            name='slider',
            options={'verbose_name_plural': '1.2 Sliders'},
        ),
        migrations.AlterModelOptions(
            name='startslider',
            options={'verbose_name_plural': '1.1 startSliders'},
        ),
        migrations.AlterModelOptions(
            name='team',
            options={'verbose_name_plural': '3.1 Team'},
        ),
        migrations.AlterModelOptions(
            name='teamdescription',
            options={'verbose_name_plural': '2.5 TeamDescription'},
        ),
        migrations.AddField(
            model_name='calltoaction',
            name='linkHeader',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
