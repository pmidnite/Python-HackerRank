# HackerRank Python Preparation(Step By Step)
## Introduction
### Downloading and Installing Python

You can download Python for Windows, macOS, and Ubuntu for free at [Python](https://python.org/downloads/).
If you download the latest version from the website’s download page, all of the programs in this git will work.

On the download page, you’ll find Python installers for 64-bit and 32-bit computers for each operating system, so first figure out which installer you need. If you bought your computer in 2007 or later, it is most likely a 64-bit system. Otherwise, you have a 32-bit version, but here’s how to find out for sure:

**_On Windows_**
> Select Start ▸ Control Panel ▸ System and check whether System Type says 64-bit or 32-bit.

**_On macOS_**
> Go the Apple menu, select About This Mac ▸ More Info ▸ System Report ▸ Hardware, and then look at the Processor Name field. If it says Intel Core Solo or Intel Core Duo, you have a 32-bit machine. If it says anything else (including Intel Core 2 Duo), you have a 64-bit machine.

**_On Ubuntu Linux_**
> Open a Terminal and run the command uname -m. A response of i686 means 32-bit, and x86_64 means 64-bit.

* On Windows, download the Python installer (the filename will end with .msi) and double-click it. Follow the instructions the installer displays on the screen to install Python, as listed here:
> Select Install for All Users and click Next.
Accept the default options for the next several windows by clicking Next.

* On macOS, download the .dmg file that’s right for your version of macOS and double-click it. Follow the instructions the installer displays on the screen to install Python, as listed here:
> When the DMG package opens in a new window, double-click the Python.mpkg file. You may have to enter the administrator password.
Accept the default options for the next several windows by clicking Continue and click Agree to accept the license.
On the final window, click Install.

* If you’re running Ubuntu, you can install Python from the Terminal by following these steps:
> Open the Terminal window.
> 1. Enter sudo apt-get install python3.
> 2. Enter sudo apt-get install idle3(Not Mandatory).
> 3. Enter sudo apt-get install python3-pip.
> 4. Install any editor Like Sublime-text, Vscode, Atom, Zed Etc.
> 5. The above editor can be used to write code in local system.
