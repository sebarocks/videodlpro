# About

Videodlpro is a webapp for downloading videos using yt-dlp module. It allows downloading videos and converting to mp3 (using FFMpeg). Built using FastAPI backend and Svelte frontend, it uses WebSockets to show download status in real time.

# Installation

## Requirements:

* Python (pip)
* Node.js (npm)
* FFMpeg

## Setting up .env

First, copy .env file

`cd app`

`cp .env.example .env `

Then feel free to edit it according to your enviroment


## Python:

`cd api`

`pip install -r requirements.txt`

`uvicorn main:app`

It will run on port 8000 by default

## Node.js (npm)

`cd app`

`npm install`

`npm run prod`

It will run on port 3000 by default