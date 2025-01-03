# Introduction to Deep Learning in Python Course

## Introduction to Deep Learning

- Deep learning is a subset of machine learning, which is a subset of artificial intelligence.
- Deep learning is a type of machine learning that trains a computer to perform human-like tasks, such as recognizing speech, identifying images or making predictions.
- Instead of organizing data to run through predefined equations, deep learning sets up basic parameters about the data and trains the computer to learn on its own by recognizing patterns using many layers of processing.
- We use Keras for this course. Keras is a high-level neural networks API, written in Python and capable of running on top of TensorFlow, CNTK, or Theano.

## Forward Propagation

- Forward propagation is the process neural networks use to make predictions.
- Bank transactions example:
  - Inputs: number of children, number of existing accounts.
  - Output: number of transactions.
  - Weights: parameters that the model learns.
  - [Model Photo](forward_propagation.png)
- Dot product: multiply the inputs by the weights and sum them up.
- Forward propagation for one data point. Output is the prediction for that data point.
- Code:

```python
import numpy as np
input_data = np.array([2, 3])
weights = {'node_0': np.array([1, 1]),
           'node_1': np.array([-1, 1]),
           'output': np.array([2, -1])}
node_0_value = (input_data * weights['node_0']).sum()
node_1_value = (input_data * weights['node_1']).sum()
hidden_layer_values = np.array([node_0_value, node_1_value])
print(hidden_layer_values)
output = (hidden_layer_values * weights['output']).sum()
print(output)
```

## Activation Functions

- Activation functions are applied to node inputs to produce node output.
- An activation function allows models to capture non-linearities.
- If the relationships in the data are non-linear, we need an activation function to capture them.
- Applied to node inputs, activation functions produce node outputs.
- Activation functions:
  - ReLU (Rectified Linear Activation): max(0, x)
  - Tanh (Hyperbolic Tangent): (e^x - e^-x) / (e^x + e^-x)
  - Sigmoid: 1 / (1 + e^-x)
  - Identity: f(x) = x
- [Activation Function Tanh](activation_function_tanh.png)

### ReLU (Rectified Linear Activation)

- ReLU is the most common activation function.
- [Activation Function ReLU](ReLU.png)

### Tanh Example

- Example code:

```python
import numpy as np
input_data = np.array([-1, 2])
weights = {'node_0': np.array([3, 3]),
           'node_1': np.array([1, 5]),
           'output': np.array([2, -1])}
node_0_input = (input_data * weights['node_0']).sum()
node_0_output = np.tanh(node_0_input)
node_1_input = (input_data * weights['node_1']).sum()
node_1_output = np.tanh(node_1_input)
hidden_layer_outputs = np.array([node_0_output, node_1_output])
output = (hidden_layer_outputs * weights['output']).sum()
print(output)
```

### ReLU Example

- Example code:

```python
def relu(input):
    '''Define your relu activation function here'''
    # Calculate the value for the output of the relu function: output
    output = max(0, input)
    
    # Return the value just calculated
    return(output)

# Calculate node 0 value: node_0_output
node_0_input = (input_data * weights['node_0']).sum()
node_0_output = relu(node_0_input)

# Calculate node 1 value: node_1_output
node_1_input = (input_data * weights['node_1']).sum()
node_1_output = relu(node_1_input)

# Put node values into array: hidden_layer_outputs
hidden_layer_outputs = np.array([node_0_output, node_1_output])

# Calculate model output (do not apply relu)
model_output = (hidden_layer_outputs * weights['output']).sum()

# Print model output
print(model_output)
```

## Deeper Networks

- There is more than one hidden layer.
- Deep networks internally build representations of patterns in the data.
- You use same forward propagation process, but apply it multiple times iteratively.
- [Deeper Networks](multiple_hidden_layers_relu.png)
- This is the mechanics for how neural networks make predictions.

### Representation Learning

- Deep networks internally build representations of patterns in the data.
- Partially replace the need for feature engineering.
- Subsequent layers build increasingly sophisticated representations of raw data.
- First layer might detect edges, second layer might detect shapes, third layer might detect high-level features. It shows us how deep learning models can learn from the data.

### Deep Learning

- Modeler doesn't need to specify the interactions.
- When you train the model, the neural network gets weights that find the relevant patterns to make better predictions.

## The need for optimization

- Optimization finds the set of weights that minimizes the loss function.
- Loss function measures how well the model's predictions match the target values.
- We use the data to update the weights.
- Making accurate predictions gets harder with more points.
- At any set of weights, there are many values of the error corresponding to the many points we make predictions for.

### Loss Function

- Aggregates errors in predictions from many data points into single number.
- Measure of model's predictive performance.
- Lower loss function value means a better model.
- We use the mean squared error loss function.
- [Loss Function Graph](loss_function_graph.png)
- Goal: Find the weights that give the lowest value for the loss function.
- Gradient descent is a general method to minimize functions.

### Gradient Descent

- Imagine you are in a pitch dark field.
- Want to find the lowest point.
- Feel the ground to see how to go downhill.
- Take small steps downhill.
- Repeat until it is uphill in every direction.
- This is gradient descent.
- Steps:
  - Start at random point.
  - Until you are somewhere flat:
    - Find the slope.
    - Take a step downhill.
- Learning rate: how big the step is.
- Too big: might miss the minimum.
- Too small: will take too long.

## Review

- The importance of model weights in making accurate predictions. Adjusting weights can significantly change the model's output.
- The concept of a loss function, which aggregates all prediction errors into a single measure, helping to evaluate the model's performance.
- Gradient descent, an algorithm used to find the set of weights that minimizes the loss function. It involves starting with random weights, calculating the slope (or gradient) of the loss function at those weights, and then adjusting the weights in the direction that reduces the loss.

## Gradient Descent (Continued)

- If the slope is positive:
  - Going opposite the slope means moving to lower numbers.
  - Subtract the slope from the current value.
  - Too big a step might lead us astray.
- Learning rate: how much we update the weights. Update each weight by subtracting the product of learning rate and slope.
- Slope calculation for a weight, need to multiply:
  - Slope of the loss function w.r.t (with respect to) the value at the node we feed into.
  - The value of the node that feeds into our weight.
  - Slope of the activation function w.r.t the value we feed into.
- Slope of mean-squared loss function w.r.t prediction:
  - 2 *(prediction - actual) = 2* error.

### Gradient Descent Example

[Example](slope_calculation_example.png)

- 2 * -4 = -8 (slope of the loss function w.r.t prediction).
- 2 *-4* 3 = -24 (slope of the loss function w.r.t prediction * node value).
- If learning rate is 0.01, the new weight would be 2 - 0.01 * -24 = 2.24. This is how we update the weights.

## Backpropagation

- Takes the error from the output layer and propagates it backward through the network.
- It calculates the necessary slopes sequentially from the weights closest to the prediction, through the hidden layers, to the input layer.
- Allow gradient descent to update all weights in the neural network (by getting gradients for all weights).
- Comes from chain rule of calculus.
- Process:
  - Trying to estimate the slope of the loss function w.r.t each weight.
  - Do forward propagation to calculate predictions and errors.
  - Go back one layer at a time.
  - Gradients for weight is product of:
    - Node value feeding into that weight.
    - Slope of loss function w.r.t node it feeds into.
    - Slope of activation function at the node it feeds into.
  - Use these gradients to update the weights.
  - Need to also keep track of slopes of the loss function w.r.t node values.
  - Slope of node values are the sum of the slopes for all weights that come out of them.

### ReLU Activation Function

- Slope is 0 for negative values.
- Slope is 1 for positive values.

## Backpropagation In Practice

- Calculating slopes associated with any weight in the network.
- Gradients for weight is product of:
  - Node value feeding into that weight.
  - Slope of the loss function w.r.t node it feeds into.
  - Slope of activation function at the node it feeds into.

[Backpropagation](backpropagation_example.png)

### Recap

- Start at some random set of weights.
- Use forward propagation to make a prediction.
- Use backward propagation to calculate the slope of the loss function w.r.t each weight.
- Multiply that slope by the learning rate, and subtract from the current weights.
- Keep going with that cycle until we get to a flat part.

## Stochastic Gradient Descent

- It is common to calculate slopes on only a subset of the data ('batch').
- Use a different batch of data to calculate the next update.
- Start over from the beginning once all data is used.
- Each time through the training data is called an epoch.
- When slopes are calculated on one batch at a time: stochastic gradient descent.
- When slopes are calculated on the whole data set: gradient descent.

## Creating a Keras Model

- Model building steps:
  - Specify architecture.
    - How many layers?
    - How many nodes in each layer?
    - What activation function?
  - Compile.
    - Loss function.
    - Optimizer.
  - Fit.
    - Iteratively improve weights.
    - Backpropagation.
    - Optimization of weights.
  - Predict.

### Model Specification

```python
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

predictors = np.loadtxt('predictors_data.csv', delimiter=',')
n_cols = predictors.shape[1]

model = Sequential()
model.add(Dense(100, activation='relu', input_shape=(n_cols,)))
model.add(Dense(100, activation='relu'))
model.add(Dense(1))
```

- Sequential model: a linear stack of layers. You can create a Sequential model by passing a list of layer instances to the constructor.
- Dense: a regular densely-connected NN layer. It is the most common and frequently used layer.
- Activation: the activation function to use. If you don't specify anything, no activation is applied (ie. "linear" activation: a(x) = x).
- Input_shape: the shape of the input to the model. It is required when using this layer as the first layer in a model.

## Compiling and fitting a model

- Why you need to compile your model:
  - Specify the optimizer.
    - Controls the learning rate.
    - Many options and mathematically complex.
    - "Adam" is usually a good choice.
  - Loss function.
    - "mean_squared_error" common for regression.
    - "categorical_crossentropy" common for classification.
  - Metrics.

### Compiling a model

```python
n_cols = predictors.shape[1]

model = Sequential()
model.add(Dense(100, activation='relu', input_shape=(n_cols,)))
model.add(Dense(100, activation='relu'))
model.add(Dense(1))
model.compile(optimizer='adam', loss='mean_squared_error')
```

### Fitting a model

- What is fitting a model?
  - Applying backpropagation and gradient descent with your data to update the weights.
  - Scaling data before fitting can ease optimization.

```python
model.fit(predictors, target)
```

## Classification Models

- Classification: 'categorical_crossentropy' loss function.
- Similar to log loss: lower is better.
- Add metrics = ['accuracy'] to compile step for easy-to-understand diagnostics.
- Output layer has separate node for each possible outcome, and uses 'softmax' activation.
- Softmax ensures the predictions sum to 1 so they can be interpreted as probabilities.

### Classification Example

```python
from tensorflow.keras.utils import to_categorical

data = pd.read_csv('basketball_shot_log.csv')
predictors = data.drop(['shot_result'], axis=1).as_matrix()
target = to_categorical(data.shot_result)

model = Sequential()
model.add(Dense(100, activation='relu', input_shape=(n_cols,)))
model.add(Dense(100, activation='relu'))
model.add(Dense(100, activation='relu'))
model.add(Dense(2, activation='softmax'))
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(predictors, target)
```

## Using Models

- Save model after fitting.
- Reload model.
- Make predictions.

### Saving, reloading and using your Model

```python
from tensorflow.keras.models import load_model
model.save('model_file.h5')
my_model = load_model('my_model.h5')
predictions = my_model.predict(data_to_predict_with)
probability_true = predictions[:,1]
```

```python
my_model.summary()
```

- Summary method shows the model's architecture.

## Understand Model Optimization

- Why optimization is hard:
  - Simultanously update thousands of weights with complex relationships.
  - Updates may not improve model meaningfully.
  - Updates too small (if learning rate is low) or too large (if learning rate is high).
  - Getting stuck in local minima.

### Stochastic Gradient Descent (SGD)

- Stochastic gradient descent:
  - Uses only a random subset of the data for each batch.
  - Faster than standard gradient descent.
  - Can be less stable than standard gradient descent.
  - Keras has the 'SGD' optimizer.
- Example:

```python
def get_new_model(input_shape = input_shape):
    model = Sequential()
    model.add(Dense(100, activation='relu', input_shape = input_shape))
    model.add(Dense(100, activation='relu'))
    model.add(Dense(2, activation='softmax'))
    return(model)

lr_to_test = [0.000001, 0.01, 1]

# Loop over learning rates
for lr in lr_to_test:
    model = get_new_model()
    my_optimizer = SGD(lr=lr)
    model.compile(optimizer=my_optimizer, loss='categorical_crossentropy')
    model.fit(predictors, target)
```

### Dying Neuron Problem

- This problem occurs when a neuron takes a value less than 0 for all rows of data.
- With the ReLU activation function, a negative input will output 0 and it also has a slope of 0.
- This means that the weights will not be updated. The neuron is "dead" because it is unlikely to fire for any data point.

### Vanishing Gradients

- Occurs when many layers have very small slopes (e.g. due to being on flat part of tanh curve).
- In deep networks, updates to backprop were close to 0.

## Model Validation

- Validation in deep learning:
  - Commonly use validation split rather than cross-validation due to computational expense.
  - Deep learning widely used on large datasets, training on a single split is common.
  - Single validation score is based on large amount of data, and is reliable.

```python
model.fit(predictors, target, validation_split=0.3)
```

### Early Stopping

- Early stopping:
  - End training when performance on validation set starts to degrade.
  - Avoid overfitting.
  - Keras has 'EarlyStopping' callback for this.
  - 2 or 3 are reasonable numbers of epochs to wait.
  - Patience parameter: number of epochs to wait before stopping.

```python
from tensorflow.keras.callbacks import EarlyStopping

early_stopping_monitor = EarlyStopping(patience=2)
model.fit(predictors, target, validation_split=0.3, epochs=20, callbacks=[early_stopping_monitor])
```

### Experimentation

- Experiment with different architectures.
- More layers.
- Fewer layers.
- Layers with more nodes.
- Layers with fewer nodes.
- Early stopping.
- Creating a great model requires experimentation.

## Thinking About Model Capacity

- Model capacity or network capacity:
  - Model's ability to capture predictive patterns in data.
  - Model capacity too low: underfitting.
  - Model capacity too high: overfitting. [Overfitting](overfittiing.png)
- Overfitting
  - Overfitting: model memorizes training data rather than learning from it.
  - Overfitting is the ability of a model to fit oddities in your training data that are there purely due to happenstance, and that won't apply in an new dataset.
  - When you are overfitting, your model will make accurate predictions on the training data, but it will make inaccurate predictions on validation data and new datatests.
- Underfitting
  - Underfitting: model is not able to capture the patterns in the data. Model fails to find important predictions in the training data.
  - Underfitting is when the model is too simple to learn the underlying structure of the data.
  - When you are underfitting, your model will make inaccurate predictions on both the training data and the validation data.
- Our validation score is the key indicator of how well our model is generalizing to new data. Ultimate measure of a model's predictive quality.
- Model capacity is a model's ability to capture predictive patterns in data.
- So, the more capacity a model has, the more patterns it can capture. Making larger layers or adding more layers increases the model's capacity.

### Worflow for Optimizing Model Capacity

- Start with a small network.
- Gradually increase capacity.
- Keep increasing capacity until validation score is no longer improving.
- [Model Capacity](sequential_experiments_model_capacity.png)

## Stepping Up To Images

### Recognizing handwritten digits

- MNIST dataset: images of handwritten digits.
- 28 x 28 grid flattened to 784 values for each image.
- Value in each part of array represents darkness of that pixel.

## Final Thoughts

- Deep learning is widely used and rapidly changing field.
- Keras is a great tool for building deep learning models.
- There are many techniques to improve your model's performance.
- Experiment with different architectures to improve performance.

###  Next Steps

- Start with standard prediction problems on tables of numbers.
- Images (with convolutional neural networks) are a common next step.
- Text data (with recurrent neural networks) is another common next step.
- Kaggle is a great place to practice.
- Wikipedia and deeplearning.ai are great resources.
- List of datasets for machine learning research: <https://en.wikipedia.org/wiki/List_of_datasets_for_machine-learning_research>
- List of datasets for computer vision and image processing: <https://en.wikipedia.org/wiki/List_of_datasets_in_computer_vision_and_image_processing>
- keras.io for excellent documentation.
- Graphical Processing Units (GPUs) can speed up training.
- Need a CUDA-compatible Nvidia GPU.
- For training on a GPU in the cloud, consider using Amazon Web Services, Google Cloud Platform, or Microsoft Azure.
