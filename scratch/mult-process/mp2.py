from multiprocessing import Process, Queue
sentinel = -1
import time

def creator(data, q):
    """
    Creates data to be consumed and waits for the consumer
    to finish processing
    """
    print('Creating data and putting it on the queue')
    for item in data:
        time.sleep(0.5)
        q.put(item)

def my_consumer(q):
    """
    Consumes some data and works on it
    In this case, all it does is double the input
    """
    print('my_consumer')

    while True:
        data = q.get()
        # print('data found to be processed: {}'.format(data))
        processed = data * 2
        print(data, processed)
        time.sleep(0.1)
        if data is sentinel:
            break

if __name__ == '__main__':
    q = Queue()

    data = [5, 10, 13, 5, 10, 13, 5, 10, 13, 5, 10, 13, 5, 10, 13, 5, 10, 13, -1]
    process_one = Process(target=creator, args=(data, q))
    process_two = Process(target=my_consumer, args=(q,))
    process_one.start()
    process_two.start()
    for i in range(20):
        print('.', end='')


    print('Waiting for processes')
    q.close()
    q.join_thread()
    process_one.join()
    process_two.join()