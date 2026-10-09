import gradio as gr
import oqs
import os

PUBLIC_KEY = "interface_public.key"
SIGNATURE = "interface_signature.sig"


def sign_file(file):
    if file is None:
        return "❌ Please select a file."

    with open(file.name, "rb") as f:
        data = f.read()

    with oqs.Signature("ML-DSA-65") as signer:
        public_key = signer.generate_keypair()
        signature = signer.sign(data)

    with open(PUBLIC_KEY, "wb") as f:
        f.write(public_key)

    with open(SIGNATURE, "wb") as f:
        f.write(signature)

    return (
        "✅ SIGNED SUCCESSFULLY\n\n"
        "Algorithm: ML-DSA-65\n"
        f"Signature size: {len(signature)} bytes"
    )


def verify_file(file):
    if file is None:
        return "❌ Please select a file."

    if not os.path.exists(PUBLIC_KEY) or not os.path.exists(SIGNATURE):
        return "❌ No signature found. Sign the file first."

    with open(file.name, "rb") as f:
        data = f.read()

    with open(PUBLIC_KEY, "rb") as f:
        public_key = f.read()

    with open(SIGNATURE, "rb") as f:
        signature = f.read()

    with oqs.Signature("ML-DSA-65") as verifier:
        valid = verifier.verify(data, signature, public_key)

    if valid:
        return "✅ VERIFIED\n\nML-DSA-65 signature is valid."
    else:
        return "❌ VERIFICATION FAILED\n\nTAMPERING DETECTED."


with gr.Blocks() as app:
    gr.Markdown("# 🔐 ML-DSA-65 Quantum-Safe File Protection")
    gr.Markdown(
        "Post-quantum digital signatures using Open Quantum Safe."
    )

    file_input = gr.File(label="📁 Select a file")

    with gr.Row():
        sign_btn = gr.Button("🔐 Sign File")
        verify_btn = gr.Button("✅ Verify File")

    result = gr.Textbox(label="Result", lines=5)

    sign_btn.click(sign_file, file_input, result)
    verify_btn.click(verify_file, file_input, result)

app.launch()