DPI = 300
PAGE_SIZE = (2480, 3508)  # A4 at 300dpi
PAGE_COLOR = (255, 255, 255)  # White
INK_COLOR = (0, 0, 0)  # Black
SAMPLE_CONST = 200000
SAMPLE_SIZE = (7, 0.5)
ADDR_OFF = 1800
DEAR_OFF = 200
ROWS_OFF = 200
MARGIN = int(DPI * SAMPLE_SIZE[1])

EXAMPLE = {
    'address1': {
        'text': "Jearom Chaoss",
        'offset': ADDR_OFF,
        'limit': SAMPLE_CONST // 4,
        'cut': True,
    },
    'address2': {
        'text': "Chemin of Thedsq 55",
        'offset': ADDR_OFF,
        'limit': SAMPLE_CONST // 4,
        'cut': True,
    },
    'address3': {
        'text': "86322 Jeslamos",
        'offset': ADDR_OFF,
        'limit': SAMPLE_CONST // 4,
        'cut': True,
    },
    'space1': {
        'text': None,
        'offset': None,
        'limit': None,
        'cut': True,
    },
    'dear': {
        'text': "Salut mon cher,",
        'offset': DEAR_OFF,
        'limit': SAMPLE_CONST,
        'cut': True,
    },
    'space2': {
        'text': None,
        'offset': None,
        'limit': None,
        'cut': True,
    },
    'text': {
        'text': "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam consectetur vel velit eget ultricies. In et lacinia nisi, ac cursus ipsum. Pellentesque efficitur at tellus feugiat consequat. Phasellus orci sem, pharetra non malesuada sed, aliquet vitae arcu. Sed aliquet, mi at porta maximus, mauris lectus interdum eros, a placerat enim velit in velit. Quisque quis nisi eleifend, mattis nibh sodales, pulvinar ante. Nam iaculis, justo vel pellentesque blandit, ipsum ligula accumsan lectus, vel auctor neque urna ut mauris. Etiam vel ipsum quam. Praesent finibus pellentesque scelerisque. Suspendisse scelerisque tristique ultrices. Proin augue nisl, malesuada sed hendrerit in, malesuada sed quam. Integer metus enim, tempor vitae dictum in, euismod vel eros. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean eget tempus lectus, at commodo enim. Vivamus in augue orci. Mauris facilisis nibh ante, ac varius justo rutrum eu. Duis in augue dictum, bibendum felis ac, tristique orci. Nulla orci nisl, porta sit amet quam sed, aliquam pellentesque massa. Duis rhoncus dolor eu elit placerat volutpat. Morbi aliquet volutpat egestas. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Sed nec dolor nec nibh ultricies posuere venenatis ac lectus. Ut accumsan commodo nisi.",
        'offset': ROWS_OFF,
        'limit': SAMPLE_CONST,
        'cut': False,
    },
    'space3': {
        'text': None,
        'offset': None,
        'limit': None,
        'cut': True,
    },
    'conclusion': {
        'text': "Please die in a fire",
        'offset': ROWS_OFF,
        'limit': SAMPLE_CONST,
        'cut': True,
    },
    'signature': {
        'text': "Me, myself and I",
        'offset': ROWS_OFF,
        'limit': SAMPLE_CONST,
        'cut': True,
    },
}
