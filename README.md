# ComicBookApp

Web application that consume the restful API of Comic Vine which is the largest comic database online.

Features:
-   Show a list of the last comics
    
-   Show a detail of the selected comic

## Prerequisites
This app was set with python 3.5, so you have to make sure that you have python3 installed in your machine.

It's better to set a virtual environment. To do that first install virtualenv:

    $ pip install virtualenv
    
 then we are going to create the virtualenv to run the app, please ru the following commands in your terminal:
 
    $ mkdir myvirtualEnvs && cd myvirtualEnvs
    $ virtualenv comicAppEnv -p $(which python3)
    $ cd
    

## Getting started

First clone this repository:

    $ git clone https://github.com/Noeuclides/ComicBookApp.git

then go to the repo's directory:

    $ cd ComicBookApp
    $ source ../myvirtualEnvs/comicAppEnv/bin/activate    

There you can install all the prerequisites to run the app in your computer:

    $ pip install -r requirements.txt

Before run the application you have to ask for an api key in the Comic Vine page, you can do that in the following link:
https://comicvine.gamespot.com/api/ 

## Run the App

Now you can run the app easily. In the application folder run the following command:

    $ python apiComic.py <your-api-key>

your-api-key is the key that you get from the Comic Vine page.

If everything goes well, you should see something like this:

    (comicAppEnv) $ ~/ComicBookApp/ master* python apiComic.py 0:8080 17f5af21b9359b8cbbf8f5153c87c6feb0183aa9
     * Serving Flask app "apiComic" (lazy loading)
     * Environment: production
       WARNING: This is a development server. Do not use it in a production deployment.
       Use a production WSGI server instead.
     * Debug mode: on
     * Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
     * Restarting with stat
     * Debugger is active!
     * Debugger PIN: 256-533-796

go to your browser and write "0.0.0.0:8080", like this:
![enter image description here](https://i.imgur.com/C38ZhOC.png)

And you'll see the full comics page (100 comics in a grid):
![enter image description here](https://i.imgur.com/cqNVf3h.png)

If you want to see the detail information of a comic type (with the ID of the comic):
![enter image description here](https://i.imgur.com/AxBXXDi.png)

And you'll see that specific comic's info page:
![enter image description here](https://i.imgur.com/fsVvlkI.png)


