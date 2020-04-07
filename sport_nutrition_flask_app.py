import flask
import telebot
from sport_nutrition_keyboards import Generate
from telebot import types
import time
import os
import re


TOKEN 
WEBHOOK_HOST
WEBHOOK_LISTEN = '0.0.0.0'

bot = telebot.TeleBot(TOKEN)

app = flask.Flask(__name__)
app.config["DEBUG"] = True


def do_write(cid, cost):
    file1 = open('files/info.txt', "a")
    file1.write(cid)
    file1.write(cost)
    file1.write('\n')
    file1.close()


def do_read():
    file1 = open('files/info.txt', "r")
    in_file = file1.read()
    file1.close()
    return in_file


def rewriting_file(cid):
    in_file = do_read()
    in_file = re.sub(cid, '_', in_file)
    file1 = open('files/info.txt', "w")
    file1.write(in_file)
    file1.close()


def show_data(id):
    dl = len(id)
    with open('files/info.txt') as file1:
        price = [int(line[dl:]) for line in file1 if id in line]
    cost = 0
    for i in range(len(price)):
        cost += int(price[i])
    return cost


# Process web hook calls
@app.route('/' + TOKEN, methods=['POST'])
def get_message():
    update = flask.request.get_json()

    if "callback_query" in update:

# Protein
        if 'ip1' in call_data:
            if call_data == 'ip1p1':
                do_write(chatid, '10')
                bot.answer_callback_query(call_id, "Added")
            elif call_data == 'ip1p2':
                do_write(chatid, '20')
                bot.answer_callback_query(call_id, "Added")
            elif call_data == 'ip1p3':
                do_write(chatid, '30')
                bot.answer_callback_query(call_id, "Added")
            elif call_data == 'ip1p4':
                do_write(chatid, '40')
                bot.answer_callback_query(call_id, "Added")
            if call_data == "ip1next1":
                bot.edit_message_text(chat_id=chatid, message_id=mesid, text='WGS 450gr',
                                      reply_markup=Generate().inl_protein_first_pos_one())
            elif call_data == "ip1next2":
                bot.edit_message_text(chat_id=chatid, message_id=mesid, text='909gr',
                                      reply_markup=Generate().inl_protein_first_pos_two())
            elif call_data == 'ip1next3':
                bot.edit_message_text(chat_id=chatid, message_id=mesid, text='2.27kg',
                                      reply_markup=Generate().inl_protein_first_pos_three())
            elif call_data == 'ip1next4':
                bot.edit_message_text(chat_id=chatid, message_id=mesid, text='4.54kg',
                                      reply_markup=Generate().inl_protein_first_pos_four())

        if 'ip2' in call_data:
            if call_data == 'ip2p1':
                do_write(chatid, '10')
                bot.answer_callback_query(call_id, "Added")
            elif call_data == 'ip2p2':
                do_write(chatid, '20')
                bot.answer_callback_query(call_id, "Added")
            if call_data == "ip2next1":
                bot.edit_message_text(chat_id=chatid, message_id=mesid, text='WGSN 907gr',
                                      reply_markup=Generate().inl_protein_second_pos_one())
            elif call_data == "ip2next2":
                bot.edit_message_text(chat_id=chatid, message_id=mesid, text='2.27kg',
                                      reply_markup=Generate().inl_protein_second_pos_two())

        # Support | Test
        if 'ip3' in call_data:
            if call_data == 'ip3p1':
                bot.answer_callback_query(call_id, "Added")
                do_write(chatid, '10')
            if call_data == 'ip3next1':
                bot.edit_message_text(chat_id=chatid, message_id=mesid, text='722gr',
                                      reply_markup=Generate().inl_protein_third_pos_one())

        if 'ip4' in call_data:
            if call_data == 'ip4p1':
                bot.answer_callback_query(call_id, "Added")
                do_write(chatid, '10')
            elif call_data == 'ip4p2':
                bot.answer_callback_query(call_id, "Added")
                do_write(chatid, '20')
            if call_data == "ip4next1":
                bot.edit_message_text(chat_id=chatid, message_id=mesid, text='795gr',
                                      reply_markup=Generate().inl_protein_fourth_pos_one())
            elif call_data == "ip4next2":
                bot.edit_message_text(chat_id=chatid, message_id=mesid, text='1.59kg',
                                      reply_markup=Generate().inl_protein_fourth_pos_two())

        if 'ip5' in call_data:
            if call_data == 'ip5p1':
                bot.answer_callback_query(call_id, "Added")
                do_write(chatid, '10')
            elif call_data == 'ip5p2':
                bot.answer_callback_query(call_id, "Added")
                do_write(chatid, '20')
            if call_data == "ip5next1":
                bot.edit_message_text(chat_id=chatid, message_id=mesid, text='1.36kg',
                                      reply_markup=Generate().inl_protein_fifth_pos_one())
            elif call_data == "ip5next2":
                bot.edit_message_text(chat_id=chatid, message_id=mesid, text='2.26kg',
                                      reply_markup=Generate().inl_protein_fifth_pos_two())

        if 'ip6' in call_data:
            if call_data == 'ip6p1':
                bot.answer_callback_query(call_id, "Added")
                do_write(chatid, '10')
            if call_data == 'ip6p2':
                bot.answer_callback_query(call_id, "Added")
                do_write(chatid, '20')
            if call_data == "ip6next1":
                bot.edit_message_text(chat_id=chatid, message_id=mesid, text='1.36kg',
                                      reply_markup=Generate().inl_protein_sixth_pos_one())
            elif call_data == "ip6next2":
                bot.edit_message_text(chat_id=chatid, message_id=mesid, text='2.26kg',
                                      reply_markup=Generate().inl_protein_sixth_pos_two())

        if 'ip7' in call_data:
            if call_data == 'ip7p1':
                bot.answer_callback_query(call_id, "Added")
                do_write(chatid, '10')
            elif call_data == 'ip7p2':
                bot.answer_callback_query(call_id, "Added")
                do_write(chatid, '20')
            if call_data == "ip7next1":
                bot.edit_message_text(chat_id=chatid, message_id=mesid, text='909gr',
                                      reply_markup=Generate().inl_protein_seventh_pos_one())
            elif call_data == "ip7next2":
                bot.edit_message_text(chat_id=chatid, message_id=mesid, text='1.81kg',
                                      reply_markup=Generate().inl_protein_seventh_pos_two())

        if 'ip8' in call_data:
            if call_data == 'ip8p1':
                bot.answer_callback_query(call_id, "Added")
                do_write(chatid, '10')
            if call_data == "ip8next1":
                bot.edit_message_text(chat_id=chatid, message_id=mesid, text='1.81kg',
                                      reply_markup=Generate().inl_protein_eigth_pos_one())

        if 'ip9' in call_data:
            if call_data == 'ip9p1':
                bot.answer_callback_query(call_id, "Added")
                do_write(chatid, '10')
            if call_data == "ip9next1":
                bot.edit_message_text(chat_id=chatid, message_id=mesid, text='720gr',
                                      reply_markup=Generate().inl_protein_eigth_pos_one())

# Gainer    TEXT odnorangovyh positsiy include in Logic part
        if 'ig1' in call_data:
            if call_data == 'ig1p1':
                bot.answer_callback_query(call_id, "Added")
                do_write(chatid, '10')
            if call_data == 'ig1p2':
                bot.answer_callback_query(call_id, "Added")
                do_write(chatid, '20')
            if call_data == 'ig1p3':
                bot.answer_callback_query(call_id, "Added")
                do_write(chatid, '30')

            if call_data == "ig1next1":
                bot.edit_message_text(chat_id=chatid, message_id=mesid, text='GSG 51grP',
                                      reply_markup=Generate().inl_gainer_first_pos_one())
            elif call_data == "ig1next2":
                bot.edit_message_text(chat_id=chatid, message_id=mesid, text='2.30kg',
                                      reply_markup=Generate().inl_gainer_first_pos_two())
            elif call_data == 'ig1next3':
                bot.edit_message_text(chat_id=chatid, message_id=mesid, text='4.67kg',
                                      reply_markup=Generate().inl_gainer_first_pos_three())

        if 'ig2' in call_data:
            if call_data == 'ig2p1':
                bot.answer_callback_query(call_id, "Added")
                do_write(chatid, '10')

        if 'ig3' in call_data:
            if call_data == 'ig3p1':
                bot.answer_callback_query(call_id, "Added")
                do_write(chatid, '10')
            if call_data == 'ig3p2':
                bot.answer_callback_query(call_id, "Added")
                do_write(chatid, '20')
            if call_data == "ig3next1":
                bot.edit_message_text(chat_id=chatid, message_id=mesid, text='SM 2.72kg',
                                      reply_markup=Generate().inl_gainer_first_pos_one())
            elif call_data == "ig3next2":
                bot.edit_message_text(chat_id=chatid, message_id=mesid, text='5.44kg',
                                      reply_markup=Generate().inl_gainer_first_pos_two())

# Creatine
        if 'ic1' in call_data:
            if call_data == 'ic1p1':
                bot.answer_callback_query(call_id, "Added")
                do_write(chatid, '10')
            if call_data == 'ic1p2':
                bot.answer_callback_query(call_id, "Added")
                do_write(chatid, '20')
            if call_data == 'ic1p3':
                bot.answer_callback_query(call_id, "Added")
                do_write(chatid, '30')
            if call_data == 'ic1p4':
                bot.answer_callback_query(call_id, "Added")
                do_write(chatid, '40')
            if call_data == "ic1next1":
                bot.edit_message_text(chat_id=chatid, message_id=mesid, text='C Powder 150gr',
                                      reply_markup=Generate().inl_creatine_first_pos_one())
            elif call_data == "ic1next2":
                bot.edit_message_text(chat_id=chatid, message_id=mesid, text='300gr',
                                      reply_markup=Generate().inl_creatine_first_pos_two())
            elif call_data == 'ic1next3':
                bot.edit_message_text(chat_id=chatid, message_id=mesid, text='600gr',
                                      reply_markup=Generate().inl_creatine_first_pos_three())
            elif call_data == 'ic1next4':
                bot.edit_message_text(chat_id=chatid, message_id=mesid, text='1200gr',
                                      reply_markup=Generate().inl_creatine_first_pos_four())

        if 'ic2' in call_data:
            if call_data == 'ic2p1':
                bot.answer_callback_query(call_id, "Added")
                do_write(chatid, '10')
# Amino
        if 'ia1' in call_data:
            if call_data == 'ia1p1':
                bot.answer_callback_query(call_id, "Added")
                do_write(chatid, '10')
            if call_data == 'ia1p2':
                bot.answer_callback_query(call_id, "Added")
                do_write(chatid, '20')
            if call_data == 'ia1p3':
                bot.answer_callback_query(call_id, "Added")
                do_write(chatid, '30')
            if call_data == 'ia1p4':
                bot.answer_callback_query(call_id, "Added")
                do_write(chatid, '40')
            if call_data == "ia1next1":
                bot.edit_message_text(chat_id=chatid, message_id=mesid, text='18gr',
                                      reply_markup=Generate().inl_amino_first_pos_one())
            if call_data == "ia1next2":
                bot.edit_message_text(chat_id=chatid, message_id=mesid, text='270gr',
                                      reply_markup=Generate().inl_amino_first_pos_two())
            if call_data == "ia1next3":
                bot.edit_message_text(chat_id=chatid, message_id=mesid, text='300gr',
                                      reply_markup=Generate().inl_amino_first_pos_three())
            if call_data == "ia1next4":
                bot.edit_message_text(chat_id=chatid, message_id=mesid, text='585gr',
                                      reply_markup=Generate().inl_amino_first_pos_four())

        if 'ia2' in call_data:
            if call_data == 'ia2p1':
                do_write(chatid, '10')
                bot.answer_callback_query(call_id, "Added")

        if 'ia3' in call_data:
            if call_data == 'ia3p1':
                do_write(chatid, '10')
                bot.answer_callback_query(call_id, "Added")
            if call_data == 'ia3p2':
                do_write(chatid, '20')
                bot.answer_callback_query(call_id, "Added")
            if call_data == "ia3next1":
                bot.edit_message_text(chat_id=chatid, message_id=mesid, text='A 2000 160tab',
                                      reply_markup=Generate().inl_amino_third_pos_one())
            if call_data == "ia3next2":
                bot.edit_message_text(chat_id=chatid, message_id=mesid, text='320tab',
                                      reply_markup=Generate().inl_amino_third_pos_two())

        if 'ia4' in call_data:
            if call_data == 'ia4p1':
                do_write(chatid, '10')
                bot.answer_callback_query(call_id, "Added")

        if 'ia5' in call_data:
            if call_data == 'ia5p1':
                do_write(chatid, '10')
                bot.answer_callback_query(call_id, "Added")
# BCAA
        if 'ib1' in call_data:
            if call_data == 'ib1p1':
                do_write(chatid, '10')
                bot.answer_callback_query(call_id, "Added")

        if 'ib2' in call_data:
            if call_data == 'ib2p1':
                do_write(chatid, '10')
                bot.answer_callback_query(call_id, "Added")

        if 'ib3' in call_data:
            if call_data == 'ib3p1':
                do_write(chatid, '10')
                bot.answer_callback_query(call_id, "Added")
            if call_data == 'ib3p2':
                do_write(chatid, '20')
                bot.answer_callback_query(call_id, "Added")
            if call_data == "ib3next1":
                bot.edit_message_text(chat_id=chatid, message_id=mesid, text='B 1000 200pil',
                                      reply_markup=Generate().inl_bcaa_third_pos_one())
            if call_data == "ib3next2":
                bot.edit_message_text(chat_id=chatid, message_id=mesid, text='400pil',
                                      reply_markup=Generate().inl_bcaa_third_pos_two())

        if 'ib4' in call_data:
            if call_data == 'ib4p1':
                do_write(chatid, '10')
                bot.answer_callback_query(call_id, "Added")
            if call_data == 'ib4p2':
                do_write(chatid, '20')
                bot.answer_callback_query(call_id, "Added")
            if call_data == "ib4next1":
                bot.edit_message_text(chat_id=chatid, message_id=mesid, text='B Powder 345gr',
                                      reply_markup=Generate().inl_bcaa_fourth_pos_one())
            if call_data == "ib4next2":
                bot.edit_message_text(chat_id=chatid, message_id=mesid, text='380gr',
                                      reply_markup=Generate().inl_bcaa_fourth_pos_two())
# L-Carnitine
        if 'ilc1p1' in call_data:
            if call_data == 'ilc1p1':
                do_write(chatid, '10')
                bot.answer_callback_query(call_id, "Added")
#

    # ______________________________________________________________________________________________________________________
    if "message" in update:

        if text == '/start':

            bot.send_message(chat_id, 'Hello here! Use /shop to start shopping:')

        if text == '/shop':
            bot.send_message(chat_id, 'You on main categories page', reply_markup=Generate().all_products_name_markup())

        if text == 'Protein':
            bot.send_message(chat_id, 'Proteins:', reply_markup=Generate().protein_markup())

        if text == 'Whey Gold Standard!':
            bot.send_message(chat_id, 'You choose: Whey Gold Standard')
            # pic
            bot.send_message(chat_id, 'WGS 450gr', reply_markup=Generate().inl_protein_first_pos_one())
        if text == '100% Whey Gold Standard Natural!':
            bot.send_message(chat_id, 'You choose: 100% Whey Gold Standard Natural')
            # pic
            bot.send_message(chat_id, 'WGSN 907gr', reply_markup=Generate().inl_protein_second_pos_one())
        if text == 'Gold Standard 100% Plant!':
            bot.send_message(chat_id, 'You choose: Gold Standard 100% Plant')
            # pic
            bot.send_message(chat_id, 'GSP 722gr', reply_markup=Generate().inl_protein_third_pos_one())
        if text == 'Platinum Hydrowhey!':
            bot.send_message(chat_id, 'You choose: Platinum Hydrowey')
            # pic
            bot.send_message(chat_id, 'PH 795gr ', reply_markup=Generate().inl_protein_fourth_pos_one())
        if text == '100% Isolate!':
            bot.send_message(chat_id, 'You choose: 100% Isolate')
            bot.send_message(chat_id, '100% Is 1.36kg', reply_markup=Generate().inl_protein_fifth_pos_one())
        if text == 'Isolate!':
            bot.send_message(chat_id, 'You choose: Isolate')
            bot.send_message(chat_id, '1.36kg', reply_markup=Generate().inl_protein_sixth_pos_one())
        if text == '100% Gold Standard Casein!':
            bot.send_message(chat_id, 'You choose: 100% Gold Standard Casein')
            bot.send_message(chat_id, 'GSC 909gr', reply_markup=Generate().inl_protein_seventh_pos_one())
        if text == '100% Natural Casein Protein!':
            bot.send_message(chat_id, 'You choose: 100% Natural Casein Protein')
            bot.send_message(chat_id, 'NCP 1818gr', reply_markup=Generate().inl_protein_eigth_pos_one())
        if text == 'Protein Energy!':
            bot.send_message(chat_id, 'You choose: Protein Energy')
            bot.send_message(chat_id, 'PE 720gr', reply_markup=Generate().inl_protein_ninth_pos_one())
        if text == 'Back to main<-':
            bot.send_message(chat_id, 'You on main categories page', reply_markup=Generate().all_products_name_markup())

        if text == 'Gainer':
            bot.send_message(chat_id, 'Gainers:', reply_markup=Generate().gainer_markup())
        if text == 'Gold Standart Gainer!':
            bot.send_message(chat_id, 'You choose: Gold Standart Gainer')
            bot.send_message(chat_id, 'GSG probnik 51gr', reply_markup=Generate().inl_gainer_first_pos_one())
        if text == 'Pro Complex Gainer!':
            bot.send_message(chat_id, 'You choose: Pro Complex Gainer')
            bot.send_message(chat_id, 'PCG 4.30kg', reply_markup=Generate().inl_gainer_second_pos_one())
        if text == 'Serious Mass!':
            bot.send_message(chat_id, 'You choose: Serious Mass')
            bot.send_message(chat_id, 'SM 2.72kg', reply_markup=Generate().inl_gainer_third_pos_one())

        if text == 'Creatine':
            bot.send_message(chat_id, 'Creatine list:', reply_markup=Generate().creatine_markup())
        if text == 'Creatine Powder!':
            bot.send_message(chat_id, 'You choose: Creatine Powder')
            bot.send_message(chat_id, 'C Powder 150gr', reply_markup=Generate().inl_creatine_first_pos_one())
        if text == 'Creatine 2500!':
            bot.send_message(chat_id, 'You choose: Creatine 2500')
            bot.send_message(chat_id, 'C 2500 300pil', reply_markup=Generate().inl_creatine_second_pos_one())

        if text == 'Amino':
            bot.send_message(chat_id, 'Amino:', reply_markup=Generate().creatine_markup())
        if text == 'Essential Amino Energy!':
            bot.send_message(chat_id, 'You choose: Essential Amino Energy')
            bot.send_message(chat_id, 'EAE probnik 18gr', reply_markup=Generate().inl_amino_first_pos_one())
        if text == 'Amino Energy + Electrolytes!':
            bot.send_message(chat_id, 'You choose: Amino Energy + Electrolytes')
            bot.send_message(chat_id, 'AE+E 285gr', reply_markup=Generate().inl_amino_second_pos_one())
        if text == 'Amino 2222!':
            bot.send_message(chat_id, 'You choose: Amino 2222')
            bot.send_message(chat_id, 'A 2222 160tab', reply_markup=Generate().inl_amino_third_pos_one())
        if text == 'Amino Energy TEA SERIES!':
            bot.send_message(chat_id, 'You choose: Amino Energy Tea Series')
            bot.send_message(chat_id, 'AETS 270gr', reply_markup=Generate().inl_amino_fourth_pos_one())
        if text == 'BETA ALANINE(Natural)!':
            bot.send_message(chat_id, 'You choose: Beta Alanine(natural)')
            bot.send_message(chat_id, 'BA 263gr', reply_markup=Generate().inl_amino_fifth_pos_one())

        if text == 'BCAA':
            bot.send_message(chat_id, 'BCAA:', reply_markup=Generate().bcaa_markup())
        if text == 'BCAA Train + Recover!':
            bot.send_message(chat_id, 'You choose: BCAA Train + Recover')
            bot.send_message(chat_id, 'B T+R 280gr', reply_markup=Generate().inl_bcaa_first_pos_one())
        if text == 'PRO BCAA!':
            bot.send_message(chat_id, 'You choose: PRO BCAA')
            bot.send_message(chat_id, 'PRO B 390gr', reply_markup=Generate().inl_bcaa_second_pos_one())
        if text == 'BCAA Train + Recover!':
            bot.send_message(chat_id, 'You choose: BCAA 1000')
            bot.send_message(chat_id, 'B 1000 200cap', reply_markup=Generate().inl_bcaa_third_pos_one())
        if text == 'BCAA Train + Recover!':
            bot.send_message(chat_id, 'You choose: BCAA Powder')
            bot.send_message(chat_id, 'B Powder 345gr', reply_markup=Generate().inl_bcaa_fourth_pos_one())

        if text == 'L-carnitine':
            bot.send_message(chat_id, 'L-carnitine:', reply_markup=Generate().l_carnitine_markup())
        if text == 'L-Carnitine 500!':
            bot.send_message(chat_id, 'You choose: L-Carnitine 500')
            bot.send_message(chat_id, 'L 500 60tab', reply_markup=Generate().inl_bcaa_first_pos_one())

        if text == 'Supplements and vitamins':
            bot.send_message(chat_id, 'Supplements and vitamins: ',
                             reply_markup=Generate().supplements_and_vitamins_markup())
        if text == 'Fish Oil!':
            bot.send_message(chat_id, 'You choose: Fish Oil')
            bot.send_message(chat_id, 'FO 100cap', reply_markup=Generate().inl_supplements_and_vitamins_first_pos_one())
        if text == 'Glutamine Powder!':
            bot.send_message(chat_id, 'You choose: Glutamine Powder')
            bot.send_message(chat_id, 'GP 300gr', reply_markup=Generate().inl_supplements_and_vitamins_second_pos_one())
        if text == 'Glutamine 1000!':
            bot.send_message(chat_id, 'You choose: Glutamine 1000')
            bot.send_message(chat_id, 'G 1000 120cap',
                             reply_markup=Generate().inl_supplements_and_vitamins_third_pos_one())
        if text == 'CLA!':
            bot.send_message(chat_id, 'You choose: CLA')
            bot.send_message(chat_id, 'C 90cap', reply_markup=Generate().inl_supplements_and_vitamins_fourth_pos_one())
        if text == 'Opti Men!':
            bot.send_message(chat_id, 'You choose: Opti Men')
            bot.send_message(chat_id, 'OM 90tab', reply_markup=Generate().inl_supplements_and_vitamins_fifth_pos_one())
        if text == 'Opti Women!':
            bot.send_message(chat_id, 'You choose: Opti Women')
            bot.send_message(chat_id, 'OW 60tab', reply_markup=Generate().inl_supplements_and_vitamins_sixth_pos_one())
        if text == 'Tribulus 625!':
            bot.send_message(chat_id, 'You choose: Tribulus 625')
            bot.send_message(chat_id, 'T 100tap', reply_markup=Generate().inl_supplements_and_vitamins_seventh_pos_one())
        if text == 'PRE-Workout!':
            bot.send_message(chat_id, 'You choose: PRE-Workout')
            bot.send_message(chat_id, 'P-W 300gr', reply_markup=Generate().inl_supplements_and_vitamins_eighth_pos_one())
        if text == 'ZMA!':
            bot.send_message(chat_id, 'You choose: ZMA')
            bot.send_message(chat_id, 'Z 90cap', reply_markup=Generate().inl_supplements_and_vitamins_ninth_pos_one())
        if text == 'CO-Q10!':
            bot.send_message(chat_id, 'You choose: CO-Q10')
            bot.send_message(chat_id, 'COQ 150cap', reply_markup=Generate().inl_supplements_and_vitamins_tenth_pos_one())
        if text == 'Melatonin!':
            bot.send_message(chat_id, 'You choose: Melatonin')
            bot.send_message(chat_id, 'M 100tab', reply_markup=Generate().inl_supplements_and_vitamins_eleventh_pos_one())
        if text == 'Vitamin D!':
            bot.send_message(chat_id, 'You choose: Vitamin D')
            bot.send_message(chat_id, 'D 200cap', reply_markup=Generate().inl_supplements_and_vitamins_twelfth_pos_one())
        if text == 'Vitamin E!':
            bot.send_message(chat_id, 'You choose: Vitamin E')
            bot.send_message(chat_id, 'E 200cap',
                             reply_markup=Generate().inl_supplements_and_vitamins_thirteenth_pos_one())

        if text == 'Корзина заказов':
            cost = show_data(chat_id)
            bot.send_message(chat_id, 'Your price: ' + str(cost), reply_markup=Generate().basket_markup())
        if text == 'Сбросить заказ':
            rewriting_file(chat_id)
            bot.send_message(chat_id, 'Успешно. Используйте команду /start')  # ,reply_markup = Generate.gen....
        if text == 'Подтвердить заказ':
            bot.send_message(chat_id, 'Ожидайте, с вами свяжется оператор.')

    return 'ok', 200


@app.route("/")
def webhook():
    bot.remove_webhook()
    time.sleep(0.1)
    bot.set_webhook(url+ TOKEN)
    return "!", 200


if __name__ == "__main__":
    app.run(host=WEBHOOK_LISTEN, port=int(os.environ.get('PORT', 5000)))
