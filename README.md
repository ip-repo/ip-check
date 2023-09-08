<h2>Simple cli to check public ip</h2>

<hr>
This tool use <a href="https://icanhazip.com/"> icanhazip  </a> to get the user public ip address.<br>
The user can choose the <b>type</b> of ip address he want and also to copy it.
<br><br>
<h2>The options are:</h4>
<ul>
<li>-1 or --ipv4 : print the public ipv4 address.</li>
<li>-2 or --ipv6: print the  public ipv6 address.</li>
<li>-3 or --both: print the public ipv4 and ipv6 address.</li>
<li>-c or --copy: copy to cliboard the ip address.</li>
<li><b>no option: the program will act as if -1 was picked.</b></li>
</ul>
<br>
<h2>How to use:</h2>


```console
mkdir ip-cli #Create a new directory.

cd ip-cli    #Navigate to the new folder.

git clone https://github.com/ip-repo/ip-checker.git #Clone this repo.

python3 -m venv env-directory #Create a new virtual enivronment.

source env-directory/bin/activate #activate env

pip install -r ip-checker/requirements.txt #Install requiered python packages.

python3 ip-checker/get_public_ip.py #Run the script.

```


This will print the  public ipv4 address sence no options were stated.


<h3>Examples:</h3>

```console
python3 get_public_ip.py -h #get help

python3 get_public_ip.py --both #get ipv4 and ipv6

python3 get_public_ip.py --2 -c #get ipv6 and copy it to clipboard

```

<h3>Gui</h3>

```console
python3 get_public_ip.py --gui #launch gui
```
<image src="assets/gui.png">
<br>
<h2>Using as command from terminal</h2>

In the repo find the file <b>script.sh</b> and alter the paths to correspond with your system.

```console
#!/bin/bash

source /full/path/to/env/directory/bin/activate #activate env

python3 /full/path/to/python/script/get_public_ip.py --ipv -c #print and copy ipv4 address.

deactivate #deactivate env
```
Give execution rights to the owner.
```console
chmod u+x script.sh
```
Create alias for this script.

```console
sudo nano .bashrc

alias yourcommandname="/full/path/to/script.sh"


```
Now run the command.
```console 
yourcommandname
```
You should see your public ipv4 address and it will be copied to clipboard.
