import os
print('Exist:', os.access('C:\pp2\lab6\directoriies', os.F_OK))
print('Readable:', os.access('C:\pp2\lab6\directoriies', os.R_OK))
print('Writable:', os.access('C:\pp2\lab6\directoriies', os.W_OK))
print('Executable:', os.access('C:\pp2\lab6\directoriies', os.X_OK))
