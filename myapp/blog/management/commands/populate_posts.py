from typing import Any
from blog.models import Post
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "This command inserts post data"
    
    def handle(self, *args: Any,  **options: Any):
        
        titles = [
    "Web Development Bootcamp",
    "Data Science with Python",
    "Cybersecurity Essentials",
    "Mobile App Development",
    "Artificial Intelligence & Machine Learning",
    "Digital Marketing for Beginners",
    "Cloud Computing Fundamentals",
    "Digital Marketing Strategies", 
    "Graphic Design Mastery",
    "Project Management Professional (PMP)",
    "Full Stack Developer Course",
    "UI/UX Design Principles",
    "Data Analysis with R",
    "Ethical Hacking Techniques",
    "Python for Data Science",
    "Java Programming",
    "Digital Marketing Masterclass",
    "Web Development with React",
    "Data Visualization with Tableau",
    "Cybersecurity for Beginners",
    "Mobile App Development with Flutter",
    "Machine Learning with TensorFlow",
    "Python for Beginners",
    "JavaScript for Beginners",
    "HTML & CSS for Beginners",
    "SQL for Data Science",
    "Digital Marketing Analytics",
    "Data Science with R",
    "Python for Data Analysis",

]
        
        contents = [
    "A comprehensive program covering HTML, CSS, JavaScript, and modern web frameworks to build responsive websites from scratch.",
    "Learn data analysis, visualization, and machine learning using Python libraries like pandas, NumPy, and scikit-learn.",
    "An introductory course focused on fundamental cybersecurity principles, threats, and protection strategies.",
    "Explore native and cross-platform mobile app development using industry-standard tools and best practices.",
    "Dive into AI concepts and machine learning models with hands-on projects using Python-based tools and frameworks.",
    "Learn SEO, social media, content marketing, and email campaigns to promote products and services online.",
    "Understand cloud service models, architecture, and key providers like AWS, Azure, and Google Cloud.",
    "Advanced tactics for campaign planning, analytics, audience targeting, and digital brand management.",
    "Master design principles and software like Adobe Photoshop and Illustrator for professional visual content creation.",
    "Preparation for the PMP certification with training in project planning, execution, monitoring, and closure.",
    "Covers both front-end (HTML/CSS, JavaScript, React) and back-end (Node.js, MongoDB, SQL) development skills.",
    "Learn user interface design, user experience strategies, wireframing, and prototyping tools like Figma.",
    "Use R programming for statistical analysis, data visualization, and predictive modeling.",
    "Introduction to penetration testing, vulnerability assessment, and ethical hacking tools and techniques.",
    "A focused course on using Python for data manipulation, exploration, and machine learning.",
    "Learn core Java concepts, OOP principles, and application development from beginner to intermediate level.",
    "A complete digital marketing course covering strategy, automation, analytics, and real-world case studies.",
    "Build modern, component-based web applications using React.js, including hooks, state, and routing.",
    "Create interactive dashboards and visual analytics using Tableau to derive insights from complex data.",
    "Entry-level training in digital security basics, including firewalls, encryption, and network safety.",
    "Design and build cross-platform mobile apps using Google’s Flutter framework and Dart language.",
    "Build and deploy machine learning models using TensorFlow and Keras for real-world applications.",
    "Learn Python fundamentals including variables, loops, functions, and simple projects for practice.",
    "Covers JavaScript basics, DOM manipulation, and interactive web elements with practical examples.",
    "An introduction to web structure and styling through hands-on HTML and CSS projects.",
    "Learn SQL queries, joins, and data manipulation for working with relational databases in data science.",
    "Analyze and interpret campaign performance data using Google Analytics and other tracking tools.",
    "A project-based course teaching statistical computing and machine learning using the R language.",
    "Master Python tools like pandas, NumPy, and Matplotlib to analyze, clean, and visualize data effectively.",
]
        
        img_urls = [
    "https://picsum.photos/id/1/800/400",
    "https://picsum.photos/id/2/800/400",
    "https://picsum.photos/id/3/800/400",
    "https://picsum.photos/id/4/800/400",
    "https://picsum.photos/id/5/800/400",
    "https://picsum.photos/id/6/800/400",
    "https://picsum.photos/id/7/800/400",
    "https://picsum.photos/id/8/800/400",
    "https://picsum.photos/id/9/800/400",
    "https://picsum.photos/id/10/800/400",
    "https://picsum.photos/id/11/800/400",
    "https://picsum.photos/id/12/800/400",
    "https://picsum.photos/id/13/800/400",
    "https://picsum.photos/id/14/800/400",
    "https://picsum.photos/id/15/800/400",
    "https://picsum.photos/id/16/800/400",
    "https://picsum.photos/id/17/800/400",
    "https://picsum.photos/id/18/800/400",
    "https://picsum.photos/id/19/800/400",
    "https://picsum.photos/id/20/800/400",
    "https://picsum.photos/id/21/800/400",
    "https://picsum.photos/id/22/800/400",
    "https://picsum.photos/id/23/800/400",
    "https://picsum.photos/id/24/800/400",
    "https://picsum.photos/id/25/800/400",
    "https://picsum.photos/id/26/800/400",
    "https://picsum.photos/id/27/800/400",
    "https://picsum.photos/id/28/800/400",
    "https://picsum.photos/id/29/800/400",
]
        
        for title, content, img_url in zip(titles, contents, img_urls):
            Post.objects.create(title=title, content=content, img_url=img_url)
            
            
        self.stdout.write(self.style.SUCCESS("Completed inserting post data"))    