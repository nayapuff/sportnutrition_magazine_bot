from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


class Generate:
    # __________________________________________reply keyboards____________________________________________________
    def init_markup(self):
        markup = types.ReplyKeyboardMarkup(row_width=1)
        first_b = types.KeyboardButton('Купить продукцию')
        second_b = types.KeyboardButton('Корзина заказов')
        third_b = types.KeyboardButton('Информация и контакты')
        fourth_b = types.KeyboardButton('Гибкий подбор')
        markup.add(first_b, second_b, third_b, fourth_b)
        return markup

    def all_products_name_markup(self):
        markup = types.ReplyKeyboardMarkup(row_width=1)
        first_b = types.KeyboardButton('Protein')
        second_b = types.KeyboardButton('Gainer')
        third_b = types.KeyboardButton('Creatine')
        fourth_b = types.KeyboardButton('Amino')
        fifth_b = types.KeyboardButton('BCAA')
        sixth_b = types.KeyboardButton('L-carnitine')
        seventh_b = types.KeyboardButton('Supplements and vitamins')
        eighth_b = types.KeyboardButton('Factory Clothes')
        markup.add(first_b, second_b, third_b, fourth_b, fifth_b, sixth_b, seventh_b, eighth_b)
        return markup

    def protein_markup(self):
        markup = types.ReplyKeyboardMarkup(row_width=1)
        first_b = types.KeyboardButton('Whey Gold Standard!')
        second_b = types.KeyboardButton('100% Whey Gold Standard Natural!')
        third_b = types.KeyboardButton('Gold Standard 100% Plant!')
        fourth_b = types.KeyboardButton('Platinum Hydrowhey!')
        fifth_b = types.KeyboardButton('100% Isolate!')
        sixth_b = types.KeyboardButton('Isolate!')
        seventh_b = types.KeyboardButton('100% Gold Standard Casein!')
        eighth_b = types.KeyboardButton('100% Natural Casein Protein!')
        ninth_b = types.KeyboardButton('Protein Energy!')
        tenth_b = types.KeyboardButton('Back to main<-')
        markup.add(first_b, second_b, third_b, fourth_b, fifth_b, sixth_b, seventh_b, eighth_b, ninth_b, tenth_b)
        return markup

    def gainer_markup(self):
        markup = types.ReplyKeyboardMarkup(row_width=1)
        first_b = types.KeyboardButton('Gold Standard Gainer!')
        second_b = types.KeyboardButton('Pro Complex Gainer!')
        third_b = types.KeyboardButton('Serious Mass!')
        fourth_b = types.KeyboardButton('Back to main<-')
        markup.add(first_b, second_b, third_b, fourth_b)
        return markup

    def creatine_markup(self):
        markup = types.ReplyKeyboardMarkup(row_width=1)
        first_b = types.KeyboardButton('Creatine Powder!')
        second_b = types.KeyboardButton('Creatine 2500!')
        third_b = types.KeyboardButton('Back to main<-')
        markup.add(first_b, second_b, third_b)
        return markup

    def amino_markup(self):
        markup = types.ReplyKeyboardMarkup(row_width=1)
        first_b = types.KeyboardButton('Essential Amino Energy!')
        second_b = types.KeyboardButton('Amino Energy + Electrolytes!')
        third_b = types.KeyboardButton('Amino 2222!')
        fourth_b = types.KeyboardButton('Amino Energy TEA SERIES!')
        fifth_b = types.KeyboardButton('BETA ALANINE(Natural)!')
        six_b = types.KeyboardButton('Back to main<-')
        markup.add(first_b, second_b, third_b, fourth_b, fifth_b, six_b)
        return markup

    def bcaa_markup(self):
        markup = types.ReplyKeyboardMarkup(row_width=1)
        first_b = types.KeyboardButton('BCAA Train + Recover!')
        second_b = types.KeyboardButton('PRO BCAA!')
        third_b = types.KeyboardButton('BCAA 1000!')
        fourth_b = types.KeyboardButton('BCAA Powder!')
        fifth_b = types.KeyboardButton('Back to main<-')
        markup.add(first_b, second_b, third_b, fourth_b, fifth_b)
        return markup

    def l_carnitine_markup(self):
        markup = types.ReplyKeyboardMarkup(row_width=1)
        first_b = types.KeyboardButton('L-Carnitine 500!')
        second_b = types.KeyboardButton('Back to main<-')
        markup.add(first_b, second_b)
        return markup

    def supplements_and_vitamins_markup(self):
        markup = types.ReplyKeyboardMarkup(row_width=1)
        first_b = types.KeyboardButton('Fish Oil!')
        second_b = types.KeyboardButton('Glutamine Powder!')
        third_b = types.KeyboardButton('Glutamine 1000!')
        fourth_b = types.KeyboardButton('CLA!')
        fifth_b = types.KeyboardButton('Opti Men!')
        sixth_b = types.KeyboardButton('Opti Women!')
        seventh_b = types.KeyboardButton('Tribulus 625!')
        eighth_b = types.KeyboardButton('PRE-Workout!')
        ninth_b = types.KeyboardButton('ZMA!')
        tenth_b = types.KeyboardButton('CO-Q10!')
        eleventh_b = types.KeyboardButton('Melatonin!')
        twelfth_b = types.KeyboardButton('Vitamin D!')
        thirteenth_b = types.KeyboardButton('Vitamin E!')
        fourteenth_b = types.KeyboardButton('Back to main<-')
        markup.add(first_b, second_b, third_b, fourth_b, fifth_b, sixth_b, seventh_b, eighth_b, ninth_b, tenth_b,
                   eleventh_b, twelfth_b, thirteenth_b, fourteenth_b)
        return markup

    def factory_clothes(self):
        markup = types.ReplyKeyboardMarkup(row_width=1)
        first_b = types.KeyboardButton('KEPKA!')
        second_b = types.KeyboardButton('Back to main<-')
        markup.add(first_b, second_b)
        return markup
    # __________________________________________inline keyboards____________________________________________________

    def inl_protein_first_pos_one(self):
        markup = InlineKeyboardMarkup(row_width=2)
        first_b = InlineKeyboardButton("+", callback_data='ip1p1')  # just 'added'
        second_b = InlineKeyboardButton("Далее", callback_data='ip1next2')
        markup.add(first_b, second_b)
        return markup

    def inl_protein_first_pos_two(self):
        markup = InlineKeyboardMarkup(row_width=2)
        first_b = InlineKeyboardButton("+", callback_data='ip1p2')
        second_b = InlineKeyboardButton("Далее", callback_data='ip1next3')
        third_b = InlineKeyboardButton("Назад", callback_data='ip1next1')
        markup.add(first_b, second_b, third_b)
        return markup

    def inl_protein_first_pos_three(self):
        markup = InlineKeyboardMarkup(row_width=2)
        first_b = InlineKeyboardButton("+", callback_data='ip1p3')
        second_b = InlineKeyboardButton("Далее", callback_data='ip1next4')
        third_b = InlineKeyboardButton("Назад", callback_data='ip1next2')
        markup.add(first_b, second_b, third_b)
        return markup

    def inl_protein_first_pos_four(self):
        markup = InlineKeyboardMarkup(row_width=2)
        first_b = InlineKeyboardButton("+", callback_data='ip1p4')
        second_b = InlineKeyboardButton("Назад", callback_data='ip1next3')
        markup.add(first_b, second_b)
        return markup

    def inl_protein_second_pos_one(self):
        markup = InlineKeyboardMarkup(row_width=2)
        first_b = InlineKeyboardButton("+", callback_data='ip2p1')
        second_b = InlineKeyboardButton("Далее", callback_data='ip2next2')
        markup.add(first_b, second_b)
        return markup

    def inl_protein_second_pos_two(self):
        markup = InlineKeyboardMarkup(row_width=2)
        first_b = InlineKeyboardButton("+", callback_data='ip2p2')
        second_b = InlineKeyboardButton("Назад", callback_data='ip2next1')
        markup.add(first_b, second_b)
        return markup

    def inl_protein_third_pos_one(self):
        markup = InlineKeyboardMarkup(row_width=1)
        first_b = InlineKeyboardButton("+", callback_data='ip3p1')
        markup.add(first_b)
        return markup

    def inl_protein_fourth_pos_one(self):
        markup = InlineKeyboardMarkup(row_width=2)
        first_b = InlineKeyboardButton("+", callback_data='ip4p1')
        second_b = InlineKeyboardButton("Далее", callback_data='ip4next2')
        markup.add(first_b, second_b)
        return markup

    def inl_protein_fourth_pos_two(self):
        markup = InlineKeyboardMarkup(row_width=2)
        first_b = InlineKeyboardButton("+", callback_data='ip4p2')
        second_b = InlineKeyboardButton("Назад", callback_data='ip4next1')
        markup.add(first_b, second_b)
        return markup

    def inl_protein_fifth_pos_one(self):
        markup = InlineKeyboardMarkup(row_width=2)
        first_b = InlineKeyboardButton("+", callback_data='ip5p1')
        second_b = InlineKeyboardButton("Далее", callback_data='ip5next2')
        markup.add(first_b, second_b)
        return markup

    def inl_protein_fifth_pos_two(self):
        markup = InlineKeyboardMarkup(row_width=2)
        first_b = InlineKeyboardButton("+", callback_data='ip5p2')
        second_b = InlineKeyboardButton("Назад", callback_data='ip5next1')
        markup.add(first_b, second_b)
        return markup

    def inl_protein_sixth_pos_one(self):
        markup = InlineKeyboardMarkup(row_width=2)
        first_b = InlineKeyboardButton("+", callback_data='ip6p1')
        second_b = InlineKeyboardButton("Далее", callback_data='ip6next2')
        markup.add(first_b, second_b)
        return markup

    def inl_protein_sixth_pos_two(self):
        markup = InlineKeyboardMarkup(row_width=2)
        first_b = InlineKeyboardButton("+", callback_data='ip6p2')
        second_b = InlineKeyboardButton("Назад", callback_data='ip6next1')
        markup.add(first_b, second_b)
        return markup

    def inl_protein_seventh_pos_one(self):
        markup = InlineKeyboardMarkup(row_width=2)
        first_b = InlineKeyboardButton("+", callback_data='ip7p1')
        second_b = InlineKeyboardButton("Далее", callback_data='ip7next2')
        markup.add(first_b, second_b)
        return markup

    def inl_protein_seventh_pos_two(self):
        markup = InlineKeyboardMarkup(row_width=2)
        first_b = InlineKeyboardButton("+", callback_data='ip7p2')
        second_b = InlineKeyboardButton("Далее", callback_data='ip7next3')
        third_b = InlineKeyboardButton("Назад", callback_data='ip7next1')
        markup.add(first_b, second_b, third_b)
        return markup

    def inl_protein_eigth_pos_one(self):
        markup = InlineKeyboardMarkup(row_width=2)
        first_b = InlineKeyboardButton("+", callback_data='ip8p1')
        second_b = InlineKeyboardButton("Далее", callback_data='ip8next2')
        markup.add(first_b, second_b)
        return markup

    def inl_protein_ninth_pos_one(self):
        markup = InlineKeyboardMarkup(row_width=2)
        first_b = InlineKeyboardButton("+", callback_data='ip9p1')
        markup.add(first_b)
        return markup

    def inl_gainer_first_pos_one(self):
        markup = InlineKeyboardMarkup(row_width=2)
        first_b = InlineKeyboardButton("+", callback_data='ig1p1')
        second_b = InlineKeyboardButton("Далее", callback_data='ig1next2')
        markup.add(first_b, second_b)
        return markup

    def inl_gainer_first_pos_two(self):
        markup = InlineKeyboardMarkup(row_width=2)
        first_b = InlineKeyboardButton("+", callback_data='ig1p2')
        second_b = InlineKeyboardButton("Далее", callback_data='ig1next3')
        third_b = InlineKeyboardButton("Назад", callback_data='ig1next1')
        markup.add(first_b, second_b, third_b)
        return markup

    def inl_gainer_first_pos_three(self):
        markup = InlineKeyboardMarkup(row_width=2)
        first_b = InlineKeyboardButton("+", callback_data='ig1p3')
        second_b = InlineKeyboardButton("Назад", callback_data='ig1next2')
        markup.add(first_b, second_b)

    def inl_gainer_second_pos_one(self):
        markup = InlineKeyboardMarkup(row_width=2)
        first_b = InlineKeyboardButton("+", callback_data='ig2p1')
        markup.add(first_b)
        return markup

    def inl_gainer_third_pos_one(self):
        markup = InlineKeyboardMarkup(row_width=2)
        first_b = InlineKeyboardButton("+", callback_data='ig3p1')
        second_b = InlineKeyboardButton("Далее", callback_data='ig3next2')
        markup.add(first_b, second_b)
        return markup

    def inl_gainer_third_pos_two(self):
        markup = InlineKeyboardMarkup(row_width=2)
        first_b = InlineKeyboardButton("+", callback_data='ig3p2')
        second_b = InlineKeyboardButton("Назад", callback_data='ig3next1')
        markup.add(first_b, second_b)
        return markup



#    def inl_gainer_fourth_pos_one(self):
#        markup = InlineKeyboardMarkup(row_width=2)
#        first_b = InlineKeyboardButton("+", callback_data='ig4p1')
#        markup.add(first_b)
#        return markup

    def inl_creatine_first_pos_one(self):
        markup = InlineKeyboardMarkup(row_width=2)
        first_b = InlineKeyboardButton("+", callback_data='ic1p1')
        second_b = InlineKeyboardButton("Далее", callback_data='ic1next2')
        markup.add(first_b, second_b)
        return markup


    def inl_creatine_first_pos_two(self):
        markup = InlineKeyboardMarkup(row_width=2)
        first_b = InlineKeyboardButton("+", callback_data='ic1p2')
        second_b = InlineKeyboardButton("Далее", callback_data='iс1next3')
        third_b = InlineKeyboardButton("Назад", callback_data='ic1next1')
        markup.add(first_b, second_b, third_b)
        return markup

    def inl_creatine_first_pos_three(self):
        markup = InlineKeyboardMarkup(row_width=2)
        first_b = InlineKeyboardButton("+", callback_data='iс1p3')
        second_b = InlineKeyboardButton("Далее", callback_data='iс1next4')
        third_b = InlineKeyboardButton("Назад", callback_data='iс1next2')
        markup.add(first_b, second_b, third_b)
        return markup

    def inl_creatine_first_pos_four(self):
        markup = InlineKeyboardMarkup(row_width=2)
        first_b = InlineKeyboardButton("+", callback_data='iс1p4')
        second_b = InlineKeyboardButton("Назад", callback_data='ic1next3')
        markup.add(first_b, second_b)
        return markup

    def inl_creatine_second_pos_one(self):
        markup = InlineKeyboardMarkup(row_width=2)
        first_b = InlineKeyboardButton("+", callback_data='ic2p1')
        markup.add(first_b)
        return markup

    def inl_amino_first_pos_one(self):
        markup = InlineKeyboardMarkup(row_width=2)
        first_b = InlineKeyboardButton("+", callback_data='ia1p1')
        second_b = InlineKeyboardButton("Далее", callback_data='iaa21next2')
        markup.add(first_b, second_b)
        return markup

    def inl_amino_first_pos_two(self):
        markup = InlineKeyboardMarkup(row_width=2)
        first_b = InlineKeyboardButton("+", callback_data='ia1p2')
        second_b = InlineKeyboardButton("Далее", callback_data='ia1next3')
        third_b = InlineKeyboardButton("Назад", callback_data='ia1next1')
        markup.add(first_b, second_b, third_b)
        return markup

    def inl_amino_first_pos_three(self):
        markup = InlineKeyboardMarkup(row_width=2)
        first_b = InlineKeyboardButton("+", callback_data='ia1p3')
        second_b = InlineKeyboardButton("Далее", callback_data='ia1next4')
        third_b = InlineKeyboardButton("Назад", callback_data='ia1next2')
        markup.add(first_b, second_b, third_b)
        return markup

    def inl_amino_first_pos_four(self):
        markup = InlineKeyboardMarkup(row_width=2)
        first_b = InlineKeyboardButton("+", callback_data='ia1p4')
        second_b = InlineKeyboardButton("Назад", callback_data='ia1next3')
        markup.add(first_b, second_b)
        return markup

    def inl_amino_second_pos_one(self):
        markup = InlineKeyboardMarkup(row_width=2)
        first_b = InlineKeyboardButton("+", callback_data='ia2p1')
        markup.add(first_b)
        return markup

    def inl_amino_third_pos_one(self):
        markup = InlineKeyboardMarkup(row_width=2)
        first_b = InlineKeyboardButton("+", callback_data='ia3p1')
        second_b = InlineKeyboardButton("Далее", callback_data='ia3next2')
        markup.add(first_b, second_b)
        return markup

    def inl_amino_third_pos_two(self):
        markup = InlineKeyboardMarkup(row_width=2)
        first_b = InlineKeyboardButton("+", callback_data='ia3p2')
        second_b = InlineKeyboardButton("Назад", callback_data='ia3next1')
        markup.add(first_b, second_b)
        return markup

    def inl_amino_fourth_pos_one(self):
        markup = InlineKeyboardMarkup(row_width=2)
        first_b = InlineKeyboardButton("+", callback_data='ia4p1')
        markup.add(first_b)
        return markup

    def inl_amino_fifth_pos_one(self):
        markup = InlineKeyboardMarkup(row_width=2)
        first_b = InlineKeyboardButton("+", callback_data='ia5p1')
        markup.add(first_b)
        return markup

    def inl_bcaa_first_pos_one(self):
        markup = InlineKeyboardMarkup(row_width=2)
        first_b = InlineKeyboardButton("+", callback_data='ib1p1')
        markup.add(first_b)
        return markup

    def inl_bcaa_second_pos_one(self):
        markup = InlineKeyboardMarkup(row_width=2)
        first_b = InlineKeyboardButton("+", callback_data='ib2p1')
        markup.add(first_b)
        return markup

    def inl_bcaa_third_pos_one(self):
        markup = InlineKeyboardMarkup(row_width=2)
        first_b = InlineKeyboardButton("+", callback_data='ib3p1')
        second_b = InlineKeyboardButton("Далее", callback_data='ib3next2')
        markup.add(first_b, second_b)
        return markup

    def inl_bcaa_third_pos_two(self):
        markup = InlineKeyboardMarkup(row_width=2)
        first_b = InlineKeyboardButton("+", callback_data='ib3p2')
        second_b = InlineKeyboardButton("+", callback_data='ib3next1')
        markup.add(first_b, second_b)
        return markup

    def inl_bcaa_fourth_pos_one(self):
        markup = InlineKeyboardMarkup(row_width=2)
        first_b = InlineKeyboardButton("+", callback_data='xp1')
        second_b = InlineKeyboardButton("Далее", callback_data='ib4next2')
        markup.add(first_b, second_b)
        return markup

    def inl_bcaa_fourth_pos_two(self):
        markup = InlineKeyboardMarkup(row_width=2)
        first_b = InlineKeyboardButton("+", callback_data='ib4p2')
        second_b = InlineKeyboardButton("Назад", callback_data='ib4next1')
        markup.add(first_b, second_b)
        return markup

    def inl_l_carnitine_pos_one(self):
        markup = InlineKeyboardMarkup(row_width=2)
        first_b = InlineKeyboardButton("+", callback_data='ilc1p1')
        markup.add(first_b)
        return markup


# Fish oil 1
    def inl_supplements_and_vitamins_first_pos_one(self):
        markup = InlineKeyboardMarkup(row_width=2)
        first_b = InlineKeyboardButton("+", callback_data='isav1p1')
        second_b = InlineKeyboardButton("Далее", callback_data='isav1next2')
        markup.add(first_b, second_b)
        return markup

#Fish oil 2
    def inl_supplements_and_vitamins_first_pos_two(self):
        markup = InlineKeyboardMarkup(row_width=2)
        first_b = InlineKeyboardButton("+", callback_data='isav1p1')
        second_b = InlineKeyboardButton("Назад", callback_data='isav1next1')
        markup.add(first_b, second_b)
        return markup

#Glut Powder 1
    def inl_supplements_and_vitamins_second_pos_one(self):
        markup = InlineKeyboardMarkup(row_width=2)
        first_b = InlineKeyboardButton("+", callback_data='isav2p1')
        second_b = InlineKeyboardButton("Далее", callback_data='isav2next2')
        markup.add(first_b, second_b)
        return markup

#glut Powder 2
    def inl_supplements_and_vitamins_second_pos_two(self):
        markup = InlineKeyboardMarkup(row_width=2)
        first_b = InlineKeyboardButton("+", callback_data='isav2p2')
        second_b = InlineKeyboardButton("Далее", callback_data='isav2next3')
        third_b = InlineKeyboardButton("Назад", callback_data='isav2next1')
        markup.add(first_b, second_b, third_b)
        return markup

# Glut powder 3
    def inl_supplements_and_vitamins_second_pos_three(self):
        markup = InlineKeyboardMarkup(row_width=2)
        first_b = InlineKeyboardButton("+", callback_data='isav2p3')
        second_b = InlineKeyboardButton("Назад", callback_data='isav2next2')
        markup.add(first_b, second_b)
        return markup

# glutamine 1000
    def inl_supplements_and_vitamins_third_pos_one(self):
        markup = InlineKeyboardMarkup(row_width=2)
        first_b = InlineKeyboardButton("+", callback_data='isav3p1')
        markup.add(first_b)
        return markup

# cla
    def inl_supplements_and_vitamins_fourth_pos_one(self):
        markup = InlineKeyboardMarkup(row_width=2)
        first_b = InlineKeyboardButton("+", callback_data='isav4p1')
        markup.add(first_b)
        return markup

# opti men
    def inl_supplements_and_vitamins_fifth_pos_one(self):
        markup = InlineKeyboardMarkup(row_width=2)
        first_b = InlineKeyboardButton("+", callback_data='isav5p1')
        second_b = InlineKeyboardButton("Далее", callback_data='isav5next2')
        markup.add(first_b, second_b)
        return markup

    def inl_supplements_and_vitamins_fifth_pos_two(self):
        markup = InlineKeyboardMarkup(row_width=2)
        first_b = InlineKeyboardButton("+", callback_data='isav5p2')
        second_b = InlineKeyboardButton("Далее", callback_data='isav5next3')
        third_b = InlineKeyboardButton("Назад", callback_data='isav5next1')
        markup.add(first_b, second_b, third_b)
        return markup

    def inl_supplements_and_vitamins_fifth_pos_three(self):
        markup = InlineKeyboardMarkup(row_width=2)
        first_b = InlineKeyboardButton("+", callback_data='isav5p3')
        second_b = InlineKeyboardButton("Назад", callback_data='isav5next2')
        markup.add(first_b, second_b)
        return markup

# opti women
    def inl_supplements_and_vitamins_sixth_pos_one(self):
        markup = InlineKeyboardMarkup(row_width=2)
        first_b = InlineKeyboardButton("+", callback_data='isav6p1')
        second_b = InlineKeyboardButton("Далее", callback_data='isav6next2')
        markup.add(first_b, second_b)
        return markup

    def inl_supplements_and_vitamins_sixth_pos_two(self):
        markup = InlineKeyboardMarkup(row_width=2)
        first_b = InlineKeyboardButton("+", callback_data='isav6p2')
        second_b = InlineKeyboardButton("Назад", callback_data='isav6next1')
        markup.add(first_b, second_b)
        return markup

# Tribulus
    def inl_supplements_and_vitamins_seventh_pos_one(self):
        markup = InlineKeyboardMarkup(row_width=2)
        first_b = InlineKeyboardButton("+", callback_data='isav7p1')
        markup.add(first_b)
        return markup

# Pre-Workout
    def inl_supplements_and_vitamins_eighth_pos_one(self):
        markup = InlineKeyboardMarkup(row_width=2)
        first_b = InlineKeyboardButton("+", callback_data='isav8p1')
        second_b = InlineKeyboardButton("Далее", callback_data='isav9next2')
        markup.add(first_b, second_b)
        return markup

    def inl_supplements_and_vitamins_eighth_pos_two(self):
        markup = InlineKeyboardMarkup(row_width=2)
        first_b = InlineKeyboardButton("+", callback_data='isav8p2')
        second_b = InlineKeyboardButton("Назад", callback_data='isav9next1')
        markup.add(first_b, second_b)
        return markup

# ZMA
    def inl_supplements_and_vitamins_ninth_pos_one(self):
        markup = InlineKeyboardMarkup(row_width=2)
        first_b = InlineKeyboardButton("+", callback_data='isav9p1')
        second_b = InlineKeyboardButton("Далее", callback_data='isav9next2')
        markup.add(first_b, second_b)
        return markup

    def inl_supplements_and_vitamins_ninth_pos_two(self):
        markup = InlineKeyboardMarkup(row_width=2)
        first_b = InlineKeyboardButton("+", callback_data='isav9p2')
        second_b = InlineKeyboardButton("Назад", callback_data='isav9next1')
        markup.add(first_b, second_b)
        return markup

# CO Q 10
    def inl_supplements_and_vitamins_tenth_pos_one(self):
        markup = InlineKeyboardMarkup(row_width=2)
        first_b = InlineKeyboardButton("+", callback_data='isav10p1')
        markup.add(first_b)
        return markup

# Melatonin
    def inl_supplements_and_vitamins_eleventh_pos_one(self):
        markup = InlineKeyboardMarkup(row_width=2)
        first_b = InlineKeyboardButton("+", callback_data='isav11p1')
        markup.add(first_b)
        return markup

# Vitamin E
    def inl_supplements_and_vitamins_twelfth_pos_one(self):
        markup = InlineKeyboardMarkup(row_width=2)
        first_b = InlineKeyboardButton("+", callback_data='isav12p1')
        markup.add(first_b)
        return markup

# Vitamin D
    def inl_supplements_and_vitamins_thirteenth_pos_one(self):
        markup = InlineKeyboardMarkup(row_width=2)
        first_b = InlineKeyboardButton("+", callback_data='isav13p1')
        markup.add(first_b)
        return markup

    def basket_markup(self):
        markup = InlineKeyboardMarkup(row_width=2)
        first_b = InlineKeyboardButton("Подтвердить")
        second_b = InlineKeyboardButton("Сбросить")
        markup.add(first_b, second_b)
        return markup
