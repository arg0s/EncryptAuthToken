from distutils.core import setup

setup(
    name='encryptauthtoken',
    version='0.1.0',
    author='arg0s',
    author_email='arvi@alumni.iastate.edu',
    scripts=['crypt.py'],
    url='https://github.com/arg0s/EncryptAuthToken',
    license='LICENSE',
    description='A simple module to help you encrypt/decrypt social media authentication tokens with AES before storing them... well, wherever you\'d like to!',
    long_description=open('README.md').read(),
    install_requires=[
        "pycrypto >= 2.6.1"
    ],
)
