import enum

class MessageStatus(enum.Enum):
    sent = "sent"
    received = "received"
    read = "read"

class MessageType(enum.Enum):
    text = "text"
    image = "image"
    video = "video"
    audio = "audio"
    file = "file"

class UserStatus(enum.Enum):
    online = "online"
    offline = "offline"
