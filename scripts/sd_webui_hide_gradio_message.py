try:
    from modules import patches, script_callbacks
    import gradio.helpers
    import warnings


    def log_message(message: str, level="info", *args, **kwargs):
        if level == "info":
            print(message)
        elif level == "warning":
            warnings.warn(message)


    original_log_message = patches.patch(__name__, gradio.helpers, 'log_message', log_message)


    def undo():
        patches.undo(__name__, gradio.helpers, 'log_message')


    script_callbacks.on_script_unloaded(undo)

except Exception as e:
    print(f'sd-webui-hide-gradio-message failed to patch gradio.helpers.log_message: {e}')
