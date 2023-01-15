from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from db.sqlite_db import sql_add_admin, admin_chek
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.filters import Text

class FSMadd(StatesGroup):
    typ = State()
    tmid = State()
    name = State()

kb = InlineKeyboardMarkup(row_width=3).add(InlineKeyboardButton(text="admin", callback_data="admin"),
                                           InlineKeyboardButton(text="techer", callback_data="techer"),
                                           InlineKeyboardButton(text="student", callback_data="student"))

#begining add_humen
async def abegining_add(message : types.Message):
    if admin_chek(message.from_user.id) == 1:
        await FSMadd.typ.set()
        await message.answer("Whom?", reply_markup=kb)
    
#begining delit_humen
async def abegining_delit(message : types.Message):
    pass

#Exit FMS
async def exit_fms(message: types.message, state: FSMContext):
    _state = await state.get_state()
    if _state is None:
        return
    state.finish()
    await state.finish()
    await message.answer("OK")

#add_humen2
async def typ_add(call: types.CallbackQuery, state: FSMadd):
    if admin_chek(call.from_user.id):
        async with state.proxy() as data:
            data['typ'] = call.data
        await FSMadd.next()
        await call.message.answer("Whot tmid?")
        await call.answer()
    
#add_humen3
async def tmid_add(message: types.Message, state: FSMadd):
    if admin_chek(message.from_user.id):
        async with state.proxy() as data:
            data['tmid'] = message.text
        await FSMadd.next()
        await message.answer("Whot name?")

#add_humen4
async def name_add(message: types.Message, state: FSMadd):
    if admin_chek(message.from_user.id):
        async with state.proxy() as data:
            data['name'] = message.text
        await sql_add_admin(state)
        await state.finish()


def register_message_Admin(dp : Dispatcher):
    dp.register_message_handler(abegining_add, commands = 'add', state = None)
    dp.register_message_handler(exit_fms, commands = 'exit', state = "*")
    dp.register_callback_query_handler(typ_add, Text(startswith=""), state = FSMadd.typ)
    dp.register_message_handler(tmid_add, content_types="text", state = FSMadd.tmid)
    dp.register_message_handler(name_add, content_types="text", state = FSMadd.name)
