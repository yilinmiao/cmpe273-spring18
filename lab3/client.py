import zmq
import sys
from multiprocessing import Process


def req_sender(user):
    context = zmq.Context()
    sock_push = context.socket(zmq.PUSH)
    sock_push.connect("tcp://127.0.0.1:5678")
    while True:
        try:
            msg = input("[%s] > " % user)
        except KeyboardInterrupt:
            continue
        if len(msg) != 0:
            sock_push.send_string("[{}]: ".format(user) + msg)


def sub_receiver(user):
    context = zmq.Context()
    sock_sub = context.socket(zmq.SUB)
    sock_sub.setsockopt_string(zmq.SUBSCRIBE, '')
    sock_sub.connect("tcp://127.0.0.1:5600")
    while True:
        msg = sock_sub.recv_string()      
        if msg.find(user) == -1:
            print("\n" + msg + "\n[%s] > " % user, end='')


if __name__ == "__main__":
    try:
        user = " ".join(sys.argv[1:])
        print("User[%s] Connected to the chat server." % user)
        Process(
            target=sub_receiver, args=[
                user,
            ]).start()
        req_sender(user)
    except Exception as e:
        print(e)
