
res = [str(x) for x in xrange(1, 6)]
show_keyboard1 = {'keyboard': [res]}
tmp_message = ''
for i in range(len(res)):
    tmp_message = tmp_message + str(i) + '\n'
bot.sendMessage(msg['from']['id'], '1212', reply_markup=show_keyboard1)