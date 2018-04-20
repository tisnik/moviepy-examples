from moviepy.editor import VideoClip
import numpy

WIDTH = 256
HEIGHT = 256

index = 0


def make_frame(t):
    global index
    print("time: {t}, index: {i}".format(t=t, i=index))

    # vyplneni trojrozmerneho pole nulami
    frame = numpy.zeros((HEIGHT, WIDTH, 3))

    # vyplneni barvovym prechodem
    for y in range(HEIGHT):
        for x in range(WIDTH):
            frame[y][x][0] = x
            frame[y][x][2] = y
            frame[y][x][1] = index
    index += 1
    return frame


# vytvoreni video klipu
animation = VideoClip(make_frame, duration=10)

# export videa do formatu GIF
# animation.write_gif("colors.gif", fps=25)

# znovunastaveni pocitadla
index = 0

# export videa do formatu MPEG-4
animation.write_videofile("colors.mp4", fps=25)
