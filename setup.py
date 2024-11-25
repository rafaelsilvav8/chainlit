from setuptools import setup

with open("README.md", "r") as arq:
    readme = arq.read()

setup(name='chainlit-v8',
    version='0.0.1',
    license='MIT License',
    author='V8.Tech',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='suporte@v8.tech',
    keywords='chainlit',
    description=u'Wrapper não oficial do chainlit',
    packages=['chainlit-v8'])