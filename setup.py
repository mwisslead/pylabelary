from setuptools import setup

def main():
    VERSION='1.0.0rc1'

    setup(
        name='labelary',
        version=VERSION,
        packages=['labelary'],
        package_data={
        },
        install_requires=['requests'],
        test_suite='nose.collector',
        tests_require=['nose'],
    )

if __name__ == '__main__':
    main()
