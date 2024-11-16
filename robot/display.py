#!/usr/bin/env python3
from vilib import Vilib

try:
    Vilib.camera_start(vflip=False, hflip=False)
    Vilib.show_fps()
    Vilib.display(local=True, web=True) 
except KeyboardInterrupt:
    pass
except Exception as e:
    print(f"se acabo")
finally:
    Vilib.camera_close()