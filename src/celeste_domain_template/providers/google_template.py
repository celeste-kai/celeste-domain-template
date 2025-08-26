from typing import Any, Never

from celeste_core import Provider
from celeste_core.base.client import (
    BaseClient,  # TODO: Replace with domain-specific base class
)

# TODO: Add imports for your domain
# from celeste_core import ImageArtifact  # Your artifact type
# from google import genai  # Your provider SDK


class GoogleDomainTemplateClient(BaseClient):
    def __init__(self, model: str = "your-default-model", **kwargs: Any) -> None:
        super().__init__(
            model=model,
            provider=Provider.GOOGLE,
            **kwargs,
        )
        # TODO: Initialize your provider's client using celeste-core settings
        # Example: self.client = genai.Client(api_key=settings.google.api_key)
        # Note: Always use settings from celeste-core, not custom dotenv/auth logic

    async def generate_content(
        self, prompt: str, **kwargs: Any
    ) -> Never:  # TODO: Replace with domain method
        """TODO: Replace with your domain's method.

        Examples:
        - generate_image(prompt) -> List[ImageArtifact]
        - generate_speech(text, voice_name) -> AudioArtifact
        - generate_embeddings(texts) -> AIResponse
        """
        # TODO: Implement provider API call and return domain artifact
        # response = await self.client.api_call(model=self.model, ...)
        # return YourArtifact(data=response.data)
        raise NotImplementedError

    async def stream_generate_content(self, prompt: str, **kwargs: Any) -> Never:
        """TODO: Implement streaming or remove if not needed."""
        raise NotImplementedError


# TODO: Customize this template:
# 1. Replace BaseClient with domain base class (BaseImageGenerator, BaseTTSClient, etc.)
# 2. Add your artifact and SDK imports
# 3. Rename file/class to match your provider
# 4. Replace generate_content with domain method
# 5. Implement provider API call
