#here we can create models

from django.db import models

from django.contrib.auth.models import User

class Profile(models.Model):
    username=models.OneToOneField(User,on_delete=models.CASCADE)
    address=models.TextField()
    profile_pic=models.ImageField(upload_to='pp')

#upload_to='pp': This is a parameter of the ImageField that specifies the directory 
# where uploaded files will be stored. In this case, it's set to 'pp', 
# which means that uploaded images will be stored in a directory named 'pp' within your media directory.

#When you use this field in a Django model, Django will handle the file upload process,
#  storing the uploaded image in the specified directory and
#  maintaining a reference to it in the corresponding database record.

#in simple way we need to create a model,for 1 user(mailor ph no) 1 account so we r using 1to1 field
#in a folder named as pp all the images of users will be stored