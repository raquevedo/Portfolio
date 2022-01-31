def build_context():
    return {
        'apps': [
            {
                'title': 'About Me',
                'text': 'Who I am, my skills and my CV.',
                'link_text': 'Visit',
                'url': 'about_me:about_me'
            },
            {
                'title': 'Projects',
                'text': 'A look at the projects I\'ve worked on.',
                'link_text': 'Visit',
                'url': 'projects:projects'
            },
            {
                'title': 'Contact',
                'text': 'Ways of contacting me.',
                'link_text': 'Visit',
                'url': 'contact:contact'
            }
        ]
    }
