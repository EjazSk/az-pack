import requests
import json
from st2common.runners.base_action import Action


__all__ = ["All"]


class All(Action):
    BASE_URL = "https://jsonplaceholder.typicode.com/todos"

    def __init__(self, config) -> None:
        super(All, self).__init__(config)

        self.url = config.get("base_url")

    def run(self):
        if self.url:
            result = requests.get(self.url).json()
        else:
            result = requests.get(self.BASE_URL).json()
        return result
