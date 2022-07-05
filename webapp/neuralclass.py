import numpy 
import scipy.special
#our neural network class

class neuralNetwork():
    
    def __init__(self,no_of_Inodes,no_of_Hnodes,no_of_Onodes,learning_rate):
        self.inputnodes = no_of_Inodes
        self.hiddennodes = no_of_Hnodes
        self.outputnodes = no_of_Onodes
        self.lr = learning_rate
        
        self.w_input_hidden = numpy.random.normal(0.0,pow(self.inputnodes,-0.5),(self.hiddennodes,self.inputnodes))
        self.w_hidden_output = numpy.random.normal(0.0,pow(self.hiddennodes,-0.5),(self.outputnodes,self.hiddennodes))
        
        self.activation_function = lambda x: scipy.special.expit(x)
        pass
    
    # this function train our neural network
    def train(self, input_values,target_values):
        inputs = numpy.array(input_values,ndmin=2).T
        targets = numpy.array(target_values,ndmin=2).T
        
        hidden_inputs = numpy.dot(self.w_input_hidden,inputs)
        hidden_outputs = self.activation_function(hidden_inputs)
        
        final_inputs = numpy.dot(self.w_hidden_output, hidden_outputs)
        final_outputs = self.activation_function(final_inputs)
        
        output_errors = targets - final_outputs
        hidden_errors = numpy.dot(self.w_hidden_output.T,output_errors)
        
        self.w_hidden_output += self.lr * numpy.dot((output_errors * final_outputs * (1.0 - final_outputs)), 
                                                    numpy.transpose(hidden_outputs))
        
        self.w_input_hidden += self.lr * numpy.dot((hidden_errors * hidden_outputs * (1.0 - hidden_outputs)), 
                                                    numpy.transpose(inputs))
        pass
    
    #function to help us query from our neural network

    def query(self,inputs_list):

            inputs = numpy.array(inputs_list,ndmin=2).T

            signal_into_hidden_layer = numpy.dot(self.w_input_hidden,inputs)
            signal_from_hidden_layer = self.activation_function(signal_into_hidden_layer)

            signal_into_output_layer = numpy.dot(self.w_hidden_output,signal_from_hidden_layer)
            network_final_output = self.activation_function(signal_into_output_layer)

            return network_final_output