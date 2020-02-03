from pathlib import Path
from  boxfish_flir_cam import FLIR_server_utils
FLIR_server_utils.register()

yaml_dir = Path.cwd() / 'nbs/common'
FLIR_server_utils.server(yaml_dir)
