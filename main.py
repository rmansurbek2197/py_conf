class ConfigSystem:
    def __init__(self, **defaults):
        self.settings = defaults

    def update(self, **new_settings):
        self.settings.update(new_settings)

    def get(self, key, default=None):
        return self.settings.get(key, default)

    def load_profile(self, *profiles):
        for profile in profiles:
            self.settings.update(profile)


config = ConfigSystem(debug=True, db="sqlite")

dev_profile = {"debug": False, "cache": True}
prod_profile = {"debug": False, "db": "postgres"}

config.load_profile(dev_profile, prod_profile)

print(config.settings)
