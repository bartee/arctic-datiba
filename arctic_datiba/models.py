import json
from django.db.models import Model, fields


class BlockModel(Model):
    """
    Abstract Block Model
    Blocks have a type, and - apart from some status info - contain a JSON field

    """
    type = "base"
    is_active = fields.BooleanField()
    context = fields.TextField()
    updated_at = fields.DateTimeField(auto_now=True)

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

    def clean_context(self):
        """
        Return the context, see if it's valid JSON.

        :return:
        """
        pass

    class Meta:
        abstract = True
