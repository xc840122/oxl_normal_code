"""
    main_logic.py
    author: Peter
    description: Welcome screen
"""
import random
from typing import List

from game_data import data

from higher_lower_game.entity import ComparedItem
from higher_lower_game.welcome import welcome_screen


# data prepared, convert json format to object
# change data structure to be dict
def json_data_handler():
    compared_obj_list = []
    for item in data:
        compared_item = ComparedItem(item['name'], item['follower_count'],
                                     item['description'], item['country'])
        compared_obj_list.append(compared_item)
    return compared_obj_list


# compare the two items
def compare_logic(item1: ComparedItem, item2: ComparedItem):
    return item1.follower_count - item2.follower_count


# play logic
def play_game():
    score = 0
    data_list: List[ComparedItem] = json_data_handler()
    # pick another one for computer
    computer_item: ComparedItem = random.choice(data_list)
    # remove picked one
    data_list.remove(computer_item)
    while True:
        if len(data_list) == 0:
            print("Bravo, you have win all")
            break
        # pick one for player
        own_item: ComparedItem = random.choice(data_list)
        # remove the picked one
        data_list.remove(own_item)
        # print both
        print(f'computer item is: \t{computer_item.name}-{computer_item.country}-{computer_item.description},'
              f'there is {computer_item.follower_count} followers')
        print(f'your item is: \t\t{own_item.name}-{own_item.country}-{own_item.description}')

        # handle invalid input
        judgement = ''
        input_times = 3
        while input_times > 0:
            # get input from console
            judgement = input("higher(type 1) or lower(type 0): ")
            if judgement == '1' or judgement == '0':
                break
            else:
                print('invalid input, try again:')
                input_times -= 1

        if input_times <= 0:
            print('you are kidding me')
            return

        # compare logic
        if (judgement == '1' and compare_logic(own_item, computer_item) > 0) or (
                judgement == '0' and compare_logic(own_item, computer_item) < 0):
            # get score
            score += 1
            print(f"Correct,{own_item.name} has {own_item.follower_count} followers, "
                  f"{computer_item.name} has {computer_item.follower_count} followers, score is {score}")
            # switch items
            computer_item = own_item
        else:
            print(f"Wrong,{own_item.name} has {own_item.follower_count} followers, "
                  f"{computer_item.name} has {computer_item.follower_count} followers, score is {score}")
            break


if __name__ == '__main__':
    welcome_screen()
    play_game()
