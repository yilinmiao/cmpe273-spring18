import zmq


def start():
    context = zmq.Context()
    sock_pull = context.socket(zmq.PULL)
    sock_pub = context.socket(zmq.PUB)
    sock_pull.bind("tcp://127.0.0.1:5678")
    sock_pub.bind("tcp://127.0.0.1:5600")
    while True:
        msg = sock_pull.recv_string()
        sock_pub.send_string(msg)
        print(msg)


if __name__ == "__main__":
    try:
        start()
    except Exception as e:
        print(e)
