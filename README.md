# Youtube Downloader
This code was made for fun to test out [Selenium Web Driver](https://selenium-python.readthedocs.io/).

## How to use the code
* Clone the repository and install Selenium WebDriver:<br>

    ```bash
    $ git clone https://github.com/Mastermind0100/Youtube-Downloader.git
    $ pip install selenium
    ```
* You will also need to install the WebDriver for whichever browser you prefer. I have used Google Chrome here. Link for downloading is [here](https://selenium-python.readthedocs.io/installation.html#drivers).
* Go to the file urls.txt and save all the links from [YouTube](https://www.youtube.com/) you want to download, in separate lines.
* Open ytdownloader.py in an editor or IDE and edit line 15 to be whatever location you have installed the WebDriver in
* Run the code, in the file directory:<br>

    ```bash
    python ytdownloader.py
    ```
* You can select the quality of download on the website. That bit is left for user discretion and is not automated.