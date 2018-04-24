#!/usr/bin/env python3
# vim: set fileencoding=utf-8

from moviepy.editor import VideoClip
import numpy
import palette_mandmap


WIDTH = 320
HEIGHT = 240

MAXITER = 255

# pocatecni podminky

x0 = -0.7913539
y0 = 0.161779
scale = 1.0000
scale_factor = 0.97


def calc_corner(c_width, c_height, xpos, ypos, scale):
    return xpos - c_width * scale, \
           ypos - c_height * scale, \
           xpos + c_width * scale, \
           ypos + c_height * scale


def calc_mandelbrot(width, height, maxiter, palette, xpos, ypos, scale, array):

    xmin, ymin, xmax, ymax = calc_corner(2.0, 1.5, xpos, ypos, scale)
    c = complex(xmin, ymin)
    for y in range(0, height):
        c = complex(xmin, c.imag)
        for x in range(0, width):
            z = 0.0 + 0.0J
            i = 0

            # iteracni smycka
            while i < maxiter:
                if abs(z) > 4.0:
                    break
                z = z**2 + c
                i += 1

            # vypocet barvy
            r = palette[i][0]
            g = palette[i][1]
            b = palette[i][2]
            array[y][x][0] = r
            array[y][x][1] = g
            array[y][x][2] = b
            # posun na dalsi bod na radku
            c += (xmax - xmin) / width
        # posun na dalsi radek
        c += 1J*(ymax - ymin) / height


def make_frame(t):
    """Vytvoreni jednoho snimku videa."""
    global scale
    print("time: {t}, scale: {s}".format(t=t, s=scale))

    # vyplneni trojrozmerneho pole nulami
    frame = numpy.zeros((HEIGHT, WIDTH, 3))

    calc_mandelbrot(WIDTH, HEIGHT, MAXITER, palette_mandmap.palette, x0, y0, scale, frame)
    scale *= scale_factor

    return frame


# vytvoreni video klipu
animation = VideoClip(make_frame, duration=15)

# export videa do formatu Ogg Video File
# animation.write_videofile("mandelbrot_zoom.ogv", fps=20, progress_bar=False, bitrate="2000000")
animation.write_videofile("mandelbrot_zoom.ogv", fps=20, progress_bar=False, bitrate="300000")

# export videa do formatu MPEG-4
# animation.write_videofile("mandelbrot_zoom.mp4", fps=20, progress_bar=False, bitrate="700000")

# export videa do formatu GIF
# animation.write_gif("colors.gif", fps=25)
