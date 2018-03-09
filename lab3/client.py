import zmq
import sys
from zmq.eventloop import ioloop, zmqstream
from multiprocessing import Process


def req_sender(user):
    context = zmq.Context()
    # push own messages to server
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
    # Tornado Event Loop
    ioloop.install()
    context = zmq.Context()
    # subscribe other messages from server
    sock_sub = context.socket(zmq.SUB)
    # no filter
    sock_sub.setsockopt_string(zmq.SUBSCRIBE, '')
    sock_sub.connect("tcp://127.0.0.1:5679")
    # register a print for when a message is ready to receive
    stream_sub = zmqstream.ZMQStream(sock_sub)

    def print_message(msg):
        msg = b''.join(msg).decode('ascii')
        if msg.find(user) == -1:
            print(msg)

    stream_sub.on_recv(print_message)
    ioloop.IOLoop.instance().start()


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
