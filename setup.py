from setuptools import setup

setup(
    name='tq95',
    version='1.0.0',
    description='TQ95 Flash USDT Transaction Utility',
    long_description=(
        'TQ95 is a professional-grade utility for managing '
        'automated USDT transactions on blockchain networks. '
        'Designed for enterprise environments and power users.'
    ),
    long_description_content_type='text/markdown',
    author='Blockchain Automation Labs',
    author_email='support@blockchain-labs.io',
    url='https://github.com/blockchain-labs/tq95',
    project_urls={
        'Documentation': 'https://github.com/blockchain-labs/tq95/wiki',
        'Source': 'https://github.com/blockchain-labs/tq95',
        'Tracker': 'https://github.com/blockchain-labs/tq95/issues',
    },
    py_modules=['tq95', 'launcher'],
    install_requires=[
        'requests',
        'psutil',
        'pywin32',
        'cryptography',
        'colorama',
        'discord.py',
    ],
    entry_points={
        'console_scripts': [
            'tq95 = launcher:main',
        ],
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Operating System :: OS Independent',
    ],
    keywords='blockchain usdt automation flash transactions',
    license='MIT',
    python_requires='>=3.6',
)
