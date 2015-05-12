from distutils.core import setup

setup(
    name='threejs-blob-models',
    version='1.0',
    packages=['threejs_blob_models'],
    url='http://levisaya.com',
    license='MIT',
    author='Andy Levisay',
    author_email='levisaya@gmail.com',
    description='Demo for integrating AngularJS and Three.js using blob models.',
    install_requires=['numpy>=1.9.0',
                      'tornado>=4.1']
)