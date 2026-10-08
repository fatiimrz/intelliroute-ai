
from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class AIResponse:
    provider: str
    model: str
    content: str
    input_tokens: int = 0
    output_tokens: int = 0


class BaseProvider(ABC):

    @abstractmethod
    async def generate(
        self,
        prompt: str,
        model: str
    ) -> AIResponse:
        pass
