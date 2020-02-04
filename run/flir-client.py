import sys
from  pathlib import Path
sys.path.append(str(Path.cwd()))

from FLIR_pubsub import FLIR_client_utils

FLIR_client_utils.client(name='FrontLeft', url='localhost')


