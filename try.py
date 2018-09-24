
# coding: utf-8

# In[3]:


from flask import Flask


# In[7]:



app = Flask(__name__)

@app.route('/')

def hello():
    return "Hello World"

app.run(debug = True)

