from setuptools import setup, find_packages

setup(
    name='EmotionDetection',
    version='1.0.0',
    description='A package for emotion detection using Watson NLP',
    author='Your Name',
    author_email='your.email@example.com',
    packages=find_packages(),
    install_requires=[
        'requests',
        'flask',
    ],
    python_requires='>=3.6',
)