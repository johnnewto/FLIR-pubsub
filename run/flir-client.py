from FLIR_pubsub import FLIR_client_utils as flir

if __name__ == '__main__':
    name='FrontLeft'
    # name='FrontRight'
    url='192.168.183.220'

    print(f'Connecting to {name} on {url}')
    flir.client(name=name, url=url)

