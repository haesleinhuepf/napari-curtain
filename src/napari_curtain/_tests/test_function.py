# from napari_curtain import threshold, image_arithmetic

# add your tests here...


def test_curtain():
    import numpy as np
    image1 = np.asarray([
        [1, 1, 1, 1],
        [1, 1, 1, 1]
    ])
    image2 = np.asarray([
        [2, 2, 2, 2],
        [2, 2, 2, 2]
    ])

    reference = np.asarray([
        [1, 1, 4, 4],
        [1, 1, 4, 4]
    ])

    from napari_curtain._function import curtain

    result = curtain()(image1, image2, 1, 2, 50)

    assert np.allclose(result, reference)
