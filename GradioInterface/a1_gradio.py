# pip install gradio
# After start check at:  http://localhost:7860 or http://127.0.0.1:7860

'''
fn: The function to wrap a user interface (UI) around
inputs: The Gradio component(s) to use for the input. The number of components should match the number of arguments in your function.
outputs: The Gradio component(s) to use for the output. The number of components should match the number of return values from your function.
Gradio includes more than 30 built-in components (such as the gr.Textbox(), gr.Image(), and gr.HTML()
'''

import gradio as gr

def greet(name, intensity):
  return "Hello, " + name + "!" * int(intensity)

demo = gr.Interface(
  fn=greet,
  inputs=["text", "slider"],
  outputs=["text"],
)
demo.launch()