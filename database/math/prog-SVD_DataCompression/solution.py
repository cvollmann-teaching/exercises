import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg as linalg


def load_image_as_gray(path_to_image):
    """
    loads image and returns luma transform as numpy array
    """
    import matplotlib
    img = matplotlib.image.imread(path_to_image)
    print(np.shape(img))
    # ITU-R 601-2 luma transform (rgb to gray)
    img = np.dot(img, [0.2989, 0.5870, 0.1140])
    return img


def generate_video(U, Vt, sigma):
    from matplotlib import animation
    dpi = 250
    idlist = range(120)
    frames = []  # for storing the generated images
    fig = plt.figure()
    for i in idlist:
        aux = np.zeros((m, 2*n+50))
        aux[:, :n] = U[:, :i] @ np.diag(sigma[:i]) @ Vt[:i, :]
        aux[:, -n:] = A
        storage = np.round(100 * i * (1. + m + n) / (m * n), 2)
        frames.append([plt.imshow(aux, cmap='gray'),
                       plt.text(1, 1,
                                "k={}, storage={}%".format(str(idlist[i]),
                                   str(storage)),
                                horizontalalignment='left',
                                verticalalignment='top',
                                color="white"),
                                plt.title(
                                        "Truncated SVD A_k   VS   Original A"
                                        )])
    ani = animation.ArtistAnimation(fig,
                                    frames,
                                    interval=180,
                                    blit=True,
                                    repeat_delay=1000)
    ani.save('movie.mp4', dpi=dpi)
    plt.show()
    return None


if __name__ == "__main__":

    path_to_image = 'kalle.jpg'
    A = load_image_as_gray(path_to_image)

    U, sigma, Vt = linalg.svd(A)
    m, n = np.shape(A)

    # 1 plot singular values
    plt.figure()
    plt.subplot(3, 3, 1)
    plt.title(r'$\sigma$')
    x = np.linspace(1, sigma.size, sigma.size)
    plt.semilogy(x,
                 sigma,
                 'o-',
                 label='sigma',
                 markersize=3)
    plt.semilogy([100, 100, 0],
                 [0, sigma[100],
                  sigma[100]],
                 '-',
                 lw=2,
                 color='red')
    plt.grid(True)

    # 2 plot truncated svd images
    K = [1, 3, 5, 10, 20, 50, 100]
    for k in K:
        truncated_svd = U[:, :k] @ np.diag(sigma[:k]) @ Vt[:k, :]
        print("\nrank = {} \nrelative storage (truncated-SVD/A): {}%".format(
                k, np.round(100 * k * (1. + m + n) / (m * n), 2)))
        plt.subplot(3, 3, K.index(k)+2)
        plt.imshow(truncated_svd, cmap='gray')
    #    TODO: fix title issue
    #    plt.title("\nrank = {} \nrelative storage: {}%".format(
    #            k, np.round(100 * k * (1. + m + n) / (m * n), 2)))
        plt.tight_layout(pad=0.4, w_pad=0.05, h_pad=0.5)

    # 3 plot original
    plt.subplot(3, 3, 9)
    plt.imshow(A, cmap='gray')
    plt.title("original")

#    generate_video(U, Vt, sigma)
