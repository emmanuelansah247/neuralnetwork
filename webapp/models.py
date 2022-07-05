from django.db import models
import os

# Create your models here.

class TrainApp(models.Model):
    epochs = models.IntegerField(default=0)
    hiddennodes = models.IntegerField(default=0)
   
    def __str__(self) -> str:
        return str(self.epochs) + "\t \t" + str(self.hiddennodes)


class TrainImage(models.Model):
    image = models.ImageField(upload_to="media/train_images/")

    def filename(self):
        return os.path.basename(self.image.name)