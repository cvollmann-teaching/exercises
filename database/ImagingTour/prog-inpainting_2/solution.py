from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import scipy.sparse as sparse


def masking_matrix(image_shape, percentage):
    """Randomly sets (1-percentage)*100 % of the pixels to zero, i.e.
    percentage*100% of the pixels are kept"""
    import numpy as np
    import scipy.sparse as sparse
    dim = np.prod(image_shape)
    indices = np.random.choice(np.arange(dim), replace=False, size=int(dim * percentage))
    A = sparse.coo_matrix((np.ones(len(indices)),
                           (indices, indices)), shape=(dim, dim)).tocsr()
    A = A.tocsr()
    return A


def generate_data(original, noisy, percentage):
    original_img = np.array(Image.open("steinpilz.png").convert("L"))
    original_img = original_img[::2,::2]
    img_shape = np.shape(original_img)
    masking_matrix(img_shape, percentage)

    A = masking_matrix(img_shape, percentage)
    b = A.dot(original_img.ravel()).reshape(img_shape)
    np.save("noisy_image", b)
    np.save("original_image", original_img)
    return None

def estimate_masking(data):

    data = data.ravel()
    indices = np.where(data != 0)[0]
    dim = np.prod(np.shape(data))
    A = sparse.coo_matrix((np.ones(len(indices)),
                           (indices, indices)), shape=(dim, dim)).tocsr()
    A = A.tocsr()
    return A

def difference_matrix(image_shape):
    """returns difference matrix D; shape = edges x nodes (graph=squared grid)"""
    H, W = image_shape
    n = H * W
    D = sparse.eye(n+1, n, k=0) - sparse.eye(n+1, n, k=-1)
    D_horizontal = sparse.kron(sparse.eye(H), sparse.eye(W-1, W, k=0) - sparse.eye(W-1, W, k=1))
    D_vertical = sparse.kron(sparse.eye(H-1, H, k=0) - sparse.eye(H-1, H, k=1), sparse.eye(W))
    D = sparse.vstack((D_horizontal, D_vertical))
    D = D.tocsr()
    return D

def reg_lstsq(A, b, D, reg_param=0.1, verbose=1):
    """A csr nxn, b vector nx1, D csr pxn, delta float"""
    import scipy.sparse.linalg
    _delta = reg_param
#    n = len(b)
    if verbose:
        print("start solving")
    recon_img = scipy.sparse.linalg.gmres(A.T @ A + _delta * D.T @ D, A.dot(b),maxiter=30)[0]
    if verbose:
        print("finished solving")
    # scipy.sparse.linalg.spsolve(A.T@A + _delta * D.T@D, A.dot(b))#
    return recon_img

def experiment(data_fname, reg_param, save=False):

    b = np.load(data_fname)
    img_shape = np.shape(b)
    print("Resolution:", img_shape)

    A = estimate_masking(b)
    D = difference_matrix(img_shape)
    recon_img = reg_lstsq(A, b.ravel(), D, reg_param=reg_param)

    plt.figure("Image Inpainting")
    plt.subplot(1, 2, 1)
    plt.imshow(b.reshape(img_shape), cmap='gray')
    plt.title("noisy image")
    plt.axis(False)

    plt.subplot(1, 2, 2)
    plt.imshow(recon_img.reshape(img_shape), cmap='gray')
    plt.axis(False)
    plt.title("reconstructed image: reg-param delta={}".format(reg_param))
    plt.show()

    if save:
        plt.savefig("Image_Inpainting", dpi='figure')

    return None




if __name__ == "__main__":

    generate_data(original="steinpilz.png", noisy="noisy_image", percentage=0.01)
    original = np.load("original_image.npy")
    plt.imshow(original, cmap="gray")
    experiment("noisy_image.npy", 0.02, save=False)
