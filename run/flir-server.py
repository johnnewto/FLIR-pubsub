import sys
from  pathlib import Path
sys.path.append(str(Path.cwd()))

from FLIR_pubsub import FLIR_server_utils
FLIR_server_utils.register()

yaml_dir = Path.cwd() / 'nbs/common'
FLIR_server_utils.server(yaml_dir)
