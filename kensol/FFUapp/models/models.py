from django.db import models

## 자재비 산출
# 원자재
class RawMaterial(models.Model):
    quality = models.CharField(max_length = 50)     # 재질
    weight = models.FloatField()                    # 비중
 
# 원자재_두께
class RawMaterialThickness(models.Model):
    raw_material = models.ForeignKey(RawMaterial,
                                        on_delete = models.SET_NULL,
                                        null = True)
    thickness = models.FloatField()   # 두께

# 전개 사이즈
class PlanarFigureSize(models.Model):
    width = models.FloatField()                     # 가로
    length = models.FloatField()                    # 세로

    @property
    def 중량(self):
        return (self.width * self.length
                * self.casing.raw_material_thickness.thickness * self.casing.raw_material_thickness.raw_material.weight) / 1000000 * self.casing.necessary_quantity


# 자재 사이즈
class MaterialSize(models.Model):
    width = models.FloatField()                     # 가로
    length = models.FloatField()                    # 세로
    manufacture_quantity = models.IntegerField()                # 가공수량

# 자재비
class MaterialCost(models.Model):
    won_per_kg = models.FloatField()                     # 원/kg
    
    @property
    def 중량(self):                                 # 중량
        return (self.casing.MaterialSize.width * self.casing.MaterialSize.length
                * self.casing.raw_material_thickness.thickness
                * self.casing.raw_material_thickness.raw_material.weight / 1000000) / self.casing.MaterialSize.manufacture_quantity * self.casing.necessary_quantity

    @property
    def 원자재금액(self):                           # 원자재금액
        return self.won_per_kg * self.중량


# 견적
class Estimate(models.Model):
    size = models.CharField(max_length = 50)            # 규격
    motorType = models.CharField(max_length = 50)       # 모터 종류
    spec = models.CharField(max_length = 50)        # 일반 / 고사양

# 도장비
class PaintCost(models.Model):
    won_per_square_meter = models.FloatField()                     # 원/m^2

    @property
    def square_meter(self):                                 # m^2
        return (self.PlanarFigureSize.width * self.PlanarFigureSize.length) / 1000000 * 2

    @property
    def 도장금액(self):                           # 도장금액
        return self.square_meter * self.won_per_square_meter


# Casing
class Casing(models.Model):
    item = models.CharField(max_length = 50)       # 이름
    necessary_quantity = models.IntegerField()                # 필요수량
    estimate = models.ForeignKey(Estimate,          # 견적
                                    related_name = 'casings',
                                    on_delete = models.SET_NULL,
                                    null = True)
    raw_material_thickness = models.OneToOneField(RawMaterialThickness,    # 원자재_두께
                                            on_delete = models.SET_NULL,
                                            
                                            null = True)
    planar_figure_size = models.OneToOneField(PlanarFigureSize,                              # 전개 사이즈
                                related_name = 'casing',
                                on_delete = models.SET_NULL,
                                null = True)
    material_size = models.OneToOneField(MaterialSize,                              # 자재 사이즈
                                related_name = 'casing',
                                on_delete = models.SET_NULL,
                                null = True)
    material_cost = models.OneToOneField(MaterialCost,                              # 자재비
                                related_name = 'casing',
                                on_delete = models.SET_NULL,
                                null = True)
    paint_cost = models.OneToOneField(PaintCost,                              # 도장비
                                related_name = 'casing',
                                on_delete = models.SET_NULL,
                                null = True)

# Option
class Option(models.Model):
    item = models.CharField(max_length = 50)       # 이름
    necessary_quantity = models.IntegerField()                # 필요수량
    estimate = models.ForeignKey(Estimate,          # 견적
                                    related_name = 'option',
                                    on_delete = models.SET_NULL,
                                    null = True)
    raw_material_thickness = models.OneToOneField(RawMaterialThickness,    # 원자재_두께
                                            on_delete = models.SET_NULL,
                                            
                                            null = True)
    planar_figure_size = models.OneToOneField(PlanarFigureSize,                              # 전개 사이즈
                                related_name = 'option',
                                on_delete = models.SET_NULL,
                                null = True)
    material_size = models.OneToOneField(MaterialSize,                              # 자재 사이즈
                                related_name = 'option',
                                on_delete = models.SET_NULL,
                                null = True)
    material_cost = models.OneToOneField(MaterialCost,                              # 자재비
                                related_name = 'option',
                                on_delete = models.SET_NULL,
                                null = True)
    paint_cost = models.OneToOneField(PaintCost,                              # 도장비
                                related_name = 'option',
                                on_delete = models.SET_NULL,
                                null = True)
    


#############################################
############# ffu 샘플 데이터 ################
#############################################

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