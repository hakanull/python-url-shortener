<h1 align="center">
  <br>
  <br>
  Python URL Shortener
  <br>
</h1>


<div align="center">
    <img src="https://i.ibb.co/Y7Nbcqg/git.png" width="600px"</img> 
</div>

## Update Notes

Aug 10 - 2023
*Added function to update source url of shortened url

Aug 5 - 2023
* Shortened url list edited to sort new to oldest.
* QR code border added.
* QR code download button added.
* Interface navigation buttons added.


## Key Features


This web application basically intended to shorten long links and track link clicks.

* /
  - / a standard index rotation from which our functions begin.
* /create_link
  - /create_link link is the part where the output of the transactions made after the abbreviation and the qr code are found
* /links
  - With the /links rotation, you can access the database image with information such as shortened links, number of clicks.

## How To Use

First clone this repository and after install requirements with command "pip install -r requirements.txt". From your command line:

```bash
# Clone this repository
$ git clone https://github.com/ihakan0/url_shortener_sv.git

# Go into the repository
$ cd url_shortener_sv
# install requirements
$ pip install -r requirements.txt

# Run the app
#You must be in the same folder as the "__init__.py" file before running the command
$ flask run
```
