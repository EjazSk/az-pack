import requests
import json
from st2common.runners.base_action import Action


__all__ = [
    'All'
]

class All(Action):

    def __init__(self, config) -> None:
        super(All,self).__init__(config)

        self.url = config.get('base_url')

    
    def run(self):
        result = requests.get(self.url).json()
        return result