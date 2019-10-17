from colorama import Fore

def print_usage():
    """
    Display Banner
    """
    BANNER = '''
 _____    _ _ _   ___
| ____|__| (_) |_|_ _|_ __ ___   __ _  __ _  ___
|  _| / _` | | __|| || '_ ` _ \ / _` |/ _` |/ _ \\
| |__| (_| | | |_ | || | | | | | (_| | (_| |  __/
|_____\__,_|_|\__|___|_| |_| |_|\__,_|\__, |\___|
                                      |___/
    '''

    USAGE = '''
usage: editimage.py : 1.0.0 [-h] [--version] [--mode {comp,resize}] [-q Q]
                            [-o O] [--height HEIGHT] [--witdh WITDH]
                            input
jpg encoder given images.
positional arguments:
  input                 input file
optional arguments:
  -h, --help            show this help message and exit
  --version             show program's version number and exit
  --mode {comp,resize}  mode choice
  -q Q                  quality (0 to 100)
  -o O                  output file (default=resize.jpg)
  --height HEIGHT       Image height (default=100)
  --witdh WITDH         Image width (default=100)
'''

    print(Fore.YELLOW + BANNER)
    print(Fore.WHITE + USAGE)

<<<<<<< HEAD:usage.py
=======
    return 0

>>>>>>> 30cbdc2cc2d984b27aea19058fce1d9b83c70dc2:src/usage.py
print_usage()
