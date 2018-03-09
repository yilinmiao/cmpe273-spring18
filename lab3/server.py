import zmq
import time


def start():
    context = zmq.Context()
    # Pull messages from each client
    sock_pull = context.socket(zmq.PULL)
    # publish messages to all clients
    sock_pub = context.socket(zmq.PUB)
    sock_pull.bind("tcp://127.0.0.1:5678")
    sock_pub.bind("tcp://127.0.0.1:5679")
    # ZMQ Poller
    poller = zmq.Poller()
    poller.register(sock_pull, zmq.POLLIN)
    while True:
        socks = dict(poller.poll())
        # poll the sockets to check if we have messages to recv and publish it
        if sock_pull in socks and socks[sock_pull] == zmq.POLLIN:
            msg = sock_pull.recv_string()
            sock_pub.send_string(msg)
            print(msg)
        time.sleep(0.1)


if __name__ == "__main__":
    try:
        start()
    except Exception as e:
        print(e)
