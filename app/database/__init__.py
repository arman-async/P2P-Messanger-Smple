from .model import *

engine = create_engine('sqlite:///p2p_messenger.db')
Base.metadata.create_all(engine)