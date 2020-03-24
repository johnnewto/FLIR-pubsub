import sys, os
from  pathlib import Path
sys.path.append(str(Path.cwd()))

from FLIR_pubsub import FLIR_server_utils as flir

if __name__ == '__main__':
    flir.register()
    # print('Path.cwd() ', Path.cwd())
    # yaml_dir = Path.cwd() / '../nbs/common'
    # # yaml_dir = Path('./nbs/common')
    dir_path = os.path.dirname(os.path.realpath(__file__))
    yaml_dir = Path(dir_path)
    flir.server(yaml_dir)

# /home/john/github/FLIR_pubsub/nbs/common/19312752.yaml
# nbs/common/19312752.yamlls