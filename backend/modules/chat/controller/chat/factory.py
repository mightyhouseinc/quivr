from uuid import UUID

from .brainful_chat import BrainfulChat
from .brainless_chat import BrainlessChat


def get_chat_strategy(brain_id: UUID | None = None):
    return BrainfulChat() if brain_id else BrainlessChat()
