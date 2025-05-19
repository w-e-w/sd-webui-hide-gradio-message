try:
    from modules import patches, script_callbacks
    from datetime import datetime
    from tqdm import tqdm
    import gradio.helpers
    import warnings


    def log_message(message: str, level="info", *args, **kwargs):
        try:
            tqdm.write(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S,%f")} - Gradio - {str(level).upper()} - {message}')
        except Exception:
            pass


    original_log_message = patches.patch(__name__, gradio.helpers, 'log_message', log_message)


    def undo():
        try:
            patches.undo(__name__, gradio.helpers, 'log_message')
        except RuntimeError:
            pass


    script_callbacks.on_script_unloaded(undo)

except Exception as e:
    print(f'sd-webui-hide-gradio-message failed to patch gradio.helpers.log_message: {e}')
