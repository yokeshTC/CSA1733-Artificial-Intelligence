import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

def train_network(X, y, epochs, learning_rate):
    np.random.seed(1)

    input_layer_size = X.shape[1]
    hidden_layer_size = 4
    output_layer_size = y.shape[1]

    weights_input_hidden = np.random.uniform(size=(input_layer_size, hidden_layer_size))
    weights_hidden_output = np.random.uniform(size=(hidden_layer_size, output_layer_size))

    for epoch in range(epochs):
        input_layer = X
        hidden_layer_input = np.dot(input_layer, weights_input_hidden)
        hidden_layer_output = sigmoid(hidden_layer_input)

        final_input = np.dot(hidden_layer_output, weights_hidden_output)
        output = sigmoid(final_input)

        output_error = y - output
        output_delta = output_error * sigmoid_derivative(output)

        hidden_error = output_delta.dot(weights_hidden_output.T)
        hidden_delta = hidden_error * sigmoid_derivative(hidden_layer_output)

        weights_hidden_output += hidden_layer_output.T.dot(output_delta) * learning_rate
        weights_input_hidden += input_layer.T.dot(hidden_delta) * learning_rate

    return weights_input_hidden, weights_hidden_output

def predict(X, weights_input_hidden, weights_hidden_output):
    hidden = sigmoid(np.dot(X, weights_input_hidden))
    output = sigmoid(np.dot(hidden, weights_hidden_output))
    return output

def main():
    X = np.array([
        [0, 0],
        [0, 1],
        [1, 0],
        [1, 1]
    ])

    y = np.array([
        [0],
        [1],
        [1],
        [0]
    ])

    epochs = 10000
    learning_rate = 0.1

    w1, w2 = train_network(X, y, epochs, learning_rate)

    print("Predictions after training:")
    for x in X:
        output = predict(np.array([x]), w1, w2)
        print(x, "->", output.round(3))

if __name__ == "__main__":
    main()
