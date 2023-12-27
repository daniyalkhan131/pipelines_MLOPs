import random
import sys
import yaml
from dvclive import Live

with Live(save_dvc_exp=True) as live:
    #epochs = 10 #we are tracking for 10 epochs and saving records  for each epoch

    #we can change params.yaml file in dvclive to control things, anf for manipulating .yaml use uaml lib

    train_params=yaml.safe_load(open('params.yaml'))['train']
    epochs=train_params['epochs ']
    live.log_param ("epochs", epochs)
    for epoch in range(epochs):
        live.log_metric("train/accuracy", epoch + random.random()) 
        live.log_metric("train/loss", epochs - epoch - random.random())
        live.log_metric("val/accuracy", epoch + random.random())
        live.log_metric("val/loss", epochs - epoch - random.random()) 
        live.next_step()

#some files are created using this like dvclive and in that we plot things and do
#pass things and in return got these, we are not having any model tight now
