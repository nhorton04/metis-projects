import numpy as np
import os
import pickle
import streamlit as st
import sys
import tensorflow as tf
import urllib

# from align import align
# from encode import code

import config
import dnnlib
import dnnlib.tflib as tflib
import pickle
import PIL.Image
import cv2
import argparse
import numpy as np
import config
import dnnlib
import dnnlib.tflib as tflib
import pickle
import PIL.Image
# sys.path.append('tl_gan')
# sys.path.append('pg_gan')
# import feature_axis
# import tfutil
# import tfutil_cpu

# This should not be hashed by Streamlit when using st.cache.
TL_GAN_HASH_FUNCS = {
    tf.compat.v1.InteractiveSession: id
}

def main():

            # load the StyleGAN model into Colab
    URL_FFHQ = 'https://drive.google.com/uc?id=1MEGjdvVpUsu1jB4zrXZN7Y4kBBOzizDQ'
    tflib.init_tf()
    with dnnlib.util.open_url(URL_FFHQ, cache_dir=config.cache_dir) as f:
        generator_network, discriminator_network, Gs_network = pickle.load(f)
    # load the latents
    s1 = np.load('latent_representations/Lrs/165531_v9_ba_01.npy')
    s2 = np.load('latent_representations/IMG_9585_01.npy')
    s3 = np.load('latent_representations/2348caca290df9583c11a157c6d37e6b_01.npy')

    s1 = np.expand_dims(s1,axis=0)
    s2 = np.expand_dims(s2,axis=0)
    s3 = np.expand_dims(s3,axis=0)
    # combine the latents with an average:

    x = st.slider('picture 1', 0.01, 0.99, 0.33)
    y = st.slider('picture 2', 0.01, 0.99, 0.33)
    z = st.slider('picture 3', 0.01, 0.99, 0.33)
    savg = (x*s1+y*s2+z*s3)

    # run the generator network to render the latents:
    synthesis_kwargs = dict(output_transform=dict(func=tflib.convert_images_to_uint8, nchw_to_nhwc=False), minibatch_size=8)
    images = Gs_network.components.synthesis.run(savg, randomize_noise=False, **synthesis_kwargs)

    for image in images:
        st.image((PIL.Image.fromarray(images.transpose((0,2,3,1))[0], 'RGB').resize((512,512),PIL.Image.LANCZOS)))


if __name__ == "__main__":
    main()
