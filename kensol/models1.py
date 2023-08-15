# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class FfuappCasing(models.Model):
    id = models.BigAutoField(primary_key=True)
    item = models.CharField(max_length=50)
    necessary_quantity = models.IntegerField()
    estimate = models.ForeignKey('FfuappEstimate', models.DO_NOTHING, blank=True, null=True)
    material_cost = models.OneToOneField('FfuappMaterialcost', models.DO_NOTHING, blank=True, null=True)
    material_size = models.OneToOneField('FfuappMaterialsize', models.DO_NOTHING, blank=True, null=True)
    paint_cost = models.OneToOneField('FfuappPaintcost', models.DO_NOTHING, blank=True, null=True)
    planar_figure_size = models.OneToOneField('FfuappPlanarfiguresize', models.DO_NOTHING, blank=True, null=True)
    raw_material_thickness = models.OneToOneField('FfuappRawmaterialthickness', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'FFUapp_casing'


class FfuappEstimate(models.Model):
    id = models.BigAutoField(primary_key=True)
    size = models.CharField(max_length=50)
    motortype = models.CharField(db_column='motorType', max_length=50)  # Field name made lowercase.
    spec = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'FFUapp_estimate'


class FfuappMaterialcost(models.Model):
    id = models.BigAutoField(primary_key=True)
    won_per_kg = models.FloatField()

    class Meta:
        managed = False
        db_table = 'FFUapp_materialcost'


class FfuappMaterialsize(models.Model):
    id = models.BigAutoField(primary_key=True)
    width = models.FloatField()
    length = models.FloatField()
    manufacture_quantity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'FFUapp_materialsize'


class FfuappOption(models.Model):
    id = models.BigAutoField(primary_key=True)
    item = models.CharField(max_length=50)
    necessary_quantity = models.IntegerField()
    estimate = models.ForeignKey(FfuappEstimate, models.DO_NOTHING, blank=True, null=True)
    material_cost = models.OneToOneField(FfuappMaterialcost, models.DO_NOTHING, blank=True, null=True)
    material_size = models.OneToOneField(FfuappMaterialsize, models.DO_NOTHING, blank=True, null=True)
    paint_cost = models.OneToOneField('FfuappPaintcost', models.DO_NOTHING, blank=True, null=True)
    planar_figure_size = models.OneToOneField('FfuappPlanarfiguresize', models.DO_NOTHING, blank=True, null=True)
    raw_material_thickness = models.OneToOneField('FfuappRawmaterialthickness', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'FFUapp_option'


class FfuappPaintcost(models.Model):
    id = models.BigAutoField(primary_key=True)
    won_per_square_meter = models.FloatField()

    class Meta:
        managed = False
        db_table = 'FFUapp_paintcost'


class FfuappPlanarfiguresize(models.Model):
    id = models.BigAutoField(primary_key=True)
    width = models.FloatField()
    length = models.FloatField()

    class Meta:
        managed = False
        db_table = 'FFUapp_planarfiguresize'


class FfuappRawmaterial(models.Model):
    id = models.BigAutoField(primary_key=True)
    quality = models.CharField(max_length=50)
    weight = models.FloatField()

    class Meta:
        managed = False
        db_table = 'FFUapp_rawmaterial'


class FfuappRawmaterialthickness(models.Model):
    id = models.BigAutoField(primary_key=True)
    thickness = models.FloatField()
    raw_material = models.ForeignKey(FfuappRawmaterial, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'FFUapp_rawmaterialthickness'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


## 일반사양 자재비 ##
class GenMaterialcost(models.Model):
    item = models.CharField(primary_key=True, max_length=32) # item  # The composite primary key (item, size) found, that is not supported. The first column is selected.
    size = models.CharField(max_length=16) # ffu 규격
    matherialsize_width = models.FloatField() # 자재사이즈 가로
    matherialsize_length = models.FloatField() # 자재사이즈 세로
    rawmaterial_thickness = models.FloatField() # 원자재 두께
    rawmaterial_density = models.FloatField() # 원자재 비중
    manufacture_quantity = models.IntegerField() # 자재 가공수량
    necessary_quantity = models.IntegerField() # 자재 필요수량

    class Meta:
        managed = False
        db_table = 'gen_materialcost'
        unique_together = (('item', 'size'),)


## 고사양 자재비 ##
class HighMaterialcost(models.Model):
    item = models.CharField(primary_key=True, max_length=32) # item  # The composite primary key (item, size) found, that is not supported. The first column is selected.
    size = models.CharField(max_length=16) # ffu 규격
    matherialsize_width = models.FloatField() # 자재사이즈 가로
    matherialsize_length = models.FloatField() # 자재사이즈 세로
    rawmaterial_thickness = models.FloatField() # 원자재 두께
    rawmaterial_density = models.FloatField() # 원자재 비중
    manufacture_quantity = models.IntegerField() # 자재 가공수량
    necessary_quantity = models.IntegerField() # 자재 필요수량

    class Meta:
        managed = False
        db_table = 'high_materialcost'
        unique_together = (('item', 'size'),)


## 일반사양 도장비 ##
class GenPaint(models.Model):
    item = models.CharField(primary_key=True, max_length=32) # item  # The composite primary key (item, size) found, that is not supported. The first column is selected.
    size = models.CharField(max_length=16) # ffu 규격
    figure_width = models.FloatField() # 전개사이즈 가로
    figure_length = models.FloatField() # 전개사이즈 세로
    won_per_meter = models.IntegerField() # 원/m^2

    class Meta:
        managed = False
        db_table = 'gen_paint'
        unique_together = (('item', 'size'),)


## 고사양 도장비 ##
class HighPaint(models.Model):
    item = models.CharField(primary_key=True, max_length=32)  # item  # The composite primary key (item, size) found, that is not supported. The first column is selected.
    size = models.CharField(max_length=16) # ffu 규격
    figure_width = models.FloatField() # 전개사이즈 가로
    figure_length = models.FloatField() # 전개사이즈 세로
    won_per_meter = models.IntegerField() # 원/m^2

    class Meta:
        managed = False
        db_table = 'high_paint'
        unique_together = (('item', 'size'),)


## 일반사양 볼트 ##
class GenVolt(models.Model):
    size = models.CharField(primary_key=True, max_length=50) # ffu 규격  # The composite primary key (size, volt_name) found, that is not supported. The first column is selected.
    volt_name = models.CharField(max_length=50) # 볼트 품명 + 규격
    volt_price = models.IntegerField() # 단가
    volt_count = models.IntegerField() # 수량

    class Meta:
        managed = False
        db_table = 'gen_volt'
        unique_together = (('size', 'volt_name'),)


## 고사양 볼트 ##
class HighVolt(models.Model):
    size = models.CharField(primary_key=True, max_length=50) # ffu 규격  # The composite primary key (size, volt_name) found, that is not supported. The first column is selected.
    volt_name = models.CharField(max_length=50)  # 볼트 품명 + 규격
    volt_price = models.IntegerField() # 단가
    volt_count = models.IntegerField() # 수량

    class Meta:
        managed = False
        db_table = 'high_volt'
        unique_together = (('size', 'volt_name'),)


## 일반사양 NCT 가공비 ##
class GenNct(models.Model):
    size = models.CharField(primary_key=True, max_length=16) # ffu 규격
    nct_price = models.FloatField() # nct 판금 가공비

    class Meta:
        managed = False
        db_table = 'gen_nct'


## 고사양 NCT 가공비 ##
class HighNct(models.Model):
    size = models.CharField(primary_key=True, max_length=16) # ffu 규격
    nct_price = models.FloatField() # nct 판금 가공비 

    class Meta:
        managed = False
        db_table = 'high_nct'


## 일반사양 조립비 ##
class GenAssembly(models.Model):
    size = models.CharField(primary_key=True, max_length=16) # ffu 규격  # The composite primary key (size, assembly_price) found, that is not supported. The first column is selected.
    assembly_price = models.IntegerField() # 조립 인건비

    class Meta:
        managed = False
        db_table = 'gen_assembly'
        unique_together = (('size', 'assembly_price'),)


## 고사양 조립비 ##
class HighAssembly(models.Model):
    size = models.CharField(primary_key=True, max_length=16) # ffu 규격  # The composite primary key (size, assembly_price) found, that is not supported. The first column is selected.
    assembly_price = models.IntegerField() # 조립 인건비

    class Meta:
        managed = False
        db_table = 'high_assembly'
        unique_together = (('size', 'assembly_price'),)


## 일반사양 포장비 ##
class GenPack(models.Model):
    size = models.CharField(primary_key=True, max_length=16) # ffu 규격  # The composite primary key (size, pack_price) found, that is not supported. The first column is selected.
    pack_price = models.IntegerField() # 포장비

    class Meta:
        managed = False
        db_table = 'gen_pack'
        unique_together = (('size', 'pack_price'),)


## 고사양 포장비 ##
class HighPack(models.Model):
    size = models.CharField(primary_key=True, max_length=16) # ffu 규격  # The composite primary key (size, pack_price) found, that is not supported. The first column is selected.
    pack_price = models.IntegerField() # 포장비

    class Meta:
        managed = False
        db_table = 'high_pack'
        unique_together = (('size', 'pack_price'),)



