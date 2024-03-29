import gradio as gr
from fastai.vision.all import *
import skimage

learn = load_learner('model.pkl')

labels = learn.dls.vocab
def predict(img):
    img = PILImage.create(img)
    pred,pred_idx,probs = learn.predict(img)
    return {labels[i]: float(probs[i]) for i in range(len(labels))}
 
title = "Rhino or Elephant?"
description = "A classifier for Rhino vs Elephant built with fastai and trained with images from duckduckgo."
examples = ['elephant.jpg']
interpretation='default'
enable_queue=True

gr.Interface(fn=predict,inputs=gr.inputs.Image(shape=(512, 512)),outputs=gr.outputs.Label(num_top_classes=2),title=title,description=description,examples=examples,interpretation=interpretation,enable_queue=enable_queue).launch()
