import gradio as gr
import oqs

def sign_file(file):
    if file is None:
        return "❌ Please select a file."

    filename = file.name

    with open(filename, "rb") as f:
        data = f.read()

    with oqs.Signature("ML-DSA-65") as signer:
        public_key = signer.generate_keypair()
        secret_key = signer.export_secret_key()
        signature = signer.sign(data)

    # Save keys and signature
    with open("interface_public.key", "wb") as f:
        f.write(public_key)

    with open("interface_secret.key", "wb") as f:
        f.write(secret_key)

    with open("interface_signature.sig", "wb") as f:
        f.write(signature)

    return (
        "✅ FILE SIGNED SUCCESSFULLY\n\n"
        f"Algorithm: ML-DSA-65\n"
        f"File: {filename}\n"
        f"Signature size: {len(signature)} bytes"
    )


app = gr.Interface(
    fn=sign_file,
    inputs=gr.File(label="Choose a file"),
    outputs=gr.Textbox(label="Result"),
    title="ML-DSA-65 Digital Signature",
    description="Sign a file using post-quantum ML-DSA-65."
)

app.launch()