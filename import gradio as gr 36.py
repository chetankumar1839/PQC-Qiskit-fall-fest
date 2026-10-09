import gradio as gr
import oqs

def sign_file(file):
    if file is None:
        return "❌ Please select a file."

    with open(file.name, "rb") as f:
        data = f.read()

    with oqs.Signature("ML-DSA-65") as signer:
        public_key = signer.generate_keypair()
        secret_key = signer.export_secret_key()
        signature = signer.sign(data)

    with open("interface_public.key", "wb") as f:
        f.write(public_key)

    with open("interface_secret.key", "wb") as f:
        f.write(secret_key)

    with open("interface_signature.sig", "wb") as f:
        f.write(signature)

    return (
        "✅ FILE SIGNED SUCCESSFULLY\n\n"
        "Algorithm: ML-DSA-65\n"
        f"Signature size: {len(signature)} bytes"
    )


def verify_file(file):
    if file is None:
        return "❌ Please select a file."

    try:
        with open(file.name, "rb") as f:
            data = f.read()

        with open("interface_public.key", "rb") as f:
            public_key = f.read()

        with open("interface_signature.sig", "rb") as f:
            signature = f.read()

        with oqs.Signature("ML-DSA-65") as verifier:
            valid = verifier.verify(data, signature, public_key)

        if valid:
            return "✅ VERIFIED\n\nThe file has a valid ML-DSA-65 signature."
        else:
            return "❌ VERIFICATION FAILED\n\nThe file does not match the signature."

    except FileNotFoundError:
        return "❌ No signature found. Sign a file first."


with gr.Blocks() as app:
    gr.Markdown("# 🔐 ML-DSA-65 Digital Signature")
    gr.Markdown("Post-quantum file signing and verification")

    file_input = gr.File(label="Choose a file")

    with gr.Row():
        sign_button = gr.Button("🔐 Sign File")
        verify_button = gr.Button("✅ Verify File")

    result = gr.Textbox(label="Result", lines=5)

    sign_button.click(
        sign_file,
        inputs=file_input,
        outputs=result
    )

    verify_button.click(
        verify_file,
        inputs=file_input,
        outputs=result
    )

app.launch()