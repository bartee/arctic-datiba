import json
from django.db.models import Model, fields

class BlockModel(Model):
    """
    Block Model

    """
    type = "base"
    is_active = fields.BooleanField()
    context = fields.TextField()
    updated_at = fields.DateTimeField(auto_now=True, auto_now_add=True)


    def get_context_data(self):
        pass

    @property
    def context_data(self):
        """
        Return the block context as a string

        :return: dict
        """
        try:
            context = json.loads(self.context)
            if not context:
                context = {}
        except (ValueError, TypeError):
            context = {}
        return context
