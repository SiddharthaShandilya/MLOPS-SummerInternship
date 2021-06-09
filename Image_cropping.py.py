#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2


# In[ ]:


photo = cv2.imread('Pramod_Bus.JPG')


# In[ ]:


type(photo)


# In[ ]:


photo.shape


# In[ ]:


cv2.imshow('hi',photo)
cv2.waitKey()
cv2.destroyAllWindows()


# In[2]:


#this function will help us launch the photo 
def pic_show(photo):
    cv2.imshow('hi',photo)
    cv2.waitKey()
    cv2.destroyAllWindows()


# In[ ]:


photore = cv2.imread('Niraj_2-faces.JPG')


# In[4]:


import numpy


# In[ ]:


photore.shape


# In[ ]:


type(photo)


# In[ ]:


photo[5] = [0, 255,0]


# In[ ]:


len(photo)


# In[ ]:


photo = cv2.imread('Pramod_Bus.JPG')
for i in range(len(photo)//5):
    a = i*3
    #photo[a] = [0, 255,0]
    photo[i] = [0, 255,0]
    
pic_show(photo)


# In[ ]:


photo = cv2.imread('Pramod_Bus.JPG')

crop1 = cv2.rectangle(photo,(50,50),(700,800), [0,20,155], 5)


# In[ ]:


photo = cv2.imread('Pramod_Bus.JPG')
crop2 = photo[50:700,50:800]

photore = cv2.imread('Niraj_2-faces.JPG')
crop3 = photore[50:700,50:800]


# In[ ]:





# In[ ]:


photo = cv2.imread('Pramod_Bus.JPG')
crop2 = photo[50:700,50:800]

photore = cv2.imread('Niraj_2-faces.JPG')
crop3 = photore[50:700,50:800]
#_--------------------------------------
add_photo = crop2 + crop3 
pic_show(add_photo)


# In[ ]:


photo = cv2.imread('Pramod_Bus.JPG')
crop2 = photo[50:700,50:800]

photore = cv2.imread('Niraj_2-faces.JPG')
crop3 = photore[50:700,50:800]

#-----------------------------------------
crop2 = (crop2*6)%255
crop3 = (crop3*3)%255
add_photo = crop2 + crop3 
pic_show(add_photo)


# In[5]:


photo = cv2.imread('Pramod_Bus.JPG')
crop2 = photo[50:500,50:500]

photore = cv2.imread('Niraj_2-faces.JPG')
crop3 = photore[50:500,50:500]
#-_______________________________________________________
crop4 = numpy.vstack((crop2,crop3))
pic_show(crop4)


# In[ ]:


crop4 = numpy.vstack((crop2,crop3))


# In[6]:


photo = cv2.imread('Pramod_Bus.JPG')
crop2 = photo[50:500,50:500]

photore = cv2.imread('Niraj_2-faces.JPG')
crop3 = photore[50:500,50:500]
#-_______________________________________________________
crop4 = numpy.hstack((crop2,crop3))
pic_show(crop4)


# In[ ]:




