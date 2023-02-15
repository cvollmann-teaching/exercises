import numpy as np
import matplotlib.pyplot as plt
import scipy.sparse as sparse
import scipy.sparse.linalg


def load_image_as_gray(path_to_image):
    import matplotlib
    img = matplotlib.image.imread(path_to_image)
    # ITU-R 601-2 luma transform (rgb to gray)
    img = np.dot(img, [0.2989, 0.5870, 0.1140])
    return img


def masking(img, percentage):
    """Randomly sets (1-percentage)*100 % of the pixels to zero

    Parameters
    ----------
    img : (H, W) ndarray
          original image
    percentage : float
                 number in (0,1)

    Returns
    -------
    b : ndarray
        masked image of shape (H*W, 1)
    indices : list
              of length <=H*W, subset of {0,...,(H*W-1)}
              contains indices of pixels that were kept
    """
    # flatten image in C order, i.e., append row by row
    print("Image dimensions: ", img.shape)
    img = img.ravel()
    n = len(img)
    # masking operator
    indices = np.random.choice(np.arange(n), replace=False,
                               size=int(n * percentage))

    b = np.zeros(n)
    b[indices] = img[indices]

    return b, indices


def inpainting(b, indices, delta, G):
    """
    inpainting based on trivial 1-d Sobolev Regularization

    Parameters
    ----------
    b : ndarray
        of shape (n, 1)
    indices : list or array-like
              of length <= n, subset of {0,...,(n-1)}
              contains indices of pixels that were kept
    delta : float
            positive number, regularization parameter
    G : numpy.ndarray
        of dimension (m,n), determining regularization

    Returns
    -------
    reconImg : ndarray
               of shape (n, 1)
               reconstructed image
    """
    n = len(b)
    # masking operator with A = A.T@A (n,n)
    A = sparse.coo_matrix((np.ones(len(indices)),
                           (indices, indices)), shape=(n, n)).tocsr()
    # solve with scipy sparse (note that: A.T@A = A)
    reconImg = scipy.sparse.linalg.spsolve(A + delta * G.T@G, A.dot(b))
    return reconImg


if __name__ == "__main__":

    # INPUT PARAMETERS
    # --------------
    path_to_image = 'kalle.jpg'  # 'happy_dog.jpg' # the image
    percentage = 0.1  # we randomly keep 100*percentage % of the data
    delta = 0.001  # regularization parameter

    # ORIGINAL IMAGE
    # --------------
    img = load_image_as_gray(path_to_image)
    H, W = np.shape(img)
    # plot original image
    plt.figure("Image Inpainting")
    plt.subplot(1, 3, 1)
    plt.imshow(img, cmap='gray')
    plt.title("original")

    # MASKED IMAGE
    # -----------
    b, indices = masking(img, percentage)
    n = len(b)
    # plot noisy image
    plt.subplot(1, 3, 2)
    plt.imshow(b.reshape((H, W)), cmap='gray')
    plt.title("masked image: {}% of pixels randomly lost".format(
              (1-percentage)*100))

    # RECONSTRUCTED IMAGE
    # -------------------
    # difference quotient (k+1,k)
    G = sparse.eye(n+1, n, k=0) - sparse.eye(n+1, n, k=-1)  # sparse.eye(n,n) #
    reconImg = inpainting(b, indices, delta, G)
    # plot denoised image
    plt.subplot(1, 3, 3)
    plt.imshow(reconImg.reshape((H, W)), cmap='gray')
    plt.title("reconstructed image: reg-param delta={}".format(delta))
#    plt.savefig("Image_Inpainting")
