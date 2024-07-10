# Advanced_Lessons => Add Logging To Your Code 
- Print Out To Console Or File
- Print Logs Of What Happens
<hr>

- DEBUG
- INFO
- WARNING
- ERROR
- CRITICAL
## name => Logging Module Give It To The Default Logger.
Basic Config
- level => Level of Severity
- filename => File Name and Extension
- mode => Mode Of The File a => Append
- format => Format For The Log Message

## getLogger => Return a Logger With the Specified Name
```python []
import logging

# print(dir(logging))

logging.basicConfig(filename="myApp.log", filemode="a", 
                    format="(%(asctime)s) | %(name)s | %(levelname)s -> '%(message)s'",
                    datefmt="%d %b %Y, %H:%M:%S")

myLogger = logging.getLogger("khaled")

logging.warning("this is warning msg")
myLogger.warning("this is warning msg")
myLogger.error("this is eror msg")
myLogger.critical("this is critical msg")
```