# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 19:46:03 2018

@author: hsf
"""
import texasfunction as tf
import texas_predict as tp

player_tmp = tf.usr("robot")  
player_tmp.handcards([39,23])
cards=[12,13,14]
print(tp.predict_self(player_tmp, cards, 6, 10000))

