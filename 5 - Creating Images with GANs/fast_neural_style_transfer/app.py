import streamlit as st
from models import TransformerNet
from utils import *
import torch
import numpy as np
from torch.autograd import Variable
import argparse
import tkinter as tk
import os
import cv2
import matplotlib
matplotlib.use('TkAgg')
st.set_option('deprecation.showfileUploaderEncoding', False)
import matplotlib.pyplot as plt
import tqdm
from torchvision.utils import save_image
from PIL import Image


def main():

    uploaded_file = st.file_uploader("Choose a pic", type=['jpg', 'png', 'webm', 'mp4', 'gif', 'jpeg'])
    if uploaded_file is not None:
        st.image(uploaded_file, width=300)

    folder = os.path.abspath(os.getcwd())
    fold = folder
    folder = folder + '/models'
    points = fold + '/checkpoints'

    fnames = []
    pnames= []

    for basename in os.listdir(folder):
        fname = os.path.join(folder, basename)

        if fname.endswith('.pth'):
            fnames.append(fname)
    checkpoint = st.selectbox('Select a pretrained model', fnames)


    os.makedirs("images/outputs", exist_ok=True)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    # device = torch.device("cpu")
    transform = style_transform()

    # for basename1 in os.listdir(points):
    #     print(basename1)
    #     pname = os.path.join(points, basename1)
    #
    #     if pname.endswith('.pth'):
    #         pnames.append(pname)
    # checkpoint2 = st.selectbox('Select a pretrained checkpoint', pnames)

    try:
        # Define model and load model checkpoint
        transformer = TransformerNet().to(device)
        transformer.load_state_dict(torch.load(checkpoint))
        transformer.eval()

        # Prepare input
        image_tensor = Variable(transform(Image.open(uploaded_file).convert('RGB'))).to(device)
        image_tensor = image_tensor.unsqueeze(0)

        # Stylize image
        with torch.no_grad():
            stylized_image = denormalize(transformer(image_tensor)).cpu()


        fn = str(np.random.randint(0, 100)) + 'image.jpg'
        style_name = os.path.basename(checkpoint).split(".")[0]
        save_image(stylized_image, f"images/outputs/{style_name}-{fn}")

        st.image(f"images/outputs/{style_name}-{fn}", width=700)


    except:
        st.write('Choose an image')
    # imagee = cv2.imread(f"images/outputs/stylized-{fn}")
    # cv2.imshow('Image', imagee)



if __name__ == "__main__":
    main()
