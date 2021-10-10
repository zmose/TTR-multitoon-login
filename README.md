# TTR-multitoon-login
quick way to log into multiple toons without inputting username/pass every time

# What do you need
* Python 3.6+ installed
* python packages (just pip install <<package>> in bash/cmd/PS/etc, but you should have pretty much all of these in the default python install):
  * os
  * requests
  * time
  * config

# How To Use
1. Copy the ```config.py``` and ```launch.py``` files and put them in your ```Toontown Rewritten``` directory (should be same level as phase files, ```Launcher.exe```, and ```TTREngine.exe```)
2. Go into config.py in your favorite IDE
  a. Change parameters in ```usernames``` array to your desired usernames. Be sure to remember quotes. You may also add onto the end of the array or take away parameters if you are only logging with 2 or 3 multitoons.
  b. Change parameters in ```passwords``` array to your desired passwords. Be sure to remember quotes. You may also add onto the end of the array or take away parameters if you are only logging with 2 or 3 multitoons. Be sure to match number of passwords with number of usernames as I did not add error handling in this hackjob.
3. Execute launch.py and watch as windows are opened. First the python terminal, and then x instances of Toontown. 
