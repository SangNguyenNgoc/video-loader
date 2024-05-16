import asyncio
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from Service.DiscordBot import bot
from Service.YoutubeService import YoutubeService

app = FastAPI()

youtubeService = YoutubeService()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup_event():
    asyncio.create_task(bot.start())


@app.get("/")
async def root(url: str):
    result = await youtubeService.download_video(url)
    return result


@app.get("/hello/{name}")
async def say_hello(name: str):
    # print(name)
    return {"message": f"Hello {name}"}
