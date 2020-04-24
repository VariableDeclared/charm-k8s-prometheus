
import sys
sys.path.append('lib')
from ops.charm import CharmBase
from ops.main import main


class MyCharm(CharmBase):
    pass


if __name__ == "__main__":
    main(MyCharm)

