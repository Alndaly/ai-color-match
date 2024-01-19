import cv2
import numpy as np
import gradio as gr

def getRgbChannels(image):
    b = image[:,:,0]
    g = image[:,:,1]
    r = image[:,:,2]
    return r, g, b

def main(image):
    r,g,b = getRgbChannels(image)
    return r

with gr.Blocks() as app:
    gr.Markdown(f"# AI一键调色\n\n> 活在自由而蔚蓝的天空之下！\n\n开发者：[Kinda](https://github.com/Alndaly)")
    with gr.Row():
        with gr.Column():
            inp = gr.Image(label="调色前")
            generateButton = gr.Button("一键调色")
        out = gr.Image(label="调色后")
    generateButton.click(main, inputs=inp, outputs=out)

if __name__ == "__main__":
    app.launch()