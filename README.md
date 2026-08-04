# python

Python
│
├── Built-in Functions
│   ├── print()
│   ├── input()
│   ├── len()
│   ├── type()
│   ├── id()
│   ├── help()
│   ├── dir()
│   ├── open()
│   ├── range()
│   ├── enumerate()
│   ├── zip()
│   ├── sorted()
│   ├── sum()
│   ├── min()
│   ├── max()
│   ├── abs()
│   ├── round()
│   ├── map()
│   ├── filter()
│   ├── any()
│   ├── all()
│   └── ...
│
├── File Handling
│   ├── open()
│   │
│   ├── File Object Methods
│   │   ├── read()
│   │   ├── readline()
│   │   ├── readlines()
│   │   ├── write()
│   │   ├── writelines()
│   │   ├── seek()
│   │   ├── tell()
│   │   ├── flush()
│   │   └── close()
│   │
│   ├── Modes
│   │   ├── "r"
│   │   ├── "w"
│   │   ├── "a"
│   │   ├── "x"
│   │   ├── "rb"
│   │   ├── "wb"
│   │   └── "ab"
│   │
│   └── Context Manager
│       └── with open(...)
│
├── Standard Library
│   │
│   ├── os
│   │   ├── getcwd()
│   │   ├── chdir()
│   │   ├── listdir()
│   │   ├── mkdir()
│   │   ├── makedirs()
│   │   ├── remove()
│   │   ├── rename()
│   │   ├── replace()
│   │   ├── rmdir()
│   │   ├── walk()
│   │   ├── scandir()
│   │   ├── system()
│   │   ├── getenv()
│   │   ├── cpu_count()
│   │   └── path
│   │       ├── exists()
│   │       ├── join()
│   │       ├── dirname()
│   │       ├── basename()
│   │       ├── splitext()
│   │       ├── isfile()
│   │       ├── isdir()
│   │       ├── abspath()
│   │       ├── realpath()
│   │       ├── getsize()
│   │       ├── getctime()
│   │       └── getmtime()
│   │
│   ├── pathlib
│   │   ├── Path()
│   │   ├── cwd()
│   │   ├── exists()
│   │   ├── mkdir()
│   │   ├── rename()
│   │   ├── unlink()
│   │   ├── iterdir()
│   │   ├── read_text()
│   │   └── write_text()
│   │
│   ├── shutil
│   │   ├── copy()
│   │   ├── copy2()
│   │   ├── copytree()
│   │   ├── move()
│   │   ├── rmtree()
│   │   └── make_archive()
│   │
│   ├── math
│   │   ├── sqrt()
│   │   ├── pow()
│   │   ├── ceil()
│   │   ├── floor()
│   │   ├── factorial()
│   │   ├── sin()
│   │   ├── cos()
│   │   ├── pi
│   │   └── e
│   │
│   ├── random
│   │   ├── random()
│   │   ├── randint()
│   │   ├── randrange()
│   │   ├── choice()
│   │   ├── choices()
│   │   ├── sample()
│   │   ├── shuffle()
│   │   └── seed()
│   │
│   ├── datetime
│   │   ├── datetime.now()
│   │   ├── date.today()
│   │   ├── timedelta()
│   │   ├── strftime()
│   │   └── strptime()
│   │
│   ├── time
│   │   ├── sleep()
│   │   ├── time()
│   │   ├── ctime()
│   │   └── perf_counter()
│   │
│   ├── json
│   │   ├── load()
│   │   ├── loads()
│   │   ├── dump()
│   │   └── dumps()
│   │
│   ├── csv
│   │   ├── reader()
│   │   ├── writer()
│   │   ├── DictReader()
│   │   └── DictWriter()
│   │
│   ├── re
│   │   ├── search()
│   │   ├── match()
│   │   ├── findall()
│   │   ├── finditer()
│   │   ├── sub()
│   │   ├── split()
│   │   └── compile()
│   │
│   ├── sqlite3
│   │   ├── connect()
│   │   ├── cursor()
│   │   ├── execute()
│   │   ├── executemany()
│   │   ├── fetchone()
│   │   ├── fetchall()
│   │   ├── commit()
│   │   └── close()
│   │
│   ├── threading
│   │   ├── Thread()
│   │   ├── Lock()
│   │   ├── Event()
│   │   └── start()
│   │
│   ├── multiprocessing
│   │   ├── Process()
│   │   ├── Pool()
│   │   ├── Queue()
│   │   └── Lock()
│   │
│   ├── logging
│   │   ├── basicConfig()
│   │   ├── info()
│   │   ├── warning()
│   │   ├── error()
│   │   ├── debug()
│   │   └── critical()
│   │
│   ├── collections
│   │   ├── Counter
│   │   ├── defaultdict
│   │   ├── deque
│   │   ├── OrderedDict
│   │   └── namedtuple
│   │
│   ├── itertools
│   │   ├── count()
│   │   ├── cycle()
│   │   ├── repeat()
│   │   ├── chain()
│   │   ├── combinations()
│   │   └── permutations()
│   │
│   ├── functools
│   │   ├── reduce()
│   │   ├── lru_cache()
│   │   ├── partial()
│   │   └── wraps()
│   │
│   ├── hashlib
│   │   ├── md5()
│   │   ├── sha1()
│   │   ├── sha256()
│   │   └── sha512()
│   │
│   ├── uuid
│   │   ├── uuid1()
│   │   └── uuid4()
│   │
│   ├── socket
│   │   ├── socket()
│   │   ├── bind()
│   │   ├── listen()
│   │   ├── connect()
│   │   ├── send()
│   │   └── recv()
│   │
│   ├── subprocess
│   │   ├── run()
│   │   ├── Popen()
│   │   ├── call()
│   │   └── check_output()
│   │
│   └── abc
│       ├── ABC
│       └── abstractmethod