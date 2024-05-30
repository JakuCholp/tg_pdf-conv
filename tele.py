import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
import django
from aiogram.types import FSInputFile
from asgiref.sync import sync_to_async
from django.utils import timezone
from django.db import transaction
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from django.db.models import Q
from aiogram.types import (KeyboardButton, Message, ReplyKeyboardMarkup,
                           ReplyKeyboardRemove)
from aiogram.types import CallbackQuery
import os

import io
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DocumentBot.settings')
django.setup()


from tgbot.models import DocumentType, User_doc, User_tg, Field, User_field, UserFieldsChange
data = DocumentType.objects.all()
result1 = list(data.values_list('name', flat=True))

numbered_items = []


import django











# для теста сохранения файла в файловую систему





for i, item in enumerate(result1, start=1):
    numbered_item = f"{i}) {item}"
    numbered_items.append(numbered_item)


output = '\n'.join(numbered_items)


users_waiting_for_product_name = {}




@sync_to_async
def get_document_field(document):
    with transaction.atomic():
        all_doc_field = Field.objects.filter(document=document)
        result11 = list(all_doc_field.values_list('display_name', flat=True))

        return result11





logging.basicConfig(level=logging.INFO)
bot = Bot(token="7013845085:AAHfjG1fEW3k2PhxzzM2OEfHS9TwvjtJOps")
dp = Dispatcher()


pool = None






@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    kb = [[types.KeyboardButton(text='select document to change')]]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("Привет! Я бот, который помогу заполнить pdf_forms. Напишите /select, чтобы получить список pdf-form", reply_markup=keyboard)

users_choise_field_change = {}

@dp.message(F.text == 'select field to change')
async def cmd_startd(message: types.Message):
    user_id = message.from_user.id
    user, created = await sync_to_async(User_tg.objects.get_or_create)(chat_id=user_id)
    userdoc = await latest_user_doc(user)
    all_us_field = await get_all_us_name_fields(userdoc)
    buttons = []


    for i in(all_us_field):
        button_text = f"{i}"
        button = InlineKeyboardButton(text=button_text, callback_data=str(i))
        buttons.append(button)

    inline_keyboard = [buttons] 
    keyboard = InlineKeyboardMarkup(inline_keyboard=inline_keyboard)
    try:
        del current_fill_process[user_id]
    except:
        pass
    users_choise_field_change[message.from_user.id] = True

    await message.answer('Выберите поле,которое хотите поменять:', reply_markup=keyboard)



chan_doc = {}

@dp.message(F.text == 'select document to change')
async def cmd_startd(message: types.Message):
    user_id = message.from_user.id
    chan_doc[user_id] = True
    user, created = await sync_to_async(User_tg.objects.get_or_create)(chat_id=user_id)
    userdoc_list = await list_user_doc(user)

    buttons = []


    for i in(userdoc_list):
        button_text = f"{i}"
        button = InlineKeyboardButton(text=button_text, callback_data=str(i))
        buttons.append(button)

    inline_keyboard = [buttons] 
    keyboard = InlineKeyboardMarkup(inline_keyboard=inline_keyboard)


    await message.answer('Выберите документ,который хотите поменять:', reply_markup=keyboard)





users_field_change = {}


@dp.callback_query()
async def process_callback(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    
    if user_id in users_waiting_for_product_name:
        selected_option = callback_query.data
        message_sim = types.Message(
            message_id=callback_query.message.message_id,
            from_user=callback_query.from_user,
            date=callback_query.message.date,
            chat=callback_query.message.chat,
            content_type='text',
            text=selected_option,
            reply_to_message_id=callback_query.message.message_id,
        )
        users_waiting_for_product_name[message_sim.from_user.id] = True
        await handle_product_name(message_sim)
    elif user_id in users_choise_field_change:
        selected_option = callback_query.data
        message_sim = types.Message(
            message_id=callback_query.message.message_id,
            from_user=callback_query.from_user,
            date=callback_query.message.date,
            chat=callback_query.message.chat,
            content_type='text',
            text=selected_option,
            reply_to_message_id=callback_query.message.message_id,
        )
        user_id = callback_query.from_user.id
        user = await sync_to_async(User_tg.objects.get)(chat_id=user_id)

        userdoc = await latest_user_doc(user)

        selected_field = callback_query.data
        await callback_query.message.answer(f'Вы выбрали поле "{selected_field}". Введите новое значение для этого поля.')
        users_choise_field_change[user_id] = selected_field
        users_field_change[user_id] = True
        await handle_product_name(message_sim)
    elif user_id in chan_doc:
        selected_option = callback_query.data
        message_sim = types.Message(
            message_id=callback_query.message.message_id,
            from_user=callback_query.from_user,
            date=callback_query.message.date,
            chat=callback_query.message.chat,
            content_type='text',
            text=selected_option,
            reply_to_message_id=callback_query.message.message_id,
        )
        user_id = callback_query.from_user.id
        user = await sync_to_async(User_tg.objects.get)(chat_id=user_id)

        await handle_product_name(message_sim)


        
    await callback_query.answer()










# chan_doc = {}

# @dp.message(Command("choose_doc_change"))
# async def cmd_startd(message: types.Message):
#     user_id = message.from_user.id
#     await message.answer(output)
#     chan_doc[user_id] = True
#     await message.answer('Выберите документ, который хотите поменять')







# @dp.message(Command("select"))
# async def cmd_start(message: types.Message):
#     await message.answer(output)
#     users_waiting_for_product_name[message.from_user.id] = True
#     await message.answer("Пожалуйста, введите название PDF-формы:")

@sync_to_async
def get_all_doc_type():
    data = DocumentType.objects.all()
    result1 = list(data.values_list('name', flat=True))

    return result1




@dp.message(Command("select"))
async def cmd_start(message: types.Message):

    result1 = await get_all_doc_type()
    buttons = []

    for i in(result1):
        button_text = f"{i}"
        button = InlineKeyboardButton(text=button_text, callback_data=str(i))
        buttons.append(button)

    inline_keyboard = [buttons] 
    keyboard = InlineKeyboardMarkup(inline_keyboard=inline_keyboard)
    users_waiting_for_product_name[message.from_user.id] = True
    await message.answer("Выберите PDF-форму:", reply_markup=keyboard)









@sync_to_async
def get_latest_user_doc_name(user):
    with transaction.atomic():
        user_doc = User_doc.objects.filter(Q(user=user)).order_by('-created_at').first()
        doc = user_doc.document if user_doc else None
        doc_name = doc.name

        return doc_name
    

@sync_to_async
def get_latest_user_fields_change(user, new_value):
    with transaction.atomic():
        user_field_change = UserFieldsChange.objects.filter(Q(user=user)).order_by('-created_at').first()
        user_field1 = user_field_change.user_field
        user_field1.value = new_value
        user_field1.save()
        return user_field1


@sync_to_async
def get_latest_user_doc(user):
    with transaction.atomic():
        user_doc = User_doc.objects.filter(Q(user=user)).order_by('-created_at').first()
        doc = user_doc.document if user_doc else None


        return doc
    


    


@sync_to_async
def get_field(field_name, document):
    with transaction.atomic():
        field = Field.objects.get(name = field_name, document = document)
        return field
    

@sync_to_async
def latest_user_doc(user):
    with transaction.atomic():
        user_doc = User_doc.objects.filter(Q(user=user)).order_by('-created_at').first()



        return user_doc
    


@sync_to_async
def list_user_doc(user):
    with transaction.atomic():
        list_user_doc = User_doc.objects.filter(Q(user=user))
        document_names = [user_doc.document.name for user_doc in list_user_doc]



        return document_names

    

@sync_to_async
def latest_user_doc_by_dc(user, document):
    with transaction.atomic():
        current_time = timezone.now()
        user_doc = User_doc.objects.filter(Q(user=user, document = document)).order_by('-created_at').first()
        user_doc.created_at = current_time
        user_doc.save()



        return user_doc




@sync_to_async
def get_user_field(user,userdoc,field):
    with transaction.atomic():
        user_field = User_field.objects.get(userdoc = userdoc, field = field)
        return user_field    
    

@sync_to_async
def get_all_us_name_fields(user_doc):
    all_finsihed_fields = User_field.objects.filter(userdoc = user_doc)
    field_names = list(all_finsihed_fields.values_list('field__display_name', flat=True))

    return field_names





@sync_to_async
def get_all_fields(document, user_doc):
    all_fields1 = list(Field.objects.filter(document=document).order_by('order'))
    user_fields = list(User_field.objects.filter(userdoc=user_doc).values_list('field', flat=True))
    all_user = list(Field.objects.filter(document=document, id__in=user_fields))
    all_fields = list(set(all_fields1) - set(all_user))
    return all_fields


@sync_to_async
def get_all_finished_fields(user_doc):
    all_finsihed_fields = User_field.objects.filter(userdoc = user_doc)
    user_fields_dict = {}
    for uf in all_finsihed_fields:
        user_fields_dict[uf.field.name] = uf.value

    return user_fields_dict

current_fill_process = {}

@dp.message(Command("fill"))
async def cmd_start(message: types.Message):
    kb = [[types.KeyboardButton(text='select field to change')]]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    user_id = message.from_user.id
    user, created = await sync_to_async(User_tg.objects.get_or_create)(chat_id=user_id)

    doc_name = await get_latest_user_doc_name(user)
    document = await get_latest_user_doc(user)
    userdoc = await latest_user_doc(user)
    await message.answer(doc_name)
    all_fields = await get_all_fields(document, userdoc)
    if all_fields:  
        current_fill_process[user_id] = {
            "document": document,
            "current_field_index": 0,
            "fields": all_fields
        }
        await message.answer(f"Отлично. Вы заполняете {all_fields[0].name}. Пожалуйста, напишите {all_fields[0].description}:", reply_markup=keyboard)
    else:
        await message.answer("Нет доступных полей для заполнения в этом документе.")

import time
@sync_to_async
def fill_res(userdoc, value):
    userdoc.result = value
    userdoc.save()



@dp.message()
async def handle_product_name(message: types.Message):
    user_id = message.from_user.id
    
    if user_id in users_waiting_for_product_name:
        user, created = await sync_to_async(User_tg.objects.get_or_create)(chat_id=user_id)
        if user_id in users_waiting_for_product_name:
            document_name = message.text
            del users_waiting_for_product_name[user_id]
            if document_name in result1:
                documen = await sync_to_async(DocumentType.objects.get)(name=document_name)
                new_user_doc = await sync_to_async(User_doc.objects.create)(user=user, document=documen)
                text = f'Отлично. Начните заполнять документ "{documen.name}". Напишите /fill чтобы начать'
            
                await bot.send_message(chat_id=message.chat.id, text=text)
    elif user_id in current_fill_process:
        process = current_fill_process[user_id]
        user = await sync_to_async(User_tg.objects.get)(chat_id=user_id) 
        user_doc_id =  await latest_user_doc(user=user)
        fields = process["fields"]
        current_field_index = process["current_field_index"]


        current_field = fields[current_field_index]

        user_field = await sync_to_async(User_field.objects.create)(userdoc = user_doc_id, field = current_field, value = message.text)
        doc = str(user_field.userdoc.document.name)
        iop = doc + str(message.chat.id)
        current_field_index += 1
        if current_field_index < len(fields):
            process["current_field_index"] = current_field_index
            next_field = fields[current_field_index]
            await message.answer(f"Отлично. Вы заполняете {next_field.display_name}. Пожалуйста, напишите {next_field.description}:")
        else:
            del current_fill_process[user_id]
            all_finished_fields = await get_all_finished_fields(user_doc_id)
            get_res = await fill_res(user_doc_id, all_finished_fields)
            # time.sleep(2)
            file_path = f'tg_pdf-conv/documents/{iop}.pdf'
            documentntn = FSInputFile(path=file_path, )
            await bot.send_document(message.chat.id, document=documentntn)
            await message.answer("Вы успешно заполнили все поля документа. Спасибо!")

    
    elif user_id in users_choise_field_change:
        field_name = message.text
        user, created = await sync_to_async(User_tg.objects.get_or_create)(chat_id=user_id)
        document = await get_latest_user_doc(user)
        field = await get_field(field_name=field_name, document=document)
        userdoc = await latest_user_doc(user)
        user_field = await get_user_field(user = user, field = field, userdoc = userdoc )
        user_fieldchange = await sync_to_async(UserFieldsChange.objects.create)(user = user, user_field = user_field)
        del users_choise_field_change[user_id]
    elif user_id in users_field_change:
        user, created = await sync_to_async(User_tg.objects.get_or_create)(chat_id=user_id)
        upd_value = message.text
        User_field_change = await get_latest_user_fields_change(user, upd_value)
        del users_field_change[user_id]
        await bot.send_message(chat_id=message.chat.id, text = "Чтобы продолжить заполнения напишите /fill")
    elif user_id in chan_doc:
        user, created = await sync_to_async(User_tg.objects.get_or_create)(chat_id=user_id)
        doc_name = message.text
        documentt = await sync_to_async(DocumentType.objects.get)(name=doc_name)
        all_fields_doc = await get_document_field(documentt)
        userdocc = latest_user_doc_by_dc(user, documentt)
        buttons = []

        for i in(all_fields_doc):
            button_text = f"{i}"
            button = InlineKeyboardButton(text=button_text, callback_data=str(i))
            buttons.append(button)

        inline_keyboard = [buttons] 
        keyboard = InlineKeyboardMarkup(inline_keyboard=inline_keyboard)

        await bot.send_message(chat_id=message.chat.id, text = 'Выберите поле, которое хотите поменять', reply_markup=keyboard)
       


    





async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())