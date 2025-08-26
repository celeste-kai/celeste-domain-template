"""Celeste Domain Template: Template for creating new Celeste domains"""

from importlib import import_module
from typing import Any, Union

from celeste_core import Provider
from celeste_core.base.client import BaseClient
from celeste_core.config.settings import settings

from .mapping import PROVIDER_MAPPING

__version__ = "0.1.0"


def create_domain_template_client(
    provider: Union[Provider, str], **kwargs: Any
) -> BaseClient:
    """
    Factory function to create a domain template client instance based on the provider.

    Args:
        provider: The domain template provider to use (string or Provider enum).
        **kwargs: Additional arguments to pass to the domain template constructor.

    Returns:
        An instance of a domain template client
    """
    provider_enum = Provider(provider) if isinstance(provider, str) else provider

    if provider_enum not in PROVIDER_MAPPING:
        raise ValueError(
            f"Provider '{provider_enum.value}' is not supported for domain template."
        )

    settings.validate_for_provider(provider_enum.value)
    module_path, class_name = PROVIDER_MAPPING[provider_enum]
    module = import_module(f"celeste_domain_template{module_path}")
    return getattr(module, class_name)(**kwargs)


__all__ = ["create_domain_template_client", "BaseClient"]

# TODO: When using this template:
# 1. Replace all references to "domain_template" with your actual domain name
# 2. Replace BaseClient with your domain-specific base class
# 3. Update the factory function name to match your domain
# 4. Update imports and class references
# 5. Remove this TODO section when complete
