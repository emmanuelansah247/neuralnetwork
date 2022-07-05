from django.shortcuts import render,redirect
from webapp.forms import TrainAppForm,TrainImageForm
from .models import TrainImage
from .neuralclass import neuralNetwork
import numpy
import imageio

# Create your views here.

def home(request):
    return render(request,'home.html', {
        "train_app_form": TrainAppForm()
    })

def trainappvalue(request):
    results = 0
    if request.method ==  "POST":
        train_app_form = TrainAppForm(data=request.POST, files=request.FILES)
        if train_app_form.is_valid():
            epochs = train_app_form.cleaned_data['epochs']
            hiddennodes = train_app_form.cleaned_data['hiddennodes']
            global network_accuracy
            network_accuracy = train_network(epochs,hiddennodes)
            train_app_form.save()
    else:
        train_app_form = TrainAppForm()
    
    return render (
        request, 'home.html', {
            "train_app_form": train_app_form,
            "network_accuracy": network_accuracy
        }
    )


def testnetwork(request):
    if request.method == "POST":
        form = TrainImageForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            saved_image_id = form.customSave()
            filename = TrainImage.objects.get(pk=saved_image_id).filename()
            
            # filename = str(form.files['image'])
            img_array = imageio.imread("media/train_images/" + filename,as_gray=True)
            img_data = 255.0 - img_array.reshape(784)
            img_data = (img_data/255.0 * 0.99) + 0.01
            global n
            output = n.query(img_data)
            label = numpy.argmax(output)

    
    train_app_form = TrainImageForm()

    global network_accuracy
    return render(request, 'home.html', {
            "train_app_form": train_app_form,
            "network_accuracy": network_accuracy,
            "predicted_output": label
    })

def train_network(_epochs, _nodes):
            
    no_input_nodes = 784
    no_hidden_nodes = _nodes
    no_output_nodes = 10

    learning_rate_value = 0.2

    global n
    n = neuralNetwork(no_input_nodes, no_hidden_nodes,no_output_nodes,learning_rate_value)

    training_file = open("mnist_dataset/mnist_train.csv",'r')
    training_list = training_file.readlines()
    training_file.close()

    
    epochs = _epochs

    for e in range(epochs):

        for record in training_list:
            all_values = record.split(',')
            inputs = (numpy.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01
            targets = numpy.zeros(no_output_nodes) + 0.01
            targets[int(all_values[0])] = 0.99
            n.train(inputs,targets)
            pass
        pass

    test_file = open("mnist_dataset/mnist_test.csv",'r')
    test_dataset = test_file.readlines()
    test_file.close()

    scorecard = []

    #Testing our network
    for record in test_dataset:
        all_values = record.split(',')
        label_we_want_to_predict = int(all_values[0])
        inputs = (numpy.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01
        outputs = n.query(inputs)
        our_network_predicted_label = numpy.argmax(outputs)
        if(our_network_predicted_label== label_we_want_to_predict):
            scorecard.append(1)
        else:
            scorecard.append(0)
            pass
        pass

    scorecard_array = numpy.asarray(scorecard)
    return (scorecard_array.sum()/scorecard_array.size)



        