import gradio as gr
from tensorflow import keras

model = keras.models.load_model('handwritten.model')
print('HERE', model)

def predict(image):
    prediction = model.predict(image.reshape(1,28, 28)).tolist()[0]
    return str(prediction.index(1))

demo = gr.Interface(fn=predict,
             inputs="sketchpad",
             streaming = True,
             outputs="label",
             live=True).launch()













