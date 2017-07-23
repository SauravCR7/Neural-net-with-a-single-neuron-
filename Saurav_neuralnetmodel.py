from numpy import exp, array, random, dot, tanh

train_inputs = array([[0, 0, 1], [1, 1, 1], [1, 0, 1], [0, 1, 1]])

train_outputs = array([[0, 1, 0, 1]]).T


random.seed(1)

synaptic_weights = 2 * random.random((3, 1)) - 1


def train(train_inputs, train_outputs, iterations):

    for iteration in range(iterations):

 

    #getting output

        output = getoutput(train_inputs)



         	#calculating error

        error = train_outputs - output



            #calculating the adjustment

        adjustment = dot(train_inputs.T, error * sig_grad(output))

        global synaptic_weights

        synaptic_weights += adjustment



def getoutput(inputs):

    return sigmoid(dot(inputs, synaptic_weights))


def sigmoid(x):

    return tanh(x)


    adjustment = dot(train_inputs.T, error * sig_grad(output))

    global synaptic_weights

    synaptic_weights += adjustment


def sig_grad(x):

    return 1 - (tanh(x) ** 2)

print ("Random starting synaptic weights - ")

print (synaptic_weights)





train(train_inputs, train_outputs, 10000)





print ("synaptic weights after training: ")

print (synaptic_weights)



# Testing neural network 

print ("For testing output [1, 0, 0]:  ")

x= getoutput(array([1,1,0]))

print (x)    
