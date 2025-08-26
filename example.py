import asyncio

import streamlit as st
from celeste_core import Provider, list_models
from celeste_core.enums.capability import Capability

from celeste_domain_template import create_domain_template_client

st.set_page_config(page_title="Celeste Domain Template", page_icon="🚀", layout="wide")
st.title("🚀 Celeste Domain Template Example")

# TODO: Replace Capability.TEXT_GENERATION with your domain's capability
all_models = list_models(capability=Capability.TEXT_GENERATION)
providers = sorted({m.provider for m in all_models}, key=lambda p: p.value)

with st.sidebar:
    st.header("⚙️ Configuration")

    if providers:
        provider = st.selectbox(
            "Provider:", [p.value for p in providers], format_func=str.title
        )

        # Filter models by selected provider
        models = [m for m in all_models if m.provider == Provider(provider)]
        model_names = [m.display_name or m.id for m in models]
        selected_idx = st.selectbox(
            "Model:", range(len(models)), format_func=lambda i: model_names[i]
        )
        model = models[selected_idx].id

        # TODO: Add domain-specific configuration options
        st.subheader("🎛️ Parameters")
        # Example for TTS: voice selection, sample rate
        # Example for image: size, style, quality
        # Example for video: duration, resolution
        # voice = st.selectbox("Voice:", voice_options)
        # quality = st.slider("Quality:", 1, 10, 5)

    else:
        st.error(
            "No models found for this capability. Make sure providers are configured."
        )
        st.stop()

st.markdown(f"*Powered by {provider.title()}*")

# TODO: Replace with your domain-specific input
input_text = st.text_area(
    "Enter your input:",
    "Hello! This is a template example.",
    height=100,
    placeholder="Enter the input for your domain...",
)

# Create client when provider/model selection changes
client = create_domain_template_client(Provider(provider), model=model)

if st.button("🚀 Generate", type="primary", use_container_width=True):
    if not input_text.strip():
        st.error("Please enter some input.")
    else:
        with st.spinner("Generating..."):
            try:
                # TODO: Replace with your domain-specific generation call
                # Example for TTS: result = asyncio.run(
                #     client.generate_speech(text=input_text, voice=voice)
                # )
                # Example for images: result = asyncio.run(
                #     client.generate_image(prompt=input_text, size="1024x1024")
                # )
                result = asyncio.run(client.generate_content(input_text))

                # TODO: Replace with your domain-specific result display
                st.success("✅ Generated successfully!")
                st.write(f"**Result:** {result}")

                # TODO: Add domain-specific result display
                # Example for audio: st.audio(audio_data)
                # Example for images: st.image(image_data)
                # Example for video: st.video(video_data)

                # Show metadata
                with st.expander("📊 Details"):
                    st.write(f"**Provider:** {provider}")
                    st.write(f"**Model:** {model}")
                    # TODO: Add domain-specific metadata

            except Exception as e:
                st.error(f"Error generating: {str(e)}")

st.markdown("---")
st.caption("Built with Streamlit • Powered by Celeste Domain Template")

# TODO: When using this template:
# 1. Replace Capability.TEXT_GENERATION with your domain's capability enum
# 2. Replace "domain_template" references with your actual domain name
# 3. Update the UI elements to match your domain (voice selection, image
#    parameters, etc.)
# 4. Replace the generation call with your domain-specific method
# 5. Update result display to show your domain's artifacts (audio player,
#    image display, etc.)
# 6. Update the title, icon, and descriptions
# 7. Remove this TODO section when complete
