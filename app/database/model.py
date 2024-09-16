from sqlalchemy import (
    create_engine,
    String,
    Integer,
    LargeBinary,
    DateTime,
    Enum,
    ForeignKey
)
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    relationship
)
from datetime import datetime

from app.utils.types import *

class Base(DeclarativeBase):
    pass



class Chat(Base):
    __tablename__ = 'chats'
    
    chatid: Mapped[str] = mapped_column(String(64), primary_key=True)
    pub: Mapped[str] = mapped_column(String(256), nullable=False)
    passphrase: Mapped[str] = mapped_column(String(256), nullable=False)

    messages: Mapped[list["Message"]] = relationship(back_populates="chat")

class Message(Base):
    __tablename__ = 'messages'
    
    message_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    chat_id: Mapped[str] = mapped_column(ForeignKey('chats.chatid'), nullable=False)
    sender_pub_key: Mapped[str] = mapped_column(String(256), nullable=False)
    receiver_pub_key: Mapped[str] = mapped_column(String(256), nullable=False)
    encrypted_message: Mapped[bytes] = mapped_column(LargeBinary, nullable=False)
    timestamp: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    message_status: Mapped[MessageStatus] = mapped_column(Enum(MessageStatus), default=MessageStatus.sent)
    message_type: Mapped[MessageType] = mapped_column(Enum(MessageType), default=MessageType.text) 

    chat: Mapped["Chat"] = relationship(back_populates="messages")

engine = create_engine('sqlite:///p2p_messenger.db')


Base.metadata.create_all(engine)
