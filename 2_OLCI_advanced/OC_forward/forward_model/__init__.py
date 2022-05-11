"""
Ocean Colour Forward Model
~~~~~~~~~~~~~~~
"""
from .__version__ import __title__, __description__, __url__, __version__ 
from .__version__ import __author__, __author_email__, __license__

from .forward_model import ForwardModel
from .read_samples import read_rrs_samples 
from .read_params import read_iop_params, read_iops
