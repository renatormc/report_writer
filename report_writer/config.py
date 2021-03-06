import os
from pathlib import Path
import tempfile

LIBDIR = Path(os.path.dirname(os.path.realpath(__file__)))
TEMPFOLDER = Path(tempfile.gettempdir(), "report_writer")
if not TEMPFOLDER.exists():
    TEMPFOLDER.mkdir()