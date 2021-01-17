#Python 3.7

__authors__ = ("Arial Nathan")
__contact__ = ("gg")
__version__ = "0"
__copyright__ = "Arial nathan C tout droit réservé"
__date__ = "Janvier 2021"

import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':

    #Imag a marquer
    img=plt.imread("images.jpg")
    plt.imshow(img)

    #image a dissimuler
    pix=np.uint8(plt.imread("watermarque.png"))
    plt.imshow(pix)

    # ou cacher l'information
    # ici l'octet bleu

    plan = np.zeros(img.shape[0:2], dtype="uint8")
    plan[:,:] = img[:,:,2]

    # profnondeur de gravure
    #clef comprise entre 0 et 7
    #clef
    clef=5

    #afficher les valeur en binnaire
    print(bin(255))
    print(bin((255-2**clef)))

    #mise a 0 du plan qui vas servir de support
    plan_troue = np.bitwise_and(plan,(np.ones(img.shape[0:2], dtype="uint8")*(255-2**clef)))

    #creation de la marque
    marque = np.zeros(img.shape[0:2], dtype="uint8")
    marque = ((pix)*(2**clef))

    #insertion de la marque
    plan_marque= np.bitwise_or(plan_troue,marque)

    #nouvelle image couleur tatouer
    img2=np.copy(img)

    #on remplace le bleu
    img2[:,:,2]=plan_marque

    #  Affichage & save
    plt.imshow(img2)
    plt.imsave("image_marque.bmp",img2,vmin = 0, vmax = 255, format="bmp")

    #simmulation attaque par compression
    plt.imsave("image_marque.jpg",img2,vmin = 0, vmax = 255, format="jpg")