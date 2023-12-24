from sqlalchemy.orm import Session
import models, schemas
from openai import OpenAI
import os
from dotenv import load_dotenv
import asyncio

load_dotenv()


# all functions