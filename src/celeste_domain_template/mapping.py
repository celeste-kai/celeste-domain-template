from celeste_core.enums.capability import Capability
from celeste_core.enums.providers import Provider

# Capability for this domain package
CAPABILITY: Capability = (
    Capability.TEXT_GENERATION
)  # TODO: Replace with your capability

# Provider wiring for domain template clients
PROVIDER_MAPPING: dict[Provider, tuple[str, str]] = {
    # Add your provider mappings here. Examples:
    # Provider.GOOGLE: (".providers.google", "GoogleDomainTemplateClient"),
    # Provider.OPENAI: (".providers.openai", "OpenAIDomainTemplateClient"),
    # Provider.ANTHROPIC: (".providers.anthropic", "AnthropicDomainTemplateClient"),
}

__all__ = ["CAPABILITY", "PROVIDER_MAPPING"]

# TODO: BEFORE using this template:
# 1. Add your capability to celeste-core/src/celeste_core/enums/capability.py
#    if it doesn't exist
#    Example: YOUR_CAPABILITY = 1 << 14  (use next available bit)
# 2. Replace CAPABILITY with your actual capability enum
# 3. Add actual provider mappings in PROVIDER_MAPPING dict
# 4. Add models to celeste-core/src/celeste_core/models/catalog.py with your capability
# 5. Remove this TODO section when complete
