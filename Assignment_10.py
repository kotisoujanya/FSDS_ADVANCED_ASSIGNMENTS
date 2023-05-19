#!/usr/bin/env python
# coding: utf-8

# # Q1. What is the difference between __getattr__ and __getattribute__?
In Python, __getattr__ and __getattribute__ are two special methods that are called when an attribute is accessed on an object. However, there is a key difference between these two methods:

==>>>  __getattr__(self, name) is called when an attribute is not found in the usual places (i.e., in the object's dictionary, in the class hierarchy, or in the instance's __dict__). It takes a single argument, name, which is the name of the attribute being accessed. If __getattr__ is defined for a class, it is called whenever an attribute is not found by the usual means.

===>>>  __getattribute__(self, name) is called every time an attribute is accessed on an object, regardless of whether the attribute exists or not. It takes a single argument, name, which is the name of the attribute being accessed. If __getattribute__ is defined for a class, it is always called when an attribute is accessed.

 *  The key difference between __getattr__ and __getattribute__ is that __getattr__ is only called when an attribute is not found by the usual means, whereas __getattribute__ is always called when an attribute is accessed. This means that __getattr__ can be used to define default behavior for attributes that do not exist, while __getattribute__ can be used to override the default behavior for all attributes.

*  It's worth noting that __getattribute__ is more powerful than __getattr__, but also more dangerous, because it can cause an infinite recursion if not used carefully. Therefore, it's usually recommended to use __getattr__ instead of __getattribute__ unless you have a specific need for the latter.
# # Q2. What is the difference between properties and descriptors?
In Python, properties and descriptors are two mechanisms for controlling access to object attributes. Here are the key differences between the two:

===>> A property is a special kind of attribute that is accessed like a regular attribute but is actually the result of a method call. It allows you to define custom behavior when getting or setting an attribute. Properties are defined using the @property decorator in Python.

===>> A descriptor is a more general mechanism for controlling attribute access. It allows you to define custom behavior for getting, setting, and deleting attributes, and can be used for more complex attribute access patterns. Descriptors are defined by implementing the __get__, __set__, and/or __delete__ methods.

The main difference between properties and descriptors is that properties are a simpler mechanism for defining custom behavior for getting and setting an attribute, while descriptors are a more powerful and flexible mechanism that can be used for more complex attribute access patterns. In general, properties are appropriate for simple cases where you just need to define custom behavior for getting or setting an attribute, while descriptors are more appropriate for more complex cases where you need more control over attribute access.
# # Q3. What are the key differences in functionality between __getattr__ and __getattribute__, as well as properties and descriptors?
The key differences between __getattr__ and __getattribute__, as well as properties and descriptors, can be summarized as follows:

   ==> __getattr__ and __getattribute__: Both of these methods are used to customize attribute access on an object. However, __getattr__ is only called when an attribute is not found in the usual places, while __getattribute__ is called every time an attribute is accessed. This means that __getattr__ can be used to define default behavior for attributes that don't exist, while __getattribute__ can be used to override the default behavior for all attributes. However, because __getattribute__ is more powerful and can lead to infinite recursion if not used carefully, it is generally recommended to use __getattr__ instead of __getattribute__ whenever possible.

  ===>  Properties and descriptors: Both properties and descriptors are used to customize attribute access on an object, but they work in slightly different ways. Properties are a simpler mechanism for defining custom behavior for getting and setting an attribute, while descriptors are a more powerful and flexible mechanism that can be used for more complex attribute access patterns. Properties are defined using the @property decorator and are accessed like regular attributes, but are actually the result of a method call. Descriptors, on the other hand, are defined by implementing the __get__, __set__, and/or __delete__ methods and are typically used to define custom behavior for accessing attributes on a class, rather than an instance.

In summary, __getattr__ and properties are simpler mechanisms for customizing attribute access on an object, while __getattribute__ and descriptors are more powerful and flexible mechanisms that can be used for more complex cases.
# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




