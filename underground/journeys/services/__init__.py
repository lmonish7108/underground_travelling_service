# Data access objects
class BaseDAO:

    @classmethod
    def get_obj(cls, **kwargs):
        return cls.model.objects.get(**kwargs)

    @classmethod
    def create_obj(cls, **kwargs):
        return cls.model.objects.create(**kwargs)

    @classmethod
    def filter_obj(cls, **kwargs):
        return cls.model.objects.filter(**kwargs)
    
    @classmethod
    def get_or_create_obj(cls, **kwargs):
        return cls.model.objects.get_or_create(**kwargs)
    
    @classmethod
    def update_obj(cls, **kwargs):
        return cls.model.objects.filter(**kwargs['filters']).update(**kwargs['updates'])
    
    @classmethod
    def update_or_create_obj(cls, **kwargs):
        return cls.model.objects.update_or_create(**kwargs)
    
    @classmethod
    def list_obj(cls, **kwargs):
        return cls.models.objects.filter(**kwargs.get('filters')).values(*kwargs['columns'])
