from dataclasses import dataclass
from abc import abstractmethod, ABC
from typing import Any, Union

from sqlalchemy import Select, Update, Delete


@dataclass
class AbstractFilter(ABC):
    @abstractmethod
    def apply(self, query: Any) -> Union[Select, Update, Delete]:
        pass
