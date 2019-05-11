from django.db import models


class Vip(models.Model):
    '''VIP表'''
    name = models.CharField(max_length=32, verbose_name='会员等级对应的名称')
    level = models.IntegerField(verbose_name='VIP 等级')
    price = models.FloatField(verbose_name='会员等级对应的价格')


class Permission(models.Model):
    '''权限表'''
    name = models.CharField(max_length=16, verbose_name='权限名称')
    desc = models.TextField(verbose_name='对权限的描述')


class VipPermRelation(models.Model):
    '''Vip 和 权限 的关系表'''
    vip_id = models.IntegerField()
    perm_id = models.IntegerField()
