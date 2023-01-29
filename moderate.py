
# block_words = ["Hoe", "http://", "nigger", "sand nigger",]

# @client.event
# async def on_message(msg):
#     if msg.author != client.user:
#         for text in block_words:
#             if "Moderator" not in str(msg.author.roles) and text in str(msg.content.lower()):
#                 await msg.delete()
#                 return
#         print("not deleting")