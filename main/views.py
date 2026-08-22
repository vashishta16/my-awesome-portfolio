from django.shortcuts import render

def home(request):
    context = {
        'name': 'MUDALA VASHISHTA REDDY',
        'title': 'AI Engineer • Cloud Enthusiast • Full Stack Developer',
        'tagline': 'Data Science & AI enthusiast passionate about extracting insights from data, building intelligent systems, and solving complex real-world problems. Skilled in machine learning, statistical analysis, and deploying AI solutions at scale. Always eager to learn, innovate, and collaborate on impactful data-driven projects.',
        'about_text1': "I'm passionate about leveraging AI and machine learning to solve real-world problems. With a strong foundation in both theory and practical implementation, I bridge the gap between cutting-edge AI research and production systems.",
        'about_text2': "My journey spans across Python development, cloud infrastructure with AWS, and building full-stack applications with React. I'm constantly learning new technologies and sharing knowledge with the community.",
        'experience': 'Building AI/ML solutions with focus on real-world impact',
        'education': 'B.Tech in Computer Science Engineering (AI)',
        'passion': 'Creating innovative solutions that make a tangible difference',
        'skills': [
            'Python', 'Django', 'AWS', 'SQL', 'NumPy', 'Pandas',
            'JavaScript', 'React', 'Flask', 'OpenCV'
        ],
        'future_projects': [
            {
                'title': 'AI-Powered Chatbot',
                'description': 'Building an intelligent chatbot using NLP and deep learning for customer service automation.',
                'tech': 'Python, TensorFlow, FastAPI',
                'status': 'In Development'
            },
            {
                'title': 'Cloud Cost Optimizer',
                'description': 'AWS-based solution to monitor and optimize cloud infrastructure costs using machine learning.',
                'tech': 'AWS, Python, Lambda',
                'status': 'Planning Phase'
            },
            {
                'title': 'Real-Time Analytics Dashboard',
                'description': 'Interactive dashboard for real-time data visualization and business intelligence.',
                'tech': 'React, Django, WebSockets',
                'status': 'Coming Soon'
            },
        ],
        'certifications': [
            {
                'name': 'AWS Certified Cloud Practitioner',
                'issuer': 'Amazon Web Services',
                'year': '2024',
                'icon': 'fa-aws',
                'link': 'https://www.credly.com/badges/2ea3df23-0daf-43d5-9d2f-eea77718f185/public_url',
                'description': 'Cloud fundamentals and AWS services'
            },
            {
                'name': 'Oracle Certified Foundation Associate',
                'issuer': 'Oracle',
                'year': '2026',
                'icon': 'fa-database',
                'link': 'https://catalog-education.oracle.com/pls/certview/sharebadge?id=5635020EDC483C9528EF72EA3A2C321F5BA28E38E1F5950489F7785947D66E58',
                'description': 'Oracle database and cloud foundation'
            },
            {
                'name': 'Red Hat Certified Enterprise Application Developer',
                'issuer': 'Red Hat',
                'year': '2023',
                'icon': 'fa-linux',
                'link': 'https://www.credly.com/badges/d77b8e27-4e94-48fb-b67c-0f13becb4dc9/public_url',
                'description': 'Enterprise application development on Red Hat'
            },
            {
                'name': 'Automation Anywhere Certified',
                'issuer': 'Automation Anywhere',
                'year': '2025',
                'icon': 'fa-robot',
                'link': 'https://certificates.automationanywhere.com/profile/mudalavashishtareddy669253/wallet',
                'description': 'RPA and automation solutions'
            },
        ],
        'github_url': 'https://github.com/vashishta16',
        'linkedin_url': 'https://linkedin.com/in/vashishta_16',
        'twitter_url': 'https://x.com/vashishta_16',
        'email': 'vashishtareddym16@gmail.com',
    }
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def skills(request):
    return render(request, 'skills.html')

def certifications(request):
    return render(request, 'certifications.html')

def contact(request):
    return render(request, 'contact.html')