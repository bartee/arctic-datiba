import json


class Block(object):
    """
    Layout Blocks
    """
    type = "base"

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

    def validate(self, data):
        """
        Validate the input

        :param data:
        :return:
        """
        return True

