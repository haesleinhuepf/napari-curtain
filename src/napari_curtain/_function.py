from napari_plugin_engine import napari_hook_implementation
import napari
from magicgui import magicgui
import numpy as np
from napari_tools_menu import register_action

# This is the actual plugin function, where we export our function
# (The functions themselves are defined below)
@napari_hook_implementation
def napari_experimental_provide_function():
    return [curtain_gpu]


@register_action(menu="Visualization > Curtain")
def start_curtain(viewer):
    viewer.window.add_dock_widget(curtain, name="Curtain")


# We use magicgui to make the position a slider. Furthermore,
# we make the function be called once the user changes a
# parameter. Read more about magicgui:
# https://napari.org/magicgui/usage/configuration.html
@magicgui(
    auto_call=True,
    position={'widget_type': 'Slider', 'min': 0, 'max': 100}
)
def curtain(
    image1: napari.types.ImageData,
    image2: napari.types.ImageData,
    factor1: float = 1,
    factor2: float = 1,
    position: float = 50
) -> napari.types.ImageData:
    copy = image1 * factor1

    if image1 is None or image2 is None:
        return
    # check if image shapes are equal
    assert np.array_equal(image1.shape, image2.shape), "Image dimensions should match"

    image1 = np.asarray(image1)
    image2 = np.asarray(image2)

    curtain_position = int(position / 100 * image1.shape[-1])
    copy[..., curtain_position:] = image2[..., curtain_position:] * factor2

    return copy
