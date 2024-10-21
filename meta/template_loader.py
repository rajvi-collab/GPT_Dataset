import os
import logging
from jinja2 import Environment, FileSystemLoader


class TemplateLoader:
    def __init__(self, template_dir: str):
        """
        Initialize the template loader.

        :param template_dir: Directory path containing templates
        """
        self.template_dir = template_dir
        self.env = Environment(loader=FileSystemLoader(self.template_dir))

    def load_template(self, template_name: str) -> object:
        """
        Load a template from the directory.

        :param template_name: Name of the template file (without extension)
        :return: Loaded template object
        """
        try:
            logging.debug(f"Loading template: {template_name}.html")
            return self.env.get_template(f"{template_name}.html")
        except Exception as e:
            logging.error(f"Failed to load template '{template_name}': {e}")
            return None

    def render_template(self, template_name: str, **kwargs) -> str:
        """
        Render a template with variables.

        :param template_name: Name of the template file (without extension)
        :param kwargs: Variables to pass to the template
        :return: Rendered template string
        """
        template = self.load_template(template_name)
        if template:
            logging.debug(f"Rendering template: {template_name}")
            return template.render(**kwargs)
        return None


# Create a template loader instance
if __name__ == "__main__":
    template_dir = "templates"  # Update the directory path
    logging.info(f"Template Directory: {os.path.abspath(template_dir)}")

    # Check if template directory is accessible
    if not os.access(template_dir, os.R_OK):
        logging.error(f"Template directory '{template_dir}' is not readable.")
        exit(1)

    template_loader = TemplateLoader(template_dir)

    # List files in template directory
    logging.debug(f"Files in template directory: {os.listdir(template_dir)}")

    # Load a template
    template = template_loader.load_template("example_template")

    # Render a template with variables
    rendered_template = template_loader.render_template("example_template", name="John Doe", age=30)

    print(rendered_template)
    