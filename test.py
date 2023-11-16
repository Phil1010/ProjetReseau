import pickle
from message import Message

d = pickle.dumps(Message("create room", "aze"))
print(pickle.loads(d))

