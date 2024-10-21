from pathlib import Path
from jinja2 import Environment, FileSystemLoader, select_autoescape, TemplateNotFound
import os

class TemplateLoader:
    def __init__(self, template_dir: str):
        # Resolve the directory safely using Path
        self.template_dir = Path(template_dir).resolve()
        
        # Ensure the directory exists
        if not self.template_dir.is_dir():
            raise FileNotFoundError(f"Template directory '{self.template_dir}' does not exist.")
        
        # Set up Jinja2 environment with safe configuration
        self.env = Environment(
            loader=FileSystemLoader(self.template_dir),
            autoescape=select_autoescape(['html', 'xml'])
        )
    
    def load_template(self, template_name: str):
        """
        Safely loads a template from the specified directory.
        Raises a TemplateNotFound exception if the template is missing.
        """
        try:
            # Ensure we don't access outside of the template directory
            template_path = self.template_dir / template_name
            if not template_path.is_file():
                raise TemplateNotFound(template_name)
            
            # Load and return the template
            template = self.env.get_template(template_name)
            return template
        
        except TemplateNotFound:
            raise TemplateNotFound(f"Template '{template_name}' not found in directory '{self.template_dir}'")
    
    def render_template(self, template_name: str, context: dict):
        """
        Renders a template with the given context safely.
        """
        template = self.load_template(template_name)
        return template.render(context)


# Example usage
if __name__ == "__main__":
    template_loader = TemplateLoader("templates")  # Ensure this is a valid directory path
    
    try:
        # Load and render a template named 'example.html'
        rendered_content = template_loader.render_template('example.html', {"name": "John Doe"})
        print(rendered_content)
    except TemplateNotFound as e:
        print(e)
    except Exception as e:
        print(f"An error occurred: {e}")
