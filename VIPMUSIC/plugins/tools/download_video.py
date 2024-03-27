






@app.on_callback_query(filters.regex("download_video") & ~BANNED_USERS)
@languageCB
async def download_video(client, CallbackQuery, _):
    callback_data = CallbackQuery.data.strip()
    videoid = callback_data.split(None, 1)[1]
    user_id = CallbackQuery.from_user.id
