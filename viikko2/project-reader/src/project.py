class Project:
    def __init__(self, name, description, dependencies, dev_dependencies, authors, license):
        self.name = name
        self.description = description
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies
        self.authors = authors
        self.license = license

    def _stringify_dependencies(self, dependencies):
        return "\n".join([f"- {dependency}" for dependency in dependencies])

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}\n"
            f"\nLicense: {self.license}\n"
            f"\nAuthors:\n{self._stringify_dependencies(self.authors)}\n"
            f"\nDependencies:\n{self._stringify_dependencies(self.dependencies)}\n"
            f"\nDevelopment dependencies:\n{self._stringify_dependencies(self.dev_dependencies)}\n"
        )
