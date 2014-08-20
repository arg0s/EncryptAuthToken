from distutils.core import setup

setup(
    name='encrypt_auth_token',
    version='0.1.0',
    author='arg0s',
    author_email='arvi@alumni.iastate.edu',
    packages=['encrypt_auth_token'],
    scripts=['crypt.py'],
    url='https://github.com/arg0s/EncryptAuthToken',
    license='LICENSE',
    description='A simple module to help you encrypt/decrypt social media authentication tokens with AES before storing them... well, wherever you'd like to!',
    long_description=open('README').read(),
    install_requires=[
        "pycrypto >= 2.6.1"
    ],
)
