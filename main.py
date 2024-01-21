import gradio as gr
from lib.image_analysis import analysisImage
# from lib.image_color_match import generateStyledImage

with gr.Blocks() as app:
    
    gr.Markdown(f"# AI图片分析及部分操作\n\n> 活在自由而蔚蓝的天空之下！\n\n开发者：[Kinda](https://github.com/Alndaly)")
    with gr.Tab("图片分析"):
        with gr.Row():
            with gr.Column():
                image = gr.Image(label="待分析图片")
                analysisButton = gr.Button("一键分析")
        gr.Markdown(f"# 分析结果")
        with gr.Tab("主要颜色"):
            with gr.Row():
                colors = gr.Gallery(label="主要颜色成分", elem_id="gallery", columns=[1], rows=[5], object_fit="contain", height="auto")
                with gr.Column():
                    centroids1 = gr.Text(label='颜色一')
                    centroids2 = gr.Text(label='颜色二')
                    centroids3 = gr.Text(label='颜色三')
                    centroids4 = gr.Text(label='颜色四')
                    centroids5 = gr.Text(label='颜色五')
    analysisButton.click(analysisImage, inputs=[image], outputs=[centroids1, centroids2, centroids3, centroids4, centroids5, colors])
    
    # with gr.Tab("调色"):
    #     with gr.Row():
    #         with gr.Column():
    #             image = gr.Image(label="调色前")
    #             style = gr.Dropdown(choices=["古风", "扫街", "小清新", "电影感"], label="风格", info="选择调色风格", value="古风")
    #             style_degree = gr.Slider(0, 100, value=0, label="风格化程度", info="从0到100表示风格化从低到高")
    #             generateButton = gr.Button("一键调色")
    #         with gr.Column():
    #             out = gr.Image(label="主要颜色")
    # generateButton.click(generateStyledImage, inputs=[image, style, style_degree], outputs=[out])

if __name__ == "__main__":
    app.launch()