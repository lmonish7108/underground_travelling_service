# Data access objects
class BaseDAO:

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
