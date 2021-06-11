import matplotlib as mpl
import matplotlib.pyplot as plt
from gtts import gTTS
from pydub import AudioSegment
from PIL import Image
import os
from .consts import *


# From https://gist.github.com/kylemcdonald/bedcc053db0e7843ef95c531957cb90f
def full_frame(figsize=None):
    mpl.rcParams['savefig.pad_inches'] = 0
    fig = plt.figure(figsize=figsize)
    ax = plt.axes([0,0,1,1], frameon=False)
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.autoscale(tight=True)
    return fig


def create_samples(text, lang='en', tld='com', size=None):
    filename = './temp.mp3'
    tts = gTTS(text, lang=lang, tld=tld)
    tts.save(filename)
    sound = AudioSegment.from_mp3(filename)
    samples = sound.get_array_of_samples()
    if os.path.exists(filename):
        os.remove(filename)
    else:
        raise OSError('Cannot delete temp file.')
    return samples[:size]


def create_and_paste_image(samples, dest, off=(0, 0)):
    filename = './temp.png'
    fig = full_frame((min(len(samples) / SAMPLE_CONST, 1) * SAMPLE_SIZE[0], SAMPLE_SIZE[1]))
    fig.set_dpi(DPI)
    plt.plot(samples, color=INK_COLOR)
    plt.axis('off')
    plt.savefig(filename, dpi=DPI, bbox_inches='tight')
    img = Image.open(filename)
    dest.paste(img, off)
    img.close()
    if os.path.exists(filename):
        os.remove(filename)
    else:
        raise OSError('Cannot delete temp file.')


def add_text_to_image(text, dest, off=(0, 0), lang='en', tld='com', size=SAMPLE_SIZE):
    samples = create_samples(text, lang=lang, tld=tld, size=size)
    create_and_paste_image(samples, dest, off)


def add_cut_text_to_image(text, dest, off=(0, 0), lang='en', tld='com', size=SAMPLE_SIZE):
    samples = create_samples(text, lang=lang, tld=tld, size=None)
    for i in range(0, min(12, 1 + len(samples) // SAMPLE_CONST)):
        sample = samples[i * SAMPLE_CONST:min(len(samples), (i + 1) * SAMPLE_CONST)]
        create_and_paste_image(sample, dest, (off[0], off[1] + (i * MARGIN)))
    return i
