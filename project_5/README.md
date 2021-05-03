# Image Creation with Generative Adversarial Networks
![Python 3.6](https://img.shields.io/badge/python-3.6-green.svg?style=plastic)
![cuDNN 8.0.3](https://img.shields.io/badge/cudnn-8.0.3-green.svg?style=plastic)
![streamlit 0.66.0](https://img.shields.io/badge/Streamlit-0.66.0-g.svg?style=plastic)




For my final project at Metis, I set out to create a web app where a user could upload two images of faces and get back a hybridized result.


## Web Apps
I ended up making three different web apps (made possible by Streamlit's ease of use) - face swap, style transfer, and StyleGAN encoding - my original goal, blending faces ! - however, unfortunately the StyleGAN app can't accept any new images, it can only load .npy latent representation files and then blend them to different ratios using sliders. The other two apps are fully functional though (although too big to upload to Heroku - I want to host it myself soon).

I ended up making three different web apps - face swap, style transfer, and StyleGAN encoding. Try them out for yourself! [Coming soon]

---
###Style Transfer
![PyTorch 1.3.1](https://img.shields.io/badge/pytorch-1.3.1-red.svg?style=plastic)
![PIL 7.2.0](https://img.shields.io/badge/PIL-7.2.0-yellow.svg?style=plastic)
The user uploads one image, selects a model for the style from the drop down menu, and then receives a style transferred result through [eriklindernoren](https://github.com/eriklindernoren)'s [Fast Neural Style Transfer](https://github.com/eriklindernoren/Fast-Neural-Style-Transfer). The pretrained models correspond to the style images I trained, and their filesnames contain the number of iterations when the model was saved.

###Face Swap
![Open CV 4.4.0](https://img.shields.io/badge/opencv-4.4.0-indigo.svg?style=plastic)
![dlib 19.21.0](https://img.shields.io/badge/dlib-19.21.0-purple.svg?style=plastic)
The user uploads two images and then can press two buttons: Swap Down, or Swap Up. An image of the corresponding swap is returned. The face swap implementation is from [wuhuikai](https://github.com/wuhuikai)'s [Face Swap](https://github.com/wuhuikai/FaceSwap) using OpenCV and dlib.

##StyleGAN Encoder
![TensorFlow 1.15](https://img.shields.io/badge/tensorflow-1.15-orangered.svg?style=plastic)
![Keras 2.0.8](https://img.shields.io/badge/keras-2.0.8-darkred.svg?style=plastic)
The user can select a pretrained latent representation (.npy file) or encode their own by going to the StyleGAN directory and running
>python encode_images.py aligned_images/ generated_images/ latent_representations/

Then in `app.py`, set the variables `s1` and `s2` equal to `latent_representations/<your_file_here>.npy`. Finally, enjoy sliding the sliders around and watching the face change!

#### General App Instructions
Navigate to the directory of the desired app, activate your virtual environment and install the  requirements from `requirements.txt` using pip/anaconda, then run `streamlit run app.py`. 

## References

`inception_v3_features.pkl` and `inception_v3_softmax.pkl` are derived from the pre-trained [Inception-v3](https://arxiv.org/abs/1512.00567) network by Christian Szegedy, Vincent Vanhoucke, Sergey Ioffe, Jonathon Shlens, and Zbigniew Wojna. The network was originally shared under [Apache 2.0](https://github.com/tensorflow/models/blob/master/LICENSE) license on the [TensorFlow Models](https://github.com/tensorflow/models) repository.

`vgg16.pkl` and `vgg16_zhang_perceptual.pkl` are derived from the pre-trained [VGG-16](https://arxiv.org/abs/1409.1556) network by Karen Simonyan and Andrew Zisserman. The network was originally shared under [Creative Commons BY 4.0](https://creativecommons.org/licenses/by/4.0/) license on the [Very Deep Convolutional Networks for Large-Scale Visual Recognition](http://www.robots.ox.ac.uk/~vgg/research/very_deep/) project page.

`vgg16_zhang_perceptual.pkl` is further derived from the pre-trained [LPIPS](https://arxiv.org/abs/1801.03924) weights by Richard Zhang, Phillip Isola, Alexei A. Efros, Eli Shechtman, and Oliver Wang. The weights were originally shared under [BSD 2-Clause "Simplified" License](https://github.com/richzhang/PerceptualSimilarity/blob/master/LICENSE) on the [PerceptualSimilarity](https://github.com/richzhang/PerceptualSimilarity) repository.
