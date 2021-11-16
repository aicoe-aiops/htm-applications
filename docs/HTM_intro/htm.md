# Hierarical Temporal Memory

The HTM algorithm is based on the well understood principles and core building blocks of the Thousand Brains Theory. In particular, it focuses on three main properties: sequence learning, continual learning and [sparse distributed representations](https://numenta.com/assets/pdf/biological-and-machine-intelligence/BaMI-SDR.pdf). HTM is a model of general artificial intelligence.Behind this model is a learning method based on the understanding of brain neuroscience, combining mathematics and computer science theories, and finally combining it. It is an imitation is the learning ability of the human brain. 

In the [blog post](https://numenta.com/neuroscience-research/research-publications/papers/thousand-brains-theory-of-intelligence-companion-paper/) by Numenta, the author has mentioned the advantage of several HTM models over current neural networks models. 

- **Continual learning/online learning**

Neural network classifiers generally switch to prediction mode after training is completed and internal weights are determined, and they will be officially launched into service. But in the real world, new materials will continue to form new patterns. Therefore neural network-like models usually need to be retrained with new data after going online for a period of time. How to make the neural network model able to maintain the learning ability while still in service has always been everyone's own words, and there is no unified best answer. HTM claims to have such capabilities natively. 

- **Noise robustness and fault tolerance**

We currently know that neural-like networks are very sensitive to subtle disturbances of input data. Misclassified data, missing data, or deliberately altered data can interfere with the training and prediction capabilities of neural networks to a considerable extent. How to enhance the ability to resist noise interference in neural networks is still a problem under research. But HTM claims to have native noise immunity.

- **No hyperparameter tuning**

Artificial intelligence based on neural network models has always been ridiculed as "alchemy". Machine learning engineers laugh at themselves as "alchemists" or "alchemists" because there are too many in the process of training neural network models. Hyperparameter needs to be decided, but the decision is almost based on experience and luck. There is even a saying that " convergence depends on luck, and the effect depends on the destiny ". There is no systematic decision method supported by mathematical theory.

The simplest example, just how to adjust the learning rate, there are a lot of paper. Just how to set the network architecture (how many layers? What layer to use? Too few layers are not accurate, too many layers will disappear and the gradient will explode directly in the training phase) can kill people. Even with the help of NAS and AutoML later , "tuning" is still a big trouble. If HTM does not require tuning at all (or there are only a few parameters to be determined), it will really be a big advantage.

