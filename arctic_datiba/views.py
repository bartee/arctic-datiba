from django.views.generic import TemplateView, FormView
from responses import JSONResponseMixin

class BlockValidateView(TemplateView, JSONResponseMixin):
    """
    Validate the block. Retrieve the block data, 

    """

    def post(self):
        """

        - accept post data
            -> create blank model instance
            -> call model_instance.clean and return errors on ... error.

        :return:
        """
        pass




class BlockDisplayView(TemplateView):

    pass

# , BlockUpdateView