"""Maintains program loop."""

from display import Display
from user_input import UserInput
from input_handler import InputHandler


running = True


def main():
    display = Display()
    user_input = UserInput()
    input_handler = InputHandler(user_input)

    while running:
        display.build_display()
        user_input.get_user_input()
        input_handler.menu_handler()


if __name__ == '__main__':
    main()