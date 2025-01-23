import toml
import os

def load_config():
    config_path = os.path.join(os.path.dirname(__file__), '..', 'env.toml')
    config = toml.load(config_path)
    return config

def get_subscription_tokens():
    config = load_config()
    # Return tokens from the subscription_tokens section
    return config.get('subscription_tokens', {}).get('tokens', [])
