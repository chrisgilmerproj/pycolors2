#!/usr/bin/python

import colors

def main():
    c = colors.Colors()

    COLUMN = 7
    for bg_color in c.bg.ORDER:
        bg_fn = getattr(c, '{0}{1}'.format(c.bg.PREFIX, bg_color))
        for fmt in [''] + c.formats:
            line = ''
            for fg_color in c.fg.ORDER:
                if fg_color != 'reset':
                    fg = fg_color[:3]
                    fg_fn = getattr(c, fg_color)
                    for st in c.styles:
                        colored_text = fg_fn(fg, format=fmt, style=st)
                        # Trick to format correctly
                        line += ' ' * (COLUMN - len(fg)) + colored_text
            line += c.st.COLORS['reset_all']

            print(bg_fn(line))
        print('\n')


if __name__ == "__main__":
    main()
