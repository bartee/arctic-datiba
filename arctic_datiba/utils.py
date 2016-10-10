from django.apps import apps
from models import BlockModel
import inspect


class SuperModelService(object):
    """
    This service lets you filter all available models by supermodel.

    For example, if you want to have a list of all models that implement BlockModel,
    you can execute ::

        sms = SuperModelService()
        result = sms.get_submodels(BlockModel)

    """

    def __init__(self):
        self.models = apps.get_models()
        self.resultset = {}

    def get_submodels(self, classname):
        """

        :param classname:
        :return:
        """
        if not self.resultset.has_key(classname):
            result = {}
            for model in self.models:
                classes = inspect.getmembers(model, inspect.isclass)
                for class_dict_el in classes:
                    if issubclass(class_dict_el[1], classname) and class_dict_el[1] is not classname:
                        result.update({class_dict_el[0]: class_dict_el[1]})

            self.resultset.update({classname: result})

        return self.resultset.get(classname)