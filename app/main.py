import gradio as gr
import ollama
import os


MODEL_NAME = os.getenv("OLLAMA_MODEL", "llama3.2:1b")


def chat_with_ai(user_prompt):
    """Send a prompt to the local Ollama instance and get a response."""
    try:
        response = ollama.chat(model=MODEL_NAME, messages=[
            {"role": "user", "content": user_prompt}
        ])
        return response["message"]["content"]
    except Exception as e:
        error_text = str(e)
        if "not found" in error_text and "model" in error_text:
            return (
                f"Error: Model '{MODEL_NAME}' not found locally. "
                f"Run: ollama pull {MODEL_NAME}"
            )
        return f"Error: {error_text}"


def main():
    """Create and launch the Gradio interface."""
    interface = gr.Interface(
        fn=chat_with_ai,
        inputs=gr.Textbox(label="Your Prompt", lines=3),
        outputs=gr.Textbox(label="Response", lines=10),
        title=f"Local AI Assistant - {MODEL_NAME}"
    )
    interface.launch()


if __name__ == "__main__":
    main()
