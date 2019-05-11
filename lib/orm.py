class ModelMixin:
    def to_dict(self):
        '''创建模型的属性字典'''
        attr_dict = {}
        for field in self._meta.get_fields():
            name = field.attname
            attr_dict[name] = getattr(self, name)
        return attr_dict
