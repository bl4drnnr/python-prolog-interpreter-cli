import curses


def pad_refresh(pad, pad_pos, height, width):
    pad.refresh(pad_pos, 0, 0, 0, height - 1, width)


def navigation_control(pad, y, height, width):
    key_up, key_down = 'AB'

    for c in iter(pad.getkey, 'q'):
        if c in '\x1b\x5b':
            continue
        y -= (c == key_up)
        y += (c == key_down)
        pad_refresh(pad, y, height, width)


def print_raw_input(stdscr, prompt_string):
    curses.echo()
    stdscr.addstr(prompt_string)
    stdscr.refresh()
    user_input = stdscr.getstr()
    return user_input.decode('utf-8')
