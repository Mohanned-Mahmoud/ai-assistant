import gradio as gr
import ollama


def chat_with_ai(user_prompt):
    """Send a prompt to the local Ollama instance and get a response."""
    try:
        response = ollama.chat(model="gemma3", messages=[
            {"role": "user", "content": user_prompt}
        ])
        return response["message"]["content"]
    except Exception as e:
        return f"Error: {str(e)}"


def main():
    """Create and launch the Gradio interface."""
    interface = gr.Interface(
        fn=chat_with_ai,
        inputs=gr.Textbox(label="Your Prompt", lines=3),
        outputs=gr.Textbox(label="Response", lines=10),
        title="Local AI Assistant - Gemma"
    )
    interface.launch()


if __name__ == "__main__":
    main()
