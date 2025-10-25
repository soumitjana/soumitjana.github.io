#!/usr/bin/env python
"""
Build static files for GitHub Pages deployment.
"""
import os
import sys
import shutil
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'personal_website.settings')
import django
django.setup()

from django.template.loader import render_to_string
from apps.roadmap.models import Category

def build_static_site():
    """Build static files for GitHub Pages."""
    # Get all categories with related data
    categories = Category.objects.prefetch_related(
        'phases__topics', 
        'phases__projects'
    ).all()
    
    context = {
        'categories': categories,
    }
    
    # Render roadmap page
    roadmap_html = render_to_string('roadmap/roadmap.html', context)
    roadmap_path = project_root / 'roadmap'
    roadmap_path.mkdir(exist_ok=True)
    
    # Write static roadmap file
    with open(roadmap_path / 'index.html', 'w', encoding='utf-8') as f:
        f.write(roadmap_html)

    # Create an empty .nojekyll so GitHub Pages won't run Jekyll (prevents ignoring files)
    nojekyll_path = roadmap_path / '.nojekyll'
    if not nojekyll_path.exists():
        nojekyll_path.write_text('', encoding='utf-8')
    
    # Copy CSS file if it exists
    css_source = project_root / 'web.css'
    if css_source.exists():
        shutil.copy(css_source, project_root / 'roadmap' / 'web.css')
    
    print('Static files built successfully:')
    print(f'- {roadmap_path}/index.html')

if __name__ == '__main__':
    build_static_site()