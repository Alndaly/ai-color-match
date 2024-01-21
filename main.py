import cv2
import numpy as np
import gradio as gr
from lib.color import getRgbChannels


def main(image):
    r,g,b = getRgbChannels(image)
    return r

with gr.Blocks() as app:
    gr.Markdown(f"# AI一键调色\n\n> 活在自由而蔚蓝的天空之下！\n\n开发者：[Kinda](https://github.com/Alndaly)")
    with gr.Row():
        with gr.Column():
            inp = gr.Image(label="调色前")
            gr.Dropdown(choices=["古风", "扫街", "小清新"], label="风格", info="选择调色风格")
            gr.Slider(0, 100, value=0, label="风格化程度", info="从0到100表示风格话从低到高")
            generateButton = gr.Button("一键调色")
        out = gr.Image(label="调色后")
    generateButton.click(main, inputs=inp, outputs=out)

if __name__ == "__main__":
    app.launch()