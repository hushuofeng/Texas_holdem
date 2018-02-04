# -*- coding: utf-8 -*-
import texasfunction as tf
#import texas_statistic as ts
import texas_predict as tp
            
"""初始化牌桌"""
player_num_init = 2  # 玩家人数
poke = tf.cards()    # 生成牌桌
player_list = []    # 生成玩家列表
for i in range(player_num_init):
    player_list.append(tf.usr(str(i)))

"""统计数据"""
stat_card_types = []
stat_win_players = []

"""开始游戏"""
for r in range(1):
    player_num = len(player_list)
    poke.change_nums(player_num)
    poke.shuffle()  #洗牌
    cards = []
    poke.generate_usr_cardlist(r % player_num)   # 生成玩家手牌，根据序号生成
    for i in range(player_num):     #分发玩家手牌
        player_list[i].handcards(poke.usr_cardlist[i])

    """预测胜利的概率"""

    # 第〇轮
    card_deal = poke.deal()     # 发牌
    #加注
    tp.predict_result(player_list, cards)
    
    # 第一轮，发三张牌发第一轮三张牌
    cards = next(card_deal)
    #加注
    tp.predict_result(player_list, cards)
    
    # 第二轮，发一张牌
    cards.append(next(card_deal))
    #加注
    tp.predict_result(player_list, cards)
    
    # 第三轮，发一张牌
    cards.append(next(card_deal))
    #加注
    tp.predict_result(player_list, cards)
    
    # 生成玩家手牌类型
    for i in range(player_num):
        player_list[i].cardtype(cards)
    # 输出测试
    tf.print_cards(player_list,cards)
    
    result = tf.player_rank(player_list[:])
    for i in range(len(result)):
        if result[i] == 0:
            print("玩家" + player_list[i].name + "获胜！")
            
            

#    for i in range(player_num):
#        stat_card_types.append(card_types[player_list[i].handcard_type[0]])
#        if result[i] == 0:
#            stat_win_players.append(player_list[i].name)
#
#ts.bar_card_type(stat_card_types,card_types)
#ts.bar_player(stat_win_players,[x.name for x in player_list])




