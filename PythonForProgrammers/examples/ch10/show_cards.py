#/%matplotlib inline
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

from deck import DeckOfCards
from pathlib import Path

deck_of_cards = DeckOfCards()

path = Path('.').joinpath('card_images')

figure, axes_list = plt.subplots(nrows = 4, ncols = 13)

for axes in axes_list.ravel():
    axes.get_xaxis().set_visible(False)
    axes.get_yaxis().set_visible(False)
    image_name = deck_of_cards.deal_card().image_name
    img = mpimg.imread(str(path.joinpath(image_name).resolve()))
    axes.imshow(img)

deck_of_cards.shuffle()

for axes in axes_list.ravel():
    axes.get_xaxis().set_visible(False)
    axes.get_yaxis().set_visible(False)
    image_name = deck_of_cards.deal_card().image_name
    img = mpimg.imread(str(path.joinpath(image_name).resolve()))
    axes.imshow(img)
    