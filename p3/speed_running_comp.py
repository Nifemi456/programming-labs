from datetime import timedelta

def init_leaderboard() -> dict[str, timedelta]:
    leaderboard = {}
    return leaderboard

def add_player(leaderboard, player_name)->bool:
    if player_name not in leaderboard:
        leaderboard[player_name] = None
        return True
    else:
        return False

def add_run(leaderboard:dict, player_name:str, time:timedelta)->int:
    if time < timedelta(0) :
        return 1
    elif player_name not in leaderboard:
        return 2
    else:
        if None == leaderboard[player_name] or time < leaderboard[player_name] :
            leaderboard[player_name] = time
        return 0

def clear_score(leaderboard:dict, player_name:str)->bool:
    if player_name not in leaderboard:
        return False
    else:
        leaderboard[player_name] = None
        return True

def display_leaderboard(leaderboard:dict, n:int=3)->None:
    new_leaderboard = {}
    for name, value in leaderboard.items():
        if value:
            new_leaderboard[name] = value
    if new_leaderboard.values():
        temp_dict = sorted(new_leaderboard.keys(), key=new_leaderboard.__getitem__)
        for i in range(n):
            if i<len(temp_dict):
                print(f'{i+1}\t{temp_dict[i]}\t{new_leaderboard[temp_dict[i]]}')
    else:
        print('Leaderboard is empty.')

def calculate_average_time(leaderboard:dict)->bool or tuple[bool,float]:
    new_leaderboard = {}
    for name, value in leaderboard.items():
        if value:
            new_leaderboard[name] = value
    if new_leaderboard.values():
        temp = timedelta(0)
        num = 0
        for i in new_leaderboard.values():
            if i:
                temp += i
                num += 1
        avg_value = temp/num
        return True, avg_value
    else:
        return False, None

# leaderboard_1 = init_leaderboard()
# add_player(leaderboard_1, "Frank")
# add_player(leaderboard_1, "Joe")
# add_player(leaderboard_1, "Alan")
# add_player(leaderboard_1, "Steve")
# add_player(leaderboard_1, "Chris")
# display_leaderboard(leaderboard_1)
# # print(leaderboard_1)
# add_run(leaderboard_1, "Frank", timedelta(hours=1))
# add_run(leaderboard_1, "Joe", timedelta(hours=2))
# add_run(leaderboard_1, "Alan", timedelta(hours=3))
# add_run(leaderboard_1, "Alan", timedelta(minutes=57))
# add_run(leaderboard_1, "Steve", timedelta(minutes=49))
# add_run(leaderboard_1, "Chris", timedelta(minutes=69))
# clear_score(leaderboard_1, "Steve")
# # print(leaderboard_1)
# display_leaderboard(leaderboard_1)
# print(f"Average best time: {calculate_average_time(leaderboard_1)[1]}")

leaderboard = init_leaderboard()
display_leaderboard(leaderboard, n=2)
add_player(leaderboard, "Alice")
display_leaderboard(leaderboard, n=2)
add_player(leaderboard, "Bob")
display_leaderboard(leaderboard, n=2)
add_player(leaderboard, "Charlie")
display_leaderboard(leaderboard, n=2)
add_run(leaderboard, "Alice", timedelta(seconds=67))
display_leaderboard(leaderboard, n=2)
add_run(leaderboard, "Bob", timedelta(seconds=53))
display_leaderboard(leaderboard, n=2)
add_run(leaderboard, "Charlie", timedelta(seconds=63))
display_leaderboard(leaderboard, n=2)