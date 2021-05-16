import requests
from st2common.runners.base_action import Action


__all__ = ["All"]


class One(Action):
    BASE_URL = "https://jsonplaceholder.typicode.com/todos"

    def __init__(self, config) -> None:
        super(One, self).__init__(config)

        self.id = self.config.get("id")

    def run(self):
        if self.url:
            result = requests.get(f"{self.url}/{self.id}").json()
        else:
            result = requests.get(f"{self.BASE_URL}/{self.id}").json()
        return result
