from django.views.generic import TemplateView, FormView
from responses import JSONResponseMixin

class BlockValidateView(TemplateView, JSONResponseMixin):
    """
    Validate the block. Retrieve the block data,
    """

    def post(self):
        pass




class BlockDisplayView(TemplateView):

    pass

# , BlockUpdateView