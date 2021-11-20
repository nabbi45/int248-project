# int248-project
Group members -
1. Naveen Pratap (11804642)
2. Aman Kumar Upadhyay (11804635)

CONVOLUTIONAL NEURAL NETWORKS

Convolutional neural network, is a part of artificial neural networks which deals with images. We can use this neural network to manipulate and use deep learning with images, videos and pixals. It consisits of artificial neurons to deal with complex problems of images and videos.

Let us have a set of elements, namely M M = {m1, m2, …,mn} …(1)

and set of input itights, namely Wt respectively Wt = {wt1, wt2, …..,wtn} …(2)

and an input bias . Thus the output is represented as N = f(∑i (mi * wti) + bias) …(3)

Thus it have a single output for a series of inputs. This concept of Artificial Neural Network is used in Convolutional Neural Networks as convolution operation. When an image is given as input, it apply some mask or filter on it, to obtain the desired output. Every image is made up of pixels, that is, some numeric values. Now these masks, of a very small size, are moved on the image such that every pixel becomes an input to these masks.

The input part of the image, say In(0,0), In(0,1), In(0,2) In(1,0), In(1,1), In(1,2) In(2,0), In(2,1), In(2,2) …(4)

Is masked on with the values of the mask or the filter, and the final output is a single value given by N = M1 * In(0,0) +M2 * In(0,1) +M3 * In(0,2) + M4 * In(1,0) +M5 * In(1,1) +M6 * In(1,2) + M7 * In(2,0) +M8 * In(2,1) +M9 * In(2,2) …(5)

Thus the masked value at point I on the image is replaced by Z in the new image.

AUTO ENCODERS

Auto encoders are neural networks that provide easy entries to understand and comprehend more complex concepts in machine learning. Auto encoders give us the output with same values as the input, after applying a series of operations on the data.

Model is the  approach towards colorization of greyscale images. It uses (5,5) filter in the initial layer of the model, besides working on the principles of CNN.

 Dataset Used: The Alpha model is trained on the Flower Dataset. The dataset contains around 10,000 images of various flower species. It provides us with high variety of images to get optimized results and minimum error.

 Optimizer: The optimizer used in the Aloha Model is Adaptive Moment Optimization, or commonly known as Adam. Adam Optimizer combines the heuristics or gradient descent with momentum algorithms and Root Mean Square Propagation.

Pt = (Ω1 * Pt-1) – (1- Ω1)*Gtt …(12) Qt = (Ω2 * Qt-1) – (1- Ω2)Gtt2

Where, Pt: Exponential Average of Gradients Qt: Exponential Average of Gradient Squares Gtt: Gradient at time t Ω: Hyper parameters

Exponential Average of Gradients, that is, Pt can also be written as:

Pt = (1- Ω2) ∑nx=1 Ω2t-x* Gtt*2 …(14)

Hence the expected value of the exponential moving average at time t is [3]:

Exp[Pt] = Exp [(1- Ω2) ∑nx=1 Ω2t-x * Gtt2] = Exp [Gtt2](1- Ω2) ∑nx=1 Ω2t-x+c = Exp [Gtt2]*(1- Ω2) + c …(15)

Thus Adam showcases promising results with the dataset by increasing the efficiency in colorizing them into RGB format.

 Architecture: The Alpha Model uses stacked up auto encoders for converting greyscale images into coloured ones. Based on the mechanisms of Convolutional Neural Networks, it also includes dropouts to introduce noise, thus to prevent overfitting. It also includes initial three convolution layers, followed by an up sampling layer, then six convolution layers and again an up sampling layer. In the end it has three more convolution layers before the output layer.

 Loss: The Model inures a loss of about 0.0415 and a value loss of about 0.0388. Thus it shows that using these parameters, as used in the model, the loss between the final output images as compared to the input image, was low.
