# Generated by Django 2.0 on 2017-12-27 13:42

from django.db import migrations, models
import django.db.models.deletion
import products.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent_path', products.fields.LtreeField(db_index=True, editable=False)),
                ('name', models.CharField(max_length=30)),
                ('active', models.BooleanField(default=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='products.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent_path', products.fields.LtreeField(db_index=True, editable=False)),
                ('name', models.CharField(max_length=30)),
                ('active', models.BooleanField(default=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='products.Category')),
            ],
        ),
    ]
