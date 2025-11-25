# This is a sample Python script.
from binascii import Incomplete


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
def gave_base_story(user_input):
    if len(user_input) % 2:
        print("Кот залез на шкаф, увидел птицу, чихнул — и упал в цветочный горшок. Все смеялись!")
    else:
        print("Девочка нашла монетку, купила мороженое, а оно оказалось с сюрпризом — внутри кольцо!")

if __name__ == '__main__':
    try:
        user_input = input()
        if user_input is None or not len(user_input):
            raise Incomplete()
        print_hi(user_input)
        gave_base_story(user_input)
    except Incomplete as ex:
        print("Вы не ввели приветствие!")
    except Exception as ex:
        print(f"Rsaised generic exception: {ex}")
